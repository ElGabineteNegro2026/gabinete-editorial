#!/usr/bin/env python3
"""Cubiertas de El Gabinete Negro (KDP tapa blanda 6x9 y ebook).

Uso:  python3 scripts/cubierta.py proyectos/<slug> [--variante N]
      (--variante N usa [cubierta.variantes.N] de libro.toml y guarda los ficheros con el sufijo _pN)

Lee la sección [cubierta] de proyectos/<slug>/libro.toml:
    ilustracion = "cubierta/ilustracion.jpg"   # arte de portada (dominio público o propio)
    portada     = "cubierta/portada.jpg"       # opcional: portada ya diseñada (p. ej. por el responsable); se usa
                                               # tal cual, escalada al alto del panel y ampliada con el color de fondo
    sinopsis    = "Texto de contracubierta…"     # admite *cursiva*
    cita        = "«Frase destacada»"           # opcional
    cita_autor  = "Maurice Leblanc"             # opcional
    papel       = "crema"                       # "blanco" | "crema"
    paginas     = 0                             # 0 = se leen del PDF interior
    dossier     = "I"                           # solo Archivo Lupin
Genera en proyectos/<slug>/cubierta/:
    <slug>_cubierta_kdp.pdf    cubierta completa (contra + lomo + portada) con sangrado 3,2 mm, 300 ppp
    <slug>_cubierta_kdp.jpg    vista previa con guías (corte, lomo, zona de seguridad)
    <slug>_portada_ebook.jpg   portada ebook 1600 x 2560 px
La estética de cada colección está descrita en colecciones/<coleccion>.json ("cubierta") y en CLAUDE.md.
Es una base reutilizable: el agente la adapta por libro (composición, tamaños) y revisa visualmente cada resultado.
"""
import math, re, subprocess, sys, tomllib, json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps

RAIZ = Path(__file__).resolve().parent.parent
F = RAIZ / "fuentes"
PPP = 300
MM = PPP / 25.4
SANGRADO = 0.125 * PPP                      # 3,175 mm
ANCHO, ALTO = 6 * PPP, 9 * PPP              # 6 x 9 in
GROSOR = {"blanco": 0.002252, "crema": 0.0025}   # pulgadas por página (KDP)

def fuente(nombre, tam, peso=None):
    f = ImageFont.truetype(str(F / nombre), int(tam))
    if peso:
        try: f.set_variation_by_name(peso)
        except Exception: pass
    return f

def hexa(c): return tuple(int(c[i:i+2], 16) for i in (1, 3, 5))

def texto_espaciado(d, xy_centro, txt, f, color, espaciado=0.0, ancla_y="m"):
    """Texto centrado con tracking (espaciado en fracción del cuerpo)."""
    sp = f.size * espaciado
    anchos = [d.textlength(ch, font=f) for ch in txt]
    total = sum(anchos) + sp * (len(txt) - 1)
    x = xy_centro[0] - total / 2
    for ch, w in zip(txt, anchos):
        d.text((x, xy_centro[1]), ch, font=f, fill=color, anchor="l" + ancla_y)
        x += w + sp
    return total

def cursiva_de(f):
    """Fuente cursiva equivalente (para *cursiva* en sinopsis y citas)."""
    ruta = Path(f.path)
    alt = {"CormorantGaramond.ttf": "CormorantGaramond-Italic.ttf", "Caladea-Regular.ttf": "Caladea-Italic.ttf",
           "Carlito-Regular.ttf": "Carlito-Italic.ttf"}.get(ruta.name)
    if not alt: return f
    fi = ImageFont.truetype(str(ruta.with_name(alt)), f.size)
    try:
        nombre = f.get_variation_name().decode() if isinstance(f.get_variation_name(), bytes) else f.get_variation_name()
        fi.set_variation_by_name(nombre + " Italic" if "Italic" not in nombre else nombre)
    except Exception: pass
    return fi

def parrafo(d, caja, txt, f, color, interlineado=1.35, centrado=False):
    """Párrafo ajustado a la caja; *texto* se compone en cursiva."""
    x0, y0, x1, _ = caja
    fi = cursiva_de(f)
    # palabras con su estilo
    palabras, ital = [], False
    for w in txt.split():
        empieza = w.startswith("*") or (w[:1] in "«(“" and w[1:2] == "*")
        if empieza: ital = True
        limpio = w.replace("*", "")
        palabras.append((limpio, ital))
        if w.rstrip(".,;:!?»)”…").endswith("*"): ital = False
    esp = d.textlength(" ", font=f)
    ancho = lambda linea: sum(d.textlength(t, font=fi if i else f) for t, i in linea) + esp * (len(linea) - 1)
    lineas, actual = [], []
    for w in palabras:
        if actual and ancho(actual + [w]) > x1 - x0: lineas.append(actual); actual = [w]
        else: actual.append(w)
    if actual: lineas.append(actual)
    y = y0
    for l in lineas:
        x = x0 + ((x1 - x0) - ancho(l)) / 2 if centrado else x0
        for t, i in l:
            fu = fi if i else f
            d.text((x, y), t, font=fu, fill=color); x += d.textlength(t, font=fu) + esp
        y += f.size * interlineado
    return y

def preparar_grabado(im, C, recorte=0.035, invertir=False):
    """Grabado de dominio público (papel blanco, tinta negra) → paleta de la colección:
    recorta el margen del papel, oscurece y tiñe de fondo (sombras) a acento/texto (luces).
    recorte: fracción por lado o lista [izq, arriba, der, abajo] (para quitar sellos, firmas…).
    invertir: negativo (papel oscuro, trazo claro), útil con xilografías de mucho blanco."""
    est = C["cubierta"]
    im = ImageOps.grayscale(im)
    w, h = im.size
    l, t, r, b = recorte if isinstance(recorte, (list, tuple)) else (recorte,) * 4
    im = im.crop((int(w*l), int(h*t), int(w*(1-r)), int(h*(1-b))))
    im = ImageOps.autocontrast(im, cutoff=1)
    if invertir:
        im = ImageOps.invert(im)
    im = im.point(lambda v: int(255 * (v / 255) ** 1.6))          # más nocturno
    luz = est.get("luz_grabado", est["texto"])
    return ImageOps.colorize(im, black=est["fondo"], mid=est.get("medio_grabado", est["acento"]), white=luz)

ENCUADRE = (0.5, 0.5)   # centro del recorte (x, y); se fija con `encuadre = [x, y]` en [cubierta]

def encaja(img, w, h):
    return ImageOps.fit(img.convert("RGB"), (int(w), int(h)), Image.LANCZOS, centering=ENCUADRE)

def portada_dada(img, w, h, cx=None):
    """Portada terminada → lienzo w x h: se escala al alto del lienzo y se centra en cx (centro del corte);
    los laterales se rellenan con el color de las esquinas (las portadas de la casa tienen fondo liso)."""
    img = img.convert("RGB")
    fondo = img.getpixel((2, 2))
    esc = h / img.height
    im = img.resize((round(img.width * esc), h), Image.LANCZOS)
    lienzo = Image.new("RGB", (w, h), fondo)
    cx = w / 2 if cx is None else cx
    lienzo.paste(im, (round(cx - im.width / 2), 0))
    return lienzo

# ------------------------------------------------------------------ portadas por colección
# Cada función dibuja la portada en un lienzo de w x h (sirve para KDP y para ebook).

def portada_limite_abisal(L, C, ilu, w, h):
    est = C["cubierta"]; im = Image.new("RGB", (w, h), hexa(est["fondo"])); d = ImageDraw.Draw(im)
    u = w / 1253
    texto_espaciado(d, (w/2, 155*u), L["autor"].upper(), fuente("Carlito-Regular.ttf", 46*u), "#f0f0f0", 0.12)
    ft = fuente("CormorantGaramond.ttf", 175*u, "Medium")
    lineas = L.get("titulo_portada", L["titulo"].upper()).split("|")
    while max(d.textlength(l.strip(), font=ft) for l in lineas) > w * 0.86 and ft.size > 60*u:   # títulos largos: reducir hasta que quepan
        ft = fuente("CormorantGaramond.ttf", ft.size * 0.96, "Medium")
    y = 330*u
    for l in lineas:
        sombra = Image.new("L", (w, h), 0); ds = ImageDraw.Draw(sombra)
        ds.text((w/2+6*u, y+6*u), l.strip(), font=ft, fill=255, anchor="mm")
        im.paste((10, 12, 14), mask=sombra.filter(ImageFilter.GaussianBlur(4*u)))
        d.text((w/2, y), l.strip(), font=ft, fill=est["acento"], anchor="mm")
        y += 150*u
    bx, by, bw, bh = 235*u, 615*u, 783*u, 1130*u
    if L.get("subtitulo_portada"):
        fs = fuente("CormorantGaramond.ttf", 52*u, "Medium")
        ys = y - 40*u
        for l in L["subtitulo_portada"].split("|"):
            d.text((w/2, ys), l.strip(), font=fs, fill="#c9d6e0", anchor="mm"); ys += 62*u
        if ys + 10*u > by:   # el subtítulo baja la ilustración (y la acorta) para no quedar tapado
            fondo = by + bh; by = ys + 10*u; bh = fondo - by; bw = bh * 783 / 1130; bx = (w - bw) / 2
    if ilu: im.paste(encaja(ilu, bw, bh), (int(bx), int(by)))
    texto_espaciado(d, (w/2, 1815*u), "EL GABINETE NEGRO", fuente("Carlito-Regular.ttf", 36*u), "#f0f0f0", 0.2)
    texto_espaciado(d, (w/2, 1870*u), "COLECCIÓN LÍMITE ABISAL", fuente("Carlito-Regular.ttf", 22*u), "#8fa3b4", 0.2)
    d.text((w/2, 1905*u), (f"Vol. {L['volumen']}" if re.fullmatch(r"[IVXLC]+", str(L['volumen'])) else str(L['volumen'])), font=fuente("Carlito-Regular.ttf", 22*u), fill="#8fa3b4", anchor="mm")
    return im

def portada_camara_sellada(L, C, ilu, w, h):
    est = C["cubierta"]; im = Image.new("RGB", (w, h), hexa(est["fondo"])); d = ImageDraw.Draw(im)
    u = w / 1253; oro = est["acento"]
    d.text((w/2, 140*u), "El Gabinete Negro", font=fuente("Cinzel.ttf", 46*u, "Regular"), fill="#f2ece0", anchor="mm")
    d.line((w/2-150*u, 178*u, w/2+150*u, 178*u), fill="#f2ece0", width=max(1, int(2*u)))
    texto_espaciado(d, (w/2, 255*u), "COLECCIÓN CÁMARA SELLADA", fuente("CormorantGaramond.ttf", 30*u, "Medium"), "#f2ece0", 0.25)
    bx, by, bw, bh = 233*u, 385*u, 818*u, 1225*u
    if ilu:
        arte = encaja(ilu, bw, bh)
        velo = Image.new("L", arte.size, 0); dv = ImageDraw.Draw(velo)
        for i in range(int(bh*0.38)): dv.line((0, i, bw, i), fill=int(170 * (1 - i/(bh*0.38))))
        arte.paste((15, 12, 8), mask=velo)
        im.paste(arte, (int(bx), int(by)))
    for k, g in ((14, 3), (26, 1)):
        d.rectangle((bx+k*u, by+k*u, bx+bw-k*u, by+bh-k*u), outline=oro, width=max(1, int(g*u)))
    ft = fuente("Cinzel.ttf", 98*u, "Bold"); y = by + 205*u
    for l in L.get("titulo_portada", L["titulo"].upper()).split("|"):
        d.text((w/2, y), l.strip(), font=ft, fill="#e2c99a", anchor="mm"); y += 105*u; ft = fuente("Cinzel.ttf", 66*u, "Bold")
    lin_aut = L.get("autor_portada", L["autor"]).upper().split("|")   # `autor_portada` (con «|») para antologías
    fa = fuente("Cinzel.ttf", 54*u if len(lin_aut) == 1 else 34*u, "SemiBold")
    while max(d.textlength(la.strip(), font=fa) * 1.12 for la in lin_aut) > bw * 0.84 and fa.size > 12*u:   # que quepa en el marco
        fa = fuente("Cinzel.ttf", fa.size * 0.95, "SemiBold")
    for k, la in enumerate(lin_aut):
        texto_espaciado(d, (w/2, by+bh-95*u - (len(lin_aut)-1-k)*48*u), la.strip(), fa, "#e2c99a", 0.1)
    vol = f"VOL.{L['volumen']}" if re.fullmatch(r"[IVXLC]+", str(L["volumen"])) else str(L["volumen"]).upper()
    texto_espaciado(d, (w/2, 1795*u), vol, fuente("CormorantGaramond.ttf", 40*u, "Medium"), "#f2ece0", 0.25)
    return im

def portada_archivo_lupin(L, C, ilu, w, h):
    est = C["cubierta"]; im = Image.new("RGB", (w, h), hexa(est["fondo"])); d = ImageDraw.Draw(im)
    u = min(w / 625, h / 1000); crema, oro = est["texto"], est["acento"]
    if ilu:
        arte = encaja(ilu, w, h); velo = Image.new("L", (w, h), 0); dv = ImageDraw.Draw(velo)
        for i in range(h):
            t = i / h
            a = 200 * max(0, 1 - t/0.33) + 230 * max(0, (t - 0.62) / 0.38)
            dv.line((0, i, w, i), fill=int(min(235, a)))
        arte.paste(hexa(est["fondo"]), mask=velo); im.paste(arte, (0, 0))
    d.rectangle((14*u, 14*u, w-14*u, h-14*u), outline=oro, width=max(1, int(1.2*u)))
    d.text((40*u, 62*u), f"DOSSIER {L.get('dossier', L['volumen'])}", font=fuente("Cinzel.ttf", 9*u, "Medium"), fill=oro, anchor="lm")
    texto_espaciado(d, (w/2, 112*u), "EL ARCHIVO", fuente("CormorantGaramond.ttf", 26*u, "SemiBold"), crema, 0.32)
    d.text((w/2, 225*u), "LUPIN", font=fuente("BodoniModa.ttf", 128*u, "Black"), fill=crema, anchor="mm")
    cx, cy, r = w/2, 755*u, 22*u
    d.ellipse((cx-r, cy-r, cx+r, cy+r), outline=oro, width=max(1, int(1.2*u)))
    d.ellipse((cx-5*u, cy-12*u, cx+5*u, cy-2*u), outline=oro, width=max(1, int(1.2*u)))
    d.line((cx, cy-2*u, cx, cy+14*u), fill=oro, width=max(1, int(1.2*u)))
    d.line((cx, cy+8*u, cx+5*u, cy+8*u), fill=oro, width=max(1, int(1.2*u)))
    titulo = f"{L.get('dossier', L['volumen'])}. {L['titulo'].upper()}"
    texto_espaciado(d, (w/2, 805*u), titulo, fuente("CormorantGaramond.ttf", 23*u, "Medium"), crema, 0.05)
    d.polygon([(w/2, 834*u), (w/2+6*u, 840*u), (w/2, 846*u), (w/2-6*u, 840*u)], fill="#b3262b")
    texto_espaciado(d, (w/2, 870*u), L["autor"].upper(), fuente("Cinzel.ttf", 15*u, "Medium"), crema, 0.18)
    texto_espaciado(d, (w/2, 907*u), "EL GABINETE NEGRO", fuente("Cinzel.ttf", 9*u, "Regular"), "#927c4d", 0.2)
    d.line((w/2-38*u, 944*u, w/2+38*u, 944*u), fill=oro, width=max(1, int(u)))
    return im

def componer(coleccion, L, C, ilu, w, h):
    """Las portadas de referencia miden 1253 x 2000 (proporción 1,6, la del ebook). En imprenta
    (6,125 x 9,25 in con sangrado, 1,51) se compone a 1,6 y se ajusta sobre el color de fondo."""
    if coleccion in ("archivo-lupin", "archivo-arcano"):   # composición que se adapta a cualquier proporción
        return PORTADAS[coleccion](L, C, ilu, w, h)
    base = PORTADAS[coleccion](L, C, ilu, w, round(w * 2000 / 1253))
    return ImageOps.pad(base, (w, h), color=hexa(C["cubierta"]["fondo"]))

PORTADAS = {"limite-abisal": portada_limite_abisal, "camara-sellada": portada_camara_sellada,
            "archivo-lupin": portada_archivo_lupin}

# ------------------------------------------------------------------ cubierta completa

def portada_archivo_arcano(L, C, ilu, w, h):
    """Tapa dura. Referencia: referencias/cubiertas/archivo-arcano_Dracula_tapa_dura.jpg.
    Fondo negro, marco dorado ornamental, autor arriba, título en serif clásica crema,
    subtítulo en rojo, ilustración de grabado oscuro con acentos rojos, colección abajo."""
    est = C["cubierta"]; im = Image.new("RGB", (w, h), hexa(est["fondo"])); d = ImageDraw.Draw(im)
    u = min(w / 1800, h / 2700); oro, crema, rojo = est["acento"], est["texto"], est.get("rojo", "#b3262b")
    m = 70 * u
    if ilu:
        bx0, by0, bx1, by1 = m + 30*u, 1050*u, w - m - 30*u, h - m - 260*u
        arte = encaja(ilu, bx1 - bx0, by1 - by0)
        velo = Image.new("L", arte.size, 0); dv = ImageDraw.Draw(velo); aw, ah = arte.size
        for i in range(ah):
            t = i / ah; a = 255 * max(0, 1 - t / 0.18) + 200 * max(0, (t - 0.82) / 0.18)
            dv.line((0, i, aw, i), fill=int(min(255, a)))
        arte.paste(hexa(est["fondo"]), mask=velo)
        im.paste(arte, (int(bx0), int(by0)))
    # Marco: doble filete dorado con remates en las esquinas
    for k, g in ((0, 6), (22, 2)):
        d.rectangle((m + k*u, m + k*u, w - m - k*u, h - m - k*u), outline=oro, width=max(1, int(g*u)))
    for cx, cy in ((m, m), (w - m, m), (m, h - m), (w - m, h - m)):
        r = 38 * u
        d.polygon([(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)], fill=hexa(est["fondo"]), outline=oro)
        d.polygon([(cx, cy - r/2), (cx + r/2, cy), (cx, cy + r/2), (cx - r/2, cy)], fill=oro)
    def filete(y, ancho):
        d.line((w/2 - ancho, y, w/2 - 22*u, y), fill=oro, width=max(1, int(3*u)))
        d.line((w/2 + 22*u, y, w/2 + ancho, y), fill=oro, width=max(1, int(3*u)))
        d.polygon([(w/2, y - 12*u), (w/2 + 14*u, y), (w/2, y + 12*u), (w/2 - 14*u, y)], fill=oro)
    texto_espaciado(d, (w/2, 230*u), L["autor"].upper(), fuente("Cinzel.ttf", 64*u, "SemiBold"), oro, 0.12)
    filete(310*u, 520*u)
    lineas = L.get("titulo_portada", L["titulo"].upper()).split("|")
    ft = fuente("Cinzel.ttf", 190*u if len(lineas) == 1 else 150*u, "Bold"); y = 470*u
    for l in lineas:
        d.text((w/2 + 5*u, y + 6*u), l.strip(), font=ft, fill="#000000", anchor="mm")
        d.text((w/2, y), l.strip(), font=ft, fill=crema, anchor="mm"); y += ft.size * 1.05
    if L.get("subtitulo_portada"):
        fs = fuente("Cinzel.ttf", 82*u, "SemiBold")
        for l in L["subtitulo_portada"].upper().split("|"):
            d.text((w/2, y), l.strip(), font=fs, fill=rojo, anchor="mm"); y += fs.size * 1.1
    filete(y + 30*u, 420*u)
    texto_espaciado(d, (w/2, h - m - 110*u), "ARCHIVO ARCANO · EL GABINETE NEGRO", fuente("Cinzel.ttf", 40*u, "SemiBold"), crema, 0.06)
    return im

PORTADAS["archivo-arcano"] = portada_archivo_arcano

def lomo_vertical(C, L, coleccion, alto, ancho):
    """Tira del lomo (texto de abajo arriba al girar), alto x ancho en píxeles."""
    est = C["cubierta"]; crema, oro = est["texto"], est["acento"]
    tira = Image.new("RGB", (int(alto), max(1, int(ancho))), hexa(est["fondo"])); dt = ImageDraw.Draw(tira)
    t = max(18, int(ancho * 0.42))
    if coleccion == "archivo-arcano":
        # Como la referencia: marco dorado, autor y colección en horizontal arriba y abajo,
        # título · subtítulo en vertical en el centro, ajustado al hueco disponible.
        v = Image.new("RGB", (max(1, int(ancho)), int(alto)), hexa(est["fondo"])); dv = ImageDraw.Draw(v)
        aw = v.width; g = max(2, int(aw * 0.02))
        dv.rectangle((aw*0.08, alto*0.012, aw*0.92, alto*0.988), outline=oro, width=g)
        dv.rectangle((aw*0.13, alto*0.017, aw*0.87, alto*0.983), outline=oro, width=max(1, g//2))
        fa = fuente("Cinzel.ttf", aw * 0.16, "SemiBold"); y = alto * 0.07
        for parte in L["autor"].upper().split():
            dv.text((aw/2, y), parte, font=fa, fill=crema, anchor="mm"); y += fa.size * 1.1
        dv.line((aw*0.3, y + aw*0.05, aw*0.7, y + aw*0.05), fill=oro, width=g)
        fc = fuente("Cinzel.ttf", aw * 0.13, "SemiBold")
        dv.text((aw/2, alto*0.90), "ARCHIVO", font=fc, fill=crema, anchor="mm")
        dv.text((aw/2, alto*0.90 + fc.size*1.15), "ARCANO", font=fc, fill=crema, anchor="mm")
        tit = L["titulo"].upper() + (" · " + L["subtitulo_portada"].replace("|", " ").upper() if L.get("subtitulo_portada") else "")
        hueco = alto * 0.62; t = aw * 0.38
        ft = fuente("Cinzel.ttf", t, "SemiBold")
        while dv.textlength(tit, font=ft) > hueco and t > 10:
            t *= 0.95; ft = fuente("Cinzel.ttf", t, "SemiBold")
        tw = int(dv.textlength(tit, font=ft)) + 10
        banda = Image.new("RGB", (tw, int(aw * 0.7)), hexa(est["fondo"]))
        ImageDraw.Draw(banda).text((tw/2, banda.height/2), tit, font=ft, fill=oro, anchor="mm")
        banda = banda.rotate(-90, expand=True)
        v.paste(banda, (int((aw - banda.width)/2), int(alto*0.48 - banda.height/2)))
        return v
    if True:
        f_tit = fuente("BodoniModa.ttf", t, "Black") if coleccion == "archivo-lupin" else fuente("Cinzel.ttf", t, "SemiBold")
        tit = "EL ARCHIVO LUPIN" if coleccion == "archivo-lupin" else L["titulo"].upper()
        while dt.textlength(tit, font=f_tit) > alto * 0.46 and f_tit.size > 10:   # hueco 0,17–0,63
            f_tit = fuente("BodoniModa.ttf", int(f_tit.size * 0.95), "Black") if coleccion == "archivo-lupin" \
                else fuente("Cinzel.ttf", int(f_tit.size * 0.95), "SemiBold")
        dt.text((alto * 0.40, ancho / 2), tit, font=f_tit, fill=crema, anchor="mm")
        fa = fuente("Cinzel.ttf", int(t * 0.7), "Medium")
        while dt.textlength(L.get("autor_lomo", L["autor"]).upper(), font=fa) > alto * 0.24 and fa.size > 8:      # hueco 0,66–0,90
            fa = fuente("Cinzel.ttf", int(fa.size * 0.95), "Medium")
        dt.text((alto * 0.78, ancho / 2), L.get("autor_lomo", L["autor"]).upper(), font=fa, fill=oro, anchor="mm")
        if re.fullmatch(r"[IVXLC]+", str(L.get("dossier", L["volumen"]))):   # «Edición especial» no cabe en el lomo
            dt.text((alto * 0.07, ancho / 2), str(L.get("dossier", L["volumen"])), font=fuente("Cinzel.ttf", int(t * 0.8), "Medium"), fill=oro, anchor="mm")
    return tira.rotate(-90, expand=True)

def main():
    dir_proy = (Path.cwd() / sys.argv[1]).resolve(); slug = dir_proy.name
    meta = tomllib.loads((dir_proy / "libro.toml").read_text(encoding="utf-8"))
    col = meta["coleccion"]
    C = json.loads((RAIZ / "colecciones" / f"{col}.json").read_text(encoding="utf-8"))
    cub = meta.get("cubierta", {})
    # --variante N: aplica [cubierta.variantes.N] (otra ilustración, encuadre…) y añade _pN a los ficheros
    variante = sys.argv[sys.argv.index("--variante") + 1] if "--variante" in sys.argv else None
    if variante:
        cub = {**cub, **cub.get("variantes", {})[variante]}
    sufv = f"_p{variante}" if variante else ""
    L = {**meta, **cub}
    global ENCUADRE
    ENCUADRE = tuple(cub.get("encuadre", ENCUADRE))
    ilu = Image.open(dir_proy / cub["ilustracion"]) if cub.get("ilustracion") else None
    if ilu is not None and cub.get("grabado"):   # grabado de dominio público: teñir a la paleta de la colección
        ilu = preparar_grabado(ilu, C, cub.get("recorte_grabado", 0.035), cub.get("invertir_grabado", False))
    portada = Image.open(dir_proy / cub["portada"]) if cub.get("portada") else None
    if portada is not None:
        ppp_ef = PPP * portada.height / (ALTO + 2 * SANGRADO)
        print(f"Portada dada: {portada.width} x {portada.height} px → {ppp_ef:.0f} ppp efectivos en imprenta"
              + ("  (AVISO: < 300 ppp; pedir un original mayor)" if ppp_ef < 290 else ""))
    paginas = cub.get("paginas", 0)
    if not paginas:
        pdf = dir_proy / "interior" / f"{slug}_interior_6x9.pdf"
        paginas = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout).group(1))
    tapa_dura = C.get("formato") == "tapa-dura"
    provisional = False
    if tapa_dura:
        # KDP tapa dura (case laminate): margen exterior = vuelta 15 mm + sangrado 3 mm (0,709 in),
        # bisagras de 0,394 in a cada lado del lomo; el lomo de tapa dura lo da la calculadora de KDP.
        papel = "blanco"  # KDP solo ofrece papel blanco en tapa dura
        EXT = cub.get("vuelta_in", 0.709) * PPP
        BIS = cub.get("bisagra_in", 0.394) * PPP
        if cub.get("lomo_in"):
            lomo = cub["lomo_in"] * PPP
        else:
            provisional = True
            lomo = (paginas * GROSOR["blanco"] + 0.06) * PPP   # estimación: confirmar con la calculadora de KDP
    else:
        papel = cub.get("papel", "crema")
        EXT, BIS = SANGRADO, 0
        lomo = paginas * GROSOR[papel] * PPP
    # Medidas exactas en pulgadas (KDP compara con 3 decimales); el lienzo se redondea hacia arriba a píxeles
    # enteros y el PDF se guarda con la resolución que da justo esas pulgadas (antes se truncaba: 12,713 ≠ 12,715)
    W_in = (2 * EXT + 2 * ANCHO + 2 * BIS + lomo) / PPP; H_in = (ALTO + 2 * EXT) / PPP
    W = math.ceil(W_in * PPP - 1e-6); H = math.ceil(H_in * PPP - 1e-6)
    if tapa_dura and cub.get("ancho_total_in"):           # medidas exactas de la plantilla de KDP
        W_in, H_in = cub["ancho_total_in"], cub["alto_total_in"]
        W, H = math.ceil(W_in * PPP - 1e-6), math.ceil(H_in * PPP - 1e-6)
        lomo = W - 2 * EXT - 2 * ANCHO - 2 * BIS
    est = C["cubierta"]
    lienzo = Image.new("RGB", (W, H), hexa(est["fondo"])); d = ImageDraw.Draw(lienzo)
    x_contra = EXT; x_lomo = EXT + ANCHO + BIS; x_portada = x_lomo + lomo + BIS
    # Portada
    if tapa_dura:   # se compone a tamaño de corte y la vuelta queda del color de fondo
        lienzo.paste(componer(col, L, C, ilu, ANCHO, ALTO), (int(x_portada), int(EXT)))
    elif portada is not None:   # portada terminada: centrada en el corte (el sangrado exterior queda a la derecha)
        lienzo.paste(portada_dada(portada, int(W - x_portada), H, ANCHO / 2), (int(x_portada), 0))
    else:
        lienzo.paste(componer(col, L, C, ilu, int(W - x_portada), H), (int(x_portada), 0))
    # Lomo (KDP: texto solo con más de 79 páginas)
    crema = est["texto"]; oro = est["acento"]
    if paginas > 79:
        alto_lomo = ALTO if tapa_dura else H
        lienzo.paste(lomo_vertical(C, L, col, alto_lomo, lomo), (int(x_lomo), int(EXT if tapa_dura else 0)))
    # Contracubierta
    m = 0.5 * PPP; x0, x1 = x_contra + m, x_contra + ANCHO - m
    y0 = EXT if tapa_dura else SANGRADO
    if col == "archivo-arcano":
        d.rectangle((x_contra + 0.23*PPP, y0 + 0.23*PPP, x_contra + ANCHO - 0.23*PPP, y0 + ALTO - 0.23*PPP), outline=oro, width=6)
        d.rectangle((x_contra + 0.30*PPP, y0 + 0.30*PPP, x_contra + ANCHO - 0.30*PPP, y0 + ALTO - 0.30*PPP), outline=oro, width=2)
    y = y0 + 0.85 * PPP
    if cub.get("gancho"):   # frase de cabecera de contracubierta (Archivo Arcano)
        y = parrafo(d, (x0, y, x1, 0), cub["gancho"].upper(), fuente("Cinzel.ttf", 0.17 * PPP, "SemiBold"), oro, 1.3, centrado=True) + 0.25 * PPP
    else:
        texto_espaciado(d, ((x0 + x1) / 2, y), C["nombre"].upper() if col != "archivo-lupin" else "EL ARCHIVO LUPIN",
                        fuente("Cinzel.ttf", 0.11 * PPP, "Medium"), oro, 0.25)
        y += 0.45 * PPP
        d.text(((x0 + x1) / 2, y), L["titulo"], font=fuente("CormorantGaramond.ttf", 0.22 * PPP, "Medium"), fill=crema, anchor="mm")
        y += 0.5 * PPP
    centrar_sinopsis = col == "archivo-arcano"
    for bloque in cub.get("sinopsis", "").split("\n\n"):
        y = parrafo(d, (x0, y, x1, 0), bloque, fuente("CormorantGaramond.ttf", 0.165 * PPP, "Medium"), crema, centrado=centrar_sinopsis) + 0.1 * PPP
    if cub.get("cita"):
        y += 0.25 * PPP
        y = parrafo(d, (x0 + 0.2 * PPP, y, x1 - 0.2 * PPP, 0), cub["cita"], fuente("CormorantGaramond-Italic.ttf", 0.17 * PPP, "Medium Italic"), oro, centrado=True)
        if cub.get("cita_autor"):
            texto_espaciado(d, ((x0 + x1) / 2, y + 0.12 * PPP), cub["cita_autor"].upper(), fuente("Cinzel.ttf", 0.07 * PPP), oro, 0.2)
    texto_espaciado(d, ((x0 + x1) / 2, y0 + ALTO - 1.75 * PPP), "EL GABINETE NEGRO", fuente("Cinzel.ttf", 0.1 * PPP, "Medium"), oro, 0.25)
    d.text((x0, y0 + ALTO - 0.6 * PPP), "ELGABINETENEGRO.COM", font=fuente("Cinzel.ttf", 0.075 * PPP), fill=oro, anchor="lm")
    # Espacio reservado para el código de barras de KDP (2 x 1,2 in, abajo a la derecha, a 0,25 in del corte):
    # se deja libre, SIN recuadro blanco (KDP lo coloca por su cuenta y el recuadro quedaba desplazado; 18-11-2026).
    # Solo se marca en la vista previa con guías.
    bxr = x_contra + ANCHO - 0.4 * PPP; byb = y0 + ALTO - 0.4 * PPP
    caja_barras = (bxr - 2 * PPP, byb - 1.2 * PPP, bxr, byb)
    out = dir_proy / "cubierta"; out.mkdir(exist_ok=True)
    sufijo = "tapa_dura" if tapa_dura else "kdp"
    lienzo.save(out / f"{slug}_cubierta_{sufijo}{sufv}.pdf", dpi=(W / W_in, H / H_in))
    guia = lienzo.copy(); dg = ImageDraw.Draw(guia)
    xs = (x_contra, x_contra + ANCHO, x_lomo, x_lomo + lomo, x_portada, x_portada + ANCHO)
    for x in xs: dg.line((x, 0, x, H), fill="#ff00ff", width=3)
    for yy in (y0, y0 + ALTO): dg.line((0, yy, W, yy), fill="#ff00ff", width=3)
    dg.rectangle(caja_barras, outline="#ff00ff", width=3)   # zona del código de barras (solo en la vista previa)
    guia.thumbnail((2400, 2400)); guia.save(out / f"{slug}_cubierta_{sufijo}{sufv}.jpg", quality=88)
    (portada_dada(portada, 1600, 2560) if portada is not None else componer(col, L, C, ilu, 1600, 2560)).save(out / f"{slug}_portada_ebook{sufv}.jpg", quality=92)
    aviso = "  ¡LOMO PROVISIONAL! Copia ancho_total_in, alto_total_in y lomo_in de la calculadora de KDP." if provisional else ""
    print(f"Cubierta {'tapa dura' if tapa_dura else 'tapa blanda'}: {paginas} págs, papel {papel}, "
          f"lomo {lomo / MM:.2f} mm, total {W_in:.3f} x {H_in:.3f} in ({W / MM:.1f} x {H / MM:.1f} mm){aviso}")

if __name__ == "__main__":
    main()

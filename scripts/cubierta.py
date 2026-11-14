#!/usr/bin/env python3
"""Cubiertas de El Gabinete Negro (KDP tapa blanda 6x9 y ebook).

Uso:  python3 scripts/cubierta.py proyectos/<slug> [--variante N]

Lee la sección [cubierta] de proyectos/<slug>/libro.toml:
    ilustracion = "cubierta/ilustracion.jpg"   # arte de portada (dominio público o propio)
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
import re, subprocess, sys, tomllib, json
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

def parrafo(d, caja, txt, f, color, interlineado=1.35, centrado=False):
    x0, y0, x1, _ = caja
    palabras, lineas, actual = txt.split(), [], ""
    for p in palabras:
        prueba = (actual + " " + p).strip()
        if d.textlength(prueba.replace("*", ""), font=f) <= x1 - x0: actual = prueba
        else: lineas.append(actual); actual = p
    if actual: lineas.append(actual)
    y = y0
    for l in lineas:
        limpio = l.replace("*", "")
        x = x0 + ((x1 - x0) - d.textlength(limpio, font=f)) / 2 if centrado else x0
        d.text((x, y), limpio, font=f, fill=color)
        y += f.size * interlineado
    return y

def encaja(img, w, h):
    return ImageOps.fit(img.convert("RGB"), (int(w), int(h)), Image.LANCZOS)

# ------------------------------------------------------------------ portadas por colección
# Cada función dibuja la portada en un lienzo de w x h (sirve para KDP y para ebook).

def portada_limite_abisal(L, C, ilu, w, h):
    est = C["cubierta"]; im = Image.new("RGB", (w, h), hexa(est["fondo"])); d = ImageDraw.Draw(im)
    u = w / 1253
    texto_espaciado(d, (w/2, 155*u), L["autor"].upper(), fuente("Carlito-Regular.ttf", 46*u), "#f0f0f0", 0.12)
    ft = fuente("CormorantGaramond.ttf", 175*u, "Medium")
    lineas = L.get("titulo_portada", L["titulo"].upper()).split("|")
    y = 330*u
    for l in lineas:
        sombra = Image.new("L", (w, h), 0); ds = ImageDraw.Draw(sombra)
        ds.text((w/2+6*u, y+6*u), l.strip(), font=ft, fill=255, anchor="mm")
        im.paste((10, 12, 14), mask=sombra.filter(ImageFilter.GaussianBlur(4*u)))
        d.text((w/2, y), l.strip(), font=ft, fill=est["acento"], anchor="mm")
        y += 150*u
    if L.get("subtitulo_portada"):
        d.text((w/2, y + 10*u), L["subtitulo_portada"], font=fuente("CormorantGaramond.ttf", 52*u, "Medium"), fill="#c9d6e0", anchor="mm")
    bx, by, bw, bh = 235*u, 615*u, 783*u, 1130*u
    if ilu: im.paste(encaja(ilu, bw, bh), (int(bx), int(by)))
    texto_espaciado(d, (w/2, 1815*u), "EL GABINETE NEGRO", fuente("Carlito-Regular.ttf", 36*u), "#f0f0f0", 0.2)
    texto_espaciado(d, (w/2, 1870*u), "COLECCIÓN LÍMITE ABISAL", fuente("Carlito-Regular.ttf", 22*u), "#8fa3b4", 0.2)
    d.text((w/2, 1905*u), f"Vol. {L['volumen']}", font=fuente("Carlito-Regular.ttf", 22*u), fill="#8fa3b4", anchor="mm")
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
    texto_espaciado(d, (w/2, by+bh-95*u), L["autor"].upper(), fuente("Cinzel.ttf", 54*u, "SemiBold"), "#e2c99a", 0.1)
    texto_espaciado(d, (w/2, 1795*u), f"VOL.{L['volumen']}", fuente("CormorantGaramond.ttf", 40*u, "Medium"), "#f2ece0", 0.25)
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

def portada_archivo_arcano(L, C, ilu, w, h):
    # Sin referencia aún: composición tipo Cámara Sellada con tipografía de biblioteca antigua.
    im = portada_camara_sellada(L, {**C, "cubierta": {**C["cubierta"], "acento": C["cubierta"]["acento"]}}, ilu, w, h)
    d = ImageDraw.Draw(im); u = w / 1253
    d.rectangle((0, 225*u, w, 285*u), fill=C["cubierta"]["fondo"])
    texto_espaciado(d, (w/2, 255*u), "COLECCIÓN ARCHIVO ARCANO", fuente("CormorantGaramond.ttf", 30*u, "Medium"), "#f2ece0", 0.25)
    return im

def componer(coleccion, L, C, ilu, w, h):
    """Las portadas de referencia miden 1253 x 2000 (proporción 1,6, la del ebook). En imprenta
    (6,125 x 9,25 in con sangrado, 1,51) se compone a 1,6 y se ajusta sobre el color de fondo."""
    if coleccion == "archivo-lupin":
        return PORTADAS[coleccion](L, C, ilu, w, h)
    base = PORTADAS[coleccion](L, C, ilu, w, round(w * 2000 / 1253))
    return ImageOps.pad(base, (w, h), color=hexa(C["cubierta"]["fondo"]))

PORTADAS = {"limite-abisal": portada_limite_abisal, "camara-sellada": portada_camara_sellada,
            "archivo-lupin": portada_archivo_lupin, "archivo-arcano": portada_archivo_arcano}

# ------------------------------------------------------------------ cubierta completa

def main():
    dir_proy = (Path.cwd() / sys.argv[1]).resolve(); slug = dir_proy.name
    meta = tomllib.loads((dir_proy / "libro.toml").read_text(encoding="utf-8"))
    C = json.loads((RAIZ / "colecciones" / f"{meta['coleccion']}.json").read_text(encoding="utf-8"))
    cub = meta.get("cubierta", {})
    L = {**meta, **cub}
    ilu = Image.open(dir_proy / cub["ilustracion"]) if cub.get("ilustracion") else None
    paginas = cub.get("paginas", 0)
    if not paginas:
        pdf = dir_proy / "interior" / f"{slug}_interior_6x9.pdf"
        paginas = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout).group(1))
    papel = cub.get("papel", "crema")
    lomo = paginas * GROSOR[papel] * PPP
    W = int(2 * ANCHO + lomo + 2 * SANGRADO); H = int(ALTO + 2 * SANGRADO)
    est = C["cubierta"]
    lienzo = Image.new("RGB", (W, H), hexa(est["fondo"])); d = ImageDraw.Draw(lienzo)
    x_lomo = SANGRADO + ANCHO; x_portada = x_lomo + lomo
    # Portada (ocupa del lomo al borde exterior con sangrado)
    pw, ph = int(W - x_portada), H
    lienzo.paste(componer(meta["coleccion"], L, C, ilu, pw, ph), (int(x_portada), 0))
    # Lomo (KDP permite texto si > 79 páginas)
    crema = est["texto"]; oro = est["acento"]
    if paginas > 79:
        tira = Image.new("RGB", (H, max(1, int(lomo))), hexa(est["fondo"])); dt = ImageDraw.Draw(tira)
        t = max(18, int(lomo * 0.42))
        f_tit = fuente("BodoniModa.ttf", t, "Black") if meta["coleccion"] == "archivo-lupin" else fuente("Cinzel.ttf", t, "SemiBold")
        lomo_tit = "EL ARCHIVO LUPIN" if meta["coleccion"] == "archivo-lupin" else L["titulo"].upper()
        dt.text((H * 0.40, lomo / 2), lomo_tit, font=f_tit, fill=crema, anchor="mm")
        dt.text((H * 0.76, lomo / 2), L["autor"].upper(), font=fuente("Cinzel.ttf", int(t * 0.7), "Medium"), fill=oro, anchor="mm")
        dt.text((H * 0.07, lomo / 2), str(L.get("dossier", L["volumen"])), font=fuente("Cinzel.ttf", int(t * 0.8), "Medium"), fill=oro, anchor="mm")
        lienzo.paste(tira.rotate(-90, expand=True), (int(x_lomo), 0))
    # Contracubierta
    m = 0.5 * PPP; x0, x1 = SANGRADO + m, SANGRADO + ANCHO - m
    y = SANGRADO + 0.75 * PPP
    texto_espaciado(d, ((x0 + x1) / 2, y), C["nombre"].upper() if meta["coleccion"] != "archivo-lupin" else "EL ARCHIVO LUPIN",
                    fuente("Cinzel.ttf", 0.11 * PPP, "Medium"), oro, 0.25)
    y += 0.45 * PPP
    d.text(((x0 + x1) / 2, y), L["titulo"], font=fuente("CormorantGaramond.ttf", 0.22 * PPP, "Medium"), fill=crema, anchor="mm")
    y += 0.5 * PPP
    for bloque in cub.get("sinopsis", "").split("\n\n"):
        y = parrafo(d, (x0, y, x1, 0), bloque, fuente("CormorantGaramond.ttf", 0.155 * PPP, "Medium"), crema) + 0.08 * PPP
    if cub.get("cita"):
        y += 0.25 * PPP
        y = parrafo(d, (x0 + 0.2 * PPP, y, x1 - 0.2 * PPP, 0), cub["cita"], fuente("CormorantGaramond-Italic.ttf", 0.17 * PPP, "Medium Italic"), oro, centrado=True)
        if cub.get("cita_autor"):
            texto_espaciado(d, ((x0 + x1) / 2, y + 0.12 * PPP), cub["cita_autor"].upper(), fuente("Cinzel.ttf", 0.07 * PPP), oro, 0.2)
    texto_espaciado(d, ((x0 + x1) / 2, SANGRADO + ALTO - 1.75 * PPP), "EL GABINETE NEGRO", fuente("Cinzel.ttf", 0.1 * PPP, "Medium"), oro, 0.25)
    d.text((x0, SANGRADO + ALTO - 0.55 * PPP), "ELGABINETENEGRO.COM", font=fuente("Cinzel.ttf", 0.075 * PPP), fill=oro, anchor="lm")
    # Hueco para código de barras de KDP (2 x 1,2 in, abajo a la derecha, a 0,25 in de los bordes)
    bxr = SANGRADO + ANCHO - 0.25 * PPP; byb = SANGRADO + ALTO - 0.25 * PPP
    d.rectangle((bxr - 2 * PPP, byb - 1.2 * PPP, bxr, byb), fill="#ffffff")
    out = dir_proy / "cubierta"; out.mkdir(exist_ok=True)
    lienzo.save(out / f"{slug}_cubierta_kdp.pdf", resolution=PPP)
    guia = lienzo.copy(); dg = ImageDraw.Draw(guia)
    for x in (SANGRADO, x_lomo, x_portada, W - SANGRADO): dg.line((x, 0, x, H), fill="#ff00ff", width=3)
    for yy in (SANGRADO, H - SANGRADO): dg.line((0, yy, W, yy), fill="#ff00ff", width=3)
    guia.thumbnail((2400, 2400)); guia.save(out / f"{slug}_cubierta_kdp.jpg", quality=88)
    componer(meta["coleccion"], L, C, ilu, 1600, 2560).save(out / f"{slug}_portada_ebook.jpg", quality=92)
    print(f"Cubierta: {paginas} págs, papel {papel}, lomo {lomo / MM:.2f} mm, total {W / MM:.1f} x {H / MM:.1f} mm")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Maquetación de un proyecto de El Gabinete Negro.

Uso:  python3 scripts/maquetar.py proyectos/<slug> [--solo pdf|docx|epub]

Lee  proyectos/<slug>/libro.toml   (metadatos; ver plantillas/libro.ejemplo.toml)
     proyectos/<slug>/texto/*.md   (en orden alfabético; ver CLAUDE.md, «Formato del texto»)
Genera en proyectos/<slug>/:
     build/libro.json                       datos intermedios
     interior/<slug>_interior_6x9.pdf      PDF de imprenta (Typst, plantillas/libro.typ)
     ebook/<slug>_kindle_create.docx        para importar en Kindle Create y exportar el KPF
     ebook/<slug>.epub                      EPUB (alternativa: KDP lo acepta directamente)
"""
import json, re, subprocess, sys, tomllib
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------- lectura

INLINE = re.compile(r"(\*\*\*[^*]+\*\*\*|\*\*[^*]+\*\*|\*[^*]+\*)")

def runs(texto):
    """'Hola *mundo*' -> [['Hola ', ''], ['mundo', 'i']]"""
    out = []
    for trozo in INLINE.split(texto):
        if not trozo:
            continue
        if trozo.startswith("***"):
            out.append([trozo[3:-3], "bi"])
        elif trozo.startswith("**"):
            out.append([trozo[2:-2], "b"])
        elif trozo.startswith("*") and trozo.endswith("*") and len(trozo) > 2:
            out.append([trozo[1:-1], "i"])
        else:
            out.append([trozo, ""])
    return out

IMAGEN = re.compile(r"^!\[(.*)\]\((.+)\)$")

def bloques_de(lineas, base=RAIZ):
    """Convierte líneas Markdown (sin títulos) en bloques.

    `![pie opcional](ruta)` en una línea propia inserta una imagen (ruta relativa al proyecto)."""
    bloques, buf, tipo = [], [], "p"
    def cierra():
        nonlocal buf, tipo
        if buf:
            bloques.append({tipo: runs(" ".join(buf))})
        buf, tipo = [], "p"
    for l in lineas:
        s = l.strip()
        if not s:
            cierra(); continue
        if s in ("***", "* * *", "---"):
            cierra(); bloques.append({"sep": True}); continue
        if s.startswith(">"):
            if tipo != "cita": cierra(); tipo = "cita"
            buf.append(s.lstrip("> ").strip()); continue
        if s.startswith("->") and s.endswith("<-"):
            cierra(); bloques.append({"centrado": runs(s[2:-2].strip())}); continue
        if s.startswith("-->"):
            cierra(); bloques.append({"derecha": runs(s[3:].strip())}); continue
        m = IMAGEN.match(s)
        if m:
            ruta = (base / m.group(2)).resolve()
            if not ruta.exists():
                sys.exit(f"Falta la imagen {ruta}")
            cierra(); bloques.append({"imagen": str(ruta.relative_to(RAIZ)), "pie": runs(m.group(1).strip())}); continue
        buf.append(s)
    cierra()
    return bloques

# Página de petición de reseña (encargo del 20-11-2026): breve, sin promesas ni incentivos
# (Amazon prohíbe ofrecer nada a cambio de una reseña). Se desactiva con `pagina_resena = false`
# en libro.toml; el texto puede cambiarse con `texto_resena = ["párrafo", …]`.
RESENA_TITULO = "Una petición del Gabinete"
RESENA = [
    "Si este libro le ha acompañado en alguna noche larga, le agradeceríamos que dejara una breve reseña "
    "en la tienda donde lo adquirió.",
    "Bastan unas líneas, favorables o no. Una opinión sincera ayuda a otros lectores a encontrar estas páginas "
    "y permite a una editorial independiente seguir rescatando del olvido textos que merecen volver a leerse.",
    "Gracias por su lectura.",
]

def lee_proyecto(dir_proy: Path):
    meta = tomllib.loads((dir_proy / "libro.toml").read_text(encoding="utf-8"))
    col = json.loads((RAIZ / "colecciones" / f"{meta['coleccion']}.json").read_text(encoding="utf-8"))
    ficheros = sorted((dir_proy / "texto").glob("*.md"))
    prologo, apendice, cuerpo = [], [], []
    capitulos_impar = meta.get("capitulos_en_impar", False)
    for f in ficheros:
        lineas = f.read_text(encoding="utf-8").splitlines()
        nombre = f.stem.lower()
        if "prologo" in nombre:
            prologo += bloques_de([l for l in lineas if not l.startswith("#")], dir_proy); continue
        if "apendice" in nombre:
            apendice += bloques_de([l for l in lineas if not l.startswith("#")], dir_proy); continue
        actual, buf = None, []
        def vuelca():
            if actual is not None and actual["tipo"] == "capitulo":
                actual["bloques"] = bloques_de(buf, dir_proy)
        for l in lineas:
            if l.startswith("% "):
                vuelca(); buf = []
                tit, _, sub = l[2:].partition("|")   # «% TÍTULO|Subtítulo»
                actual = {"tipo": "titulo-obra", "titulo": tit.strip(), "subtitulo": sub.strip() or None}; cuerpo.append(actual)
            elif l.startswith("# "):
                vuelca(); buf = []
                actual = {"tipo": "parte", "titulo": l[2:].strip(), "subtitulo": None}; cuerpo.append(actual)
            elif l.startswith("## "):
                if actual is not None and actual["tipo"] == "parte" and actual["subtitulo"] is None and not any(x.strip() for x in buf) \
                        and not re.match(r"[IVXLC]+(\. |$)", l[3:].strip()):   # «## I» o «## I. TÍTULO» es capítulo, no subtítulo
                    actual["subtitulo"] = l[3:].strip(); continue
                vuelca(); buf = []
                actual = {"tipo": "capitulo", "titulo": l[3:].strip(), "impar": capitulos_impar, "bloques": []}
                cuerpo.append(actual)
            else:
                buf.append(l)
        vuelca()
    datos = {
        "titulo": meta["titulo"], "subtitulo": meta.get("subtitulo"), "autor": meta["autor"],
        "volumen": meta.get("volumen", "x"),
        # «XX» → «Volumen XX»; un texto («Edición especial») se imprime tal cual
        "volumen_txt": (f"Volumen {meta.get('volumen', 'x')}" if re.fullmatch(r"[IVXLC]+|x", str(meta.get("volumen", "x")))
                        else str(meta.get("volumen"))),
        "isbn": meta.get("isbn", "En trámite"),
        # ISBN del ebook: el de KDP para tapa blanda (979-8…) no vale para el ebook; "" = sin línea de ISBN
        "isbn_ebook": meta.get("isbn_ebook", meta.get("isbn", "En trámite")),
        "creditos_obra": meta.get("creditos_obra"), "traduccion": meta.get("traduccion"),
        "proximo_titulo": meta.get("proximo_titulo"),
        "resena": ({"titulo": RESENA_TITULO, "texto": meta.get("texto_resena", RESENA)}
                   if meta.get("pagina_resena", True) else None),
        "prologo": prologo, "apendice": apendice, "cuerpo": cuerpo, "coleccion": col,
    }
    return meta, col, datos

# ---------------------------------------------------------------- PDF (Typst)

def hace_pdf(dir_proy, slug, json_path):
    import typst
    out = dir_proy / "interior" / f"{slug}_interior_6x9.pdf"
    out.parent.mkdir(exist_ok=True)
    def compila(extra):
        typst.compile(str(RAIZ / "plantillas" / "libro.typ"), output=str(out), root=str(RAIZ),
                      font_paths=[str(RAIZ / "fuentes")],
                      sys_inputs={"datos": "/" + str(json_path.relative_to(RAIZ)), **extra})
        info = subprocess.run(["pdfinfo", str(out)], capture_output=True, text=True).stdout
        return int(re.search(r"Pages:\s+(\d+)", info).group(1))
    paginas = compila({})
    if paginas % 2:  # la imprenta exige un número par de páginas
        paginas = compila({"blanca_final": "1"})
    print(f"PDF: {out.relative_to(RAIZ)} ({paginas} páginas)")
    return out, paginas

# ---------------------------------------------------------------- DOCX para Kindle Create

def hace_docx(dir_proy, slug, meta, col, datos):
    from docx import Document
    from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
    from docx.shared import Pt, Cm, RGBColor
    from docx.oxml.ns import qn

    d = Document()
    sec = d.sections[0]
    sec.page_width, sec.page_height = Cm(15.24), Cm(22.86)
    for m in ("top_margin", "bottom_margin", "left_margin", "right_margin"):
        setattr(sec, m, Cm(2.03))

    def fuente(estilo, nombre, tam, negrita=None, color=None):
        st = d.styles[estilo]
        st.font.name = nombre; st.font.size = Pt(tam)
        st.element.rPr.rFonts.set(qn("w:eastAsia"), nombre)
        if negrita is not None: st.font.bold = negrita
        st.font.color.rgb = color or RGBColor(0, 0, 0)
        return st
    n = fuente("Normal", "Cambria", 11)
    n.paragraph_format.space_after = Pt(6); n.paragraph_format.line_spacing = 1.15
    for est, tam in (("Heading 1", 14), ("Heading 2", 13)):
        h = fuente(est, "Calibri", tam, True)
        h.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        h.paragraph_format.space_before = Pt(24); h.paragraph_format.space_after = Pt(24)
        h.paragraph_format.page_break_before = True
        h.font.italic = False

    def p_runs(rs, align=WD_ALIGN_PARAGRAPH.JUSTIFY, estilo=None):
        p = d.add_paragraph(style=estilo); p.alignment = align
        for t, s in rs:
            r = p.add_run(t); r.italic = "i" in s; r.bold = "b" in s
        return p
    def bloques(bs):
        for b in bs:
            if "sep" in b: p_runs([["* * *", ""]], WD_ALIGN_PARAGRAPH.CENTER)
            elif "cita" in b:
                p = p_runs(b["cita"]); p.paragraph_format.left_indent = Cm(1); p.paragraph_format.right_indent = Cm(1)
            elif "centrado" in b: p_runs(b["centrado"], WD_ALIGN_PARAGRAPH.CENTER)
            elif "derecha" in b: p_runs(b["derecha"], WD_ALIGN_PARAGRAPH.RIGHT)
            elif "imagen" in b:
                p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.add_run().add_picture(str(RAIZ / b["imagen"]), width=Cm(11))
                if b["pie"]: p_runs(b["pie"], WD_ALIGN_PARAGRAPH.CENTER)
            else: p_runs(b["p"])
    def salto():
        d.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
    def centrado(texto, tam=None, negrita=False, antes=0):
        p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(antes)
        r = p.add_run(texto); r.bold = negrita
        if tam: r.font.size = Pt(tam)

    if col.get("emblema_inicial"):
        p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.add_run().add_picture(str(RAIZ / col["emblema_inicial"]), width=Cm(3.2)); salto()
    # Portadilla
    centrado(datos["titulo"], 22, True, 60)
    if datos["subtitulo"]: centrado(datos["subtitulo"], *((14, False) if len(datos["subtitulo"]) > 40 else (22, True)))
    centrado(datos["autor"], 14, antes=30)
    centrado(f"{col['linea_coleccion']} · {datos['volumen']}\nEl Gabinete Negro", 9, antes=60)
    salto()
    # Créditos
    for t in ["© De la presente edición: El Gabinete Negro", f"Colección: {col['nombre']}\n{datos['volumen_txt']}"] \
             + (datos["creditos_obra"] or []) \
             + ["Esta edición utiliza un texto en dominio público revisado y adaptado para esta colección."] \
             + ([datos["traduccion"]] if datos["traduccion"] else []) \
             + ([f"ISBN: {datos['isbn_ebook']}"] if datos["isbn_ebook"] else []) + ["Edición publicada por El Gabinete Negro", "Reservados todos los derechos de esta edición."]:
        p = d.add_paragraph(t); p.runs[0].font.size = Pt(9.5)
    salto()
    if col.get("ex_libris"):
        p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.add_run().add_picture(str(RAIZ / col["ex_libris"]), width=Cm(8)); salto()
    # Manifiesto
    if col.get("manifiesto_subtitulo"):
        centrado(col["manifiesto_titulo"], negrita=True); centrado(col["manifiesto_subtitulo"], negrita=True)
    else:
        d.add_paragraph().add_run(col["manifiesto_titulo"]).bold = True
    for g in col["manifiesto"]:
        p = d.add_paragraph("\n".join(g))
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY if len(g) == 1 else WD_ALIGN_PARAGRAPH.LEFT
    # Prólogo
    if datos["prologo"]:
        d.add_heading(col["prologo_titulo"], level=2)
        bloques(datos["prologo"])
        p_runs([["— El Editor\nEl Gabinete Negro", ""]], WD_ALIGN_PARAGRAPH.RIGHT)
    # Cuerpo
    for s in datos["cuerpo"]:
        if s["tipo"] == "titulo-obra":
            salto(); centrado(s["titulo"], 12, True, 70)
            if s.get("subtitulo"): centrado(s["subtitulo"], 11)
        elif s["tipo"] == "parte":
            d.add_heading(s["titulo"], level=1)
            if s["subtitulo"]: centrado(s["subtitulo"], 14, True)
        else:
            d.add_heading(s["titulo"], level=2)
            bloques(s["bloques"])
    # Apéndice
    d.add_heading("APÉNDICE EXPLICATIVO", level=2)
    bloques(datos["apendice"])
    salto()
    r = d.add_paragraph().add_run("El Gabinete Negro"); r.bold = True; r.italic = True
    d.add_paragraph("\n".join(col["apendice"]))
    if col.get("proximo_titulo") and datos["proximo_titulo"]:
        centrado("Próximo título: " + (datos["proximo_titulo"] or ""))
    if datos.get("resena"):
        salto(); centrado(datos["resena"]["titulo"], 12, True, 60)
        for t in datos["resena"]["texto"]:
            p = d.add_paragraph(t); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_runs([["— El Gabinete Negro", ""]], WD_ALIGN_PARAGRAPH.RIGHT)
    # Sin índice: Kindle Create genera la tabla de contenidos a partir de los títulos.
    out = dir_proy / "ebook" / f"{slug}_kindle_create.docx"
    out.parent.mkdir(exist_ok=True)
    d.core_properties.title = datos["titulo"]; d.core_properties.author = datos["autor"]
    d.core_properties.language = "es-ES"
    d.save(out)
    print(f"DOCX: {out.relative_to(RAIZ)}")
    return out

# ---------------------------------------------------------------- EPUB

def hace_epub(dir_proy, slug, docx_path, meta, datos):
    out = dir_proy / "ebook" / f"{slug}.epub"
    cmd = ["pandoc", str(docx_path), "-o", str(out), "--split-level=2", "--toc", "--toc-depth=2",
           "-M", f"title={datos['titulo']}", "-M", f"author={datos['autor']}", "-M", "lang=es-ES",
           "-M", "publisher=El Gabinete Negro", "--css", str(RAIZ / "plantillas" / "ebook.css")]
    portada = dir_proy / "cubierta" / f"{slug}_portada_ebook.jpg"
    if portada.exists():
        cmd += ["--epub-cover-image", str(portada)]
    subprocess.run(cmd, check=True)
    print(f"EPUB: {out.relative_to(RAIZ)}")
    return out

# ----------------------------------------------------------------

def main():
    dir_proy = (Path.cwd() / sys.argv[1]).resolve()
    solo = sys.argv[sys.argv.index("--solo") + 1] if "--solo" in sys.argv else None
    slug = dir_proy.name
    meta, col, datos = lee_proyecto(dir_proy)
    build = dir_proy / "build"; build.mkdir(exist_ok=True)
    jp = build / "libro.json"
    jp.write_text(json.dumps(datos, ensure_ascii=False, indent=1), encoding="utf-8")
    capitulos = sum(1 for s in datos["cuerpo"] if s["tipo"] == "capitulo")
    palabras = sum(len(r[0].split()) for s in datos["cuerpo"] if s["tipo"] == "capitulo"
                   for b in s["bloques"] for k in ("p", "cita", "centrado", "derecha") if k in b for r in b[k])
    print(f"{datos['titulo']} — {col['nombre']} — {capitulos} capítulos, {palabras} palabras")
    if solo in (None, "pdf"):
        hace_pdf(dir_proy, slug, jp)
    if solo in (None, "docx", "epub"):
        dx = hace_docx(dir_proy, slug, meta, col, datos)
        if solo in (None, "epub"):
            hace_epub(dir_proy, slug, dx, meta, datos)

if __name__ == "__main__":
    main()

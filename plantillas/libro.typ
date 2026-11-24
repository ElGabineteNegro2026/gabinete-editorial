// =====================================================================
// El Gabinete Negro — plantilla de interior para imprenta (KDP tapa blanda)
// Formato 6 x 9 pulgadas (15,24 x 22,86 cm), común a todas las colecciones.
// Se alimenta de un JSON generado por scripts/maquetar.py:
//   typst compile --root . --font-path fuentes \
//         --input datos=proyectos/<slug>/build/libro.json \
//         plantillas/libro.typ salida.pdf
// Las diferencias entre colecciones vienen de colecciones/<coleccion>.json
// (manifiesto, emblema, ex libris, título del prólogo, «Próximo título»).
// =====================================================================

#let L = json(sys.inputs.at("datos"))
#let C = L.coleccion

// ---------- Tipografía y página (medidas de las plantillas Word) ----------
#let serif = ("Caladea", "Cambria")       // Caladea = métrica de Cambria, libre
#let sans = ("Carlito", "Calibri")        // Carlito = métrica de Calibri, libre
#let cuerpo = 11pt

#set document(title: L.titulo, author: L.autor)
#set text(font: serif, size: cuerpo, lang: "es", region: "ES",
          hyphenate: true, top-edge: "ascender", bottom-edge: "descender")
#set par(justify: true, leading: 0.18em, spacing: 6pt + 0.18em, first-line-indent: 0pt)

#set page(
  width: 6in, height: 9in,
  margin: (inside: 2.1cm, outside: 1.9cm, top: 2cm, bottom: 2.5cm),
  footer-descent: 40%,
  footer: context {
    // Sin folio en las blancas que deja a-impar(): fin de sección en p-1 e inicio en p+1
    let p = here().page()
    // (o la marca de fin está en lo alto de esta misma página: la sección anterior era una página aislada, p. ej. el manifiesto)
    let blanca = query(<ini>).any(m => m.location().page() == p + 1) and query(<fs>).any(m => m.location().page() == p - 1 or (m.location().page() == p and m.location().position().y < 2cm + 1pt))
    if not blanca { align(center, text(size: 9pt, str(p))) }
  },
)

// Páginas sin folio: preliminares y blancas
#let sin-folio(body) = page(footer: none, body)

// Salta a la siguiente página impar (recto) dejando la par en blanco y sin folio
#let a-impar() = {
  [#metadata("fs") <fs>]
  pagebreak(to: "odd", weak: true)
  [#metadata("ini") <ini>]
}

// ---------- Estilos de título ----------
// Capítulo / relato: Calibri (Carlito) negrita 13 pt, centrado (estilo Heading 2 de las plantillas)
#show heading.where(level: 2): it => {
  set par(justify: false)
  block(above: 0pt, below: 1.4cm, width: 100%,
    align(center, text(font: sans, size: 13pt, weight: "bold", it.body)))
}
// Parte: Calibri negrita 14 pt, centrada, en página propia
#show heading.where(level: 1): it => {
  set par(justify: false)
  align(center, text(font: sans, size: 14pt, weight: "bold", it.body))
}

#let runs(rs) = {
  for r in rs {
    let (t, s) = (r.at(0), r.at(1))
    if s == "i" { emph(t) } else if s == "b" { strong(t) } else if s == "bi" { strong(emph(t)) } else { t }
  }
}

#let bloque(b) = {
  if "sep" in b { align(center, block(above: 1em, below: 1em, text(tracking: 0.3em)[\* \* \*])) }
  else if "cita" in b { pad(left: 1cm, right: 1cm, par(runs(b.cita))) }
  else if "centrado" in b { align(center, par(justify: false, runs(b.centrado))) }
  else if "derecha" in b { align(right, par(justify: false, runs(b.derecha))) }
  else if "imagen" in b {
    block(above: 1.2em, below: 1.2em, breakable: false, width: 100%, align(center, {
      image("/" + b.imagen, width: 100%)
      if b.pie.len() > 0 { v(0.4em); text(size: 9pt, par(justify: false, runs(b.pie))) }
    }))
  }
  else { par(runs(b.p)) }
}

// ======================= PRELIMINARES =======================

// Emblema inicial (Archivo Lupin)
#if C.emblema_inicial != none {
  sin-folio(align(center + horizon, image("../" + C.emblema_inicial, width: 3.2cm)))
  sin-folio[]
}

// Portadilla
#sin-folio({
  set par(justify: false)
  v(2.2cm)
  align(center, text(size: 22pt, weight: "bold", hyphenate: false, L.titulo))
  if L.subtitulo != none and L.subtitulo != "" {
    v(0.2cm)
    align(center, text(size: 22pt, weight: "bold", hyphenate: false, L.subtitulo))
  }
  v(1.6cm)
  align(center, text(size: 14pt, L.autor))
  v(2.4cm)
  align(center, text(size: 9pt)[#C.linea_coleccion · #L.volumen \ El Gabinete Negro])
})

// Créditos (verso)
#sin-folio({
  set text(size: 9.5pt)
  set par(justify: false)
  [© De la presente edición: El Gabinete Negro]
  parbreak()
  [Colección: #C.nombre \ #L.at("volumen_txt", default: "Volumen " + L.volumen)]
  v(0.4cm)
  if L.creditos_obra != none { for l in L.creditos_obra { par(l) } }
  v(0.6cm)
  par[Esta edición utiliza un texto en dominio público revisado y adaptado para esta colección.]
  if L.traduccion != none { par(L.traduccion) }
  par[ISBN: #L.isbn]
  v(0.6cm)
  par[Edición publicada por El Gabinete Negro]
  par[Reservados todos los derechos de esta edición.]
})

// Ex libris (Archivo Arcano)
#if C.ex_libris != none {
  sin-folio(align(center + horizon, image("../" + C.ex_libris, width: 8cm)))
  sin-folio[]
}

// Manifiesto editorial
#sin-folio({
  if C.manifiesto_subtitulo != none {
    align(center, text(weight: "bold", size: 10pt)[#C.manifiesto_titulo \ #C.manifiesto_subtitulo])
    v(0.8cm)
  } else {
    text(weight: "bold", size: 10pt, C.manifiesto_titulo)
    v(0.3cm)
  }
  for grupo in C.manifiesto { par(grupo.join(linebreak())) }
})

// ======================= PRÓLOGO =======================
#if L.prologo != none and L.prologo.len() > 0 {
  a-impar()
  heading(level: 2, C.prologo_titulo)
  for b in L.prologo { bloque(b) }
  v(1.2cm)
  align(right, par(justify: false)[— El Editor \ El Gabinete Negro])
}

// ======================= CUERPO =======================
#let previo = none
#for s in L.cuerpo {
  if s.tipo == "parte" {
    // Si va justo tras la página de título interior, comparte página con ella (como en Belfegor)
    if previo == "titulo-obra" { v(1.5cm) } else { a-impar(); v(4.5cm) }
    heading(level: 1, s.titulo)
    if s.subtitulo != none {
      v(0.3cm)
      align(center, text(font: sans, size: 14pt, weight: "bold", s.subtitulo))
    }
    // La parte ocupa su página; el capítulo siguiente empieza en impar
  } else if s.tipo == "titulo-obra" {
    // Página de título interior (p. ej. «BELFEGOR» antes de la primera parte)
    a-impar()
    v(2.5cm)
    align(center, text(font: sans, size: 12pt, weight: "bold", s.titulo))
    if s.at("subtitulo", default: none) != none {
      v(0.25cm)
      align(center, text(font: sans, size: 11pt, s.subtitulo))
    }
  } else {
    if s.at("impar", default: false) or previo == "parte" { a-impar() } else { pagebreak(weak: true) }
    v(1cm)
    heading(level: 2, s.titulo)
    for b in s.bloques { bloque(b) }
  }
  previo = s.tipo
}

// ======================= APÉNDICE =======================
#a-impar()
#v(1cm)
#heading(level: 2, "APÉNDICE EXPLICATIVO")
#if L.apendice != none { for b in L.apendice { bloque(b) } }
#pagebreak()
#{
  text(weight: "bold", style: "italic", size: 10pt)[El Gabinete Negro]
  v(0.5cm)
  pad(left: 1cm, right: 1cm, par(justify: false, C.apendice.join(linebreak())))
  if C.proximo_titulo and L.proximo_titulo not in (none, "") {
    v(0.8cm)
    align(center, par(justify: false)[Próximo título: #if L.proximo_titulo != none { emph(L.proximo_titulo) }])
  }
}

// ============ PETICIÓN DE RESEÑA (si no se desactiva en libro.toml) ============
#if L.at("resena", default: none) != none {
  pagebreak()
  v(5cm)
  align(center, text(font: sans, size: 13pt, weight: "bold", L.resena.titulo))
  v(0.8cm)
  pad(left: 1cm, right: 1cm, {
    set par(justify: false)
    for t in L.resena.texto { align(center, par(t)) }
  })
  v(0.4cm)
  pad(right: 1cm, align(right, text(style: "italic")[— El Gabinete Negro]))
}

// ======================= ÍNDICE =======================
#pagebreak(weak: true)
#{
  set par(justify: false, spacing: 0.6em)
  v(1cm)
  align(center, text(font: sans, size: 14pt, weight: "bold")[Índice])
  v(1cm)
  context {
    for t in query(heading) {
      let p = counter(page).at(t.location()).first()
      let sangria = if t.level == 2 { 0.5cm } else { 0cm }
      let cuerpo-h = if t.level == 1 { strong(t.body) } else { t.body }
      block(above: if t.level == 1 { 1em } else { 0.5em }, below: 0pt,
        // Sin link(): en el PDF de imprenta KDP elimina los enlaces como «marcas no imprimibles»
        pad(left: sangria, grid(columns: (auto, 1fr, auto), column-gutter: 3pt,
          text(size: 10pt, cuerpo-h),
          box(width: 100%, repeat(text(size: 10pt)[.#h(2pt)])),
          text(size: 10pt, str(p)))))
    }
  }
}

// Número total de páginas par (requisito de imprenta): maquetar.py compila, cuenta
// y, si sale impar, recompila con blanca_final=1 para añadir una página en blanco sin folio.
#if sys.inputs.at("blanca_final", default: "0") == "1" { page(footer: none, hide[.]) }

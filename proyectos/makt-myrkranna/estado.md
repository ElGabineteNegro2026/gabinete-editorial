# Makt myrkranna — Bram Stoker / Valdimar Ásmundsson · Límite Abisal, vol. XIX

**Fase:** **listo para KDP** (17-11-2026; lanzamiento esta semana)

## Decisiones del responsable
- 17-11-2026: entrega el manuscrito maquetado en Word (`MAKTMYRKRANNA_El_Gabinete_Negro_6x9_editable_final.doc`), con prólogo de «El Editor», apéndice, vol. XIX e ISBN 9798143163683 (ISBN gratuito de KDP, tapa blanda), y la portada definitiva (`cubierta/portada_responsable.jpg`). Pide revisar la maquetación, generar Word y PDF para KDP y diseñar la cubierta completa a partir de la portada.
- 17-11-2026: **la traducción es de la casa** → créditos «Traducción: El Gabinete Negro».
- 17-11-2026: «El capítulo desaparecido» es parte del texto (se mantiene).
- 17-11-2026: créditos como en su manuscrito («Primera publicación: 1901»).
- 17-11-2026: **aprobados sinopsis y cita de contracubierta**.
- 17-11-2026: **precio 14,49 € tapa blanda y 2,99 € ebook**. **Lanzamiento esta misma semana.**
- 17-11-2026: entrega la ilustración central original (1024 × 1536) para mejorar la resolución de la cubierta.

## Revisión de la maquetación (17-11-2026)
Texto pasado a `texto/*.md` (fuente original guardada fuera del repositorio). Correcciones:
- **Capitulares perdidas**: faltaba la primera letra en el arranque de los 16 capítulos de la segunda parte y de 31 entradas del diario de la primera («ientras», «abían», «yer», «olo Dios»…). Restituidas.
- **Párrafos partidos** a mitad de frase (14 casos: «Tiene que haberla visto / —le dije—», «significa / «mhai löhf»?»…). Unidos.
- La **Parte II y sus 17 capítulos** no tenían estilo de título en el Word (no salían en el índice ni los detectaría Kindle Create). Ahora son parte y capítulos.
- Capítulos al formato de la colección: «CAPÍTULO UNO / Lucia Western» → «I. LUCIA WESTERN». «PARTE I/II» → «PRIMERA/SEGUNDA PARTE».
- «PROLOGO DEL AUTOR» → «PRÓLOGO DEL AUTOR». Se suprime «Próximo título:» (norma del 17-11-2026).
- Fechas del diario homogéneas (negrita, a la derecha; unas lo estaban y otras no). Líneas de rayas «————» → separador de escena. Marcas de omisión «– – –» → «— — —». «...» → «…». «no-muertas» → «no muertas».
- Cursivas recuperadas (estilo «Énfasis» del Word): *Makt myrkranna*, *Drácula* (como título), *Mörkrets makter*, *Fjallkonan*.
- Se conservan las marcas de entrega del folletín (*Fjallkonan*, n.º…, fecha) alineadas a la derecha.
- Ortografía revisada con Hunspell es_ES: solo nombres propios y extranjerismos.

## Producción
- `interior/makt-myrkranna_interior_6x9.pdf`: **186 páginas**, fuentes incrustadas (Caladea, Carlito), revisadas portadilla, créditos, título interior, prólogos, partes, capítulos, apéndice e índice.
- `ebook/makt-myrkranna_kindle_create.docx` y `ebook/makt-myrkranna.epub` (con portada). **Sin ISBN** en el ebook (`isbn_ebook = ""`): el 979-8 de KDP es solo de la tapa blanda.
- `cubierta/makt-myrkranna_cubierta_kdp.pdf`: 12,667 × 9,250 in, lomo 10,64 mm (186 págs., papel blanco; calculado, no provisional). Portada del responsable tal cual; lomo y contracubierta (sinopsis + cita del prólogo de Stoker) en el estilo de la colección. `cubierta/makt-myrkranna_portada_ebook.jpg` 1600 × 2560.
- Scripts: `maquetar.py` admite `% TÍTULO|Subtítulo`, `isbn_ebook` y no confunde «## I. …» con subtítulo de parte; `cubierta.py` admite `portada = …` (portada ya diseñada).

## Cubierta a 300 ppp (17-11-2026)
- `cubierta/componer_portada.py`: amplía la portada del responsable a 2775 px de alto (9,25 in a 300 ppp) y sustituye el recuadro por la ilustración original (`cubierta/ilustracion_responsable.webp`), con el mismo encuadre (ajuste automático) y el mismo tono verde azulado (transferencia de color por canal). Ilustración a ≈ 271 ppp efectivos (antes 216); los textos de la portada proceden de la imagen de 1253 px, ampliados con enfoque suave.
- Resultado: `cubierta/portada_300ppp.png` → cubierta KDP y portada ebook regeneradas; EPUB con la portada nueva.

## Validación de KDP (18-11-2026)
- «Tamaño previsto 12,715 × 9,250; enviado 12,667 × 9,250»: el título está configurado en KDP con **papel crema** (lomo 186 × 0,0025 = 0,465 in) y la cubierta se había calculado para blanco (0,419 in). `papel = "crema"` → lomo 11,81 mm. Además `cubierta.py` truncaba el ancho a píxeles enteros (salía 12,713): ahora el PDF se guarda con el tamaño exacto en pulgadas → **12,715 × 9,250 in**.
- «Marcas no imprimibles en la p. 185»: eran los 23 enlaces internos del índice. Se quitan de `plantillas/libro.typ` (el PDF de imprenta queda sin anotaciones). El contenido de la página no cambia.

## Pendiente
- *Fjallkonan*: la tercera marca de la primera parte dice «n.º 7, 21 de febrero de 1900» entre la n.º 2 y la n.º 4 (y la n.º 7 vuelve a aparecer después): probable errata por n.º 3. Sin respuesta todavía; se mantiene como en el manuscrito.
- Si se quiere el máximo de nitidez en los textos de portada (título, autor, colección): exportar la portada desde el diseño original a ≥ 1840 × 2780 px y volver a ejecutar `componer_portada.py` (o usarla directamente).
- Al publicar: subir a KDP `interior/…_interior_6x9.pdf` (tapa blanda, 6 × 9, papel blanco, sin sangrado) y `cubierta/…_cubierta_kdp.pdf`; el ebook desde el DOCX en Kindle Create (o el EPUB). Confirmar el día exacto para `novedades/para-redes.md`.

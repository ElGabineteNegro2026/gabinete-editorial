# Makt myrkranna — Bram Stoker / Valdimar Ásmundsson · Límite Abisal, vol. XIX

**Fase:** cubierta → **revisión** (17-11-2026)

## Decisiones del responsable
- 17-11-2026: entrega el manuscrito maquetado en Word (`MAKTMYRKRANNA_El_Gabinete_Negro_6x9_editable_final.doc`), con prólogo de «El Editor», apéndice, vol. XIX e ISBN 9798143163683 (ISBN gratuito de KDP, tapa blanda), y la portada definitiva (`cubierta/portada_responsable.jpg`). Pide revisar la maquetación, generar Word y PDF para KDP y diseñar la cubierta completa a partir de la portada.

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

## Pendiente (CONSULTA)
- **Resolución de la portada**: 1253 × 2000 px → 216 ppp en imprenta (KDP recomienda 300). Pedir exportación mayor (≥ 1840 × 2780 px) y regenerar.
- **Derechos de la traducción**: los créditos no indican traductor. Stoker (†1912) y Ásmundsson (†1902) son dominio público, pero una traducción española ajena tendría derechos propios. Confirmar el origen y, si es de la casa, añadir `traduccion = "Traducción: El Gabinete Negro"`.
- *Fjallkonan*: la tercera marca de la primera parte dice «n.º 7, 21 de febrero de 1900» entre la n.º 2 y la n.º 4 (y la n.º 7 vuelve a aparecer después): probable errata por n.º 3 (finales de enero). Confirmar.
- «El capítulo desaparecido» (rótulo dentro del diario, antes de la entrada que empieza «Durante los últimos días»): se mantiene centrado en cursiva; confirmar si es del texto o una nota editorial que debe quitarse.
- Créditos: «Primera publicación» decía 1901; el apéndice indica entregas desde enero de 1900. Puesto «por entregas en Fjallkonan (1900-1901); en libro, 1901».
- Aprobar sinopsis y cita de contracubierta. Precio y fecha de lanzamiento.

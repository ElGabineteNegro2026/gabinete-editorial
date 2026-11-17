# El peligro azul — Maurice Renard · Límite Abisal, vol. XX

**Fase:** maquetado → **cubierta** (traducción completa, prólogo aprobado, interior de 378 páginas)

## Decisiones del responsable
- 16-11-2026: aprueba *El peligro azul* para Límite Abisal (ficha `candidatos/2026-11-16_el-peligro-azul.md`); se inicia la traducción.

- 16-11-2026: el responsable confirma el vol. XX.
- 16-11-2026: **prólogo aprobado** tal como está en `texto/00_prologo.md`.
- 16-11-2026: incluir el croquis de las huellas en la nieve (1.ª parte, cap. IX), con los rótulos traducidos.
- 17-11-2026: se suprime «Próximo título» del libro (y de las normas de la casa, CLAUDE.md).
- 17-11-2026: ilustración de cubierta con Higgsfield, 2 propuestas.
- 17-11-2026: el responsable entrega una ilustración hecha con ChatGPT (vapor en el mar y tentáculos bajo el agua) → propuesta 1 de cubierta.
- 16-11-2026: **precio**: 14,49 € tapa blanda y 2,99 € ebook, IVA incluido. ISBN por determinar.
  - Comprobado con la calculadora de SelfPub Go (Amazon.es): tapa blanda 13,93 € sin IVA (4 %), coste de impresión 5,29 €, regalías ≈ 3,07 € (60 %). Ebook 2,99 € dentro de la banda del 70 % (2,69-12,99 €), regalías ≈ 1,93 € (coste de entrega estimado 0,12 €).

## Hecho (16-11-2026)
- Texto fuente francés descargado de Wikisource (edición Louis-Michaud, 1911) (no se había subido; se volvió a descargar por la API en `fuente/`, un JSON por capítulo).
- Traducido el «Préliminaire» → `texto/05_preliminar.md` (≈ 1.800 palabras).

## Traducción (completada el 16-11-2026)
- `texto/10_primera_parte.md`: **primera parte completa**, capítulos I-XXI (≈ 50.400 palabras). Cotejada párrafo a párrafo con el original (mismo número de párrafos por capítulo).
- `texto/20_segunda_parte.md`: **segunda parte completa**, capítulos I-XXI (≈ 52.900 palabras). Cotejada párrafo a párrafo (las únicas diferencias son artefactos del HTML de Wikisource: párrafos partidos o un punto suelto).
- `texto/30_epilogo.md`: epílogo (≈ 2.000 palabras).
- Total del texto de Renard: ≈ 107.000 palabras.
- Fuente: `fuente/*.json` (respuesta de la API de Wikisource, un fichero por capítulo; no se suben al repositorio, ver `fuente/.gitignore`).
- `texto/00_prologo.md`: prólogo firmado por «El Editor» (≈ 1.100 palabras, sin desvelar el secreto). Aprobado el 16-11-2026.
- `texto/99_apendice.md`: apéndice explicativo (≈ 1.350 palabras, apartados en versales como el de *813*).

## Maquetación (16-11-2026)
- `interior/el-peligro-azul_interior_6x9.pdf`: 378 páginas, todas las fuentes incrustadas (Caladea, Carlito), sin avisos de compilación. Revisadas portadilla, créditos, prólogo, preliminar, aperturas de parte, cap. X (formato teatral), diario de Robert, epílogo, apéndice e índice.
- `ebook/el-peligro-azul_kindle_create.docx` y `ebook/el-peligro-azul.epub` (sin portada todavía).
- Lomo para tapa blanda con 378 páginas: 378 × 0,002252 = 0,851 in (papel blanco).

### Dudas y decisiones de traducción
- Pieza 9 (cap. II): Le Tellier anuncia la llegada «le 16» en una carta fechada el 18 de abril; es errata del original (todo el texto dice el 26). Corregido a 26.
- Cap. XII: «dans la nuit du 19 au 30» es errata; traducido «del 19 al 20».
- Cap. XIII: el laboratorio de Maxime está en la torre «sud-ouest» (en el cap. V era «sud-est»); incoherencia del original, se respeta.
- Cap. XV: el pueblo «Coniux» del original es Conjux (Saboya), a orillas del lago del Bourget; corregido.
- Subtítulos de las partes según la tabla de la edición de 1911: «¿Dónde?… ¿Cómo?… ¿Quién?… ¿Por qué?…» (primera) y «Dónde. Cómo. Quién. Por qué.» (segunda).
- Cap. IX: croquis de las huellas en la nieve incluido tras «el esbozo que reproducimos» (p. 93 del PDF), rotulado en español («Esquema de las huellas», «Línea de cumbre», «Cruz»); ver `imagenes/CREDITOS.md`. `scripts/maquetar.py` admite ahora imágenes con `![pie opcional](ruta)` en línea propia.
- Diálogo «a la francesa» del capítulo X (acta de la deliberación): se mantiene el formato teatral («Garan. —…»), con acotaciones en cursiva.
- Términos: *sarvants* en cursiva solo la primera vez, luego en redonda y minúscula (el original alterna «Sarvants» con mayúscula); «Peligro Azul» con mayúsculas como en el preliminar. Se conservan sin traducir *mollards*, el patois del boyero (cap. XII) y los títulos de periódicos.
- Groserías del original suavizadas solo lo justo («s'en foutait pas mal» → «le importaba un bledo»).

- Diario de Robert Collin (2.ª parte, caps. IX y XI-XIII): en el original va todo en cursiva, con las palabras enfáticas en redonda. Para no componer en cursiva capítulos enteros se invierte: diario en redonda y énfasis en cursiva.
- Cap. XIII (2.ª parte): la última entrada del diario está fechada «8 septembre» en Wikisource, pero Robert muere antes del 4 (el cuerpo cae la noche del 4 al 5); es errata por «3». Corregido a 3 de septiembre.
- Juegos de palabras del epílogo (*Béryl Bleu*, *Père! il bleut, Bergère!*, *p'tit bout d'Ain*) se dejan en francés con una breve glosa en el propio texto; «avoir des araignées au plafond» → «andar mal de la azotea, y con arañas en ella».
- Cap. IX (2.ª parte): el barómetro marca «160 millimètres» en el original; es errata por 760 (la frase dice «la misma presión que en la superficie»). Corregido.

## Cubierta (17-11-2026)
- Propuesta 1 compuesta con la ilustración del responsable: `cubierta/el-peligro-azul_cubierta_kdp.pdf` (13,100 × 9,250 in, lomo 21,62 mm con 378 págs. en papel blanco, calculado a partir de las páginas: no es provisional) y `cubierta/el-peligro-azul_portada_ebook.jpg` (1600 × 2560). El EPUB ya lleva portada.
- Contracubierta: sinopsis sin desvelar el secreto y cita del epílogo («Mirad. Luego reflexionad…»).
- `scripts/cubierta.py` compone ahora las *cursivas* de sinopsis y citas (antes se quitaban los asteriscos y salía en redonda).
- **CONSULTA**: elegir la cubierta definitiva.

## Pendiente
- Una lectura de corrección completa en papel (o PDF) antes de KDP: erratas, coherencia de términos (aeróscafo, subaéreo, aerario, *air-ballasts*), cursivas.
- Cubierta Límite Abisal: buscar grabados de dominio público de cielo, abismo o seres aéreos (p. ej. Grandville, Doré, láminas de *La Nature*); 2-3 propuestas.
- ISBN y fecha de lanzamiento (CONSULTA).
- Cubierta: **bloqueada en Higgsfield** (17-11-2026). La cuenta es del plan gratuito (10 créditos) y todos los modelos de imagen probados (GPT Image 2.6 en 1k y 2k, Recraft V4.1, Soul Location) responden «Requires basic plan or higher». No se ha gastado ningún crédito. Prompts de las 2 propuestas en `cubierta/PROMPTS.md`. Opciones: que el responsable pase al plan Basic (compra: decisión suya) o genere las imágenes en ChatGPT con esos prompts.

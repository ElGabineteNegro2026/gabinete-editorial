# El peligro azul — Maurice Renard · Límite Abisal, vol. XX

**Fase:** revisión → **listo para KDP salvo ISBN** (lectura de corrección hecha el 17-11-2026; lanzamiento la semana del 23-11-2026)

## Decisiones del responsable
- 16-11-2026: aprueba *El peligro azul* para Límite Abisal (ficha `candidatos/2026-11-16_el-peligro-azul.md`); se inicia la traducción.

- 16-11-2026: el responsable confirma el vol. XX.
- 16-11-2026: **prólogo aprobado** tal como está en `texto/00_prologo.md`.
- 16-11-2026: incluir el croquis de las huellas en la nieve (1.ª parte, cap. IX), con los rótulos traducidos.
- 17-11-2026: se suprime «Próximo título» del libro (y de las normas de la casa, CLAUDE.md).
- 17-11-2026: ilustración de cubierta con Higgsfield, 2 propuestas.
- 17-11-2026: el responsable entrega una ilustración hecha con ChatGPT (vapor en el mar y tentáculos bajo el agua) → propuesta 1 de cubierta.
- 17-11-2026: el responsable entrega una segunda ilustración hecha con Manus a partir de la propuesta A → propuesta 2.
- 17-11-2026: **cubierta definitiva: propuesta 2** (cumbre del Colombier).
- 17-11-2026: **lanzamiento previsto la semana próxima** (23-29 de noviembre de 2026); se pide la lectura de corrección completa.
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
- Propuesta 1 compuesta con la ilustración del responsable (ahora `_p1`): `cubierta/el-peligro-azul_cubierta_kdp_p1.pdf` (13,100 × 9,250 in, lomo 21,62 mm con 378 págs. en papel blanco, calculado a partir de las páginas: no es provisional) y `cubierta/el-peligro-azul_portada_ebook_p1.jpg` (1600 × 2560).
- Contracubierta: sinopsis sin desvelar el secreto y cita del epílogo («Mirad. Luego reflexionad…»).
- `scripts/cubierta.py` compone ahora las *cursivas* de sinopsis y citas (antes se quitaban los asteriscos y salía en redonda).
- Propuesta 2 con la ilustración del responsable hecha en Manus a partir de la propuesta A (cumbre del Colombier, cruz, huellas, bastón roto y la mole del aeróscafo en un cielo de agua): ≈ 355 ppp en el recuadro. `scripts/cubierta.py` admite ahora `--variante N` ([cubierta.variantes.N] en `libro.toml`).
- **Definitiva: propuesta 2** (17-11-2026). Es la `ilustracion` principal de `libro.toml`: `cubierta/el-peligro-azul_cubierta_kdp.pdf` y `cubierta/el-peligro-azul_portada_ebook.jpg`; el EPUB lleva ya esta portada. La propuesta 1 se conserva con sufijo `_p1`.

## Lectura de corrección (17-11-2026)
- Lectura completa de preliminar, primera y segunda parte y epílogo, además de revisión automática (ortografía con el diccionario Hunspell es_ES, comillas, signos de apertura, rayas, cursivas, números) y cotejo con el francés en los pasajes dudosos.
- Unas 60 correcciones de texto y unos 35 ajustes tipográficos. Lo más relevante:
  - Contrasentido corregido (2.ª parte, cap. XI): «donde el hombre no podría vivir más que en el vacío absoluto» → «no podría vivir, como tampoco en el vacío absoluto».
  - Ambigüedad: «dos hijas … de diez y ocho años» (se leía «dieciocho») → «de diez y de ocho años».
  - Erratas: *acoraze* → acorace; *repónte* → reponte; «trigésimo tercera» → trigésima; «esa énfasis» → ese énfasis; «mil y un zalemas» → una; «los monte bajos» → montes; «esos especie de» → esas especies.
  - Galicismos y calcos: *dardeaba*, *tumefacta*, «cayó en 5 de octubre», «dite bien», «a toda rueda», «pintarrajeada», «picoletos» (por gendarmes), «divas» (*dives*), «ni una cienmilésima de carcel» (unidad francesa → bujía).
  - Pronombre francés sin traducir: «¿quién es ese «*les*»?» → «¿quién es ese «se»?» (2.ª parte, cap. XIII).
  - Patois del cap. XVII (1.ª parte): se añade una glosa breve en castellano, como en el cap. XII. Epílogo: glosa de los juegos de palabras con *Péril Bleu*.
  - Ortotipografía: apóstrofos tipográficos (’), números de cuatro cifras sin punto (1046, 1500, 8500), «……» → «…», «etc…» → «etc.», signos de apertura que faltaban.
  - Coherencia: «François de Agnès» en todo el libro (había tres «d’Agnès»).
- Reglas de la casa, sin cambios: *sarvants* en cursiva solo la primera vez; aeróscafo, subaéreo, aerario; *air-ballasts* en cursiva.
- Maqueta rehecha: sigue en 378 páginas (el lomo de la cubierta no cambia); fuentes incrustadas; croquis en la p. 93.

## Pendiente
- **ISBN (CONSULTA, urgente para el lanzamiento)**: en los créditos figura «En trámite». Con el ISBN: actualizar `libro.toml`, volver a maquetar (créditos) y regenerar el DOCX/EPUB. Si se publica con el ISBN gratuito de KDP, decidir qué poner en los créditos.
- Día exacto de publicación (semana del 23-11-2026). Ficha ya en `novedades/para-redes.md`.
- Opcional: que el responsable hojee el PDF final en pantalla o pida una prueba impresa de KDP antes de aprobar la tapa blanda.
- Nota: Higgsfield no generó nada (plan gratuito: «Requires basic plan or higher»; 0 créditos gastados). Las ilustraciones las aportó el responsable (ChatGPT y Manus).

## Papel crema (18-11-2026)
- Decisión del responsable: **todos los libros en papel crema**. La cubierta estaba calculada para blanco (13,100 in). Regenerada: `papel = "crema"`, lomo 378 × 0,0025 in = 24,00 mm, **13,195 × 9,250 in** exactos (también la variante _p1). Comprobar al subir que KDP espera ese ancho.
- Interior rehecho sin enlaces en el índice (KDP los quita como «marcas no imprimibles»); sigue en 378 páginas, mismo contenido.

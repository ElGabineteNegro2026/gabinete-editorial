# 813 — Maurice Leblanc · Archivo Lupin, Dossier IV

**Fase:** revisión (falta el ISBN de KDP; prólogo y apéndice aprobados)

## Decisiones del responsable
- 16-11-2026: aprueba *813* para Archivo Lupin (Dossier IV, según la ficha `candidatos/2026-11-16_813-arsene-lupin.md`).
- 16-11-2026: aporta la traducción (RTF; copia en `fuente/813_traduccion_responsable.rtf`).

- 16-11-2026 (2.ª respuesta):
  - Se omite de los créditos la línea de traducción.
  - Nombres «Arsène» / «Sholmès» aprobados.
  - Cubierta: le gusta la A; aporta una ilustración propia (ChatGPT) para adaptarla, y es la que se usa ahora.
  - Precio: 13,95 € tapa blanda y 2,99 € ebook, IVA incluido. Papel crema.
  - ISBN: lo dará el responsable al iniciar el proceso en KDP.
  - Próximo título: *El tapón de cristal*.

- 16-11-2026: aprueba el prólogo y el apéndice reescritos.

## Hecho (16-11-2026)
- Texto limpio en `texto/` desde el RTF:
  - 159 párrafos partidos por saltos de página, unidos.
  - Restituidas las 17 capitulares perdidas.
  - «---» → raya, «...» → «…» y cursivas reparadas.
  - Normalización: «Arsenio» → «Arsène» y «Sholmes» → «Sholmès», como en los Dossiers I-III.
  - La nota 1 del traductor se ha colocado como «Nota del autor» en el cap. I.
- Borradores de prólogo (`00_prologo.md`, PENDIENTE DE APROBACIÓN) y apéndice (`99_apendice.md`).
- Maquetación: `interior/813_interior_6x9.pdf`, 440 páginas, 112.193 palabras, fuentes incrustadas, sin avisos.
  Revisadas portadilla, créditos, manifiesto, prólogo, aperturas de parte y de capítulo, apéndice e índice.
- Ebook: `ebook/813_kindle_create.docx` (para Kindle Create) y `ebook/813.epub` (con portada A).
- Cubierta tapa blanda: papel crema, lomo de 27,94 mm (13,350 × 9,250 in).
  - Activa: propuesta A (*L'Assassinat*, Vallotton 1893).
  - Alternativa: propuesta B (*L'Anarchiste*, 1892), en `cubierta/propuestas/`.
- Plantilla (afecta a todos los libros): ya no sale folio en la blanca que sigue al manifiesto.
- `cubierta.py` admite ahora `invertir_grabado`, `recorte_grabado` y `encuadre`, y ajusta el texto del lomo.

- 16-11-2026 (tarde):
  - Créditos sin la línea de traducción; «Próximo título: El tapón de cristal».
  - Cubierta C con la ilustración del responsable (`cubierta/chatgpt_lupin_caja_fuerte.png`), sin teñir. Es la cubierta activa; la A (Vallotton) queda en `propuestas/`.
  - En la sinopsis, «Rudolf» → «Rodolfo», como en el texto.

- 16-11-2026 (noche): el responsable descarta la cubierta C por parecerse demasiado al Dossier I y aporta otra ilustración.
  Cubierta D (`cubierta/chatgpt_etretat_noche.png`) compuesta y activa; la C queda en `propuestas/`.

- 16-11-2026: el responsable pide prólogo y apéndice más extensos, con el volumen III como referencia (`demo.odt`).
  Reescritos: prólogo ≈ 1.000 palabras y apéndice ≈ 1.250, con apartados en versales y cierre «El expediente continúa abierto».
  Interior: 446 páginas. Cubierta regenerada: lomo de 28,32 mm.

## Pendiente
- Resolución de la ilustración D: el responsable envía una versión mayor, que llega a esta sesión con 1333 × 2000 px (unos 216 ppp a sangre; KDP recomienda 300 = 1838 × 2775 px). Si el original es mayor, sustituir `cubierta/chatgpt_etretat_noche.png` y volver a ejecutar `scripts/cubierta.py`.
- ISBN (al iniciar KDP) y fecha de lanzamiento.
- Nota 2 del traductor (puerta del Palacio de Justicia): no se ha encontrado su llamada en el texto, porque el RTF no conserva las marcas. Queda fuera hasta localizarla.
- Revisión de lectura completa: pueden quedar párrafos partidos que empiezan por mayúscula.
- Valorar papel blanco (lomo 25,2 mm) frente a crema.

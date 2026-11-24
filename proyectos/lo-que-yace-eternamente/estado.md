# Lo que yace eternamente — H. P. Lovecraft · Límite Abisal (edición especial)

*(Proyecto llamado antes «Los Mitos de Cthulhu» / «Lovecraft esencial»; carpeta renombrada el 24-11-2026 de `proyectos/los-mitos-de-cthulhu/`.)*

**Fase:** maquetado + cubierta (propuestas) → **revisión** (24-11-2026)

## Decisiones del responsable
- 23-11-2026: aprueba el omnibus (ficha `candidatos/2026-11-23_omnibus-lovecraft.md`) y lo pone en producción el 24-11-2026 a las 4:05. Objetivo: Navidad.

## Pendiente
- Origen de las traducciones publicadas: si no se acredita, traducción propia (ver `informes/2026-11-24_orden-produccion.md`).
- CONSULTA: precio (propuesta 24,95 € / 6,99 €), numeración, prólogo y cubierta definitiva.

## Decisiones del responsable (24-11-2026)
- **Opción A**: omnibus solo de Lovecraft con los nueve textos de la ficha. No es una antología de varios autores.
- **Traducción propia de la casa** para los nueve textos (confirmado por el responsable). Se reutilizan: no hay
  que traducir. Como la traducción es de la casa, el ebook puede ir en KDP Select y Kindle Unlimited.
- Título: *Los Mitos de Cthulhu* coincide con la antología de Rafael Llopis (Alianza). Propuesta:
  *Lovecraft esencial. Relatos y novelas de horror cósmico* (CONSULTA: título definitivo).


## Hecho (24-11-2026)
- **Fuentes**: manuscritos de la casa en `fuente/` (no se suben al repositorio: `fuente/.gitignore`).
  - *Mareas negras*, vol. IV. Traducción: Raúl Pozo.
  - *El horror de Dunwich*, vol. VIII.
  - *La sombra sobre Innsmouth*, vol. III. Traducción: Merel Funkee.
  - *El caso de Charles Dexter Ward*, vol. XII.
  - *En las montañas de la locura*, vol. XVI.
  - El responsable confirma que todas son traducciones de la casa.
  - El `.rar` subido a la raíz del proyecto (*La llamada de Cthulhu y otras historias*) **no se usa**.
- **Texto** en `texto/01…09`, por orden de escritura. Unas 179.000 palabras.
  - Relatos breves como capítulo; «La llamada de Cthulhu» y las cuatro novelas como partes, con sus capítulos.
- **Ortotipografía unificada**:
  - Comillas latinas en lugar de las rectas: unas 380, sobre todo en *Charles Dexter Ward* y *Montañas*.
  - «...» → «…».
  - Incisos con guion → raya.
  - Omisiones «---» → «———».
  - Ligaduras «ﬁ» del PDF de *Montañas* (211).
  - «1927—28» → «1927-1928».
- **Párrafos partidos unidos**: 19 (Ward 10, Dunwich 2, Montañas 5, Innsmouth 2).
- **Corrección de traducción**: en «La ciudad sin nombre», «un pasaje de Tomás Moro» → «Thomas Moore». El poema es
  de Moore (*Alciphron*), no de Moro. Además, *Image du Monde* en cursiva.
- **Epígrafes** de Blackwood («La llamada de Cthulhu») y Lamb (*Dunwich*) como cita, con la firma alineada a la
  derecha. Fórmulas de Ward centradas.
- **Prólogo**: `texto/00_prologo.md`, ≈ 900 palabras, firmado «El Editor». **BORRADOR, pendiente de aprobación.**
  Incluye un párrafo sobre los prejuicios de Lovecraft.
- **Apéndice**: siete apartados en versales (fechas, geografía, libros prohibidos, Grandes Antiguos, narrador,
  mar y herencia, sobre esta edición). Cierre: «El expediente continúa abierto».
- **Maqueta**: `interior/los-mitos-de-cthulhu_interior_6x9.pdf`, **522 páginas**.
  - Fuentes incrustadas, sin avisos.
  - Revisados portadilla, créditos, prólogo, aperturas de relato, parte y capítulo, apéndice, página de reseña e índice.
  - Con **522 páginas** cabe también en **tapa dura** (máximo 550), si se quiere una edición de regalo.
- **Ebook**: `ebook/los-mitos-de-cthulhu_kindle_create.docx` y `ebook/los-mitos-de-cthulhu.epub` (con la portada A).
- **Cubierta**: tapa blanda, crema, lomo de 33,15 mm, **13,555 × 9,250 in**. Tres propuestas con grabados de
  dominio público (`cubierta/CREDITOS.md`):
  - **A**: Doré, *La destrucción del Leviatán* (1865). Es la activa.
  - **B**: John Martin, *Satán despierta a los ángeles caídos* (1825). Más oscura. `_p1`.
  - **C**: Doré, el albatros entre los hielos (*The Rime of the Ancient Mariner*, 1876). `_p2`.
- **Scripts** (sirven para todos los libros):
  - `maquetar.py`: un `## I` solo tras una parte es capítulo, no subtítulo. Antes se perdía el texto del
    capítulo I. Ningún libro publicado usaba ese formato.
  - `maquetar.py`: volumen con texto («Edición especial»).
  - Plantilla: portadilla sin división silábica.
  - `cubierta.py`: subtítulo en la portada de Límite Abisal sin que lo tape la ilustración; el volumen no
    numérico no va en el lomo.

## Pendiente (CONSULTA) — *superado: ver «Decisiones del responsable (24-11-2026, noche)»*
1. Título definitivo. Provisional: *Lovecraft esencial. Relatos y novelas de horror cósmico*.
2. Prólogo: aprobar el borrador.
3. Cubierta definitiva: A, B o C.
4. Precio (propuesta 24,95 € / 6,99 €), numeración («Edición especial» o número de volumen) y ¿tapa dura además?
5. Créditos de traducción: «Traducción: El Gabinete Negro» de forma genérica, o por textos (Raúl Pozo, Merel Funkee…).
6. Borrar del repositorio público el `.rar` (*La llamada de Cthulhu y otras historias*) y la copia de
   *Mareas negras* de la raíz del proyecto: el repositorio es público.
7. ISBN, cuando se suba a KDP.

## 24-11-2026 (tarde)
- El responsable pide otro título, un prólogo y un apéndice más extensos y valorar su ilustración. Propone
  21,95 € para la tapa blanda.
- **Prólogo ampliado** a ≈ 2.000 palabras, en seis apartados. Sigue siendo **BORRADOR**.
- **Apéndice ampliado** a ≈ 2.600 palabras, en nueve apartados: cronología, guía de los nueve textos, geografía,
  biblioteca prohibida, Grandes Antiguos, narrador, maestros (con los autores del catálogo), círculo y herencia,
  sobre esta edición.
- Interior: **532 páginas**. Cubierta: lomo de 33,78 mm, **13,580 × 9,250 in**.
- **Propuesta D** con la ilustración del responsable (`_p3`). Es la recomendada.

## Decisiones del responsable (24-11-2026, noche)
- **Título**: *Lo que yace eternamente. Lovecraft esencial: los Mitos de Cthulhu en nueve relatos y novelas*.
- **Apéndice**: aprobado.
- **Precio**: 21,95 € tapa blanda y 6,99 € ebook, IVA incluido.
- **Volumen**: «Edición especial», sin número.
- **Créditos de traducción**: genérico, «Traducción: El Gabinete Negro».
- **Prólogo**: no le gustan los apartados.
  - Reescrito como texto continuo: sin títulos ni separadores, con transiciones entre las partes.
  - **Pendiente de aprobación.**

## Producción (24-11-2026, noche)
- Carpeta y ficheros renombrados a `lo-que-yace-eternamente`.
- Portadilla: un subtítulo largo (más de 40 caracteres) va a 14 pt sin negrita; uno corto sigue a 22 pt negrita
  como segunda línea del título. Cambio en la plantilla y en el DOCX.
- Interior: **532 páginas**, fuentes incrustadas.
- Cubierta: **13,580 × 9,250 in**, crema. Activa la **D** (ilustración del responsable), pendiente de confirmar. Variantes:
  - `_p1`: B, Martin;
  - `_p2`: C, Doré, el albatros;
  - `_p3`: A, Doré, el Leviatán.
- EPUB con la portada D.

## Pendiente
1. Aprobar el prólogo sin apartados.
2. Confirmar la cubierta D como definitiva.
3. ISBN, al darlo de alta en KDP.
4. Al terminar, borrar del repositorio el `.rar` y la copia de *Mareas negras* de la raíz del proyecto
   (lo ha pedido el responsable).

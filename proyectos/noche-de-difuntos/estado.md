# La cámara sellada — antología gótica · Cámara Sellada (volumen especial)

**Fase:** **listo para KDP salvo ISBN**; se envía la semana del 29-11 (24-11-2026)

## Decisiones del responsable
- 23-11-2026: aprueba la antología (ficha `candidatos/2026-11-23_antologia-gotica-camara-sellada.md`) y la pone en producción el 24-11-2026 a las 4:05.

## Pendiente
- Traducciones propias salvo que se acrediten las publicadas; Bécquer, en el original.
- CONSULTA: precio (propuesta 19,95 € / 5,99 €), numeración, prólogo y cubierta.

## 24-11-2026
- Recibidos 5 manuscritos de la casa: *Carmilla*, *El papel amarillo y otros relatos*, *El Horla y otros cuentos*, *La casa y el cerebro* y *El hombre de arena y otros relatos*. Están en `fuente/`, que no se sube al repositorio.
- Pendientes: *Sleepy Hollow*, *¿Qué fue eso?*, *La cruz del diablo*, *La sombra y el espejo* y *Los muertos y los invisibles*.
- Por confirmar con el responsable: la reutilización de las traducciones de Raúl Pozo (los créditos de *El papel amarillo* dicen «© De la traducción: Raúl Pozo») y de Marta Luengo (*El Horla*).

## 24-11-2026 (noche)
- El responsable confirma que **todas las traducciones son de la casa** y se pueden reutilizar, también las de
  Raúl Pozo y Marta Luengo. Crédito genérico: «Traducción: El Gabinete Negro».
- Bécquer no vino en los manuscritos. Se toma de Wikisource en español: *Obras*, Librería de Fernando Fe.
  - Ortografía actualizada: «á» → «a», «fué» → «fue», guiones de corte unidos.
  - Capitulares restituidas.
- **Selección: 17 textos (16 relatos y *Carmilla*), por orden de publicación, 1816-1893**:
  - Hoffmann: «El hombre de arena» y «La casa vacía».
  - Irving: «Sleepy Hollow».
  - O’Brien: «La habitación perdida» y «¿Qué fue eso?».
  - Bulwer-Lytton: «La casa y el cerebro».
  - Bécquer: «Los ojos verdes», «El monte de las ánimas» y «Maese Pérez».
  - Le Fanu: *Carmilla*. Sus capítulos van como rótulos centrados, no como partes, para que el índice no los
    mezcle con los relatos que siguen.
  - Braddon: «La sombra en la esquina».
  - Maupassant: «La mano» y «El Horla». Las fechas del diario, en negrita.
  - Bierce: «Halpin Frayser», «La ventana tapiada» y «La cosa maldita».
  - Gilman: «El papel amarillo».
  - Unas 134.000 palabras. Comprobado: sin párrafos partidos, sin comillas rectas, sin capitulares perdidas.
- **Prólogo**: ≈ 1.900 palabras, texto seguido sin apartados (como pidió el responsable para el de Lovecraft).
  BORRADOR, pendiente de aprobación.
- **Apéndice**: ocho apartados en versales, como el de Lovecraft:
  - cronología;
  - guía de los 17 textos;
  - el espacio cerrado;
  - lo siniestro (Freud);
  - la duda fantástica (Todorov);
  - mujeres y fantasmas;
  - herencia;
  - sobre esta edición.
- **Interior**: 404 páginas, fuentes incrustadas, página de reseña.
- **Cubierta**: tapa blanda en papel crema, lomo de 25,65 mm, **13,260 × 9,250 in**. Tres propuestas (`cubierta/CREDITOS.md`):
  - **A**: Füssli, *La pesadilla* (grabado de 1791). Es la activa.
  - **B**: Friston, ilustración de *Carmilla* (1872). `_p1`.
  - **C**: Böcklin, *La isla de los muertos* (1880). Queda muy oscura. `_p2`.
- **Scripts**:
  - `cubierta.py` admite `autor_portada` (varias líneas con «|») y `autor_lomo` para antologías.
  - El volumen con texto («Edición especial») sale bien en Cámara Sellada.
  - Los nombres de autor se ajustan al marco.

## Pendiente (CONSULTA)
1. Título (provisional: *La cámara sellada. Antología esencial del relato gótico y de fantasmas (1816-1893)*).
2. Prólogo.
3. Cubierta definitiva.
4. Precio (propuesta 19,95 € / 5,99 €) y «Edición especial».

## Decisiones del responsable (24-11-2026)
- **Título**: *Noche de difuntos. Antología esencial del relato gótico y de fantasmas*. Carpeta renombrada de
  `proyectos/la-camara-sellada/` a `proyectos/noche-de-difuntos/`.
- **Prólogo**: aprobado.
- **Precio**: 19,95 € tapa blanda y 5,99 € ebook. **Volumen**: «Edición especial».
- **Cubierta**: la ilustración la hará el responsable con ChatGPT, a partir del prompt del Editor Jefe (en el
  informe del chat del 24-11-2026 y en `cubierta/PROMPT_CHATGPT.md`). Mientras tanto, la A (Füssli) es provisional.

## Pendiente
- Ilustración del responsable → componer la cubierta y regenerar el EPUB.
- Fecha de lanzamiento (CONSULTA): el título pide la temporada de difuntos y Halloween.
- ISBN, al darlo de alta en KDP.

## Cubierta definitiva (24-11-2026)
- Ilustración del responsable (ChatGPT) compuesta en el estilo de Cámara Sellada. Pasa a ser la ilustración principal.
- Cubierta: `cubierta/noche-de-difuntos_cubierta_kdp.pdf`, **13,260 × 9,250 in**, crema.
- EPUB regenerado con la portada. Füssli queda como `_p3`.
- Resolución: ≈ 255 ppp en el recuadro. KDP lo acepta, pero si ChatGPT puede exportarla mayor (≥ 1200 × 1800 px),
  basta con sustituir `cubierta/responsable_pasillo_difuntos.png` y ejecutar `cubierta.py`.

## Para subir a KDP
- **Tapa blanda**: interior `interior/noche-de-difuntos_interior_6x9.pdf` (404 páginas, papel crema, sin sangrado)
  y cubierta `cubierta/noche-de-difuntos_cubierta_kdp.pdf`.
- **Ebook**: `ebook/noche-de-difuntos_kindle_create.docx` o `ebook/noche-de-difuntos.epub`.
- Precio: 19,95 € / 5,99 €. Serie: Cámara Sellada, sin número.

## Cupo de KDP (24-11-2026)
- **Envío: semana del 29-11 al 5-12**, junto con *813* (cupo de 2 títulos nuevos por formato y semana). Lanzamiento como regalo de Navidad: **confirmado por el responsable el 24-11-2026**.

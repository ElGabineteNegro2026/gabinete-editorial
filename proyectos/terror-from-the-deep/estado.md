# Terror from the Deep — antología en inglés (horror marino)

**Fase:** aprobado → texto (producción desde el 24-11-2026)

## Decisiones del responsable
- 23-11-2026: aprueba la n.º 1 del plan de la línea en inglés (`candidatos/2026-11-23_plan-linea-ingles.md`) y la pone en producción el 24-11-2026 a las 4:05.

## Pendiente
- No publicar antes del 1-1-2027 (Wells, †1946). Plantilla en inglés. Introducción y notas propias (edición anotada).

## 24-11-2026: preparación
- **Plantilla en inglés lista.**
  - `idioma = "en"` en `libro.toml`: créditos, firma, «Notes on the Stories», «Contents» y página de reseña en inglés.
  - Colección `limite-abisal-en`: manifiesto traducido; misma cubierta, con el rótulo «THE LÍMITE ABISAL COLLECTION».
- **Fuentes. Project Gutenberg, en mantenimiento** (503) desde el 23-11. Internet Archive bloquea las descargas
  en este entorno. Prueba con Wikisource en inglés (`scripts/fuentes/wikisource_en.py`):
  - Descargados: Poe, «MS. Found in a Bottle» y «A Descent into the Maelström»; Doyle, «The Captain of the
    Pole-Star» y «J. Habakuk Jephson's Statement»; Wells, «In the Abyss» (versión de *Amazing Stories*, 1926);
    Hodgson, «The Voice in the Night»; Cobb, «Fishhead».
  - Con problemas:
    - «The Upper Berth» (Crawford): la copia de Wikisource **no está corregida**. Trae erratas de OCR: «as
      beginning», «he wine».
    - «The Sea Raiders» (Wells) y los tres de Lovecraft: no se extrajeron; hay que repetir la descarga.
  - No están en Wikisource: Kipling, «A Matter of Fact»; Chambers, «The Harbor-Master»; Robertson, «From the
    Darkness and the Depths»; Buchan, «Skule Skerry».
- **Decisión técnica**: para una edición en inglés, los textos tienen que salir de copias corregidas (Gutenberg o
  Wikisource validado). Se espera a que vuelva Gutenberg para completar y cotejar. Mientras tanto, nada de
  maquetar con texto de OCR sin corregir.

## 25-11-2026: textos completos (salvo Kipling) y primera maqueta
**Fase: texto → maquetado.**
- **archive.org**: el responsable lo añade a la red del entorno.
  - Búsqueda y metadatos funcionan. Las descargas directas siguen bloqueadas: redirigen a los nodos `dn*.archive.org`.
  - Se descarga por la ruta `/stream/<id>/<fichero>`, que sirve el texto en la página.
  - Herramienta: `scripts/fuentes/archive_org.py` (`search "<consulta>"` o `get <identificador> <salida>`).
  - La colección «gutenberg» de archive.org es una copia antigua de Project Gutenberg, con textos corregidos.
- **Fuentes de los 15 textos**:

  | Textos | Fuente |
  |---|---|
  | Crawford, «The Upper Berth» | Gutenberg 22246, vía archive.org; sustituye a la copia de Wikisource con errores de OCR |
  | Wells, «In the Abyss» y «The Sea Raiders» | *The Plattner Story and Others*, Gutenberg 42989 |
  | Chambers, «The Harbor-Master» | caps. I-V de *In Search of the Unknown* (1904), Gutenberg 18668 |
  | Robertson, «From the Darkness and the Depths» | *The Grain Ship* (1914), Gutenberg 26194 |
  | Poe (×2), Doyle (×2), Hodgson, Cobb | Wikisource validado |
  | Lovecraft, «Dagon» (1923), «The Temple» (1925) y «The Call of Cthulhu» (1928) | Wikisource, texto de *Weird Tales* |
  | Buchan, «Skule Skerry» | OCR de dos ejemplares de *The Runagates Club* (1928) en archive.org |

  - Buchan: las dos lecturas se cotejaron palabra a palabra (40 discrepancias, casi todas de comillas), se resolvieron
    una a una y se recompusieron los párrafos partidos por cambio de página.
  - Cobb: los guiones de la fuente se corrigieron a rayas donde correspondía.
  - Se han quitado las licencias y menciones de Gutenberg y Wikisource.
- **Pendiente: Kipling, «A Matter of Fact»**.
  - Solo hay OCR de dos ediciones distintas (Nueva York, 1899, y otra posterior). No coinciden: hay variantes
    reales («Three» / «Ten», «state-room» / «cabin»), errores de OCR («j3aper», «exjDanding») y líneas perdidas.
  - No es publicable sin cotejo con una copia limpia. Opciones: que el responsable aporte el TXT de Gutenberg de
    *Many Inventions*, esperar a Gutenberg o prescindir del relato.
- **Aparato propio** (para que KDP lo acepte como *Annotated*):
  - introducción (`00_prologo.md`, firmada «— The Editor»; CONSULTA);
  - nota de cabecera en cada relato;
  - «Notes on the Stories» (`99_apendice.md`): cronología, sea serpent and kraken, the deep sea before the
    bathysphere, the drowned city, Lovecraft and his predecessors, about this edition.
  - La introducción ya menciona a Kipling: si se prescinde de él, quitar esa frase y cambiar «sixteen» por «fifteen».
- **Primera maqueta**: 290 páginas, fuentes incrustadas → `interior/terror-from-the-deep_interior_6x9.pdf`, DOCX y EPUB.
- **CONSULTAS**:
  1. texto de Kipling;
  2. introducción;
  3. volumen o numeración de la línea en inglés;
  4. cubierta (grabados de Doré o ilustración de ChatGPT).
- No se puede publicar antes del 1-1-2027 (Wells).

## Decisiones del responsable (25-11-2026)
- **Kipling fuera.** Quedan 15 relatos. La introducción («fifteen stories») y la cronología están ajustadas.
- **Introducción aprobada.**
- **Línea nueva en inglés**, fuera de las colecciones en español y con numeración propia.
  - Nombre provisional: **Black Cabinet Classics** (CONSULTA). Ficha en `colecciones/black-cabinet-classics.json`,
    con manifiesto propio («About this series»).
  - *Terror from the Deep* es el **n.º 1** de la línea.
- **Cubierta**: estética nueva (fondo hueso, linograbado a dos tintas, sans-serif condensada). Prompt para ChatGPT
  en `cubierta/PROMPT_CHATGPT_CUBIERTA_COMPLETA.md`.
- Maqueta regenerada: 290 páginas (12,975 × 9,25 in de cubierta en papel crema).

## Cubierta definitiva (26-11-2026)
- Diseño completo del responsable, hecho con ChatGPT a partir del prompt (`cubierta/PROMPT_CHATGPT_CUBIERTA_COMPLETA.md`).
  - Medida comprobada: **12,975 × 9,25 in**, la que corresponde a 290 páginas en papel crema.
  - Comprobados el lomo centrado, el texto sin erratas, los márgenes de seguridad y el hueco del código de barras libre.
- El PDF original llevaba una Helvetica sin incrustar (de ReportLab). Se ha rasterizado a 300 ppp y rehecho como PDF solo
  con la imagen, a la misma medida: `cubierta/terror-from-the-deep_cubierta_kdp.pdf`.
  - Original rasterizado: `cubierta/responsable_cubierta_completa.jpg`.
  - Portada de ebook recortada de la portada: `cubierta/terror-from-the-deep_portada_ebook.jpg` (1600 × 2560 px).
  - El EPUB lleva ya la portada.
- **Ficha KDP**: `kdp.md`.
  - Ebook al 35 % y sin KDP Select, por ser dominio público.
  - Territorios: todos salvo México y Colombia.
  - Envío: no antes de la semana del 3 al 9 de enero de 2027.
- **Fase: listo para KDP salvo ISBN y CONSULTAS**:
  1. nombre de la línea, «Black Cabinet Classics»;
  2. precios (16,99 $ la tapa blanda / 4,99 $ el ebook);
  3. autor principal: Lovecraft.

## Decisiones del responsable (26-11-2026)
- Aprobados:
  - el nombre de la línea, **Black Cabinet Classics**;
  - los precios: 16,99 $ la tapa blanda y 4,99 $ el ebook (resto de mercados, según `kdp.md`);
  - **Lovecraft** como autor principal en KDP.
- **Fase: listo para KDP salvo ISBN.** Envío: semana del 3 al 9 de enero de 2027 (no antes, por Wells).

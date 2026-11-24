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

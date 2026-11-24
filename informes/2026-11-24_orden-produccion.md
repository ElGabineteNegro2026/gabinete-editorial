# Orden de producción — martes 24-11-2026, 4:05

Aprobado por el responsable el 23-11-2026. Al empezar la sesión, leer `CLAUDE.md`, este documento y las fichas.
Trabajar en este orden y hacer commit y push a `main` tras cada paso. Lo que no dé tiempo a terminar se
continúa en la siguiente sesión.

| Prioridad | Proyecto (slug) | Ficha | Colección | Objetivo |
|---|---|---|---|---|
| 1 | `lo-que-yace-eternamente` | `candidatos/2026-11-23_omnibus-lovecraft.md` | Límite Abisal (edición especial) | **listo para KDP antes de Navidad** |
| 2 | `la-camara-sellada` | `candidatos/2026-11-23_antologia-gotica-camara-sellada.md` | Cámara Sellada (volumen especial) | febrero de 2027 |
| 3 | `terror-from-the-deep` | `candidatos/2026-11-23_plan-linea-ingles.md`, n.º 1 | línea en inglés | marzo de 2027 (**no antes del 1-1-2027**: lleva a Wells, †1946) |
| 4 | `older-than-the-church` | `candidatos/2026-11-23_plan-linea-ingles.md`, n.º 2 | línea en inglés | septiembre de 2027 |

Después: *El libro de los licántropos* (reanudar tras el omnibus; decisión del 23-11-2026).

## Criterios para todos

- **Traducciones**: no consta el origen de las del catálogo publicado. Mientras el responsable no aporte los
  manuscritos y confirme que son de la casa (o con derechos), se hace **traducción propia** desde el original en
  dominio público. Así, además, el ebook puede ir en KDP Select y Kindle Unlimited, y cobrar el 70 %.
- **Fuentes**:
  - Wikisource (en, fr, de, es); Gutenberg si ha vuelto a funcionar (el 23-11 daba 503).
  - Internet Archive: solo los metadatos (los servidores de descarga dan 403 en este entorno).
- **Formato**: estructura de `proyectos/<slug>/` y de `texto/*.md` según `CLAUDE.md`.
  - Antologías: cada relato es un `##` con su título.
  - Créditos de cada relato (título original, autor, año) en `creditos_obra`.
  - Página de reseña activa (por defecto).
- **Cubiertas**: grabados de dominio público (Doré, John Martin, Harry Clarke…), 2-3 propuestas por libro.
- **CONSULTA** (no se decide por cuenta propia):
  - precio definitivo (las fichas llevan propuestas);
  - numeración dentro de la colección;
  - prólogo firmado por «El Editor» (se redacta como borrador pendiente de aprobación);
  - cubierta definitiva.

## 1 · *Los Mitos de Cthulhu* (Lovecraft)

- Nueve textos de la ficha: «Dagón», «El templo», «La ciudad sin nombre», «La llamada de Cthulhu», «La casa maldita»,
  *El horror de Dunwich*, *La sombra sobre Innsmouth*, *El caso de Charles Dexter Ward* y *En las montañas de la locura*.
  Unas 169.000 palabras en inglés; unas 620 páginas en total.
- Orden de trabajo: fuentes → traducción (empezar por los relatos cortos y seguir con las novelas) → prólogo
  (borrador) y apéndice → maquetación → cubierta en tapa blanda, papel crema.
- Lomo previsto: unos 39 mm.
- Objetivo: el responsable lo sube a KDP antes del 20-12-2026.

## 2 · *La cámara sellada* (antología gótica)

- Relatos de la ficha:
  - Hoffmann, Irving, Bulwer-Lytton y O'Brien;
  - Bécquer, en el original español, que solo hay que limpiar;
  - Le Fanu (*Carmilla*), Braddon, Maupassant, Gilman y Bierce.
- Unas 150.000 palabras. Queda fuera *Otra vuelta de tuerca*: tiene traductora con derechos.

## 3-4 · Línea en inglés

- Son textos originales en inglés (y alguno traducido por la casa, si lo hubiera). Para KDP necesitan una
  **versión diferenciada**: introducción y notas propias, y la etiqueta «(Annotated)» o «(Illustrated)», o KDP
  la rechaza como dominio público duplicado.
- Falta una **variante en inglés de la plantilla**: créditos, página de reseña y rótulos en inglés, sin el
  manifiesto en español. Añadir `idioma = "en"` en `libro.toml` y los textos correspondientes en
  `scripts/maquetar.py` y `plantillas/libro.typ`, sin romper los libros en español.
- La competencia en Amazon.com se estimó solo por búsquedas web: el responsable la comprobará antes del lanzamiento.

— Editor Jefe

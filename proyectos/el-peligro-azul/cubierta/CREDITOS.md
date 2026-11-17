# Cubierta — El peligro azul

## Propuesta 1: el vapor y los tentáculos (17-11-2026)

- `ilustracion_chatgpt_vapor.png` (1024 × 1536 px): ilustración original del responsable, generada con ChatGPT
  y entregada el 17-11-2026. Sin derechos de terceros.
- En el recuadro de Límite Abisal (3,75 × 5,41 in) queda a ≈ 273 ppp: por debajo de 300 pero aceptable. Si
  se elige como definitiva, conviene pedir a ChatGPT la misma imagen a mayor tamaño o ampliarla.
- Composición: `scripts/cubierta.py` → `el-peligro-azul_cubierta_kdp.pdf` / `.jpg`, `el-peligro-azul_portada_ebook.jpg`.

## Propuesta 2: la cumbre del Colombier (17-11-2026)

- `ilustracion_manus_colombier.png` (1333 × 2000 px): ilustración original del responsable, generada con
  Manus (manus.im) a partir de la propuesta A de `PROMPTS.md`, entregada el 17-11-2026.
- En el recuadro de Límite Abisal queda a ≈ 355 ppp: válida para imprenta.
- Composición: `python3 scripts/cubierta.py proyectos/el-peligro-azul --variante 2` →
  `el-peligro-azul_cubierta_kdp_p2.pdf` / `_p2.jpg`, `el-peligro-azul_portada_ebook_p2.jpg`.
- Los ficheros sin sufijo son la propuesta 1 (los que usa ahora el EPUB). Cuando el responsable elija, la
  elegida pasa a ser la `ilustracion` principal de `[cubierta]` y se regenera el EPUB.

#!/usr/bin/env python3
"""Makt myrkranna: portada a 300 ppp.

Amplía la portada del responsable (portada_responsable.jpg, 1253 x 2000) al alto de la cubierta KDP con
sangrado (9,25 in = 2775 px) y sustituye el recuadro de la ilustración por la ilustración original
(ilustracion_responsable.webp, 1024 x 1536), alineada con el encuadre de la portada y con su mismo tono
(transferencia de color por canal). Resultado: portada_300ppp.png (la usa cubierta.py vía libro.toml).
Uso: python3 proyectos/makt-myrkranna/cubierta/componer_portada.py
"""
from pathlib import Path
from PIL import Image, ImageFilter
import numpy as np

D = Path(__file__).resolve().parent
por = Image.open(D / "portada_responsable.jpg").convert("RGB")
ilu = Image.open(D / "ilustracion_responsable.webp").convert("RGB")
X0, Y0, X1, Y1 = 218, 606, 1035, 1762          # recuadro de la ilustración en la portada (px, medidos)
H = 2775                                       # 9,25 in a 300 ppp
caja = np.asarray(por.crop((X0, Y0, X1, Y1))).astype(float)
bw, bh = X1 - X0, Y1 - Y0

# 1. Encuadre: la ilustración ocupa todo el ancho del recuadro; se busca el desplazamiento vertical
esc = bw / ilu.width
peq = np.asarray(ilu.resize((bw, round(ilu.height * esc)), Image.LANCZOS)).astype(float)
g = lambda a: (a.mean(2) - a.mean()) / (a.std() + 1e-6)
gc = g(caja)
mejor = min(range(0, peq.shape[0] - bh + 1), key=lambda dy: np.mean((g(peq[dy:dy + bh]) - gc) ** 2))
print(f"desplazamiento vertical: {mejor} px (de {peq.shape[0] - bh})")

# 2. Color: ajuste lineal por canal (media y desviación) de la ilustración al recuadro de la portada
ref = peq[mejor:mejor + bh]
a = [caja[..., c].std() / ref[..., c].std() for c in range(3)]
b = [caja[..., c].mean() - a[c] * ref[..., c].mean() for c in range(3)]

# 3. Composición a 300 ppp
k = H / por.height
grande = por.resize((round(por.width * k), H), Image.LANCZOS).filter(ImageFilter.UnsharpMask(1.2, 60, 2))
cx0, cy0, cx1, cy1 = (round(v * k) for v in (X0, Y0, X1, Y1))
y_ilu0 = mejor / esc; y_ilu1 = (mejor + bh) / esc     # franja de la ilustración original que se ve
recorte = ilu.crop((0, round(y_ilu0), ilu.width, round(y_ilu1))).resize((cx1 - cx0, cy1 - cy0), Image.LANCZOS)
r = np.asarray(recorte).astype(float)
r = np.stack([np.clip(a[c] * r[..., c] + b[c], 0, 255) for c in range(3)], 2).astype(np.uint8)
grande.paste(Image.fromarray(r), (cx0, cy0))
grande.save(D / "portada_300ppp.png")
ppp = 300 * ilu.width / (cx1 - cx0)
print(f"portada_300ppp.png {grande.size}; ilustración a {ppp:.0f} ppp efectivos "
      f"(recuadro {cx1 - cx0} x {cy1 - cy0} px con {ilu.width} x {round(y_ilu1 - y_ilu0)} px de origen)")

# Rotula en español el croquis de 1911 (cap. IX de la 1.ª parte).
# Uso: python3 imagenes/rotula_croquis.py imagenes/croquis_1911_960px.jpg imagenes/croquis_huellas_es.png ../../fuentes/CormorantGaramond-Italic.ttf
from PIL import Image, ImageDraw, ImageFont
import sys
src, dst, fuente = sys.argv[1:4]
im = Image.open(src).convert("L")
K = 2
im = im.resize((im.width*K, im.height*K), Image.LANCZOS)
d = ImageDraw.Draw(im)
def borra(x0,y0,x1,y1): d.rectangle((x0*K,y0*K,x1*K,y1*K), fill=255)
borra(80,78,350,156)     # título + subrayado
borra(15,294,131,319)    # Ligne de faîte
borra(460,293,494,310)   # Croix
def f(t): return ImageFont.truetype(fuente, t*K)
tinta = 40
# Título
ft = f(30)
t = "Esquema de las huellas"
w = d.textlength(t, font=ft)
d.text((85*K, 92*K), t, font=ft, fill=tinta)
cx = 85*K + w/2
d.line((cx-28*K, 148*K, cx+28*K, 148*K), fill=tinta, width=2*K)
# Rótulos
d.text((18*K, 294*K), "Línea de cumbre", font=f(20), fill=tinta)
d.text((461*K, 289*K), "Cruz", font=f(20), fill=tinta)
im.save(dst, dpi=(300,300))

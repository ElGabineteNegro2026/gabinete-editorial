#!/usr/bin/env python3
"""Genera ilustraciones de cubierta con la API de imágenes de OpenAI (la misma familia que ChatGPT).

Uso:
  python3 scripts/ilustracion.py proyectos/<slug> "descripción de la escena" [--n 3] [--formato vertical|horizontal|cuadrado] [--modelo gpt-image-2]

Guarda las imágenes en proyectos/<slug>/cubierta/ilustracion_<fecha>_<n>.png y el prompt usado en
proyectos/<slug>/cubierta/PROMPTS.md (para poder repetir o variar una ilustración).

La clave NO se guarda en el repositorio: es un secreto de red del entorno de Claude para api.openai.com,
que el proxy añade a cada petición. Si el secreto no está configurado, la API responde 401.

Las ilustraciones salen sin texto: títulos, autor y filetes los pone scripts/cubierta.py con las tipografías
de la colección, para que la composición sea siempre exacta y editable.
"""
import base64, datetime, json, os, sys, urllib.error, urllib.request
from pathlib import Path

ESTILO = {
    "limite-abisal": "dark nocturnal pastel and engraving illustration, desaturated teal and blue-green palette, "
                     "cosmic horror, vast ocean depths, ancient indifferent forces, fine cross-hatching",
    "camara-sellada": "antique sepia and aged gold illustration, Belle Epoque / Victorian gothic atmosphere, "
                      "enclosed spaces, candlelight, moonlight, ornate details, painterly etching",
    "archivo-arcano": "dark Victorian gothic engraving, black background, aged ivory and charcoal tones with "
                      "blood-red accents, castles, manuscripts, wax seals, red velvet, full moon, bats, highly detailed",
    "archivo-lupin": "cinematic Belle Epoque Paris night scene, deep petrol blue palette with warm candle highlights, "
                     "elegant gentleman thief in top hat seen from behind, mansions, safes, marble busts",
}
TAMANOS = {"vertical": "1024x1536", "horizontal": "1536x1024", "cuadrado": "1024x1024"}

def main():
    args = sys.argv[1:]
    dir_proy = (Path.cwd() / args[0]).resolve(); escena = args[1]
    opc = lambda k, d: args[args.index(k) + 1] if k in args else d
    n = int(opc("--n", "2")); formato = opc("--formato", "vertical"); modelo = opc("--modelo", "gpt-image-2")
    import tomllib
    col = tomllib.loads((dir_proy / "libro.toml").read_text(encoding="utf-8"))["coleccion"]
    prompt = (f"{escena}. Style: {ESTILO[col]}. Book cover artwork for a classic horror/mystery edition. "
              "No text, no letters, no typography, no title, no border, no frame, no watermark.")
    cuerpo = json.dumps({"model": modelo, "prompt": prompt, "n": n, "size": TAMANOS[formato], "quality": "high"}).encode()
    req = urllib.request.Request("https://api.openai.com/v1/images/generations", data=cuerpo, headers={
        "Content-Type": "application/json",
        # El proxy del entorno sustituye esta cabecera por la clave guardada como secreto de red.
        "Authorization": "Bearer " + os.environ.get("OPENAI_API_KEY", "proxy-inyecta-la-clave")})
    try:
        with urllib.request.urlopen(req, timeout=600) as r:
            datos = json.load(r)
    except urllib.error.HTTPError as e:
        try: err = json.load(e).get("error", {})
        except Exception: err = {}
        # 401: clave mal configurada · 429 insufficient_quota: la cuenta de API no tiene saldo
        sys.exit(f"OpenAI {e.code}: {err.get('code') or ''} {err.get('message') or e.reason}")
    out = dir_proy / "cubierta"; out.mkdir(exist_ok=True)
    marca = datetime.datetime.now().strftime("%Y%m%d_%H%M")
    rutas = []
    for i, img in enumerate(datos["data"], 1):
        ruta = out / f"ilustracion_{marca}_{i}.png"
        ruta.write_bytes(base64.b64decode(img["b64_json"])); rutas.append(ruta)
    with open(out / "PROMPTS.md", "a", encoding="utf-8") as f:
        f.write(f"\n## {marca} · {modelo} · {TAMANOS[formato]}\n\n{prompt}\n\n" + "\n".join(f"- {r.name}" for r in rutas) + "\n")
    for r in rutas: print(r.relative_to(dir_proy))

if __name__ == "__main__":
    main()

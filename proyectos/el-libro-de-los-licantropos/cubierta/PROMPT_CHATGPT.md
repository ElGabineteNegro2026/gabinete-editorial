# Prompt para ChatGPT: propuesta C de cubierta (*El libro de los licántropos*)

## Medidas

ChatGPT hace **solo la ilustración**. El título, los autores, el marco dorado, el lomo y la contracubierta los
compone `scripts/cubierta.py`.

| | Medida |
|---|---|
| Hueco de la ilustración en la portada (imprenta) | **5,333 × 4,400 in = 1600 × 1320 px a 300 ppp**, horizontal (proporción 1,21:1, unos 6:5) |
| Hueco en la portada del ebook | 1422 × 1333 px: casi cuadrado; se recorta por los lados |
| Imagen que hay que pedir a ChatGPT | **horizontal, 1536 × 1024 px** (el formato apaisado más cercano que genera). Sirve para los dos huecos, recortando los lados. |
| Fundidos | El 18 % de arriba y el 18 % de abajo de la imagen se funden con el negro del fondo: no poner nada importante ahí. |
| Cubierta completa (orientativa) | 14,865 × 10,418 in. **Es provisional**: la medida exacta la da la calculadora de cubiertas de KDP (tapa dura, 266 páginas, papel blanco). No afecta a la ilustración. |

## Prompt

> Crea una ilustración horizontal de 1536 × 1024 píxeles para la cubierta de un libro de tapa dura de relatos
> clásicos de hombres lobo. Estilo de grabado antiguo al aguafuerte, muy oscuro y detallado, con trama de líneas
> finas y aspecto envejecido, como una lámina victoriana. Escena: un claro en un bosque de pinos de montaña en
> pleno invierno, de noche, con la nieve iluminada por una luna velada entre nubes. En el centro de la imagen,
> de perfil, una mujer joven con un largo camisón blanco, descalza sobre la nieve, arrodillada junto a una tumba
> de piedras removidas. Su sombra, proyectada sobre la nieve, es la de un gran lobo. Al fondo, a la derecha, entre
> los troncos, una cabaña con una ventana iluminada de luz cálida. Paleta: negros profundos, grises de tinta,
> blanco hueso en la nieve y en el camisón, y un único acento rojo sangre en las manos de la mujer y en unas gotas
> sobre la nieve; nada más en color. Composición: todo lo importante (la mujer, la sombra de lobo y la tumba) en la
> franja central de la imagen y en sus dos tercios centrales a lo ancho; la franja superior, cielo oscuro y copas
> de pinos casi negras; la franja inferior, nieve en penumbra. Sin texto, sin letras, sin marco, sin borde y sin
> firma.

Si la primera versión sale demasiado clara o en color, añadir: «más oscura, casi monocroma, como un grabado en
negro sobre papel envejecido, con el rojo solo en las manos y en la nieve».

La escena es la del relato de Marryat («La loba blanca de las montañas del Harz»), el más conocido del volumen.
Guardar el resultado en `proyectos/el-libro-de-los-licantropos/cubierta/` (o adjuntarlo) en PNG, sin recortar.

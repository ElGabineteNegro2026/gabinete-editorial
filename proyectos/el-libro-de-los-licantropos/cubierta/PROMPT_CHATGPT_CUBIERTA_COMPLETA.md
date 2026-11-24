# Prompt para ChatGPT: cubierta completa de tapa dura (*El libro de los licántropos*)

Adjuntar la plantilla de KDP (tapa dura, 266 páginas, papel blanco) y pegar:

```
Diseña la cubierta completa (contracubierta + lomo + portada) de un libro de TAPA DURA, ajustándote EXACTAMENTE a la plantilla de KDP que te adjunto: respeta sus medidas, la zona de vuelta (wrap) y sangrado de 0,709 in por los cuatro lados, las bisagras de 0,394 in a cada lado del lomo y la zona segura. Nada de texto ni elementos importantes en la vuelta ni en las bisagras. Elimina las guías y los colores de la plantilla en el resultado final.

COLECCIÓN Y ESTILO: «Archivo Arcano», antologías clásicas de terror en edición de lujo. Aspecto de libro antiguo de biblioteca prohibida, sobrio y elegante, nada de estética de película moderna.
- Fondo negro profundo (#0b0a09) con textura de cuero o papel envejecido muy sutil.
- Marco dorado ornamental (#c9a25a), doble filete fino con filigrana victoriana en las esquinas, en la portada y en la contracubierta, por dentro de la zona segura.
- Tipografía: serif clásica de inscripción romana en versales (tipo Cinzel o Trajan) para títulos y autores; serif de libro (tipo Cormorant Garamond) para la sinopsis.
- Colores de texto: crema envejecido (#e8dcc0) para el título, dorado (#c9a25a) para autores y rótulos, rojo sangre (#b3262b) para el subtítulo.

PORTADA (mitad derecha), de arriba abajo:
1. Autores en dos líneas, versales doradas pequeñas y espaciadas:
   «PETRONIO · MARIE DE FRANCE · MARRYAT · CROWE»
   «ERCKMANN-CHATRIAN · STENBOCK · BIERCE · SAKI»
2. Filete dorado fino con un pequeño rombo en el centro.
3. Título muy grande, en dos líneas, crema con una ligera sombra:
   «EL LIBRO DE LOS»
   «LICÁNTROPOS»  (con tilde en la Á)
4. Subtítulo en versales rojo sangre, dos líneas:
   «HISTORIAS DE HOMBRES LOBO»
   «DE PETRONIO A SAKI»
5. Filete dorado con rombo.
6. Ilustración en la mitad inferior de la portada, fundida con el fondo negro por arriba y por abajo (sin recuadro duro): estilo grabado antiguo al aguafuerte, trama de líneas finas, negros profundos, grises de tinta y blanco hueso, con un único acento rojo. Escena: un claro en un bosque de pinos de montaña en invierno, de noche, nieve iluminada por una luna velada. En primer plano, una mujer joven de espaldas o de perfil, con un largo camisón blanco, descalza sobre la nieve, junto a una tumba de piedras removidas; su sombra sobre la nieve es la de un gran lobo. Al fondo, entre los troncos, una cabaña con una ventana de luz cálida. El acento rojo: sus manos o unas gotas en la nieve.
7. Abajo, centrado, en versales crema pequeñas: «ARCHIVO ARCANO · EL GABINETE NEGRO».

LOMO (centro), enmarcado con un doble filete dorado fino:
- Arriba, en horizontal, dos líneas doradas pequeñas: «HOMBRES» / «LOBO», y debajo un filete corto.
- En el centro, en vertical (leyéndose de arriba abajo, con el libro tumbado boca arriba), en dorado: «EL LIBRO DE LOS LICÁNTROPOS».
- Abajo, en horizontal, en crema: «ARCHIVO» / «ARCANO» y debajo «V».

CONTRACUBIERTA (mitad izquierda), dentro del marco dorado:
1. Arriba, frase gancho en versales doradas, centrada:
   «HAY ALGO EN EL BOSQUE QUE NO TERMINA DE SER UN ANIMAL»
2. Sinopsis centrada, en crema, cuerpo de lectura cómodo, dos párrafos, con este texto exacto:
   «Un soldado que se desnuda en un cementerio a la luz de la luna. Un caballero bretón al que su esposa roba la ropa. Un pastor de trece años que confiesa ante el Parlamento de Burdeos. Una madrastra hermosa que sale de noche en camisón y vuelve con las manos sucias. Una vieja que aúlla en la nieve de la Selva Negra. Un muchacho que toma el sol desnudo junto al río y que, cuando le preguntan de qué se alimenta, responde con toda naturalidad.
   Trece textos, de la Roma de Nerón a la Inglaterra eduardiana, reúnen la gran tradición literaria del hombre lobo: leyendas medievales, actas de los procesos de licantropía, cuentos góticos victorianos y relatos de Marryat, Erckmann-Chatrian, Bierce y Saki, en nueva traducción de El Gabinete Negro, con prólogo y apéndice. Antes de la luna llena y de la bala de plata, el hombre lobo era el vecino, el marido, la esposa: alguien que guardaba un secreto.»
3. Opcional: una pequeña viñeta de grabado (una cabeza de lobo o una huella en la nieve) en dorado apagado, debajo de la sinopsis.
4. Abajo, centrado: «EL GABINETE NEGRO» en versales doradas pequeñas y espaciadas; abajo a la izquierda, muy pequeño: «elgabinetenegro.com».
5. Abajo a la derecha, deja LIBRE un rectángulo de 2 × 1,2 in para el código de barras de KDP: solo fondo, sin texto, sin recuadro blanco y sin dibujar nada en él.

REGLAS: todo el texto en español, exactamente como está escrito arriba, con sus tildes. Sin otros textos, logotipos, precios ni firmas. Resolución máxima, 300 ppp si es posible.
```

## Avisos

- **Resolución.** La cubierta completa a 300 ppp mide unos 4.460 × 3.125 px. Si ChatGPT entrega menos, KDP puede
  rechazarla o imprimirla borrosa.
- **Texto.** ChatGPT se equivoca a menudo con tildes y textos largos («LICÁNTROPOS», la sinopsis). Hay que revisar
  letra a letra.
- **Plan B.** Si el resultado no sirve tal cual, basta con la ilustración de la portada (punto 6, sin texto), y el
  Editor Jefe compone la cubierta con `scripts/cubierta.py` y las medidas exactas de la plantilla.

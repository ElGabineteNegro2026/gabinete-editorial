# Alta en WooCommerce de los libros nuevos — encargo para el Responsable Social Media

Preparado por el Editor Jefe el 17-11-2026, por encargo del responsable: «dar de alta los nuevos libros en
WooCommerce tomando como referencia cualquiera de los libros ya visibles, igual o mejor».

Libros: **Makt myrkranna** (Límite Abisal XIX), **813** (Archivo Lupin, Dossier IV) y **El peligro azul**
(Límite Abisal XX). Los textos de esta ficha son los aprobados para la contracubierta, adaptados a la web.

## Cómo están hechas las fichas actuales (modelo que hay que seguir)

Referencias: *En las montañas de la locura* (id 892), *Arsène Lupin y la Aguja Hueca* (id 1040) y
*Drácula: Los manuscritos perdidos* (id 1283, la más completa).

- **Tipo:** producto *externo/afiliado* (`external`).
- **URL del producto:** la del **libro de tapa blanda** en Amazon.es. **Texto del botón:** `Tapa blanda | 14,49€`.
- **Precio normal:** el de la tapa blanda (14,49 o 13,95). Sin SKU, sin etiquetas, sin atributos.
- **Categoría:** `Colección Límite Abisal` o `Colección Archivo Lupin` (ya existen).
- **Descripción corta:** 2-3 párrafos centrales de la descripción larga y, al final, los botones de
  Shortcodes Ultimate de los demás formatos (eBook y, si lo hay, audiolibro), con este código exacto:

  ```html
  <a href="URL_AMAZON_EBOOK" class="su-button su-button-style-ghost" style="color:#ffcea5;background-color:#ffc89a;border-color:#cca07c;border-radius:0px" target="_blank" rel="noopener noreferrer"><span style="color:#ffcea5;padding:0px 24px;font-size:18px;line-height:36px;border-color:#ffd9b9;border-radius:0px"> eBook | 2,99€</span></a>
  ```
- **Descripción larga:** gancho → sinopsis con el título en negrita y cursiva → párrafo sobre la obra → «Esta
  edición de *Colección* incluye…» → cierre en dos o tres frases breves.
- **Imagen principal:** la portada. Drácula añade también ilustraciones interiores a la galería.

## Mejoras sobre el modelo (pedidas: «igual, o mejor si puede»)

1. **No poner el botón de audiolibro** si no hay audiolibro. La Aguja Hueca lo tiene con `href=""`: es un
   enlace roto (conviene corregirlo allí también, o quitar el botón).
2. **Enlaces de Amazon definitivos** del tipo `https://www.amazon.es/dp/ASIN`, no `link.amazon/...`.
3. **Texto alternativo** de la portada: «Cubierta de *Título*, de Autor (El Gabinete Negro, Colección X)».
4. **Galería:** portada + contracubierta (recorte de la cubierta completa de KDP) + material extra cuando lo
   haya (croquis de 1911 de *El peligro azul*). Si haces maquetas 3D del libro, mejor todavía.
5. **Ficha técnica** al final de la descripción larga (páginas, formato, papel, traducción, colección).
6. **Meta descripción SEO** (≤ 155 caracteres; la propongo abajo) si el plugin de SEO de la web lo permite.
7. **Corrección de un error de la referencia:** en Drácula pone «laminas»; debe ser «láminas».

## Mientras no haya enlaces de Amazon

Los tres libros **aún no están en KDP**: Makt myrkranna sale esta semana (16-22 de noviembre); 813 y El
peligro azul, la semana del 23 al 29 de noviembre. Por tanto:

- Crea las tres fichas **en borrador** (o programadas), con todo menos las URL de Amazon.
- Cuando el responsable pase los ASIN (tapa blanda y ebook), rellena las URL y **publica**. No publiques una
  ficha con el botón de compra vacío.
- No inventes ni adivines ASIN.

---

## 1. Makt myrkranna. Los poderes de la oscuridad

- **Nombre del producto:** `Makt myrkranna: Los poderes de la oscuridad`
- **Slug:** `makt-myrkranna-los-poderes-de-la-oscuridad`
- **Categoría:** Colección Límite Abisal
- **Precio:** 14,49 € · Botón: `Tapa blanda | 14,49€` · eBook: `eBook | 2,99€`
- **ISBN tapa blanda:** 979-8-14-316368-3
- **Imagen:** `novedades/portadas/makt-myrkranna_portada.jpg` (1600 × 2560). Cubierta completa:
  `proyectos/makt-myrkranna/cubierta/makt-myrkranna_cubierta_kdp.jpg`
- **Meta descripción:** «El Drácula islandés de 1900: personajes nuevos, otro castillo y otro final. Traducción
  de El Gabinete Negro. Colección Límite Abisal, vol. XIX.»

**Descripción larga**

```html
<p><strong>El lector cree conocer esta historia. Se equivoca.</strong></p>
<p>Thomas Harker, joven pasante de un bufete londinense, viaja a los Cárpatos para cerrar la venta de una vieja mansión inglesa. Su cliente, el conde Drácula, lo recibe con una cortesía exquisita en un castillo sin criados, sin espejos y sin salida.</p>
<p>En 1900, el periódico islandés <em>Fjallkonan</em> empezó a publicar por entregas una versión de <em>Drácula</em> con un prólogo firmado por el propio Bram Stoker. Durante más de un siglo se tuvo por una simple traducción abreviada, hasta que alguien la leyó con atención: personajes nuevos, una mujer que ronda al prisionero, una conspiración que alcanza a la aristocracia europea y un final distinto.</p>
<p><strong><em>Makt myrkranna</em></strong> («Los poderes de la oscuridad»), la versión islandesa preparada por Valdimar Ásmundsson, no es una copia de la novela de Stoker: es otra novela. Su autoría exacta (Ásmundsson, Stoker o ambos) sigue siendo uno de los enigmas más fascinantes de la literatura vampírica.</p>
<p>Esta edición de <strong>Límite Abisal</strong> ofrece una traducción de El Gabinete Negro e incluye el prólogo de 1900 atribuido a Stoker, un prólogo de la editorial y un apéndice explicativo sobre la historia del texto.</p>
<p><em>«Estoy totalmente convencido de que los acontecimientos aquí descritos tuvieron realmente lugar, por muy increíbles e incomprensibles que puedan parecer».</em> — Bram Stoker, prólogo de 1900</p>
<p>La misma sombra. Otro rostro.</p>
<p><strong>Ficha:</strong> Colección Límite Abisal, vol. XIX · 186 páginas · 15,24 × 22,86 cm · tapa blanda, papel crema · Traducción: El Gabinete Negro.</p>
```

**Descripción corta:** los párrafos 2.º a 4.º y debajo el botón de eBook.

**Cuidado:** no presentarlo como «una obra inédita de Stoker». Es una adaptación islandesa con material nuevo.

---

## 2. 813 (El Archivo Lupin nº 4)

- **Nombre del producto:** `813 (El Archivo Lupin nº 4)`. Sigue el patrón de «Arsène Lupin y la Aguja Hueca (El
  Archivo Lupin nº 3)»; si se prefiere más descriptivo: `Arsène Lupin: 813 (El Archivo Lupin nº 4)`.
- **Slug:** `813-el-archivo-lupin-no-4`
- **Categoría:** Colección Archivo Lupin
- **Precio:** 13,95 € · Botón: `Tapa blanda | 13,95€` · eBook: `eBook | 2,99€`
- **Imagen:** `novedades/portadas/813_portada.jpg` (1600 × 2560). Cubierta completa:
  `proyectos/813/cubierta/813_cubierta_kdp.jpg`
- **Meta descripción:** «Un magnate asesinado, una cifra indescifrable y un asesino de negro. La aventura más
  sombría de Arsène Lupin. El Archivo Lupin, Dossier IV.»

**Descripción larga**

```html
<p>Un magnate asesinado. Una cigarrera con dos iniciales. Una cifra que nadie sabe descifrar. Y, por primera vez, un enemigo más rápido que Arsène Lupin.</p>
<p>París, Palace Hotel. El millonario Rodolfo Kesselbach aparece asesinado en su suite. Junto al cadáver, una cigarrera con las iniciales «L. M.» y, en su agenda, un número: <strong>813</strong>.</p>
<p>Arsène Lupin solo había ido a robarle. Ahora es el principal sospechoso de un crimen que no ha cometido, y el asesino, un hombre vestido de negro al que nadie ha visto el rostro, va siempre un paso por delante.</p>
<p>En <strong><em>813</em></strong>, Maurice Leblanc lleva a su caballero ladrón más lejos que nunca. Para alcanzar al asesino, Lupin tendrá que desdoblarse en el príncipe Sernine y en el mismísimo jefe de la Sûreté, el señor Lenormand, y dirigir la investigación de su propio caso, mientras se asoma a un secreto capaz de sacudir los tronos de Europa.</p>
<p>Es la aventura más sombría de Lupin, y la primera en que pierde.</p>
<p>Esta edición forma parte de <strong>El Archivo Lupin</strong>, la colección de El Gabinete Negro dedicada a las aventuras de Maurice Leblanc. Incluye un <strong>prólogo literario y un apéndice contextual</strong> para situar la novela en su época.</p>
<p><strong>Cuando Lupin dice una cosa, esta se cumple.</strong></p>
<p>El expediente queda abierto.</p>
<p><strong>Ficha:</strong> El Archivo Lupin, Dossier IV · 444 páginas · 15,24 × 22,86 cm · tapa blanda, papel crema.</p>
```

**Descripción corta:** los párrafos 2.º a 4.º y debajo el botón de eBook.

---

## 3. El peligro azul

- **Nombre del producto:** `El peligro azul`
- **Slug:** `el-peligro-azul`
- **Categoría:** Colección Límite Abisal
- **Precio:** 14,49 € · Botón: `Tapa blanda | 14,49€` · eBook: `eBook | 2,99€`
- **Imagen:** `novedades/portadas/el-peligro-azul_portada.jpg` (1600 × 2560). Cubierta completa:
  `proyectos/el-peligro-azul/cubierta/el-peligro-azul_cubierta_kdp.jpg`. Galería:
  `novedades/portadas/el-peligro-azul_croquis_1911.png` (croquis de las huellas en la nieve, que va en el cap. IX).
- **Meta descripción:** «Primavera de 1912: en el Jura desaparecen objetos y luego personas, sin dejar huella.
  La novela de Maurice Renard, por primera vez en español.»

**Descripción larga**

```html
<p>Tres rastros suben por la nieve hasta la cruz de la cumbre. Ninguno baja. Arriba no hay nadie.</p>
<p>Primavera de 1912. En el Bugey, al pie del Jura, empiezan a desaparecer cosas: las agujas de un reloj, una bandera, el gallo de hierro de un campanario, una estatua de jardín. Nadie ve a los ladrones; no dejan huellas, y todo lo que se llevan estaba al aire libre y en alto. Los campesinos los llaman <em>sarvants</em>: duendes, aparecidos.</p>
<p>Un día dejan de llevarse cosas y empiezan a llevarse personas.</p>
<p>En <strong><em>El peligro azul</em></strong> (<em>Le Péril bleu</em>, 1911), Maurice Renard, el maestro de lo «maravilloso científico», convierte una crónica de pueblo en una pesadilla de escala planetaria: una novela de humor, de suspense y de vértigo cósmico sobre lo que no vemos, escrita antes de que Conan Doyle publicara <em>El horror de las alturas</em>.</p>
<p>Esta edición de <strong>Límite Abisal</strong> es, hasta donde sabemos, la primera traducción al español. Incluye un prólogo original, un apéndice explicativo y el croquis de 1911 de las huellas en la nieve, rotulado en español.</p>
<p><em>«Mirad. Luego reflexionad. Luego soñad. Esto no es imposible».</em> — Maurice Renard</p>
<p>Hay terrores que vienen de abajo. Este viene de encima.</p>
<p><strong>Ficha:</strong> Colección Límite Abisal, vol. XX · 378 páginas · 15,24 × 22,86 cm · tapa blanda, papel crema · Traducción: El Gabinete Negro.</p>
```

**Descripción corta:** los párrafos 2.º a 4.º y debajo el botón de eBook.

**Cuidado:** no revelar qué son los *sarvants* ni adónde se llevan a sus víctimas. No decir «inédita» sin
matiz: «primera traducción al español, hasta donde sabemos».

---

## Al terminar

Deja nota en este fichero (o en tu repositorio) con el id de producto de cada libro, si está en borrador o
publicado y lo que falta (ASIN). El Editor Jefe no toca la web.

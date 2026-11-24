# Plan de crecimiento — trabajo del Editor Jefe (23-11-2026)

Responde al encargo del 20-11-2026 (`informes/2026-11-20_encargo-estrategia.md`). Las decisiones se piden en el
informe semanal (`informes/2026-11-23.md`, «Decisiones pendientes»). En este documento no hay cifras económicas, salvo precios de venta propuestos.

## 1. Omnibus y packs

Fichas en `candidatos/`:

| # | Propuesta | Colección | Formatos | Páginas | Precio propuesto | Plazo | Puntuación |
|---|---|---|---|---|---|---|---|
| 1 | *Los Mitos de Cthulhu. Relatos y novelas esenciales de horror cósmico de H. P. Lovecraft* (`2026-11-23_omnibus-lovecraft.md`) | Límite Abisal | tapa blanda + ebook | ≈ 620 | 24,95 € / 6,99 € | **antes de Navidad** | 9 |
| 2 | *La cámara sellada. Antología del relato gótico y de fantasmas* (`2026-11-23_antologia-gotica-camara-sellada.md`) | Cámara Sellada | tapa blanda + ebook | ≈ 475 | 19,95 € / 5,99 € | 1.er trimestre de 2027 | 7 |
| 3 | *El Archivo Lupin. Dossiers I-IV* (`2026-11-23_pack-archivo-lupin.md`) | Archivo Lupin | solo ebook | ≈ 1.350 (ebook) | 8,99 € | en cuanto salga *813* | 8 |

**Lo que bloquea a los tres**: no consta en el repositorio el origen de las traducciones ya publicadas.
- Para cada libro que se vaya a reutilizar hace falta saber si la traducción es de la casa, de un traductor
  fallecido antes de 1946 o si se tienen derechos.
- La ficha de *Otra vuelta de tuerca* en la tienda dice «nueva traducción de Almudena Berlanga», y el RTF de *813*
  venía de una edición anterior («Arsenio Lupin # 04»).
- Si no se pueden acreditar, la casa traduce de nuevo. Para el omnibus de Lovecraft caben 3-4 sesiones antes de Navidad.

## 2. Línea en inglés

Ver `candidatos/2026-11-23_plan-linea-ingles.md` (investigación de ediciones y precios en Amazon.com).

**Aviso de derechos**: Blackwood (†1951), Machen (†1947), Dunsany (†1957) y Clark Ashton Smith (†1961) **no están en
dominio público en la UE**. En EE. UU. lo están sus textos publicados antes de 1931. Si se publican en inglés,
habría que limitar los territorios en KDP, salvo que las licencias del responsable cubran el inglés y todos los
territorios.

## 3. Inéditos

Los candidatos nuevos de esta semana priorizan las primeras traducciones al español: ver el informe semanal.

## 4. Reseñas y fichas

### 4.1 Página de petición de reseña: hecha

- Añadida a la plantilla (`plantillas/libro.typ`, `scripts/maquetar.py`). Sale en el PDF, el DOCX y el EPUB, tras la
  página «El Gabinete Negro» y antes del índice. Muestra: `informes/2026-11-23_vistas/pagina_resena_muestra.png`.
- Texto: «Una petición del Gabinete». Pide una reseña breve y sincera, «favorables o no», sin ofrecer nada a cambio.
- Por defecto va en todos los libros nuevos. `pagina_resena = false` en `libro.toml` la quita.
- *813*, *El peligro azul* y *Makt myrkranna* llevan de momento `pagina_resena = false`, para no cambiar las páginas
  ni el lomo sin aprobación. Activarla suma **2 páginas** en *813* (444 → 446) y en *El peligro azul* (378 → 380), y
  ensancha el lomo 0,005 in; hay que regenerar las cubiertas (CONSULTA).

**Libros publicados que habría que volver a subir con la página** (lo hace el responsable; el Editor Jefe puede
regenerar los interiores de los que tengan proyecto en este repositorio):

| Prioridad | Libros | Motivo |
|---|---|---|
| Alta | *Makt myrkranna* (proyecto aquí: basta con quitar `pagina_resena = false`, maquetar y regenerar la cubierta, lomo +0,005 in) | novedad, inédito |
| Alta | *El Rey de Amarillo*, *Zothique*, *En las montañas de la locura*, *La casa en el confín de la tierra*, *Los perros de Tíndalos* | Límite Abisal: la colección que más vende |
| Alta | Las 4 tapas duras de Archivo Arcano | más ingreso por venta; campaña de Navidad |
| Media | Archivo Lupin I-III | lectores en serie |
| Media | resto de Límite Abisal | — |
| Baja | Cámara Sellada | ventas bajas; mejor esperar a la antología |

Los libros sin proyecto en el repositorio necesitan su manuscrito: o se añade la página a mano en Word con el
texto de `scripts/maquetar.py` (constante `RESENA`), o el responsable deja los manuscritos y se rehacen aquí.

### 4.2 Series para KDP

KDP permite agrupar los libros en una serie, con nombre y número. Propuesta: una serie por colección, con el mismo
nombre en tapa blanda, tapa dura y ebook. **Los números de volumen de los libros publicados no constan en el
repositorio**, salvo los indicados; el resto lo rellena el responsable. El orden se toma de la tienda (por fecha de alta).

| Serie KDP (nombre exacto) | Títulos (volumen conocido o a confirmar) |
|---|---|
| **Límite Abisal (El Gabinete Negro)** | *Makt myrkranna* XIX · *El peligro azul* XX · resto a confirmar: *La sombra sobre Innsmouth*, *El gran dios Pan*, *Los Sauces – El Wendigo*, *Mareas negras*, *La Marca de la Bestia*, *El Rey de Amarillo*, *Narraciones del abismo*, *El horror de Dunwich*, *El Libro de Eibon*, *La casa en el confín de la tierra*, *El pueblo blanco*, *El caso de Charles Dexter Ward*, *Los perros de Tíndalos*, *Zothique*, *Los últimos días de la Tierra*, *En las montañas de la locura* (16 + 2 = 18 títulos para XX números: faltan 2, quizá *El mar de las tinieblas*, de la portada de referencia) |
| **Cámara Sellada (El Gabinete Negro)** | 14 títulos de la tienda, más *Belfegor* (portada de referencia; no aparece en la tienda); volúmenes a confirmar |
| **Archivo Arcano (El Gabinete Negro)** | *El libro de las casas encantadas*, *El libro de los cultos prohibidos*, *El libro de los objetos malditos*, *Drácula: Los manuscritos perdidos* (I-IV, orden a confirmar) · *El libro de los licántropos* V (en pausa) |
| **El Archivo Lupin** | I *Arsène Lupin, caballero ladrón* · II *Arsène Lupin contra Herlock Sholmès* · III *Arsène Lupin y la Aguja Hueca* · IV *813* |

Notas:
- KDP permite un libro en una sola serie. Los omnibus pueden ir en la serie de su colección sin número o con número
  propio («Límite Abisal, edición especial»). La alternativa es crear la serie «Omnibus El Gabinete Negro» (CONSULTA).
- En Amazon.es el nombre de serie aparece como enlace («Libro 3 de 4: El Archivo Lupin»). Conviene que sea igual al de la cubierta.

### 4.3 Subtítulos con palabras de búsqueda (CONSULTA)

Criterios:
- Lo que la gente busca de verdad: «relatos de terror», «terror gótico», «horror cósmico», «novela de detectives»,
  «clásicos de terror».
- Sin repetir el título.
- Sin las palabras que KDP rechaza: «bestseller», «gratis», «nuevo», «Kindle Unlimited», precios, promociones.
- Sin nombrar a otro autor (p. ej. «Lovecraft» en un libro que no es suyo): KDP lo trata como metadato engañoso.
- En tapa blanda, KDP compara los metadatos con la cubierta: si el subtítulo no figura en ella, puede pedir que
  coincidan. Lo seguro es aplicarlos primero en el **ebook** y, en papel, al resubir con la página de reseña.

| Libro | Subtítulo actual (tienda) | Subtítulo propuesto |
|---|---|---|
| Carmilla | — | La novela de vampiros que precedió a Drácula · terror gótico clásico |
| El extraño caso del Dr. Jekyll y Mr. Hyde | — | Novela clásica de terror psicológico |
| El Horla | Y otros cuentos de lo invisible | y otros cuentos de terror sobrenatural de Maupassant |
| El fantasma de Canterville | — | Un relato de fantasmas · clásico del humor gótico |
| La casa y el cerebro | — | Un relato clásico de casas encantadas |
| La habitación del Dragón Volador | — | Novela gótica de misterio y suspense victoriano |
| Otra vuelta de tuerca | — | Novela clásica de fantasmas y terror psicológico |
| El papel amarillo | y otros relatos inquietantes | y otros relatos de terror psicológico |
| El hombre de arena | Y otros relatos de lo siniestro | y otros relatos de terror gótico alemán |
| La cruz del diablo | y otras leyendas sobrenaturales | y otras leyendas de terror de Bécquer |
| El caso de Charles Dexter Ward | — | Novela de horror cósmico · los Mitos de Cthulhu |
| El horror de Dunwich | — | Relato de horror cósmico · los Mitos de Cthulhu |
| La sombra sobre Innsmouth | — | Novela corta de horror cósmico · los Mitos de Cthulhu |
| En las montañas de la locura | — | Novela de horror cósmico en la Antártida |
| Mareas negras | — | Relatos abisales de H. P. Lovecraft: Dagón, La llamada de Cthulhu y otros |
| El gran dios Pan | — | Novela corta clásica de terror sobrenatural |
| Los Sauces – El Wendigo | — | Dos relatos clásicos de terror en la naturaleza |
| La casa en el confín de la tierra | — | Novela clásica de horror cósmico |
| Narraciones del abismo | Relatos escogidos de horror, locura y muerte | (bien como está) |
| Arsène Lupin, caballero ladrón | (El Archivo Lupin) | Relatos del ladrón más famoso de Francia · novela policíaca clásica |
| *Makt myrkranna* | Los poderes de la oscuridad | Los poderes de la oscuridad. La versión islandesa de Drácula, primera traducción de la casa |
| *El peligro azul* | — | Novela de horror cósmico y ciencia ficción, primera traducción al español (solo si se confirma en la BNE y en la base de datos ISBN que no hay otra) |

«Mitos de Cthulhu» se usa como descriptor de género. Conviene evitar «Call of Cthulhu», nombre de un juego de rol con marca registrada.

## 5. Calendario de lanzamientos 2027 (propuesta, CONSULTA)

Picos: Halloween (septiembre-octubre) y Navidad (noviembre, Archivo Arcano en tapa dura). Los omnibus se reparten
a lo largo del año. «EN» = línea en inglés (`candidatos/2026-11-23_plan-linea-ingles.md`).

| Mes | Español | Inglés | Notas |
|---|---|---|---|
| dic. 2026 | **Omnibus Lovecraft** (*Los Mitos de Cthulhu*) · pack *El Archivo Lupin I-IV* (ebook) | — | si se aprueban esta semana |
| ene. | *Los vampiros de Marte* (Le Rouge), Límite Abisal XXI | — | inédito; primera traducción |
| feb. | Omnibus *La cámara sellada* (antología gótica) | — | |
| mar. | — | EN 1 *Terror from the Deep* | |
| abr. | Archivo Lupin, Dossier V (*El tapón de cristal*, traducción propia) | — | |
| may. | *El baronet embrujado* (Le Fanu), Cámara Sellada | — | inédito |
| jun. | *Memorias de un ladrón retirado* (Galopin), Archivo Lupin | EN 4 *Pale Visitors* | |
| jul. | Omnibus Lovecraft II (traducción nueva: *El color que cayó del cielo*, *La sombra fuera del tiempo*…) | — | |
| **sep.** | ***El libro de los licántropos***, Archivo Arcano V (tapa dura) | EN 2 *Older Than the Church* | Halloween |
| **oct.** | pack ebook de Halloween de Límite Abisal (3-4 títulos de traducción propia) | EN 5 *Gothic Tales from Spain and Latin America* | Halloween |
| **nov.** | ***El libro de los vampiros***, Archivo Arcano VI (tapa dura) | — | Navidad: regalo |
| dic. | — | EN 3 *The Ghost Pirates…* (o en reserva) | |

El ritmo es de algo más de un libro al mes. La traducción de las dos tapas duras de Archivo Arcano (≈ 100.000
palabras cada una) debe empezar en primavera.


## 6. Cupo de KDP y calendario de envíos (24-11-2026)

KDP limita los títulos **nuevos** a **2 por formato y semana**, con reinicio los domingos a las 00:00 UTC (las
01:00 en la España peninsular). Las actualizaciones de libros ya enviados no cuentan.

| Semana de KDP | Ebook y tapa blanda (2 + 2) | Notas |
|---|---|---|
| 22-28 nov. 2026 | *El peligro azul* (ya enviado) · *Lo que yace eternamente* | cupo completo |
| 29 nov.-5 dic. | *813* · *Noche de difuntos* | enviar el domingo 29 o el lunes 30: con 3-5 días de revisión de KDP, estarán a la venta hacia el 4-5 de diciembre, a tiempo para Navidad |
| 6-12 dic. | libre | resubidas con la página de reseña (*Makt myrkranna* y otros): no cuentan |
| 2027 | 1-2 lanzamientos al mes según el calendario del § 5 | el cupo no limita el plan. Cuidado con los picos de Halloween y noviembre: la tapa dura de Archivo Arcano tiene cupo propio, pero su ebook comparte cupo con los demás ebooks. |

Regla práctica:
- No crear borradores en KDP antes de la semana en que se vayan a enviar: también consumen cupo de creación.
- Las ediciones en inglés comparten cupo con las españolas.

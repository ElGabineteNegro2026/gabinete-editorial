# Ficha KDP — *<Título>*

Plantilla común: copiar a `proyectos/<slug>/kdp.md` y rellenarla antes de dar un libro por «listo para KDP».
Ejemplo completo: `proyectos/lo-que-yace-eternamente/kdp.md`.

## 1. Detalles (común a tapa blanda y ebook; idénticos en los dos formatos)

| Campo de KDP | Valor |
|---|---|
| Idioma | Español |
| Título | igual que en la portadilla |
| Subtítulo | con palabras de búsqueda reales, sin repetir el título y sin palabras prohibidas |
| Serie | `<Colección> (El Gabinete Negro)` + número de volumen («Edición especial»: sin número) |
| Autor principal | nombre y apellido **escritos siempre igual** que en los demás libros del mismo autor |
| Colaboradores | normalmente ninguno |
| Descripción | HTML (`<b> <i> <br> <p> <h4> <ul> <li>`), ≤ 4.000 caracteres. Las 2 primeras líneas: gancho + palabras clave principales. Incluir «Este volumen incluye» y «Una edición para leer y conservar». Sin reseñas, superlativos, precios ni nombres de otros autores. |
| Derechos | traducción o edición propia → «Soy el propietario…». Solo texto de dominio público sin aportación propia → «dominio público» (35 % y sin KDP Select). |
| Contenido explícito | No |
| Categorías (3) | 1) la natural del género; 2) una más específica; 3) una de poca competencia (relatos, antologías, clásicos) |
| Palabras clave (7 × ≤ 50 caracteres) | búsquedas reales que **no** estén ya en título, subtítulo, autor ni serie: género + «para adultos», subgénero, nombres propios de la obra, títulos incluidos, intención de regalo o temporada |
| Contenido generado por IA | texto / imágenes / traducción: responder con **verdad**. «Generado» = creado por la IA, aunque luego se edite. |

## 2. Tapa blanda

| Campo | Valor |
|---|---|
| ISBN | gratuito de KDP → `isbn` en `libro.toml` (+ `isbn_ebook = ""`) y regenerar el interior |
| Papel | blanco y negro, **crema** (tapa dura: blanco) |
| Tamaño | 6 × 9 in, sin sangrado |
| Acabado | mate (colección oscura) |
| Archivos | `interior/<slug>_interior_6x9.pdf` y `cubierta/<slug>_cubierta_kdp.pdf` (anotar el ancho exacto que debe pedir KDP) |
| Precio | Amazon.es (IVA incluido) + .com en $ + Reino Unido en £; resto de mercados en euros |
| Distribución ampliada | no, salvo libros cortos con margen suficiente |

## 3. Ebook

| Campo | Valor |
|---|---|
| Archivo | `ebook/<slug>_kindle_create.docx` (→ KPF) o `ebook/<slug>.epub`; portada `cubierta/<slug>_portada_ebook.jpg` |
| KDP Select | sí, si hay traducción o edición propia |
| Regalías | 70 % (precio entre 2,69 y 9,99 €) |
| Precio | .es / .com / .co.uk |

## 4. Después de publicar

- **Comprobaciones**: ediciones enlazadas y serie.
- **Promoción en Amazon**:
  - Author Central;
  - Contenido A+: la cubierta, «incluye» y los otros títulos de la colección;
  - enlaces desde las fichas de los libros relacionados.
- **Seguimiento**:
  - reseñas, sin incentivos;
  - revisión de categorías y palabras clave a los 30 y a los 90 días.

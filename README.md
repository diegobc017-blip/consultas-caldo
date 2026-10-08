# Consultas de Caldo

App para preparar caldos fitosanitarios con los productos registrados en el SENAVE (Paraguay). Funciona en celulares, tablets y PC, se instala como aplicación y trabaja sin internet. Los datos que carga cada persona quedan solo en su dispositivo.

**Abrir la app:** https://diegobc017-blip.github.io/consultas-caldo/ (cuando GitHub Pages esté activado)

## Qué hace
- **Productos SENAVE por rubro:** Agrícola, Hortícola y frutícola, Forestal, Pasturas y Granos almacenados. Incluye la ficha química de cada activo, su formulación, los inertes típicos y otras marcas con el mismo activo.
- **Armar caldo:**
  - Semáforo de 4 colores (verde, amarillo, naranja, rojo) para los 33 problemas posibles del caldo.
  - Medidas que bajan el riesgo: estabilizadores como antiespumante, sulfato de amonio, antideriva o adherente, prácticas de manejo y ajustes.
  - Orden de carga según la presentación del producto y prueba de jarra.
- **Calculadora de dosis:** compara la dosis de etiqueta con la que se va a aplicar y calcula el activo por hectárea, el total para la superficie, la cantidad por tanque y el número de tanques.
- **Condiciones ambientales:** temperatura, humedad, viento, Delta T y lluvia prevista. Controla los límites de la Ley 3742/09 (art. 63) y el riesgo de deriva.
- **Campos y lotes en mapa:** cada lote es un polígono con su forma real (opcional: también se pueden cargar lotes sin mapa).
  - Se dibujan tocando el mapa, se recorre el borde con el GPS del celular, se editan los límites (mover, agregar o borrar puntos) y se dividen con una línea; cada parte conserva el historial.
  - En “Armar caldo” los lotes se eligen con botones o tocándolos en el mapa.
  - Importa GeoPackage, Shapefile .zip, GeoJSON, KML, KMZ, GPX y CSV de vértices (también arrastrando el archivo al mapa). Convierte UTM 20S/21S (WGS 84 y SIRGAS 2000).
  - Exporta Shapefile .zip, GeoJSON, KML, GPX y CSV de vértices en WGS 84, además del historial y un respaldo completo.
- **Cultivos y carry-over:** se elige el cultivo actual, el momento (barbecho, preemergencia, sobre el cultivo o desecación) y el cultivo siguiente con su fecha de siembra. La app revisa si el cultivo tolera cada herbicida y cuántos días esperar para sembrar, también por residuos de aplicaciones anteriores del lote.
- **Historial de aplicaciones por lote**, con productos, dosis, condiciones y semáforo.
- **Tratamiento de semillas:** kg/ha por densidad (o valor cultural en pasturas), curasemillas, biológicos, micronutrientes e inoculante por cada 100 kg, por tanda y total; volumen máximo de caldo, orden de carga y alertas (inoculante con químicos, tiempo hasta la siembra, germinación). Registro por lote de semilla, vinculado a los lotes del campo, y directorio de empresas con sus curasemillas, biológicos e inoculantes.
- **Dureza del agua por zona:** estimación de dureza, pH y conductividad según la zona de Paraguay (acuíferos Yrendá, Patiño y Guaraní) y la fuente del agua; se carga solo si el usuario lo pide y queda marcada como estimada. Las zonas se regeneran con `python3 fuente/make_zonas_agua.py` (requiere shapely).
- **Rotación de modos de acción:**
  - Para qué se usa cada activo y qué grupos HRAC, IRAC y FRAC alternar para el mismo objetivo.
  - Avisos de rotación según el historial de cada lote.
  - Resistencias conocidas en Paraguay y la región.
- **Ejemplo eliminable:** un campo de 500 ha con 8 lotes e historial. **Ayuda** con recorrido guiado.

## Estructura
| Ruta | Contenido |
|---|---|
| `index.html`, `data.js`, `sw.js`, `manifest.webmanifest`, `icons/`, `fonts/`, `vendor/` | La app instalable que publica GitHub Pages |
| `consultas_caldo.html` | La misma app en un solo archivo, para abrir sin internet con doble clic |
| `datos/base_quimica_caldo.json` | Base química y listado SENAVE (fuente de los datos) |
| `fuente/` | Plantilla y motor (`template.html`), reglas del semáforo, rubros, usos y rotación, inertes y scripts de armado |

## Publicar en GitHub Pages
Settings → Pages → Source: *Deploy from a branch* → Branch: `main` / `(root)` → Save. En uno o dos minutos la app queda en `https://<usuario>.github.io/consultas-caldo/`.

## Actualizar con un nuevo listado del SENAVE
1. Reemplazar `datos/base_quimica_caldo.json`.
2. Ejecutar `python fuente/build_app.py` (Python 3). Regenera `index.html`, `data.js`, `sw.js` y `consultas_caldo.html`.
3. Subir los cambios. Las apps instaladas se actualizan solas la próxima vez que tengan internet.

## Avisos
- La etiqueta del producto prevalece siempre. La prueba de jarra con el agua y las dosis reales es la confirmación final.
- Los rubros y usos por activo son orientativos: el listado del SENAVE no trae cultivos ni plagas autorizadas.
- Los datos fisicoquímicos son de referencia (PPDB, HRAC, IRAC, FRAC y guías de extensión citadas en la base).

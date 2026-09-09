# Armar el proyecto en Cowork

Veinte minutos. Se hace una sola vez.

## 1. La carpeta

Crea en tu computadora una carpeta llamada `Eventos-Estadio`.
Adentro, tres subcarpetas:

```
Eventos-Estadio/
├── cowork-forms/     <- esta carpeta, tal cual
├── solicitudes/      <- aquí va el Excel de Forms
├── salidas/          <- aquí Claude deja los correos y reportes
└── scripts/          <- aquí Claude deja los programas
```

## 2. El Excel

Del formulario en Microsoft Forms: **Respuestas → Abrir en Excel**.
Descarga ese archivo y guárdalo en `solicitudes/`.

Vuelve a descargarlo cuando quieras trabajar con datos frescos.
Cowork lee el archivo que esté en la carpeta, no el que está en línea.

## 3. El proyecto

En Cowork, crea un proyecto nuevo y dale acceso a la carpeta
`Eventos-Estadio`. Es el mismo paso que hicimos con la carpeta
de vigencias.

## 4. La entrevista

Pega el prompt de `01-prompt-entrevista.md` como primer mensaje.

Contesta con calma. De ahí sale todo lo demás.

## 5. Revisa lo que escribió

Al terminar genera `instrucciones-proyecto.md` y `pendientes.md`.
Léelos antes de seguir. Si algo quedó mal entendido, es mucho más
barato corregirlo ahí que después.

## Después: los scripts

Ya con las instrucciones escritas, pídeselos **de uno en uno**.
Prueba cada uno con datos reales antes de pasar al siguiente.

| Script | Qué hace |
|---|---|
| `revisar_solicitudes.py` | Lee el Excel y saca lo que necesita tu atención: fuera de plazo, más material del que hay, proveedor externo, choques. |
| `detectar_choques.py` | Compara todas las solicitudes entre sí, espacio por espacio, usando la ventana completa de montaje a desmontaje. |
| `redactar_correos.py` | Genera un archivo de texto por cada área que tiene que enterarse, con lo que a esa área le sirve. |
| `reporte_semana.py` | El panorama de los próximos siete días. |

Si le pides los cuatro juntos vas a acabar con cuatro programas que
no probaste y no vas a saber cuál falló.

---
name: tigres-venta-boletos
description: Convierte un reporte de venta de Boleto Móvil en un corte con las zonas como Fernando las maneja, y lo agrega al archivo maestro de Club Tigres. Úsalo cuando pidan "sube el corte de la semana", "actualiza el maestro de boletos", "mapea las zonas del reporte", "cuánto vendimos por zona", o cuando alguien comparta un export de Boleto Móvil. No entra al portal ni descarga nada: el archivo llega ya bajado.
---

# Venta de boletos — Club Tigres

Toma el reporte crudo de Boleto Móvil de un periodo, traduce las zonas del
sistema a las zonas de Fernando, y agrega el corte al archivo maestro sin
duplicar ni descuadrar.

## Lo que este skill NO hace

- No entra a Boleto Móvil ni descarga el reporte. Eso lo hace Fernando desde
  su usuario y deja el archivo en `entradas/`.
- No inventa una zona. Si el reporte trae una zona que no está en el
  catálogo, se detiene y la reporta.
- No decide qué es una venta buena o mala. Eso es lectura de Fernando.

## Entradas

Tres archivos, y los tres tienen dueño:

| Archivo | Quién lo pone | Dónde |
|---|---|---|
| Export crudo de Boleto Móvil | Fernando, cada periodo | `entradas/` |
| Catálogo de zonas | Fernando, se edita cuando el estadio cambia | `catalogo-zonas.csv` |
| Archivo maestro | vive donde Fernando lo tenga | ruta en `config.json` |

`config.json` guarda las rutas y el nombre real de cada columna del export.
Se arma una vez, copiando `config.ejemplo.json`, y se ajusta el día que
Boleto Móvil cambie el formato de su reporte.

## Pasos

### 1. Leer y validar el export

Abrir el archivo de `entradas/`. Confirmar que trae las columnas que dice
`config.json`. Si falta una, parar y decir cuál — no adivinar el nombre.

Anotar el total de boletos y el importe total del archivo crudo. Ese es el
número contra el que se cuadra todo lo demás.

### 2. Mapear zonas

Correr `scripts/mapea_zonas.py`. Cruza cada renglón del export contra
`catalogo-zonas.csv` y lo reescribe con la zona de Fernando.

Reglas duras:

- **Zona sin mapeo = alto total.** El script se detiene, lista las zonas
  huérfanas y cuántos boletos e importe traen. Nadie sigue hasta que
  Fernando diga a qué zona suya va cada una y se agregue al catálogo.
- **Cuadre obligatorio.** Boletos e importe después del mapeo tienen que dar
  exactamente igual que antes. Si no cuadra, hay un renglón duplicado o una
  zona mapeada dos veces. Parar.

Salida: `salidas/corte_normalizado.csv` y `salidas/reporte_mapeo.md`.

### 3. Enseñar el corte antes de escribir

Antes de tocar el maestro, mostrar en pantalla: periodo, partidos incluidos,
boletos e importe por zona de Fernando, y total. Es la última oportunidad de
ver un número raro antes de que quede en el archivo.

### 4. Actualizar el maestro

- Sacar copia del maestro con la fecha en el nombre, antes de escribir.
- Llave para no duplicar: partido + zona + periodo. Si el periodo ya está
  cargado, no sobrescribir en silencio — decirlo y esperar respuesta.
- Agregar los renglones nuevos. No reordenar ni reformatear lo que ya
  estaba: el archivo es de Fernando, no nuestro.

### 5. Dejar rastro

Una línea en `bitacora.md`: fecha, periodo cargado, boletos, importe, zonas
nuevas agregadas al catálogo si hubo. Sirve el día que un número no cuadre y
haya que buscar cuándo entró.

## Por qué el catálogo es un archivo y no está en estas instrucciones

El mapeo de zonas es dato, no criterio. Si vive dentro del prompt cambia sin
que nadie lo note y no hay forma de auditar por qué un número se movió de
una semana a otra. En CSV, Fernando lo edita sin tocar el skill y cada
cambio queda en el historial.

## Pendiente para poder terminarlo

Esto es el esqueleto. Falta lo que solo sale de los archivos reales:

1. Un export crudo de Boleto Móvil, sin editar, de un periodo cualquiera.
2. El archivo de mapeo de zonas como Fernando lo tiene hoy.
3. El maestro con dos periodos ya cargados, para copiar cómo mete cada corte.

Con esos tres se llena `config.json`, se convierte el mapeo a
`catalogo-zonas.csv` y se termina el paso 4, que hoy está descrito pero no
automatizado.

---
name: imara-report-visual
metadata:
  version: 1.0.0
description: >
  Construye reportes y documentos de estatus de Imara como una página HTML visual, con el formato
  editorial de Direction A: puntos cortos en vez de párrafos, figuras vectoriales dibujadas dentro
  del documento, y un solo color de acento. Activar siempre que se pida armar un reporte de
  entrega, un avance de proyecto, un reporte de estatus, un documento de arquitectura o cualquier
  entregable largo que un ejecutivo va a leer de corrido — y también cuando se pida "que se vea
  como el reporte de REMA", "con el mismo estilo", "más visual", "menos texto", "que se lea rápido",
  o cuando haya que explicar agentes, pipelines o infraestructura con dibujos en vez de prosa.
  Gobierna la maqueta, la distribución del texto y las figuras. La voz la sigue gobernando el skill
  de voz de quien firma (tino-voice o alex-voice), y las reglas de marca siguen en
  imara-client-branding; este skill los ejecuta, no los reemplaza.
---

# Reporte visual de Imara

## Qué produce

Una página HTML autocontenida que se publica como artifact. Un documento largo que se lee
completo en pocos minutos porque casi todo es puntos cortos, tablas y figuras.

El ejemplo funcionando está en `assets/plantilla.html`. Se copia la hoja de estilos completa y se
reemplaza el contenido. Es más rápido y más consistente que rearmar el CSS cada vez.

## La regla que define el formato

**Una línea, una idea.** Si un punto necesita una "y" para describirse, son dos puntos.

Los ejecutivos que leen esto abren el documento una vez, sin contexto adicional. Un párrafo de
cinco líneas los obliga a extraer el dato ellos mismos. Un punto corto se lo entrega.

Antes de dejar una oración: **si la quito, ¿cambia lo que hace el lector?** Si no cambia, sobra.
Esto aplica a las oraciones de contexto, a las que justifican una afirmación que ya se sostiene
sola, y a las que solo existen para que la sección "se sienta completa".

## Cómo se distribuye el contenido

| Tipo de contenido | Cómo se presenta |
|---|---|
| Estado de varias cosas a la vez | Lista de puntos `.points`: etiqueta a la izquierda, una línea de detalle a la derecha |
| Una secuencia con orden | La misma lista, con números `01 02 03` en la etiqueta |
| Cifras que importan | Bloque `.stats`, entre 3 y 5 números grandes con su rótulo |
| Comparación de columnas | Tabla, solo cuando hay tres o más columnas reales |
| Un mecanismo | Figura vectorial. Nunca prosa explicando un flujo |
| El veredicto de la sección | Bloque `.headline`, una sola frase |
| Un riesgo o algo sin resolver | Bloque `.flag` |
| Contexto que no cabe en un punto | `.note`, en gris, máximo dos líneas |

Prosa suelta: solo cuando ninguno de los anteriores aplica, y máximo dos líneas.

## Títulos

Un título es una afirmación corta o una etiqueta. Nada más.

**Prohibido**, porque delata texto generado y obliga a leer dos veces:

- "no es X, es Y" y todas sus variantes: "no por X, sino por Y", "X, pero Y", "más que X, es Y"
- Dos ideas unidas con punto y coma o con "y": "Damián opera; el RACI necesita firmas"
- Títulos que resumen la sección entera en 15 palabras

**Así sí:** "Dónde está la entrega" · "Lo que se midió" · "Sprint de cierre · 10 días" ·
"Definition of Done · 7 de 15" · "Controles"

Si el título necesita cargar un veredicto, va en el bloque `.headline` debajo, no en el título.

## Sistema visual

Tomado de Direction A de `imara-client-branding`. No inventar variantes.

```
--ink        #0A1524   texto y fondo de las portadas
--paper      #FFFFFF   fondo del contenido
--muted      #3E4754   texto secundario
--line       #E4E3DF   separadores
--accent     #FFB24A   único acento
--accent-ink #8A5300   el acento cuando es texto sobre claro
--accent-wash #FFF3E0  relleno suave, solo dentro de figuras
```

Semáforo, aparte del acento: verde `#2F6B4F` para cumplido, terracota `#A23B2E` para pendiente.

Tipografía: **Fraunces** para títulos y números grandes, con Cambria y Georgia como respaldo.
**Arial** para todo lo demás. Los rótulos de sección van en mayúsculas con espaciado.

Prohibido: degradados, azul, tarjetas con sombra, esquinas muy redondeadas, iconos dentro de
círculos, emoji como marcadores, y cualquier color que no esté en la lista.

La portada y el cierre son los únicos bloques con fondo oscuro.

## Las figuras

Se dibujan a mano en SVG dentro del documento. Sin librerías, sin imágenes externas, sin Mermaid.
Es el mismo método de los diagramas de ByteByteGo: control total y se actualizan con el contenido.

Reglas:

- **La figura muestra un mecanismo**, no una lista de cajas con nombres. Si un renglón de texto lo
  dice igual de rápido, se escribe el renglón.
- **Las flechas van etiquetadas** cuando la relación no es obvia: "despacha", "regresa hallazgo",
  "vuelve a la siguiente tanda".
- **Punteado para lo que no está en uso** o no es firme. Un componente creado pero sin usar se
  dibuja punteado y se dice en el rótulo.
- **El acento marca una sola cosa por figura**: el paso que importa, el ciclo humano, el bloqueo.
- **Colores por `currentColor`** para que la figura funcione en claro y en oscuro. El acento se
  toma de la variable, no como valor fijo.
- **Cada figura lleva `role="img"` y `aria-label`** describiendo lo que muestra, y un pie que
  carga la afirmación de la figura.
- Texto dentro de la figura entre 9 y 13 px. Las explicaciones van en el pie, no en el dibujo.

Tipos que ya funcionaron:

1. **Escalera de estados** — los escalones de una entrega, con marca de dónde está hoy.
2. **Anatomía del sistema** — el orquestador con sus funciones adentro, los agentes alrededor, sus
   herramientas al margen, y el ciclo humano cerrando abajo.
3. **Dos salidas de una fuente** — cuando algo produce dos resultados independientes y hay que
   dejar claro que ninguno modifica al otro.
4. **Anatomía de una fila** — qué encuentra el usuario en cada bloque de una tabla o un CRM.

## Estructura de la página

```
Portada oscura          título, una línea de contexto, marca de borrador si aplica, metadatos
Índice                  dos columnas, numerado
Secciones               número, título, contenido en puntos y figuras
Cierre oscuro           el siguiente paso, en dos líneas
```

Cuando el documento sigue un estándar con secciones fijas, se respeta ese orden. El estándar manda
qué secciones existen; este skill manda cómo se ven.

## Integridad de datos

Nunca inventar una cifra, fecha o nombre. Lo que no esté confirmado va como `[A VALIDAR]` visible.
Un hueco a la vista es mejor que un dato que suena bien.

Cuando un documento mezcla resultados de dos sistemas o dos periodos, se separan de forma
explícita. Presentar resultados viejos junto a un sistema nuevo le atribuye un valor que todavía
no produjo.

## Checklist antes de publicar

```
Ningún título con estructura "no es X, es Y" ni dos ideas unidas:   ___
Ninguna sección con más de dos líneas de prosa seguidas:            ___
Cada punto cabe en una línea:                                       ___
Cada figura muestra un mecanismo, con flechas etiquetadas:          ___
Un solo acento, sin degradados ni azul:                             ___
Claro y oscuro revisados los dos:                                   ___
Cifras sin confirmar marcadas [A VALIDAR]:                          ___
```

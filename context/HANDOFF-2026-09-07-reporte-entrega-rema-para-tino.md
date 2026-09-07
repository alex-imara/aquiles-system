---
handoff_date: 2026-09-07
topic: Reporte de entrega REMA a Galera — estado del documento y cómo reproducir su estilo
from: Sesión de Alex (Claude Code, repo aquiles-system)
to: Sesión de Tino
sistema: REMA · Galera × Imara
---

# Where this picks up

El reporte de entrega de REMA existe y está publicado. Sigue las 16 secciones del
`Imara_Estandar_Entrega_Agentes_REMA.pdf`, con el research system nuevo integrado adentro como el
componente que se entrega.

**Link:** https://claude.ai/code/artifact/36071181-e6a3-4f13-9090-2064f766dfdd

Está marcado como borrador interno. No se ha enviado a Galera.

---

## Current state

### El documento

- Publicado y actualizado tres veces hoy. La última versión está reescrita a puntos cortos, sin
  párrafos largos, por instrucción de Alex.
- 16 secciones, cuatro figuras vectoriales dibujadas dentro del documento: la escalera de entrega
  con los cinco gates, la anatomía del sistema con sus agentes, los dos veredictos, y qué ve un
  socio en una fila del CRM.
- Fuente HTML: `/tmp/claude-0/-home-user-aquiles-system/6cd69a7b-a97d-53c3-83d9-232f663f1c82/scratchpad/reporte-entrega-rema.html`
  en el contenedor de esa sesión. **No sobrevive al cierre de la sesión** — si hace falta editarlo
  fuera del artifact, hay que releerlo desde el artifact publicado.

### Qué dice el reporte sobre el estado del sistema

Confirmado contra los handoffs técnicos del 4 y 7 de septiembre:

- Tres de las seis condiciones de "entregado" se cumplen: instalado, observable, con dueño.
  Aceptado no se cumple — nadie de Galera ha corrido ni revisado una corrida.
- El sistema corre en la Mac mini de Imara. La versión en n8n existe (`qZG1gDsMr6q9NcqU` y
  `96vuCeCuxkLx2pNa`) y nunca se ha ejecutado.
- Una sola corrida medida: 5 fondos, 40 de 40 llamadas sin error, $2.90 y 12.8 min por fondo.
- Ningún fondo tiene veredicto de calificación medido. Los 5 de la corrida son anteriores a los
  filtros.
- 531 fondos únicos de 609 filas de Bernardo. Costo proyectado ~$1,540. El dedupe ahorra ~$227.
- Definition of Done: 7 de 15 casillas cerradas con evidencia.

### Verificado en esta sesión, contra Drive

- "REMA 90 Day Update v1" — Slides, id `1ZsVpB7EnsODOeAQkQHJld_cIX87tGdIxqHXe8BpkSw4`. De ahí salen
  las cifras comerciales: 12 fondos contactados, 33% de respuesta, 4 juntas contra meta de 1.
- Handoff del encargo — id `1UHw-VSPpwfSdzztKjMTW2a1M8WZPq4Ng`.
- Handoff técnico del build — id `1xGXMWclnbAa0JNhk78PiBW-cmXuYnPTU`.
- Arquitectura v12 — id `1IUikOisu-3RO731Wc1UmCNhBrcxPjVTi`.

### No verificado

- El PDF del estándar de entrega (`1GUNaeHsKXaz5ELKEbwV5hlDoZE8VEFkp`) no se pudo abrir desde esta
  sesión. La estructura de 16 secciones que usa el reporte viene de los handoffs, que ya la
  resumen completa.

---

## Decisions locked (don't re-ask)

- **El reporte cubre solo el componente de investigación.** El redactor de correos queda fuera de
  esta fase — why: decisión de Tino del 4-sep, la fase se detiene en el reporte del Lead más las
  citas.
- **Damián es el responsable operativo y así se escribió el RACI** — why: Tino, 7-sep.
- **Los resultados comerciales se presentan como del sistema anterior, no de este pipeline** —
  why: las 4 juntas y el 33% de respuesta son del corte de junio a agosto, antes de que este
  sistema existiera. Atribuírselos sería reclamar un valor que todavía no produce.
- **El plan de cierre empieza por decidir dónde corre producción, no por portar el filtro a n8n**
  — why: si producción va a ser el script local, ese trabajo de porteo puede sobrar por completo.
- **No se afirma nada sobre el retainer** — why: el dato de la junta del 4-sep ("pausar hasta
  agosto") no cuadra con la fecha de la junta y no se ha verificado contra la grabación.
- **El documento nombra tecnología específica porque es interno.** La versión que se comparta con
  Galera va agnóstica a la herramienta — why: regla de marca de Imara, ya aplicada en el borrador
  de mensaje de la sección 14.

---

## Pending / next steps

1. **Revisar el borrador de mensaje a Galera** (sección 14 del reporte). Está escrito pero marcado
   como no enviable sin revisión de Tino.
2. **Confirmar el RACI.** Damián está confirmado. Faltan dueño de negocio, technical owner y quién
   firma la aceptación — hoy están como propuesta.
3. **Decidir dónde corre producción**: script local o n8n. Es el día 1 del sprint de cierre porque
   define si el resto del trabajo técnico hace falta.
4. **Verificar el dato del retainer** contra la grabación de la junta del 4-sep.
5. **Escribir el reporte de entrega final** cuando el build esté cerrado. Este documento es el
   avance, no el final.

---

## Environment / tooling notes

- El artifact se actualiza republicando el mismo archivo desde la sesión que lo creó. Desde otra
  sesión hay que pasar la URL explícitamente, o se crea un artifact nuevo en vez de actualizar el
  existente.
- La suscripción automática a comentarios del artifact no se pudo activar en esta sesión — el
  servicio la rechaza. Si alguien comenta en la página, hay que avisarle a mano a la sesión.
- El PDF del estándar vive en una carpeta de Downloads personal y no aparece por búsqueda de Drive
  desde una sesión de Claude Code.

---

## Cómo reproducir el estilo del documento

Esto es lo que hace falta para que otra sesión produzca documentos con el mismo formato. Sin esto,
sale un documento distinto aunque el contenido sea el mismo.

### 1. El skill `imara-report-visual`

Empaquetado aparte, se instala una vez. Contiene el sistema completo: tokens de color, tipografía,
la regla de puntos cortos en vez de párrafos, cómo se construyen las figuras, y la lista de
formatos de título prohibidos.

### 2. El HTML del reporte, como referencia viva

El archivo publicado es el ejemplo funcionando. Sirve como plantilla directa: se copia la hoja de
estilos y se reemplaza el contenido.

### 3. Lo que ya debe tener una sesión de Imara

- `imara-client-branding` — el sistema visual Direction A del que salen los colores y la
  tipografía.
- `tino-voice` — para el filtro de voz de Tino. El equivalente de Alex es `alex-voice`, que vive
  en el repo `aquiles-system` bajo `.claude/skills/alex-voice/`.

### Las reglas que más se rompen

- **Nada de títulos con estructura "no es X, es Y"**, ni sus variantes con "pero", "sino", o
  "antes que". Se afirma directo lo que sí es.
- **Puntos cortos, no párrafos.** Una línea, una idea. Si necesita una "y" para describirse, son
  dos líneas.
- **Cero oraciones de reafirmación.** Si quitarla no cambia lo que hace el lector, se quita.
- **Un solo color de acento.** Ámbar `#FFB24A` sobre tinta `#0A1524` y papel blanco. Sin
  degradados, sin azul, sin tarjetas con sombra.
- **Las figuras se dibujan en vector dentro del documento**, no con librerías ni imágenes. Cada
  figura muestra un mecanismo real, no una lista de cajas con nombres.

---

## Open questions

- ¿El reporte final también va a cubrir el agente redactor, o se entrega solo el de investigación
  y el otro queda como pendiente explícito en el acta?
- ¿Dónde se archiva el PDF del estándar de entrega? Hoy vive en una carpeta de Downloads.
- ¿`REMA-BUILD.md` (17-jun) sigue vigente? Describe una arquitectura distinta y nadie lo ha
  cerrado formalmente.

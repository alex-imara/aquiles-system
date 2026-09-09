# Plano del formulario

Cómo debe quedar el formulario de solicitud de eventos en Microsoft Forms.
Seis secciones. Alrededor de veinte preguntas.

## Configuración

- **Solo personas de mi organización pueden responder** — activado
- **Registrar el nombre** — activado

Con eso el nombre y el correo del solicitante se capturan solos.

---

## Sección 1 — Quién pide

| Pregunta | Tipo | Notas |
|---|---|---|
| *(nombre y correo)* | automático | No se pregunta. Viene de la configuración. |
| Departamentos involucrados | Casillas, varias respuestas | Ver lista abajo. Quien solicita marca también el suyo. |
| Responsable el día del evento | Texto | Obligatoria |
| Celular del responsable | Texto | Obligatoria. Es lo primero que se necesita cuando algo se cae. |

**Departamentos:** Presidencia · Operaciones · Deportivo · Administración ·
Comercial · Fan Experience · Responsabilidad Social · Mercadotecnia ·
Patrocinadores · Proveedores · Digital · Medios · Fuerzas Básicas ·
Academias · Seguridad · Otro

> Esta pregunta cambió de una sola respuesta a varias. Al permitir varias,
> deja de significar "de dónde eres" y pasa a significar "a quiénes hay que
> involucrar", que es lo que sirve para rutear los correos.

---

## Sección 2 — Qué es

| Pregunta | Tipo |
|---|---|
| Nombre del evento | Texto corto |
| Tipo de evento | Lista: Interno del club · Con socios o afición · Con proveedor o marca · Prensa y medios · Otro |
| Descripción | Texto largo |

---

## Sección 3 — Cuándo

| Pregunta | Tipo |
|---|---|
| Fecha del evento | Fecha |
| Hora de montaje | Lista de bloques de 30 min |
| Hora de inicio | Lista de bloques de 30 min |
| Hora de fin | Lista de bloques de 30 min |
| Hora de desmontaje | Lista de bloques de 30 min |

**Forms no tiene campo de hora.** Se arma como lista desplegable en bloques
de 30 minutos, dentro del horario de operación. Se construye una vez y se
copia a las otras tres.

Los empalmes reales pasan en el montaje, no en el evento. Por eso son
cuatro horas y no dos.

En el subtítulo de la fecha: *"Las solicitudes se reciben con mínimo 7 días
de anticipación."* La validación real la hace el flujo, no el formulario.

---

## Sección 4 — Dónde

Primero la **sede**, y de ahí se ramifica.

| Pregunta | Tipo |
|---|---|
| Sede | Lista: Estadio Universitario · Zuazua · CET · CEDECO |

### Si es Estadio Universitario

Cuatro preguntas de casillas, todas opcionales. Se parte así para que en
celular cada bloque quepa casi completo, en vez de 21 casillas seguidas.

- **Cancha y alrededores:** Cancha · Explanada Cancha · Contracancha (zona preferente) · Túnel
- **Vestidores:** Femenil · Varonil · Antiguo Local · Antiguo Visitante · Antiguo de Árbitros · Preliminar
- **Explanadas y estacionamientos:** Explanada Atarantados · Explanada Puerta 13 · Estacionamiento Jaula 0 · Patio Visitante
- **Espacios interiores:** Sala de Prensa · Sala de Acreditaciones · Gimnasio · Mundo Tigre

Más una pregunta de texto: *"¿Ningún espacio de arriba? Escribe cuál."*

> "Otro" como casilla suelta deja al sistema sin saber qué espacio es, y esa
> solicitud no se puede cruzar contra nada. Pedir el texto la manda a revisión
> manual, que es lo correcto para un caso raro.

> Ojo con la ortografía: es **Antiguo**, no "Antigüo". En el formulario actual
> está mal escrito en las tres opciones.

Después: **¿Requiere acceso vehicular?** Sí / No

---

## Sección 5 — Qué necesitas del club

### Asistentes estimados
Pregunta de texto con **restricción de número**. Abre el teclado numérico
en celular.

### Material — con cantidad

Cada material es su propia pregunta numérica. Se deja en blanco lo que no
se necesita. El tope va en el subtítulo y como restricción de número.

| Material | Disponibles | Unidad |
|---|---|---|
| Unifilas | 20 | piezas |
| Bancas | 4 | piezas |
| Sillas | 25 | piezas |
| Mesas | *falta* | piezas |
| Extensión | *falta* | **metros** |
| Tarimas | *falta* | *confirmar unidad* |
| Andamios | *falta* | *confirmar unidad* |
| Pantallas | *falta* | piezas |
| Hieleras | *falta* | piezas |
| Vallas metálicas | *falta* | *confirmar unidad* |
| Vallas electrónicas | *falta* | *confirmar unidad* |

**Cuatro no llevan cantidad**, piden otra cosa:

| Material | Qué preguntar |
|---|---|
| Alfombra Túnel y Explanada | Sí / No — es un tramo fijo, no piezas |
| WiFi | Cuántos accesos y para quién |
| Consumo | Qué y para cuántas personas |
| Otro | Texto libre |

> El tope es el inventario total, no lo que queda libre ese día. Forms frena
> al que pide 40 sillas de 25; no frena a los dos que piden 25 el mismo sábado.
> Ese cruce lo hace el flujo.

> Con 25 sillas y 4 bancas, casi cualquier evento de más de treinta personas
> se pasa del inventario. Rentar material externo va a ser lo normal, no la
> excepción.

### Proveedor externo
**¿Vas a meter material o proveedor externo?** Sí / No

Si responde **Sí**, se abren tres preguntas:
- ¿Qué vas a meter? (texto)
- ¿Quién lo trae? (texto)
- ¿A qué hora llega? (lista de horas)

---

## Sección 6 — Cierre

| Pregunta | Tipo |
|---|---|
| Observaciones | Texto largo, opcional |
| Archivo del evento | Carga de archivo, opcional |
| Reglamento | Una sola casilla obligatoria: "Acepto" |

### Texto del reglamento

Va como texto de la sección, arriba de la casilla:

> **Reglamento**
>
> La solicitud debe hacerse con al menos una semana de anticipación.
>
> Las solicitudes urgentes solo se reciben dentro del horario laboral.
> Las excepciones las autoriza el área de Operaciones.
>
> No se permite el uso de áreas durante los entrenamientos de los equipos
> varonil y femenil.
>
> No se permite el acceso sin autorización previa.
>
> Los asistentes deberán estar acompañados por un empleado del departamento
> solicitante.
>
> El organizador es responsable de cualquier daño a las instalaciones o al
> material.

> **Quitar la opción "No Acepto".** Hoy es una pregunta de dos opciones, y
> quien marca "No Acepto" manda la solicitud igual. Va como una sola casilla
> obligatoria: si no la marcan, Forms no deja enviar.

---

## Ramificación

Se configura **al final**, cuando todas las preguntas ya están en su lugar.

- Sede → cada opción salta a su bloque de espacios
- Proveedor externo "Sí" → abre las tres preguntas del proveedor

**No reordenar preguntas después de configurar la ramificación.** Forms deja
los saltos apuntando a la posición vieja y todo se descompone sin avisar.

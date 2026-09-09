# Qué hace cada pieza

Tres herramientas, cada una haciendo lo que sabe hacer.

## Microsoft Forms — captura

Le mandas el link a las áreas y cada quien mete su solicitud.
Las respuestas caen solas a un Excel que se actualiza con cada envío.

## Power Automate — entrega

Corre en la nube, sin depender de tu computadora.

Al llegar una solicitud: la revisa contra el calendario, aparta el
espacio si está libre, la manda a autorizar, y manda los correos a
las áreas. Los correos salen desde tu cuenta.

## Cowork — análisis

Cuando lo abres, lee el Excel y te dice qué se está encimando, qué
material se está sobregirando y cómo va la semana.

Es donde preguntas cosas que ningún flujo automático puede contestar.

---

## Lo que Cowork sí puede

- Leer el Excel de respuestas
- Detectar choques de espacio y horario entre solicitudes
- Avisar cuándo alguien pidió más material del que hay
- Redactar el correo para cada área, listo para copiar
- Armar el reporte de la semana
- Encontrar lo que no es obvio: dos eventos que no chocan de horario
  pero piden el mismo material

## Lo que Cowork no puede

- Mandar correos por sí solo
- Enterarse de que llegó una respuesta nueva
- Escribir en el calendario de Outlook
- Apartar un espacio
- Correr con la computadora apagada

### Por qué no puede mandar correos

No es un límite de Claude. Es la configuración de Microsoft del club:
el envío de correo desde programas externos viene apagado de fábrica,
y la otra ruta necesita que TI registre una aplicación. Las dos pasan
por César.

Por eso el envío lo hace Power Automate, que sí vive dentro de la
cuenta de Microsoft y ya está incluido en la licencia E3.

### Y solo corre con la computadora prendida

Cowork trabaja sobre una carpeta local. Una tarea programada para el
lunes a las 8:00 no corre si la laptop está cerrada — se ejecuta la
próxima vez que abras la aplicación.

Para lo que tiene que pasar sí o sí, va Power Automate.

---

## El flujo completo, cuando esté armado

1. Llega la solicitud. Se guarda y le llega el aviso a Claudia con el
   resumen y lo que hay que revisar.
2. Se revisa contra el calendario, espacio por espacio, usando la
   ventana completa de montaje a desmontaje.
3. Si no hay choque, va al autorizante con botón de aprobar o rechazar.
4. Aprobado: se crea el evento en el calendario de esa sede. Ese es el
   bloqueo.
5. Salen los correos a las áreas y la invitación de calendario al
   solicitante y al responsable.

### Dos detalles que se olvidan

**Concurrencia del flujo en 1.** Si corre en paralelo, dos solicitudes
que entran con segundos de diferencia pasan las dos la revisión de
choque y apartan el mismo espacio.

**El bloqueo pasa después de enviar, no antes.** Forms no consulta nada
mientras alguien llena. La lista de horas se ve completa para todos y el
choque se detecta después. Ver disponibilidad en vivo necesita Power Apps,
que es otra herramienta y otro tiempo de construcción.

---

## Rutear por reglas, no solo por casillas

Si el aviso a las áreas depende nada más de lo que la persona marcó, va
a fallar. Quien aprende que marcar casillas le trae más trámite deja de
marcarlas.

El ruteo tiene que ser **lo que pidieron más lo que las reglas obligan**:
quien aparta la Cancha manda aviso a Mantenimiento aunque no lo haya
marcado; arriba del umbral de asistentes entra Seguridad aunque nadie la
haya pedido; con proveedor externo entra Seguridad por el acceso.

Esas reglas viven en el flujo, no dependen de la buena voluntad de quien
llena el formulario.

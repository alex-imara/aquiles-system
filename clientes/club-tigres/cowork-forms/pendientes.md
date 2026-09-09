# Pendientes

Lo que falta definir. Nada de esto frena armar el formulario:
los topes solo afectan el subtítulo y la restricción de cada
pregunta de cantidad, y se capturan al final sin rehacer nada.

## Frenan la construcción del formulario

- [ ] **¿CET y CEDECO son sedes o espacios del estadio?**
      Vienen con responsable propio, como Zuazua, lo que sugiere
      que son sedes. Pero en el formulario actual están dentro de
      "Zona del Evento" junto a Cancha y Vestidores. Cambia la
      ramificación, así que hay que resolverlo antes de capturar.
- [ ] **Horario de operación de cada sede.** De qué hora a qué hora
      se puede pedir algo. Define las listas de horas.

## Frenan el flujo automático, no el formulario

- [ ] **Topes de material.** Faltan mesas, tarimas, andamios,
      pantallas, hieleras y los dos tipos de valla. Más los metros
      de extensión.
      Ya definidos: unifilas 20, bancas 4, sillas 25.
- [ ] **Unidad de cada material.** Extensión resultó ir en metros.
      Tarimas y vallas probablemente también se midan por metro
      lineal o por módulo. Si el formulario pide piezas y el almacén
      cuenta metros, los números nunca van a cuadrar.
- [ ] **Umbral de asistentes que obliga a seguridad.** Es política
      del club.
- [ ] **Directorio por departamento.** Cuatro columnas:
      departamento · quién recibe el aviso · quién autoriza · suplente.
      Recibir el aviso y autorizar no son la misma persona.
- [ ] **Correos por confirmar.** Tres traen problemas de captura:
      dos con acento en la parte de antes del arroba, que Microsoft 365
      no permite, y uno terminado en `.mxx`.

## Al momento de la construcción

- [ ] **Agregar "Archivo del evento" (Sección 6) después de duplicar.**
      Alex está construyendo el formulario desde una cuenta personal
      de Microsoft, sin OneDrive empresarial. Esa cuenta no ofrece el
      tipo de pregunta "Carga de archivos" — ni siquiera aparece en el
      menú. Queda pendiente hasta que Claudia duplique el formulario a
      su cuenta del club; ahí sí va a estar disponible.
- [ ] **Revisar "solo mi organización" en Configuración, ya en la cuenta de Claudia.**
      Es probable que en la cuenta personal esa opción no aparezca —
      solo "cualquier persona con el vínculo". No es un error: se
      configura bien hasta que el formulario ya viva en la cuenta de
      trabajo del club.

## De fondo

- [ ] **Dónde vive el rol de entrenamientos.** El reglamento prohíbe
      usar áreas durante los entrenamientos del varonil y el femenil.
      Es la única regla que depende de un dato que el formulario no
      tiene. Hoy la cumple Claudia de memoria.
      Se vuelve más grande con Zuazua, donde las canchas se ocupan
      casi diario por fuerzas básicas.

## Con TI (César)

- [ ] **Conector de Microsoft 365 en Cowork.** Permitiría leer correo
      y calendario directo, sin Excel descargado.
- [ ] **Buzón compartido** tipo `eventos@sinergiadeportiva.mx`, para
      que los avisos salgan del sistema y no del nombre de una persona.

---
name: alex-voice
metadata:
  version: 0.1.0-pendiente-calibracion
description: >
  Filtro de voz obligatorio para Alex Ruiz. Aplica en TODO texto en prosa de más de una oración
  que Alex vaya a firmar o enviar: emails, mensajes, reportes, resúmenes, propuestas, texto de
  documentos o de slides, sobre todo lo que vaya a leer un cliente o ejecutivo mexicano no
  técnico. Activar siempre que pida "escribe", "redacta", "manda este mensaje", "arma el
  reporte", "un correo a X", o pegue texto para revisar, acortar, limpiar o quitarle tono de IA
  ("que no se note que lo escribió una IA", "quítale paja", "esto abre la puerta a preguntas que
  no quiero que me hagan"). Distinto de un skill de personalidad: la meta no es sonar informal
  como Alex habla, es sonar profesional, plano y mínimo — cero señales de IA y cero información
  de más que un no técnico use para armar una pregunta sin respuesta lista. Gobierna voz y
  palabras, no mecánica de archivo ni el sistema de marca de Imara (imara-client-branding), que
  siguen aplicando para estructura y visual; este skill corre encima, en tono y palabra.
---

# Alex voice

## Por qué existe, y en qué se diferencia de un skill de personalidad

Un skill como el de Tino existe para que el texto suene a una persona específica, con opiniones,
ritmo, y textura — informalidad, code-switching, humor. Este skill persigue otra cosa.

El lector no es un colega. Es un director general o un socio mexicano que no le entra a la
tecnología, y que va a leer esto una sola vez, sin contexto adicional, y probablemente en su
celular entre dos juntas. Si el texto suena raro, genérico, o trae más información de la que
pidió, lo único que logra es que regrese con una pregunta — y esa pregunta puede ser una que Alex
no tenga forma de responder ahí mismo.

Entonces la meta no es personalidad. Es **control**: decir lo necesario, en el orden correcto,
sin nada que sobre, sin que se note que una máquina lo escribió.

## Principio central — economía de información deliberada

Esto es lo que hace a este skill distinto de cualquier filtro de "quítale tono de IA" genérico.
Antes de dejar una oración, pregúntate: **si la quito, ¿cambia lo que el lector hace después?**
Si no cambia, sobra.

Esto no es minimalismo por estética. Es una regla de riesgo: cada dato, cada matiz, cada
justificación de más que se mete en un mensaje es una manija más que el lector puede jalar con
una pregunta de vuelta. Menos manijas, menos preguntas sin respuesta lista.

Aplica esto de forma concreta:

- No expliques el "cómo" cuando lo único que se pidió fue el "qué" o el "cuándo".
- No agregues una razón de respaldo si la afirmación ya se sostiene sola.
- No metas un dato, una cifra o un nombre que nadie pidió, aunque lo tengas a la mano y sea
  relevante en abstracto — si no cambia la decisión del lector, se queda fuera.
- No agregues una frase de tranquilidad ("esto no debería ser un problema", "no te preocupes por
  esto") a menos que haya evidencia concreta detrás. Una tranquilidad sin respaldo suena
  hueca y a veces genera más duda que si no se dice nada.
- Si una oración existe solo para que el mensaje "se sienta completo" o "bien explicado", táchala.

Regla práctica: escribe el mensaje, y luego quita la mitad de las oraciones que no cambian una
acción o una decisión. Lo que sobrevive es el mensaje real.

## Vocabulario prohibido

Aplica igual en español y en inglés, mezclados o no. Lee la lista completa antes de escribir —
ojearla no basta.

**Español — prohibición dura:** aprovechar (como muletilla), destacar (como anuncio, "cabe
destacar" prohibido), fundamental, clave (como adjetivo de relleno), esencial, coadyuvar,
implementar (cuando "hacer" funciona), en aras de, en torno a (cuando "sobre" funciona), a fin
de (cuando "para" funciona), de cara a (cuando "para" funciona), llevar a cabo (cuando "hacer"
funciona), poner en marcha (cuando "empezar" funciona), hacer hincapié, aunado a, no obstante,
asimismo, por otra parte (como transición), además (como transición), cabe señalar que, es
importante señalar que, vale la pena mencionar que, huelga decir, robusto, integral (como
relleno), potenciar, impulsar (como relleno vacío), sinergia, ecosistema (metafórico).

**Inglés — prohibición dura:** delve, leverage (verbo), robust, comprehensive, cutting-edge,
seamless, streamline, holistic, synergy, empower, unlock (metafórico), harness, game-changing,
groundbreaking, tapestry, landscape (metafórico), navigate (metafórico), pivotal, showcase,
underscore, foster, garner, facilitate, utilize, actionable, thought leadership, value
proposition, stakeholder, bandwidth (metafórico), circle back, deep dive, move the needle,
low-hanging fruit, unpack (metafórico), at the end of the day.

**Construcciones prohibidas, ambos idiomas:** "no solo... sino también...", "desde X hasta Y"
como rango retórico (los rangos literales de fechas o números están bien), "juega un papel
crucial en", "es importante recordar que", regla de tres decorativa ("velocidad, eficiencia e
innovación").

## Anti-patrones de escritura de IA

Estos son los que delatan texto de máquina incluso cuando no hay ni una palabra prohibida de
la lista de arriba. Revísalos aparte, después de la primera pasada.

- **"No es X, es Y" y variantes.** "Esto no es un problema técnico, es un problema de proceso."
  Bórralo. Afirma directo lo que sí es: "Es un problema de proceso."
- **Transiciones mecánicas.** Furthermore, Moreover, Additionally, Por otra parte, Asimismo,
  Cabe destacar que. La mejor transición casi siempre es un punto y aparte, sin conectivo.
- **Metacomentario.** "A continuación", "En esta sección", "En resumen", "Como mencionamos
  antes". Escribe el contenido directo, sin anunciarlo.
- **Hedging de relleno.** "Vale la pena mencionar que", "cabe señalar que", "no cabe duda de
  que". Si vale la pena decirlo, dilo — no anuncies que lo vas a decir.
- **Gerundios de análisis superficial.** Frases que cierran con "-ando" o "-iendo" para simular
  profundidad: "destacando la importancia de", "reflejando un cambio en". Corta la cola, deja
  la afirmación.
- **Fórmulas de aforismo.** "X es el Y de Z", "X no es una herramienta sino un espejo". Suena a
  columna de LinkedIn. Reemplaza con la afirmación concreta a la que apunta.
- **Aperturas retóricas de falsa confidencia.** "¿La verdad?", "Seamos honestos", "Aquí está el
  punto". Si de verdad vas a decir algo honesto, solo dilo — la pausa teatral es el tell.
- **Atribuciones vagas.** "Los expertos coinciden en", "diversas fuentes indican". Si la fuente
  existe, nómbrala. Si no existe, corta la afirmación — no la disfraces de respaldo.
- **Voz pasiva sin sujeto.** "Se decidió que..." "Los resultados se preservan automáticamente."
  Ponle sujeto: quién decidió, qué preserva qué.
- **Copiar "es/son" con verbos elaborados.** "Funge como", "se erige como", "representa",
  "constituye". Escribe "es".

## Reglas de audiencia — C-level mexicano no técnico

- Cero jerga técnica sin traducir. Si hay que nombrar algo técnico, nómbralo con la palabra que
  usaría el lector, no la que usaría un ingeniero — y solo si hace falta para que actúe. Si no
  hace falta para la acción, no lo nombres (ver economía de información).
- Nunca falta de respeto disfrazada de simplicidad — no le expliques a un director general algo
  de su propio negocio que ya sabe. Explica solo la parte nueva.
- Sin fechas comprometidas que Alex no pueda sostener. Si algo no tiene fecha confirmada, no se
  inventa una para que el mensaje suene más completo.
- Sin nombrar la herramienta o el modelo de IA específico detrás de un entregable de Imara —
  regla de marca, no de esta skill, pero aplica igual aquí.
- Registro: tú, no usted, salvo que el contexto o el cliente ya lo haya marcado distinto. Nunca
  "Estimado". Nunca "Espero que se encuentre bien". Saludo directo con el nombre, cierre directo.

## Estructura y longitud

- Bajo 150 palabras: sin headers, sin bullets, párrafos cortos y ya.
- Reportes o documentos largos: bullets y tablas solo donde el contenido de verdad es una lista
  paralela o una comparación — no como forma de rellenar espacio.
- Una idea por párrafo. Si un párrafo necesita un "y" para describir de qué trata, son dos
  párrafos.
- Cierre: una acción, una fecha, o una pregunta directa — nunca un cierre genérico tipo "quedo
  al pendiente" sin ningún ask concreto detrás.
- Tono parejo de principio a fin. A diferencia de un skill de personalidad, aquí NO se busca que
  el tono cambie de sección a sección — la meta es que el lector nunca sienta un salto de
  registro. Consistencia es la señal de control, no de monotonía de máquina.

## Modos

**SILENCIOSO (default).** Entrega solo el texto final. Sin draft, sin lista de qué se cambió,
sin explicación de por qué quedó así.

**AUDITADO.** Solo cuando Alex pida ver la auditoría o pregunte "qué le cambiaste". Entonces sí,
muestra antes/después y qué regla de arriba aplicó en cada cambio.

## Integridad de datos

Nunca inventes una cifra, fecha, nombre o cita que no venga del input, de un archivo real, o de
una búsqueda hecha en la misma sesión. Si un dato hace falta y no está confirmado, dilo así:
`[A VALIDAR]` — visible, no enterrado. Un hueco a la vista es mejor que un dato inventado que
suena bien.

## Relación con otros skills

Este skill gobierna voz y palabras. No reemplaza:

- **imara-client-branding** — sigue gobernando estructura, sistema visual, y las reglas de marca
  de Imara (Direction A, Pyramid/SCQA, qué no se puede prometer). Cuando ambos aplican, primero
  se arma la estructura con imara-client-branding, y este skill se pasa encima para pulir tono y
  palabra por palabra.
- **docx / pptx / pdf** — mecánica de archivo, no de voz.

## Patrones de voz de Alex — sección pendiente de calibrar

Todo lo de arriba es universal: aplica sin necesitar ni un solo mensaje real de Alex. Pero un
filtro anti-IA genérico no es lo mismo que sonar específicamente a Alex. Lo que falta, y que
esta sección va a capturar en cuanto haya ejemplos reales:

- Cómo abre y cierra un correo o mensaje realmente (¿algo distinto a un saludo directo con
  nombre?).
- Largo típico de oración cuando escribe rápido vs. cuando arma algo con más cuidado.
- Palabras o frases que sí usa y que no están en ninguna lista de arriba (sus propias muletillas
  reales, no inventadas).
- Cómo reacciona por escrito cuando algo salió mal o hay una mala noticia que dar.
- Diferencia real entre cómo le escribe a un cliente y cómo le escribe a alguien de Imara.

**Mientras tanto:** por default, usa español de negocios mexicano neutro-directo, registro de
"tú", sin nada de la lista prohibida, con el principio de economía de información como filtro
principal. Es un punto de partida razonable, no una copia de la voz real de Alex.

**Cómo calibrar:** la próxima vez que Alex pegue 5-10 mensajes o correos reales que él mismo
escribió — ojalá incluyendo al menos uno a un cliente y uno interno — se minan patrones
concretos de ahí, igual que se hizo con tino-voice, y esta sección se llena con evidencia real en
vez de con supuestos.

## Checklist antes de entregar

```
Cada oración sobrevive la prueba "si la quito, ¿cambia lo que hace el lector":  ___
Cero vocabulario prohibido:                                                     ___
Cero anti-patrones de IA (no es X es Y, transiciones mecánicas, hedging, etc.): ___
Cero jerga técnica sin necesidad, cero herramienta/modelo nombrado:             ___
Tono parejo de principio a fin, sin cambios de registro:                       ___
Cierre con acción, fecha o pregunta concreta — no genérico:                    ___
Datos sin confirmar marcados [A VALIDAR], nada inventado:                      ___
```

## Versión

v0.1.0, sin calibrar. Estructura universal completa (vocabulario, anti-patrones, economía de
información, reglas de audiencia). Pendiente: minar patrones reales de Alex de una muestra de
sus propios mensajes, igual que tino-voice v1.1 se calibró contra ~40 mensajes reales de Tino.

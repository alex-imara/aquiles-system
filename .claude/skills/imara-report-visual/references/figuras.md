# Cómo se dibujan las figuras

Vocabulario extraído de `reporte_entrega_rema.html` y de `assets/plantilla.html`.
El SKILL.md dice qué figura va en cada caso. Este archivo dice cómo se dibuja.

## Esqueleto

```html
<figure>
  <div class="figscroll">
  <svg viewBox="0 0 900 210" role="img" aria-label="Descripción completa de lo
       que muestra la figura, en una oración larga. Un lector que no ve la
       imagen tiene que poder reconstruirla desde aquí.">
    <defs>
      <marker id="a1" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7"
              markerHeight="7" orient="auto-start-reverse">
        <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
      </marker>
      <pattern id="hatch" width="6" height="6" patternTransform="rotate(45)"
               patternUnits="userSpaceOnUse">
        <line x1="0" y1="0" x2="0" y2="6" stroke="currentColor"
              stroke-width="2.4" opacity=".35"/>
      </pattern>
    </defs>
    <g font-family="Arial, sans-serif" font-size="11" fill="currentColor">
      <!-- contenido -->
    </g>
  </svg>
  </div>
  <figcaption><strong>Figura 1.</strong> La afirmación que carga la
  figura.</figcaption>
</figure>
```

Un `id` distinto por figura (`a1`, `a2`, `a3`) o los markers se pisan entre
figuras del mismo documento.

## Estados: se dicen con relleno, no con color

| Estado | Cómo se dibuja |
|---|---|
| Cumplido | `fill="currentColor" fill-opacity=".16"` + borde `stroke-width="1.2"`. Usa `fill-opacity`, no `opacity`: `opacity` aplica al elemento completo y apaga también el borde. |
| A medias | `fill="url(#hatch)"` + borde `stroke-width="1.2"` |
| Sin empezar | `fill="none"` + borde `opacity=".45"`, y el texto también a `.55` |
| Lo que importa | `stroke="var(--accent-ink)" stroke-width="2.2"`, texto en `var(--accent-ink)` |

El acento marca **una sola cosa por figura**. Si marcas tres, no marcaste
ninguna.

## Tipografía dentro de la figura

- Rótulo de bloque: `font-size="10" opacity=".65"`, en mayúsculas.
- Texto de caja: `font-size="11"`, centrado con `text-anchor="middle"`.
- Nota al pie de un elemento: `font-size="9" opacity=".6"`.
- Nada arriba de 13px ni abajo de 9px.

## Reglas que no se negocian

- Todo en `currentColor` y variables. Ningún hex fijo, o la figura se rompe en
  tema oscuro.
- Las flechas van etiquetadas cuando la relación no es obvia: "despacha",
  "regresa hallazgo", "valida".
- Punteado (`stroke-dasharray="5 3"`) para lo que no está en uso o no es firme.
- Las explicaciones van en el `figcaption`, no dentro del dibujo.
- Sin librerías, sin Mermaid, sin imágenes externas. El CSP de los artifacts
  bloquea todo lo de fuera salvo las fuentes de Google.

## Proceso

1. Decide qué mecanismo muestra la figura. Si un renglón de texto lo dice igual
   de rápido, escribe el renglón y no dibujes nada.
2. Arma el `viewBox` con margen para las etiquetas de los extremos. Las
   etiquetas que se salen del `viewBox` no se ven.
3. Dibuja de izquierda a derecha, deja 40 a 50px entre cajas para las flechas.
4. Marca el estado con relleno, no con color.
5. Escribe el `aria-label` completo antes de dar por terminada la figura.
6. Revisa en claro y en oscuro.

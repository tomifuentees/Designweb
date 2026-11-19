# Accesibilidad y performance

El motion es un acabado. Si le cuesta a alguien leer, o si el sitio anda a 20 fps, no es un acabado: es un defecto.

## `prefers-reduced-motion`

Siempre. En CSS:

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

Ese reset global es un *piso*, no un diseño. Mejor: apagá loops, splits, marquees y scrubs, y dejá transiciones de color de 100–120 ms si ayudan a entender un estado. En JS:

```js
const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
```

En Motion, `MotionConfig reducedMotion="user"`. En GSAP, no armes el timeline si `reduce` es true; dejá el estado final. Lenis se apaga o pasa a scroll nativo. Lottie/Rive muestran un frame estático. View Transitions se saltean (`startViewTransition` no hace falta).

SplitText y cualquier split por caracter tienen que dejar el texto accesible (el SplitText de GSAP 3.13+ agrega `aria-label` y `aria-hidden` en los spans). Un split casero que mete un `<div>` por letra rompe el lector de pantalla.

## Performance

- Animá **`transform` y `opacity`**. Evitá `top`, `left`, `width`, `height`, `box-shadow`, `filter: blur()` en objetos grandes, `backdrop-filter` en toda la página.
- Cuidado con `will-change`: un rato, en el objeto que se mueve, no en todo el DOM.
- Un Lottie de 400 kb en el hero, un shader en cada card y un smooth scroll pelean por el mismo frame. Elegí uno.
- En mobile, los scrubs de scroll + WebGL son la receta para un sitio de Awwwards que no se puede usar. Medí en un teléfono real, no solo en el laptop.
- `animation-timeline: view()` corre en el compositor cuando el keyframe es transform/opacity. Si no hay soporte, no escondas el contenido en `opacity: 0`.
- GSAP y Lenis: un solo `requestAnimationFrame` (el ticker de GSAP). No dejes dos loops de RAF pelease.

## Scroll: contar, no secuestrar

Las guías de 2026 (Bubble, Envato; ver [`../estilos/fuentes-investigacion.md`](../estilos/fuentes-investigacion.md)) marcan el **scroll-jacking** como algo a retirar. Scrollytelling sigue vigente cuando el scroll *avanza una historia* y el usuario puede soltar, no cuando una librería le come la rueda 800 px.

Reglas prácticas:

- El wheel y el touch tienen que sentirse nativos, o muy cerca. Si Lenis está, el factor de lerp es conservador.
- Siempre hay un camino para saltear (un índice, un “ir al contenido”).
- No bloquees el scroll para “la experiencia”. Un `overflow: hidden` en el `body` solo mientras un modal está abierto, no durante toda la landing.
- `scroll-snap` puntual (un carousel, un capítulo) está bien; snap en todas las secciones de una home, casi nunca.

## Foco y movimiento

- Un toast no roba el foco. Un dialog sí, y lo devuelve al cerrar.
- `:focus-visible` no se anima de forma que el anillo desaparezca a mitad de camino.
- Las View Transitions no deberían dejar al usuario perdido: el `view-transition-name` va en el objeto que continúa, no en diez wrappers.

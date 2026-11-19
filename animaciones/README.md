# Animaciones

Guía de herramientas y recetas de motion para frontend, armada el 19 de noviembre de 2026 (zona America/Argentina/Salta). El objetivo no es animar de más: es que un agente deje de resolverlo todo con un `fade-in` de 0.6 s, un marquee infinito y un bounce en el toast, y elija la herramienta justa, con easing, duración y `prefers-reduced-motion`.

Esta carpeta se lee junto a [`../estilos/tipografia-kinetica.md`](../estilos/tipografia-kinetica.md), [`../estilos/scrollytelling.md`](../estilos/scrollytelling.md) y los kits de [`../componentes/bibliotecas.md`](../componentes/bibliotecas.md) (Magic UI, Motion Primitives, Cult UI). El catálogo machine-readable está en [`animaciones.json`](./animaciones.json).

## Qué hay acá

| Archivo | Contenido |
|---|---|
| [herramientas.md](./herramientas.md) | Motion (ex Framer Motion), GSAP (gratis desde abril de 2025, con un límite de licencia), Lenis, View Transitions, scroll-driven CSS, `@starting-style`, Rive, Lottie, Theatre.js, Auto-Animate |
| [microinteracciones.md](./microinteracciones.md) | Recetas: hover, press, reveal, stagger, contadores, marquee, split de texto. Snippets CSS/JS |
| [easing-duracion.md](./easing-duracion.md) | Tiempos, curvas y cuándo no animar |
| [accesibilidad-performance.md](./accesibilidad-performance.md) | `prefers-reduced-motion`, lo que se anima (compositor), scroll-jacking |
| [animaciones.json](./animaciones.json) | El mismo catálogo, para skills |
| [fuentes-investigacion.md](./fuentes-investigacion.md) | Fuentes, fechas, lo no verificado |

## Cómo elegir herramienta

1. **CSS primero** si alcanza: hover, press, entrada de un popover (`@starting-style` + `transition-behavior: allow-discrete`), un reveal al scrollear (`animation-timeline: view()`), un cambio de página (View Transition). Menos JS, menos jank, mejor default de reduced motion.
2. **Motion (`motion/react`)** para orquestar UI en React: layout, gestures, exit, stagger de listas. Es la librería que antes se llamaba Framer Motion.
3. **GSAP** cuando hay timeline compleja, ScrollTrigger, split de texto, morph SVG, pin/scrub de verdad. Desde el 30 de abril de 2025 es gratis, también los plugins que eran de Club, incluido uso comercial, con una restricción (no armar un builder visual que compita con Webflow). Ver la ficha.
4. **Lenis** si necesitás smooth scroll. Integralo con GSAP ticker; no lo apiles con otro smooth scroll ni lo uses para secuestrar el scroll en un sitio de contenido.
5. **Rive** para un control interactivo con state machine (un ícono que reacciona, un personaje). **Lottie / DotLottie** para un loop o un reveal puntual, no para toda la UI.
6. **Auto-Animate** para una lista que se reordena sin escribir transiciones. **Theatre.js** quedó documentado, pero el repo no tenía push desde agosto de 2024 en esta pasada: no lo elijas como default vivo.

Una sola familia de motion por superficie. Mezclar Magic UI + Aceternity + GSAP + Lenis + Lottie en la misma landing es el otro default de IA, el “de lujo”.

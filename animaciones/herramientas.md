# Herramientas de motion

Foto del 19 de noviembre de 2026. Licencias, homes y `pushed_at` salen de los sitios oficiales y de la API de GitHub, ese día.

## Motion (antes Framer Motion)

- **Oficial:** [motion.dev](https://motion.dev/) · Upgrade: [docs de migración](https://motion.dev/docs/react-upgrade-guide) · Historia: [Framer Motion is now independent, introducing Motion](https://motion.dev/magazine/framer-motion-is-now-independent-introducing-motion) (noviembre de 2024, GET 200). Repo: [motiondivision/motion](https://github.com/motiondivision/motion) (MIT, activo el 19/11/2026). Cuenta: [@motiondotdev](https://x.com/motiondotdev).
- **Stack:** React (`import { motion } from "motion/react"`; el paquete `framer-motion` queda como compat), más APIs para JS vanilla, Vue y CSS en el toolkit actual. Confirmá el import en la doc vigente.
- **Para qué:** transiciones de UI, `layout`, gestos, exit animations, staggers, scroll en componentes de producto. Es el motor detrás de Magic UI, Cult UI y Motion Primitives.
- **Oficio:** no animes `layout` en 40 nodos a la vez. Respetá reduced motion con `MotionConfig` o un media query. No lo uses para un scrollytelling de 3.000 px si GSAP ScrollTrigger o CSS scroll-driven lo resuelven más barato.

## GSAP (GreenSock)

- **Oficial:** [gsap.com](https://gsap.com/) · [Pricing (now free)](https://gsap.com/pricing/) · [Standard "No Charge" License](https://gsap.com/community/standard-license/) · Release [3.13, 29 de abril de 2025](https://gsap.com/blog/3-13/) · Anuncio de Webflow: [GSAP is now 100% free](https://webflow.com/updates/gsap-becomes-free) (30 de abril de 2025). Cuenta: [@greensock](https://x.com/greensock).
- **Hecho central:** desde el **30 de abril de 2025**, GSAP y **todos** los plugins que eran de Club (SplitText, MorphSVG, DrawSVG, ScrollSmoother, Inertia, MotionPath, Flip, etc.) son **gratis, también para uso comercial**. Se instalan desde el npm público; el repo privado de Club dejó de hacer falta (Webflow pidió migrar antes del 1 de junio de 2025).
- **Licencia (leída en la Standard License, last modified 30 de mayo de 2025):** permitida la implementación en sitios, apps e interfaces, incluso de empresas que compiten con Webflow en *otras* áreas. **Prohibido** usarlo en herramientas no-code que dejen construir animaciones visuales y compitan con el builder de Webflow. La propia FAQ dice que el código generado por IA (Cursor, etc.) **no** es un uso prohibido, y que el uso comercial en proyectos de clientes está cubierto. Esto no es consejo legal: leé el texto vigente.
- **SplitText** fue reescrito en 3.13 (menos peso, `aria-label` / `aria-hidden`, mask de reveals, cleanup). Es la herramienta correcta para un split de texto de oficio, no un innerHTML casero que rompe accesibilidad.
- **Oficio:** ScrollTrigger para pin/scrub; ScrollSmoother solo si hay un motivo. No uses GSAP para el hover de un botón. Integrá Lenis por el ticker (ver abajo). Cassie Evans ([@cassiecodes](https://x.com/cassiecodes)) sigue siendo la voz más clara del equipo en X.

## Lenis

- **Oficial:** [lenis.dev](https://lenis.dev/) (`lenis.darkroom.engineering` redirige acá, GET 200). Repo: [darkroomengineering/lenis](https://github.com/darkroomengineering/lenis) (MIT, push el 19/11/2026). Cuentas verificadas: [@darkroomdevs](https://x.com/darkroomdevs), [@LenisSmooth](https://x.com/LenisSmooth).
- **Qué es:** smooth scroll liviano, de Darkroom Engineering. Se usa mucho con GSAP y con sitios de [scrollytelling](../estilos/scrollytelling.md).
- **Oficio:** enganchá `lenis.on("scroll", ScrollTrigger.update)` y `gsap.ticker.add(t => lenis.raf(t * 1000))` (patrón documentado en discusiones del repo). Apagá o suavizá con `prefers-reduced-motion`. No lo combines con CSS `scroll-behavior: smooth` + otro motor. Los hilos de tendencias de 2026 (Bubble, Envato) marcan el **scroll-jacking** como algo a retirar: Lenis no es excusa para robar la rueda.

## View Transitions API

- **Docs:** [MDN, View Transition API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API) (GET 200). [web.dev: same-document view transitions are now Baseline Newly available](https://web.dev/blog/same-document-view-transitions-are-now-baseline-newly-available) (GET 200): el 14 de octubre de 2025, con Firefox 144, las transiciones *same-document* (`document.startViewTransition`, `view-transition-name`, `view-transition-class`, `:active-view-transition`) entraron a Baseline Newly available. Firefox 144 **no** traía *view transition types*; conviene progresive enhancement.
- **Cross-document** (navegación entre páginas) no estaba en el mismo piso de Baseline en esa nota: Chromium y Safari iban delante; no asumas paridad total sin mirar Can I Use el día que lo implementes.
- **Para qué:** transiciones de página y de estado en la misma documento (una lista que se vuelve detalle, un tema claro/oscuro, un tab). Mucho más barato que un framework de transiciones si el diseño es un morph de un elemento.
- **Oficio:** nombrá pocos `view-transition-name`. Animá opacity y transform. Ofrecé un fallback vacío si no hay soporte, y un corte total con reduced motion.

## CSS scroll-driven animations

- **Docs:** [MDN, Scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations) (GET 200). `animation-timeline: scroll()` o `view()`, `animation-range`, `view-timeline`.
- **Soporte (a esta fecha, sin tratarlo como tabla de Can I Use eterna):** estable en Chromium desde 115 y en Safari 26 (también citado en un post de X de junio de 2025 sobre Safari 26). **Verificá Firefox en Can I Use al implementar**; no dejes el motion crítico solo en esta API.
- **Para qué:** un reveal al entrar en viewport, un progreso de lectura, un carousel con `::scroll-marker`, parallax liviano. Jhey Tompkins ([@jh3yy](https://x.com/jh3yy)) publicó ejemplos vigentes en 2025–2026, entre ellos [carousel con scroll-driven, 28 de agosto de 2026](https://x.com/jh3yy/status/2093465874321563782) y [scroll-snap + scroll-driven, 19 de julio de 2025](https://x.com/jh3yy/status/1946371056047931675).
- **Oficio:** animá transform/opacity, no `top` ni `box-shadow`. Un fallback estático. Cero scroll-jacking.

## `@starting-style` y transiciones discretas

- **Docs:** [MDN, `@starting-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@starting-style) (GET 200). Ampliamente soportado (Chromium 117+, Firefox 129+, Safari 17.5+, según Can I Use / web-features; confirmá si tu floor de browsers es más viejo).
- **Para qué:** animar la *entrada* de un elemento que sale de `display: none` (popover, dialog, tooltip). Se combina con `transition-behavior: allow-discrete` y `@media (prefers-reduced-motion)`.
- **Oficio:** es el reemplazo correcto del “setTimeout + class + fade” que los agentes improvisan en un modal. GreatFrontend lo listaba, en octubre de 2026, entre los pares que un front debería distinguir ([post](https://x.com/greatfrontend/status/2111091192750657787)).

## Rive

- **Oficial:** [rive.app](https://rive.app/) (GET 200). Runtime React: [rive-app/rive-react](https://github.com/rive-app/rive-react) (MIT, push el 9 de noviembre de 2026).
- **Para qué:** motion **interactivo** con state machine (un ícono que se pone en hover, un toggle, un personaje). El diseño vive en el editor de Rive; el runtime lo ejecuta.
- **Oficio:** un artefacto, no un fondo de toda la landing. Tené un fallback estático (PNG/SVG) y un corte de reduced motion. El editor es un producto con su propio plan; el runtime MIT no te libra de mirar la licencia del archivo `.riv` y del plan de equipo.

## Lottie (y DotLottie)

- **Runtime clásico:** [airbnb/lottie-web](https://github.com/airbnb/lottie-web) (MIT). Último push visto: 1 de septiembre de 2025. Comunidad y hosting de archivos: [lottiefiles.com](https://lottiefiles.com/) (GET 200).
- **Para qué:** un loop o un reveal puntual diseñado en After Effects / el editor de Lottie. **No** es el mejor lugar para una UI interactiva (ahí Rive) ni para un layout de React (ahí Motion).
- **Oficio:** los Lottie pesados son un clásico de landings “premium” que pisan 20 fps en mobile. Limitá a un motivo, `play` solo cuando entra en vista, respetá reduced motion (mostrá el último frame o un estático). El ritmo del repo `lottie-web` en 2025–2026 es más calmo que Motion o GSAP; mirá también DotLottie si el proyecto lo pide, y confirmá el paquete vigente.

## Theatre.js

- **Oficial:** [theatrejs.com](https://www.theatrejs.com/) (GET 200). Repo: [theatre-js/theatre](https://github.com/theatre-js/theatre) (Apache-2.0, ~13k stars).
- **Estado:** **no se vio push desde el 14 de agosto de 2024** en esta pasada. El sitio vive, el proyecto no está archivado, pero **no es una herramienta de ritmo 2026**. Sirve como referencia de “timeline editable en el browser”; no lo elijas como motor nuevo sin confirmar que el repo volvió a moverse.
- **Para qué (histórico):** orquestar escenas 3D / WebGL con un editor de curvas. Alternativas vivas: GSAP timelines, o Motion + un canvas/R3F.

## Auto-Animate (FormKit)

- **Oficial:** [auto-animate.formkit.com](https://auto-animate.formkit.com/) (GET 200). Repo: [formkit/auto-animate](https://github.com/formkit/auto-animate) (MIT, push el 7 de noviembre de 2026).
- **Para qué:** transiciones de un contenedor cuando sus hijos se agregan, se van o se reordenan, con casi cero config. Útil en listas, boards, filtros.
- **Oficio:** no lo pongas en un árbol enorme. Combiná con reduced motion (la lib suele respetarlo; confirmá la versión). No reemplaza un layout animation deliberado de Motion cuando el diseño pide un morph.

## Qué no es una herramienta (y se confunde)

- **Magic UI / Aceternity / Motion Primitives / Cult UI** son kits de componentes: viven en [`../componentes/bibliotecas.md`](../componentes/bibliotecas.md). Abajo usan Motion o CSS.
- **ScrollTrigger** es un plugin de GSAP, no una librería aparte.
- **Lenis no es “el GSAP gratis”.** Es solo smooth scroll.

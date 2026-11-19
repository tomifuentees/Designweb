# Componentes

Catálogo de librerías, registries y patrones de UI para frontend, armado el 19 de noviembre de 2026 (zona America/Argentina/Salta). El objetivo no es coleccionar kits por coleccionar: es que un agente de código deje de copiar el default de shadcn/ui (botón pill índigo, card `rounded-2xl`, tres features idénticas, toast que rebota) y elija una base, un registro y un patrón con oficio.

Esta carpeta se lee junto a [`../tipografias/`](../tipografias/README.md) y [`../estilos/`](../estilos/README.md). Las fichas están pensadas para personas y, también, para que una skill las consuma a través de [`componentes.json`](./componentes.json).

Hay **16 librerías o registries** documentadas (con licencia, stack y estado actual verificados) y **12 patrones** de página o producto. Cada patrón trae qué se ve con terminación pro, qué hace mal el default de IA, tipografías del kit y un snippet autónomo en HTML + Tailwind (CDN).

## Qué hay acá

| Archivo | Contenido |
|---|---|
| [bibliotecas.md](./bibliotecas.md) | shadcn/ui y su ecosistema de registries, primitivas headless (Radix, Base UI, Ark, React Aria) y kits de marketing o de producto (Magic UI, Aceternity, coss/Origin, Kibo, Tremor, Cult, Motion Primitives, Animate UI, HeroUI, Park UI, 21st.dev) |
| [hero.md](./hero.md) | Hero: una promesa, no un flyer |
| [navbar.md](./navbar.md) | Navbar: densa, predecible, con estado de scroll |
| [pricing.md](./pricing.md) | Pricing: comparación clara, no tres cards gemelas |
| [features.md](./features.md) | Features: listas, ritmos y alternativas al bento de 3×3 |
| [testimonials.md](./testimonials.md) | Testimonials: voz real, no avatares inventados |
| [faq.md](./faq.md) | FAQ: preguntas que alguien se hace, no SEO vacío |
| [footer.md](./footer.md) | Footer: mapa del sitio, no un cementerio de columnas |
| [forms.md](./forms.md) | Formularios: vacío, carga, error y éxito |
| [tables.md](./tables.md) | Tablas: datos densos, no cards apiladas |
| [dashboards.md](./dashboards.md) | Dashboards: jerarquía de datos, no un muro de widgets |
| [empty-states.md](./empty-states.md) | Empty states: la nada también se diseña |
| [toasts.md](./toasts.md) | Toasts: un aviso, no un espectáculo |
| [componentes.json](./componentes.json) | El mismo catálogo, legible por máquinas |
| [fuentes-investigacion.md](./fuentes-investigacion.md) | Fuentes, fechas y lo que no se pudo verificar |

## Cómo elegir una librería

1. **Primero la primitiva, después el maquillaje.** Si estás armando un sistema de producto, empezá por Base UI (default nuevo de shadcn desde julio de 2026) o, si el proyecto ya corre, quedate en Radix: no migres por moda. Ark y React Aria entran cuando el producto es multi-framework o exige un nivel de a11y de Adobe/Chakra.
2. **shadcn no es una estética, es un flujo.** El CLI y el registry te dejan instalar componentes de varios orígenes (`@shadcn/button`, `@kibo-ui/…`, `owner/repo/item`). El look New York + zinc + Inter es un default, no una obligación. Cambiá tokens, radio, tipo y acento *antes* de sumar un kit animado.
3. **Un kit de motion, no tres.** Magic UI, Aceternity, Cult UI y Motion Primitives se pisan. Elegí uno según el trabajo: marketing pulido (Magic), un solo momento de “wow” (Aceternity), controles con microinteracción (Cult o Motion Primitives).
4. **Leé la licencia de verdad.** MIT cubre la mayoría. Animate UI es MIT + Commons Clause (podés usarlo en un producto, no revender los componentes). Aceternity y Magic UI Pro tienen términos propios. GSAP es gratis, pero no es este folder: está en [`../animaciones/`](../animaciones/README.md).
5. **No uses un efecto de landing en un dashboard.** Spotlight, beams, marquee infinito y globos 3D en una pantalla de trabajo se leen como plantilla de lanzamiento, no como producto.

## Reglas anti-IA genérica (componentes)

- No dejes el tema default de shadcn (zinc + radio grande + botón primario índigo) si el proyecto no es un tutorial.
- No armes la home como Hero centrado + logos + 3 cards + testimonials en slider + pricing de 3 columnas + FAQ. Esa es la plantilla que Reddit (r/web_design, 2026) identifica como “vibecoded”.
- No importes 20 componentes de Magic UI “por si acaso”. Un gesto de motion alcanza.
- No uses Lucide en *todos* los íconos *y* un emoji como ícono de feature. Elegí un set y un criterio; los íconos viven mejor en [`recursos/`](../recursos/) cuando esa carpeta esté lista.
- Los estados importan más que el hover: vacío, carga, error, éxito, deshabilitado, permisos. El default de IA diseña solo el happy path.

## Cómo leer un patrón

Cada ficha de patrón tiene la misma forma: cuándo usarlo, qué se ve con terminación pro, qué hace mal el default de IA, tipografía del kit y un snippet que podés pegar en un HTML. Los snippets son demostraciones de criterio, no un design system: en producción, autohospedá las fuentes (ver [`../tipografias/README.md`](../tipografias/README.md)) y conectá el componente a tus tokens.

# Recursos de UX: enciclopedias, sitios y repos

Curado el 19/11/2026. **Estrellas, último push y licencia** salen de la API de GitHub ese día (no están inventados ni redondeados a ojo; abajo se muestran en miles). Se excluyeron los repos que ya estaban en [`../recursos/repos-referencia.json`](../recursos/repos-referencia.json) y en el resto del kit (por ejemplo Sonner, ya en `componentes/toasts.md`).

Licencias: lo que no sea MIT/Apache/CC0 (o no declare licencia) se **resume y linkea**, no se copia literal.

## Las enciclopedias de referencia (sitios)

| Recurso | Qué cubre | Por qué es fuente |
|---|---|---|
| [NN/g, artículos](https://www.nngroup.com/articles/) y [glosario de UI](https://www.nngroup.com/articles/ui-elements-glossary/) | Todo: heurísticas, investigación, IA, patrones | Décadas de investigación propia; fechas en cada artículo |
| [Laws of UX](https://lawsofux.com/) | 30 leyes y principios psicológicos con fuentes | Base de [`fundamentos.md`](fundamentos.md) |
| [Baymard Institute](https://baymard.com/research) | E-commerce: checkout, búsqueda, producto, mobile, IA | 700+ guías de tests de usabilidad (parte paga) |
| [GOV.UK Design System](https://design-system.service.gov.uk/) y [Service Manual](https://www.gov.uk/service-manual) | Formularios, validación, preguntas, contenido, servicios | Cada patrón tiene investigación con usuarios reales y diversos |
| [USWDS](https://designsystem.digital.gov/) | Patrones de servicios de EE.UU., accesibilidad | Sistema federal de EE.UU. |
| [WAI-ARIA APG](https://www.w3.org/WAI/ARIA/apg/) y [WAI Tutorials](https://www.w3.org/WAI/tutorials/) | Patrones de componentes con teclado | W3C |
| [Understanding WCAG 2.2](https://www.w3.org/WAI/WCAG22/Understanding/) | Intención y técnicas de cada criterio | W3C |
| [Material Design 3](https://m3.material.io/) | Componentes, accesibilidad, contenido, M3 Expressive | Google, con investigación publicada |
| [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/) | Plataformas Apple, accesibilidad | Apple |
| [web.dev](https://web.dev/) | Core Web Vitals, formularios, accesibilidad | Chrome |
| [Smashing Magazine, UX](https://www.smashingmagazine.com/category/ux/) | Patrones, formularios, IA (Vitaly Friedman) | Artículos fechados y revisados |
| [Growth.Design case studies](https://growth.design/case-studies) | Onboarding, activación, psicología, en formato cómic | Casos de productos reales |
| [Refactoring UI](https://refactoringui.com/) | Decisiones de UI para devs | Wathan y Schoger |
| [Shape of AI](https://www.shapeof.ai/) · [Google PAIR](https://pair.withgoogle.com/guidebook/) · [Microsoft HAX](https://www.microsoft.com/en-us/haxtoolkit/ai-guidelines/) | UX de IA | Base de [`ux-ia.md`](ux-ia.md) |
| [deceptive.design](https://www.deceptive.design/) | Patrones oscuros, casos legales | Harry Brignull |
| [MeasuringU](https://measuringu.com/) | Métricas, SUS, tamaños de muestra | Jeff Sauro |
| [Inclusive Components](https://inclusive-components.design/) | Componentes accesibles explicados | Heydon Pickering |
| [The A11Y Project](https://www.a11yproject.com/) | Checklist WCAG en lenguaje llano | Comunidad |
| [Passkey Central (FIDO)](https://www.passkeycentral.org/design-user-journeys/) | Diseño de flujos con passkeys | FIDO Alliance |
| [Usability Body of Knowledge](https://www.usabilitybok.org/) | Métodos de UX | UXPA |

Galerías de patrones reales (útiles, la mayoría pagas): Mobbin, Page Flows, Pttrns. Ya hay galerías visuales en [`../inspiracion/`](../inspiracion/README.md).

## Repos (no estaban en el kit)

| Repo | ★ (API, 19/11/2026) | Último push | Licencia | Categoría | Para qué |
|---|---|---|---|---|---|
| [thedaviddias/Front-End-Checklist](https://github.com/thedaviddias/Front-End-Checklist) | 74,8 k | 2026-10-31 | MIT | Checklists | Checklist de frontend "para humanos y agentes"; usala junto a checklist-ux.md para lo técnico (meta, perf, seguridad). |
| [react-hook-form/react-hook-form](https://github.com/react-hook-form/react-hook-form) | 44,9 k | 2026-11-18 | MIT | Formularios | Estado y validación de formularios en React con modos onTouched/onBlur para la validación del kit. |
| [GoogleChrome/lighthouse](https://github.com/GoogleChrome/lighthouse) | 31,2 k | 2026-11-19 | Apache-2.0 | Medición y rendimiento | Auditoría de rendimiento, accesibilidad y buenas prácticas; Lighthouse CI para presupuestos. |
| [usablica/intro.js](https://github.com/usablica/intro.js) | 23,5 k | 2026-11-12 | NOASSERTION | Onboarding | Tours de producto. Usalo poco: el kit desaconseja tours largos; sirve para un tooltip contextual puntual. Revisá la licencia (AGPL/comercial). |
| [GoogleChrome/web-vitals](https://github.com/GoogleChrome/web-vitals) | 8,7 k | 2026-11-12 | Apache-2.0 | Medición y rendimiento | Medir LCP, INP y CLS reales (RUM) con atribución. |
| [dequelabs/axe-core](https://github.com/dequelabs/axe-core) | 7,9 k | 2026-11-18 | MPL-2.0 | Accesibilidad | Motor de tests automáticos de accesibilidad (Playwright, Jest, CI). |
| [uswds/uswds](https://github.com/uswds/uswds) | 7,2 k | 2026-11-04 | NOASSERTION | Sistemas de diseño con investigación detrás | U.S. Web Design System: componentes y patrones accesibles probados en servicios federales de EE.UU. |
| [thedaviddias/Front-End-Design-Checklist](https://github.com/thedaviddias/Front-End-Design-Checklist) | 5,4 k | 2024-12-10 | CC0-1.0 | Checklists | Checklist de diseño para handoff (estados, tipografía, assets). |
| [pa11y/pa11y](https://github.com/pa11y/pa11y) | 4,6 k | 2026-11-16 | LGPL-3.0 | Accesibilidad | Tests de accesibilidad por línea de comandos y en CI. |
| [openui/open-ui](https://github.com/openui/open-ui) | 4,5 k | 2026-11-19 | NOASSERTION | Estándares web | Investigación de componentes nativos (select personalizable, popover, invokers): por qué los nuevos primitivos funcionan como funcionan. |
| [Jakubantalik/thinking-orbs](https://github.com/Jakubantalik/thinking-orbs) | 4,0 k | 2026-08-16 | MIT | UX de IA | Indicadores de "pensando" para UIs de IA y agentes; alternativa a spinners mudos (combinar con texto de estado). |
| [a11yproject/a11yproject.com](https://github.com/a11yproject/a11yproject.com) | 3,9 k | 2026-11-09 | Apache-2.0 | Accesibilidad | The A11Y Project: checklist WCAG en lenguaje llano, posts y recursos. |
| [oil-oil/oil-ui](https://github.com/oil-oil/oil-ui) | 3,5 k | 2026-11-18 | MIT | Skills y reglas para agentes | Skill de UI para agentes que explora direcciones y compara antes de construir. |
| [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) | 3,4 k | 2026-11-19 | MIT | Skills y reglas para agentes | Colección de skills de diseño para agentes (investigación a sistemas). Comparar con la skill del kit. |
| [brunopulis/awesome-a11y](https://github.com/brunopulis/awesome-a11y) | 2,0 k | 2026-08-03 | CC0-1.0 | Accesibilidad | Lista curada de recursos de accesibilidad (CC0). |
| [raunofreiberg/interfaces](https://github.com/raunofreiberg/interfaces) | 2,0 k | 2023-09-07 | sin licencia | Detalles de interacción | Lista de detalles de interacción que hacen buena una interfaz web (sin licencia declarada: leer y linkear, no copiar). |
| [alphagov/govuk-frontend](https://github.com/alphagov/govuk-frontend) | 1,5 k | 2026-11-19 | MIT | Sistemas de diseño con investigación detrás | Código de GOV.UK Frontend: error summary, validación, preguntas de a una, todo testeado con usuarios. |
| [hendurhance/ui-ux](https://github.com/hendurhance/ui-ux) | 1,5 k | 2026-10-13 | CC0-1.0 | Aprendizaje | Ruta de aprendizaje UI/UX en tres niveles (CC0). |
| [w3c/aria-practices](https://github.com/w3c/aria-practices) | 1,4 k | 2026-11-18 | NOASSERTION | Accesibilidad | Fuente del WAI-ARIA Authoring Practices Guide (patrones y ejemplos de teclado). |
| [vercel-labs/web-interface-guidelines](https://github.com/vercel-labs/web-interface-guidelines) | 1,2 k | 2026-10-05 | MIT | Detalles de interacción | Guías de interfaz web de Vercel (teclado, foco, formularios, animación); se usan como reglas para agentes. |
| [uxchecklist/uxchecklist.github.io](https://github.com/uxchecklist/uxchecklist.github.io) | 960 | 2026-04-22 | GPL-3.0 | Checklists | Checklist de proyecto UX por etapas (GPL-3.0). |
| [alphagov/govuk-design-system](https://github.com/alphagov/govuk-design-system) | 692 | 2026-11-19 | MIT | Sistemas de diseño con investigación detrás | Sitio y guías del GOV.UK Design System (patrones, investigación detrás de cada componente). |
| [felipebasurto/unslop-ui](https://github.com/felipebasurto/unslop-ui) | 524 | 2026-11-18 | MIT | Skills y reglas para agentes | Skill que saca tells de IA de la copy de UI, gráficos y dashboards (complementa ux-writing-microcopy.md). |
| [tommyjepsen/awesome-ux-skills](https://github.com/tommyjepsen/awesome-ux-skills) | 322 | 2026-08-10 | sin licencia | Skills y reglas para agentes | Lista de skills de UX y producto para Claude, Codex, etc. (sin licencia declarada). |
| [cuellarfr/design-skills](https://github.com/cuellarfr/design-skills) | 128 | 2026-09-30 | MIT | Skills y reglas para agentes | Skills de UX: investigación, crítica, accesibilidad, journey mapping. |
| [quietloudlab/ai-interaction-atlas](https://github.com/quietloudlab/ai-interaction-atlas) | 126 | 2026-08-24 | Apache-2.0 | UX de IA | Lenguaje compartido para diseñar experiencias con IA (Apache-2.0). |
| [artouc/stop-describing-ui](https://github.com/artouc/stop-describing-ui) | 94 | 2026-10-11 | MIT | Skills y reglas para agentes | Skill que quita texto explicativo innecesario de interfaces. |
| [mohsen-rafiei/UX_datasets](https://github.com/mohsen-rafiei/UX_datasets) | 63 | 2025-11-03 | NOASSERTION | Investigación | Datasets de investigación UX para practicar análisis. |
| [marvinrez/ux-wise-agent](https://github.com/marvinrez/ux-wise-agent) | 52 | 2026-10-29 | MIT | Skills y reglas para agentes | Pack de skills para diseñadores y PMs (estrategia, discovery). |
| [keysjoao/laws-of-ux-skills](https://github.com/keysjoao/laws-of-ux-skills) | 30 | 2026-05-08 | MIT | Skills y reglas para agentes | Tres skills de Claude Code basadas en las 30 leyes de UX (asesor, auditoría, prompts). |

## Top 8 para sacarle jugo primero

1. **GOV.UK Frontend + Design System**: copiar el comportamiento del error summary, la validación y "una pregunta por página" (MIT).
2. **axe-core + pa11y**: meter accesibilidad en CI ([`accesibilidad.md`](accesibilidad.md)).
3. **web-vitals + Lighthouse**: RUM y presupuestos de rendimiento ([`rendimiento-percibido.md`](rendimiento-percibido.md)).
4. **WAI-ARIA APG (w3c/aria-practices)**: patrones de teclado de referencia.
5. **USWDS**: patrones de servicios para el mercado de EE.UU.
6. **vercel-labs/web-interface-guidelines**: reglas de interacción para agentes; cruzarlas con [`anti-patrones-ux.md`](anti-patrones-ux.md).
7. **Front-End-Checklist**: lo técnico que el checklist UX no cubre.
8. **ai-interaction-atlas + thinking-orbs**: vocabulario y estados de carga para UIs de IA ([`ux-ia.md`](ux-ia.md)).

Los repos de skills para agentes con pocas estrellas (< 200) están por novedad 2026, no por aval: revisalos antes de adoptar.

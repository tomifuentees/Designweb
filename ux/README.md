# UX: enciclopedia de experiencia de usuario

Todo lo que hace que una interfaz **funcione** para la persona (y para el agente de IA que actúa por ella): flujos, formularios, estados, feedback, navegación, accesibilidad, copy, rendimiento, IA, ética, investigación y métricas. Con reglas de decisión, do/don't y código (HTML, CSS, React + Tailwind) accesible.

Actualizado al **19/11/2026**. Fuentes: NN/g, Laws of UX, Baymard, WCAG 2.2 / WAI-ARIA APG, GOV.UK, USWDS, Material 3, Apple HIG, web.dev, Smashing, Growth.Design, Shape of AI, Google PAIR y Microsoft HAX, más señales de r/UXDesign y X. Detalle y fechas en [`fuentes-investigacion.md`](fuentes-investigacion.md). Ninguna estadística está inventada; lo que es regla de oficio o señal de comunidad está marcado.

## Cómo lo usa un agente

1. **Ubicá el problema** en la tabla de abajo (o en `ux.json` → `problema_a_archivo`) y abrí solo ese archivo.
2. **Antes de codear una vista**, escribí en el brief: tarea y persona, flujo con salidas (Atrás, Deshacer, Cancelar), matriz de estados ([`estados.md`](estados.md)), campos y validación si hay formulario, y la copy clave.
3. **Construí** con HTML semántico y los snippets de cada archivo; los umbrales numéricos están en `ux.json` → `umbrales`.
4. **Cerrá** pasando [`checklist-ux.md`](checklist-ux.md) y reportando los ids que fallan con su severidad (0–4). Severidad 4 bloquea.
5. Si el proyecto es otro repo, pegá el bloque de [`anti-patrones-ux.md`](anti-patrones-ux.md#bloque-pegable-para-claudemd-ux) en su `CLAUDE.md`.

La skill [`../skills/frontend-design/SKILL.md`](../skills/frontend-design/SKILL.md) ya hace estos pasos.

## Problema → archivo

| Si el problema es… | Abrí |
|---|---|
| No sé qué principio aplica / leyes de UX / carga cognitiva | [`fundamentos.md`](fundamentos.md) |
| Revisar una UI y priorizar problemas | [`heuristicas.md`](heuristicas.md) |
| No encuentran cosas / navegación / menús / breadcrumbs | [`arquitectura-informacion-navegacion.md`](arquitectura-informacion-navegacion.md) |
| Formularios, validación, errores, login, passkeys, OTP | [`formularios-inputs.md`](formularios-inputs.md) |
| Abandono en carrito o checkout / ficha de producto | [`checkout-ecommerce.md`](checkout-ecommerce.md) |
| Búsqueda, autocompletado, filtros, paginación | [`busqueda-filtros.md`](busqueda-filtros.md) |
| Usuarios nuevos que no se activan / permisos | [`onboarding-activacion.md`](onboarding-activacion.md) |
| Vacíos, cargas, skeletons, errores, offline, UI optimista | [`estados.md`](estados.md) |
| Toast vs modal vs inline, confirmaciones, deshacer, notificaciones | [`feedback-notificaciones.md`](feedback-notificaciones.md) |
| Dashboards, gráficos, tablas densas | [`tablas-datos-dashboards.md`](tablas-datos-dashboards.md) |
| Celular: objetivos táctiles, pulgar, gestos, teclado | [`mobile-touch.md`](mobile-touch.md) |
| WCAG 2.2, ADA, EAA, teclado, foco, ARIA, lector de pantalla | [`accesibilidad.md`](accesibilidad.md) |
| Textos de botones, errores, vacíos (ES y EN) | [`ux-writing-microcopy.md`](ux-writing-microcopy.md) |
| Se siente lento / Core Web Vitals / INP | [`rendimiento-percibido.md`](rendimiento-percibido.md) |
| Chat, copiloto, agentes, búsqueda con IA | [`ux-ia.md`](ux-ia.md) |
| Cancelaciones, cookies, urgencia, precios: ¿es manipulador o ilegal? | [`patrones-oscuros-etica.md`](patrones-oscuros-etica.md) |
| Qué método de investigación usar / test con usuarios / A/B | [`investigacion-testing.md`](investigacion-testing.md) |
| Qué medir: SUS, UMUX-Lite, SEQ, HEART, NPS | [`metricas.md`](metricas.md) |
| Revisión final antes de publicar | [`checklist-ux.md`](checklist-ux.md) |
| Errores de UX típicos de código generado por IA | [`anti-patrones-ux.md`](anti-patrones-ux.md) |
| Más sitios, enciclopedias y repos | [`recursos-ux.md`](recursos-ux.md) |

## Archivos

| Archivo | Qué tiene |
|---|---|
| [`fundamentos.md`](fundamentos.md) | UX vs UI vs experience design, Norman, modelos mentales, carga cognitiva, 23 leyes con aplicación y **calidad de la evidencia**, tiempos de respuesta |
| [`heuristicas.md`](heuristicas.md) | Las 10 de Nielsen (H1–H10) con ejemplos web, procedimiento de evaluación, escala de severidad, plantillas MD/JSON, cognitive walkthrough |
| [`arquitectura-informacion-navegacion.md`](arquitectura-informacion-navegacion.md) | Métodos (card sorting, tree testing), patrones de navegación y cuándo usarlos, disclosure nav, breadcrumb, estado en URL, SPA |
| [`formularios-inputs.md`](formularios-inputs.md) | Campos mínimos, labels, tabla de `type`/`inputmode`/`autocomplete`, **GOV.UK vs Baymard en validación** con regla de decisión, resumen de errores (vanilla y react-hook-form + zod), multipaso, passkeys y contraseñas, elección de controles |
| [`checkout-ecommerce.md`](checkout-ecommerce.md) | Números de Baymard 2026, 11 reglas de checkout, ficha de producto, IA en e-commerce, resumen de costos |
| [`busqueda-filtros.md`](busqueda-filtros.md) | Los 8 tipos de consulta de Baymard con % 2026, autocompletado, facetas, chips, paginación vs scroll infinito, búsqueda con IA |
| [`onboarding-activacion.md`](onboarding-activacion.md) | Activación, flujo SaaS, patrones, pre-prompt de permisos, checklist de activación |
| [`estados.md`](estados.md) | Matriz de 12 estados, cuándo usar cada indicador de carga, skeleton, `useOptimistic`, errores, offline, éxito proporcional |
| [`feedback-notificaciones.md`](feedback-notificaciones.md) | Elegir canal, **deshacer > confirmar**, toasts, `<dialog>` con invoker commands, banners, notificaciones, tooltips |
| [`tablas-datos-dashboards.md`](tablas-datos-dashboards.md) | Dashboards por decisión, elegir gráfico, reglas de tabla, tabla ordenable accesible, `Intl` |
| [`mobile-touch.md`](mobile-touch.md) | Objetivos (WCAG/HIG/Material), pulgar, gestos y 2.5.7, teclado en pantalla, safe areas, Liquid Glass y M3 Expressive |
| [`accesibilidad.md`](accesibilidad.md) | **Estado normativo 2026** (WCAG 3, ADA II extendida, EAA, EN 301 549 v4.1.1), lo nuevo de 2.2, checklist A-01…A-28, ARIA y APG, tabs, foco, preferencias, COGA, testing con axe |
| [`ux-writing-microcopy.md`](ux-writing-microcopy.md) | Principios, fórmulas y banco de 20 situaciones en español e inglés, plurales e i18n |
| [`rendimiento-percibido.md`](rendimiento-percibido.md) | Umbrales CWV, estado CrUX oct. 2026, soft navigations, checklists LCP/INP/CLS con código, RUM |
| [`ux-ia.md`](ux-ia.md) | Contexto 2026, HAX/PAIR/Shape of AI, chat vs embebida, patrones antes/durante/después, agentes, streaming con Detener y fuentes, card de aprobación, checklist AI-01…AI-12 |
| [`patrones-oscuros-etica.md`](patrones-oscuros-etica.md) | Catálogo con alternativa honesta, **estado legal EE.UU./UE 2026** (click-to-cancel anulada, ROSCA, Amazon, AB 2863, DSA, DFA), cancelación y cookies honestas |
| [`investigacion-testing.md`](investigacion-testing.md) | Elegir método, test de usabilidad, **los 5 usuarios con letra chica**, guion, encuestas, analítica, A/B sin autoengaño, IA en investigación |
| [`metricas.md`](metricas.md) | Métricas de tarea, SUS (con código), UMUX-Lite, CES, NPS y sus críticas, HEART + GSM |
| [`checklist-ux.md`](checklist-ux.md) | 41 ítems con id y severidad + pasadas manuales |
| [`anti-patrones-ux.md`](anti-patrones-ux.md) | 35 errores de UX de código generado por IA (UX-01…UX-35) + bloque para `CLAUDE.md` |
| [`recursos-ux.md`](recursos-ux.md) | 20 enciclopedias/sitios y 30 repos verificados con la API de GitHub (no estaban en el kit) |
| [`ux.json`](ux.json) | Machine-readable: problema→archivo, heurísticas, severidad, leyes, umbrales, WCAG 2.2 nuevos, normativa, checklist, soporte web platform, repos |
| [`fuentes-investigacion.md`](fuentes-investigacion.md) | Todas las fuentes con fecha y lo que no se pudo verificar |

## Relación con el resto del kit

- Aspecto visual de formularios, vacíos, toasts, tablas y dashboards: [`../componentes/`](../componentes/README.md). Acá está el comportamiento.
- Tells visuales de IA: [`../anti-patrones/`](../anti-patrones/README.md). Tells de layout: [`../layout/anti-patrones-layout.md`](../layout/anti-patrones-layout.md).
- Motion y `prefers-reduced-motion`: [`../animaciones/`](../animaciones/README.md).
- Contraste de paletas: [`../paletas/`](../paletas/README.md).

No es asesoramiento legal: los estados normativos están verificados al 19/11/2026.

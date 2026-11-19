# Anti-patrones de UX que genera la IA

Los tells **visuales** de la UI de IA están en [`../anti-patrones/catalogo.md`](../anti-patrones/catalogo.md) (30) y los de layout en [`../layout/anti-patrones-layout.md`](../layout/anti-patrones-layout.md). Esta lista es de **comportamiento**: cosas que se ven bien en una captura y fallan cuando alguien las usa. Ids `UX-*`.

Patrón de fondo: la IA optimiza para la captura de pantalla del estado ideal. Las comunidades de diseño lo vienen marcando en 2026 (r/UXDesign sobre *design drift* del vibe coding; posteos en X que piden un "gate" de empty, loading, error y screenshot mobile antes de revisar PRs de agentes). Son señales de comunidad, no estudios.

| id | Anti-patrón | Por qué falla | Arreglo | Ver |
|---|---|---|---|---|
| UX-01 | **Solo happy path**: sin vacío, carga, error, parcial ni éxito | La primera vez y el primer fallo son los momentos de más abandono | Matriz de estados en el brief | [`estados.md`](estados.md) |
| UX-02 | **`div onClick`** y botones que son links (o al revés) | Sin teclado, sin rol, invisible para lectores y agentes | `<button>` / `<a href>` | [`accesibilidad.md`](accesibilidad.md) |
| UX-03 | **`outline: none`** sin reemplazo | Navegar por teclado se vuelve imposible | `:focus-visible` con 2 px y contraste | [`accesibilidad.md`](accesibilidad.md) |
| UX-04 | **Placeholder como label** y floating labels | Desaparece al escribir; bajo contraste | Label visible arriba | [`formularios-inputs.md`](formularios-inputs.md) |
| UX-05 | **Validación al tipear** ("Email inválido" en la primera letra) | Grita antes de que la persona termine | On submit + on blur con contenido | [`formularios-inputs.md`](formularios-inputs.md) |
| UX-06 | **Submit deshabilitado** hasta que todo esté "perfecto" | No explica qué falta; no se enfoca | Dejar enviar y mostrar errores | [`formularios-inputs.md`](formularios-inputs.md) |
| UX-07 | **"Something went wrong" / "Algo salió mal"** | No dice qué pasó ni qué hacer | Causa + acción + datos a salvo | [`ux-writing-microcopy.md`](ux-writing-microcopy.md) |
| UX-08 | **Toast para todo** (errores incluidos, 2 s) | Se va antes de leerlo; no llega al lector | Inline para errores; toast ≥ 5 s con pausa | [`feedback-notificaciones.md`](feedback-notificaciones.md) |
| UX-09 | **"¿Estás seguro?" Sí / No** para acciones reversibles | Confirmación automática; no previene | Hacer + Deshacer | [`feedback-notificaciones.md`](feedback-notificaciones.md) |
| UX-10 | **Modal al cargar** (newsletter, bienvenida, cookies gigantes) | Interrumpe antes de dar valor | Pedir en contexto | [`feedback-notificaciones.md`](feedback-notificaciones.md) |
| UX-11 | **Spinner de página completa** para cualquier carga | Bloquea todo y se siente lento | Skeleton local; mantener datos viejos | [`estados.md`](estados.md) |
| UX-12 | **Estado que no vive en la URL** (filtros, tabs, paginación) | Recargar o Atrás pierde todo | `searchParams` | [`arquitectura-informacion-navegacion.md`](arquitectura-informacion-navegacion.md) |
| UX-13 | **Acciones solo al hover** (editar, borrar en filas) | No existen en touch ni para teclado | Visibles o en menú accesible | [`tablas-datos-dashboards.md`](tablas-datos-dashboards.md) |
| UX-14 | **Íconos sin label** en navegación y acciones | Ambiguos; sin nombre accesible | Texto visible o `aria-label` + tooltip | [`arquitectura-informacion-navegacion.md`](arquitectura-informacion-navegacion.md) |
| UX-15 | **`type="number"`** para teléfono, CP, tarjeta | Borra ceros, flechas, scroll cambia el valor | `inputmode="numeric"` | [`formularios-inputs.md`](formularios-inputs.md) |
| UX-16 | **Sin `autocomplete`** | Más tipeo, más errores; incumple 1.3.5 | Tokens correctos | [`formularios-inputs.md`](formularios-inputs.md) |
| UX-17 | **Objetivos táctiles de 16–20 px** (íconos sueltos) | Toques fallidos; incumple 2.5.8 | ≥ 24 px, mejor 44 | [`mobile-touch.md`](mobile-touch.md) |
| UX-18 | **Drag and drop como única forma** de ordenar | Incumple 2.5.7; imposible con teclado | Botones mover / menú | [`mobile-touch.md`](mobile-touch.md) |
| UX-19 | **Copy genérica en botones** ("Submit", "Continuar", "OK") | No dice el resultado | Verbo + objeto | [`ux-writing-microcopy.md`](ux-writing-microcopy.md) |
| UX-20 | **Mezcla de idiomas** (UI en español con errores de librería en inglés) | Rompe confianza | Traducir mensajes de librerías y del navegador | [`ux-writing-microcopy.md`](ux-writing-microcopy.md) |
| UX-21 | **Empty state único** para primera vez, sin resultados y sin permiso | Cada caso necesita otra salida | Tres vacíos distintos | [`estados.md`](estados.md) |
| UX-22 | **Onboarding tour de 6+ pasos** al primer login | Se saltea, no se recuerda | Plantilla + 1 acción guiada + ayuda en contexto | [`onboarding-activacion.md`](onboarding-activacion.md) |
| UX-23 | **Datos de ejemplo** que parecen reales | La persona no sabe qué es suyo | Marcados y borrables en 1 clic | [`onboarding-activacion.md`](onboarding-activacion.md) |
| UX-24 | **Layout shift** cuando llegan los datos o la imagen | Clics en el lugar equivocado; CLS | Reservar espacio | [`rendimiento-percibido.md`](rendimiento-percibido.md) |
| UX-25 | **Handlers pesados** en cada tecla o clic | INP malo; la UI se traba | Feedback primero, ceder el hilo, `useTransition` | [`rendimiento-percibido.md`](rendimiento-percibido.md) |
| UX-26 | **Dashboard de 12 gráficos** sin decisión | Nadie sabe qué mirar | 3–6 KPIs con contexto y drill-down | [`tablas-datos-dashboards.md`](tablas-datos-dashboards.md) |
| UX-27 | **Chat como única interfaz** de una función de IA | Página en blanco, difícil de verificar | IA embebida + controles + fuentes | [`ux-ia.md`](ux-ia.md) |
| UX-28 | **Streaming sin Detener** y anunciando cada token | Sin control; inunda el lector de pantalla | Botón Detener; anunciar solo el final | [`ux-ia.md`](ux-ia.md) |
| UX-29 | **Agente que actúa sin confirmar** acciones externas | Errores irreversibles | Card de aprobación con detalle | [`ux-ia.md`](ux-ia.md) |
| UX-30 | **Patrones de urgencia o escasez decorativos** ("¡Solo quedan 3!" hardcodeado) | Engañoso; riesgo legal | Datos reales o nada | [`patrones-oscuros-etica.md`](patrones-oscuros-etica.md) |
| UX-31 | **Botón "Rechazar" escondido** en cookies o upsells | Patrón oscuro (DSA, CCPA) | Opciones con el mismo peso | [`patrones-oscuros-etica.md`](patrones-oscuros-etica.md) |
| UX-32 | **Precio sin envío/fees** hasta el último paso | Principal motivo de abandono (Baymard) | Total temprano | [`checkout-ecommerce.md`](checkout-ecommerce.md) |
| UX-33 | **Sesión que expira y borra** el formulario | Pérdida de trabajo | Aviso y extender; autosave | [`formularios-inputs.md`](formularios-inputs.md) |
| UX-34 | **`user-scalable=no`** en el viewport | Impide zoom; incumple 1.4.4 | Quitarlo | [`mobile-touch.md`](mobile-touch.md) |
| UX-35 | **Ruta de SPA sin foco ni título** | El lector no se entera del cambio | Foco al `h1`, `document.title` | [`arquitectura-informacion-navegacion.md`](arquitectura-informacion-navegacion.md) |

## Bloque pegable para `CLAUDE.md` (UX)

```md
## UX (Designweb/ux)
- Antes de codear una vista: listá sus estados (vacío inicial, sin resultados, cargando, error, parcial, éxito, offline) y el flujo con sus salidas (Atrás, Deshacer, Cancelar).
- HTML semántico primero: <button>, <a href>, <dialog>, <details>, <label>. Nada de div clickeables. Foco visible siempre.
- Formularios: label visible arriba, autocomplete y inputmode correctos, validar al enviar (+ on blur con contenido), resumen de errores + error por campo, nunca vaciar campos ni deshabilitar el submit para indicar errores.
- Reversible → hacer + Deshacer. Irreversible → confirmación con verbo + objeto.
- Toasts solo para lo no crítico (≥5 s, role=status). Ningún modal al cargar.
- Copy: verbo + objeto en botones; errores con qué pasó + qué hacer; sin "Algo salió mal".
- Objetivos táctiles ≥24 px (44 en principales). Nada solo al hover. Arrastre con alternativa.
- Estado de filtros/tabs/página en la URL. En SPA, foco y título al cambiar de ruta.
- Perf: feedback <100 ms, INP ≤200 ms, reservar espacio (CLS ≤0,1).
- IA: embebida en la tarea, fuentes, Detener, editar/regenerar; agentes piden aprobación antes de lo irreversible.
- Sin patrones oscuros: rechazar = aceptar, cancelar = contratar, precio total temprano.
- Cerrá pasando ux/checklist-ux.md y reportando ids que fallan con su severidad.
```

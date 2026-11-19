# Checklist UX antes de publicar

Pasada final para humanos y agentes. Cada ítem tiene un id (también en [`ux.json`](ux.json) → `checklist`) y la **severidad si falla** en la escala de Nielsen (0–4, ver [`heuristicas.md`](heuristicas.md)).

**Regla de cierre:** cualquier ítem con severidad 4 que falle bloquea el release. Con dos o más de severidad 3, arreglá antes de cerrar. Reportá así: `FO-03 ✗ (S4): el rechazo de tarjeta vaciaba el form → arreglado`.

Complementa (no reemplaza) el checklist visual de [`../anti-patrones/checklist-revision.md`](../anti-patrones/checklist-revision.md) y el de layout en [`../layout/anti-patrones-layout.md`](../layout/anti-patrones-layout.md).

## Flujo

- [ ] **F-01** (S3) La tarea principal de cada pantalla se entiende en 5 segundos y tiene una sola acción primaria. → [`fundamentos.md`](fundamentos.md) · H8
- [ ] **F-02** (S3) Se sabe dónde estoy, qué pasó y qué sigue (estado visible, paso actual, ítem activo). → [`heuristicas.md`](heuristicas.md) · H1
- [ ] **F-03** (S4) Toda acción reversible tiene deshacer; lo irreversible pide confirmación específica con verbo. → [`feedback-notificaciones.md`](feedback-notificaciones.md) · H3, H5
- [ ] **F-04** (S3) El botón Atrás del navegador funciona; filtros, pestañas y páginas viven en la URL. → [`arquitectura-informacion-navegacion.md`](arquitectura-informacion-navegacion.md) · H3
- [ ] **F-05** (S4) No se pierde trabajo: borradores, campos que no se vacían, aviso antes de expirar la sesión. → [`estados.md`](estados.md) · H5, WCAG 2.2.1
- [ ] **F-06** (S3) Se pide solo lo necesario y cuando hace falta (registro, permisos, datos personales). → [`onboarding-activacion.md`](onboarding-activacion.md)

## Navegación

- [ ] **N-01** (S3) Rótulos descriptivos en el lenguaje de la persona; navegación consistente entre páginas. → [`arquitectura-informacion-navegacion.md`](arquitectura-informacion-navegacion.md) · H2, H4, WCAG 3.2.3
- [ ] **N-02** (S3) Hay búsqueda si hay mucho contenido; 'sin resultados' ofrece salidas. → [`busqueda-filtros.md`](busqueda-filtros.md)
- [ ] **N-03** (S3) Skip link, landmarks y título de página por ruta. → [`accesibilidad.md`](accesibilidad.md) · WCAG 2.4.1, WCAG 2.4.2

## Formularios

- [ ] **FO-01** (S3) Labels visibles arriba del campo; nada de placeholder como label. → [`formularios-inputs.md`](formularios-inputs.md) · WCAG 3.3.2
- [ ] **FO-02** (S2) type, inputmode y autocomplete correctos en cada campo. → [`formularios-inputs.md`](formularios-inputs.md) · WCAG 1.3.5
- [ ] **FO-03** (S4) Errores en texto junto al campo + resumen arriba al enviar; foco al resumen; nada se borra. → [`formularios-inputs.md`](formularios-inputs.md) · H9, WCAG 3.3.1, WCAG 3.3.3
- [ ] **FO-04** (S2) Sin validación mientras escribe; inline solo al salir de un campo con contenido. → [`formularios-inputs.md`](formularios-inputs.md)
- [ ] **FO-05** (S3) El botón de enviar no se deshabilita para indicar errores; evita doble envío con estado pending. → [`formularios-inputs.md`](formularios-inputs.md) · H1
- [ ] **FO-06** (S3) Login permite pegar y gestores; passkeys ofrecidas; sin CAPTCHA cognitivo sin alternativa. → [`formularios-inputs.md`](formularios-inputs.md) · WCAG 3.3.8
- [ ] **FO-07** (S2) No se pide dos veces el mismo dato en un proceso. → [`formularios-inputs.md`](formularios-inputs.md) · WCAG 3.3.7

## Estados

- [ ] **E-01** (S3) Cada vista con datos tiene estados: vacío inicial, sin resultados, cargando, error, parcial, éxito. → [`estados.md`](estados.md) · H1
- [ ] **E-02** (S2) Cargas >300 ms con skeleton de forma real; >10 s con progreso y estimación. → [`estados.md`](estados.md) · H1
- [ ] **E-03** (S3) Errores con causa, si se perdió algo y acción (Reintentar / pedir acceso / soporte). → [`estados.md`](estados.md) · H9
- [ ] **E-04** (S2) Offline o red inestable: banner persistente y cambios en cola. → [`estados.md`](estados.md)

## Feedback

- [ ] **FB-01** (S3) Feedback en <100 ms a toda interacción (pressed, pending). → [`rendimiento-percibido.md`](rendimiento-percibido.md) · H1
- [ ] **FB-02** (S2) Toasts solo para no crítico, duran ≥5 s, se pausan con hover/foco, anunciados con role=status. → [`feedback-notificaciones.md`](feedback-notificaciones.md) · WCAG 4.1.3, WCAG 2.2.1
- [ ] **FB-03** (S3) Ningún modal al cargar; dialog nativo con foco atrapado, Esc y foco de vuelta al cerrar. → [`feedback-notificaciones.md`](feedback-notificaciones.md) · WCAG 2.1.2

## Accesibilidad

- [ ] **A11-01** (S4) Todo operable con teclado; foco visible y no tapado por headers o banners. → [`accesibilidad.md`](accesibilidad.md) · WCAG 2.1.1, WCAG 2.4.7, WCAG 2.4.11
- [ ] **A11-02** (S3) Contraste 4,5:1 texto y 3:1 componentes; color nunca es el único medio. → [`accesibilidad.md`](accesibilidad.md) · WCAG 1.4.3, WCAG 1.4.11, WCAG 1.4.1
- [ ] **A11-03** (S3) HTML semántico; componentes custom con nombre, rol y valor; ARIA solo si no hay nativo. → [`accesibilidad.md`](accesibilidad.md) · WCAG 4.1.2, WCAG 1.3.1
- [ ] **A11-04** (S3) Zoom 200% y reflow a 320 px sin pérdida; prefers-reduced-motion respetado. → [`accesibilidad.md`](accesibilidad.md) · WCAG 1.4.4, WCAG 1.4.10
- [ ] **A11-05** (S3) axe sin violaciones A/AA y una pasada manual con lector de pantalla del flujo crítico. → [`accesibilidad.md`](accesibilidad.md)

## Mobile

- [ ] **M-01** (S3) Objetivos táctiles ≥24 px (principales ≥44 px) y separados. → [`mobile-touch.md`](mobile-touch.md) · WCAG 2.5.8
- [ ] **M-02** (S3) Gestos y arrastres con alternativa de un toque; nada solo al hover. → [`mobile-touch.md`](mobile-touch.md) · WCAG 2.5.1, WCAG 2.5.7
- [ ] **M-03** (S2) Acción primaria al alcance del pulgar; teclado correcto; sin user-scalable=no. → [`mobile-touch.md`](mobile-touch.md) · WCAG 1.4.4

## Copy

- [ ] **C-01** (S2) Botones con verbo + objeto; links que dicen adónde llevan. → [`ux-writing-microcopy.md`](ux-writing-microcopy.md) · WCAG 2.4.4
- [ ] **C-02** (S3) Errores y vacíos con fórmula qué pasó + qué hago; sin jerga, sin culpa, sin 'Algo salió mal'. → [`ux-writing-microcopy.md`](ux-writing-microcopy.md) · H9
- [ ] **C-03** (S2) Terminología consistente; idioma y formatos locales (Intl). → [`ux-writing-microcopy.md`](ux-writing-microcopy.md) · H4, WCAG 3.1.1

## Rendimiento

- [ ] **P-01** (S3) LCP ≤2,5 s, INP ≤200 ms, CLS ≤0,1 en p75 (o presupuesto equivalente en lab con CPU 4×). → [`rendimiento-percibido.md`](rendimiento-percibido.md)
- [ ] **P-02** (S2) Espacio reservado para imágenes, embeds y contenido tardío (sin saltos). → [`rendimiento-percibido.md`](rendimiento-percibido.md)

## Datos

- [ ] **D-01** (S2) KPIs con comparación, período y última actualización; tablas con números a la derecha y tabular-nums. → [`tablas-datos-dashboards.md`](tablas-datos-dashboards.md)

## IA

- [ ] **IA-01** (S3) Si hay IA: capacidades y límites claros, fuentes, Detener, editar/regenerar, contenido marcado. → [`ux-ia.md`](ux-ia.md) · AI-01, AI-04, AI-05, AI-06, AI-07
- [ ] **IA-02** (S4) Si hay agentes: plan visible, permisos mínimos, aprobación antes de lo irreversible, traspaso a humano. → [`ux-ia.md`](ux-ia.md) · AI-08, AI-09

## Ética

- [ ] **ET-01** (S4) Sin patrones oscuros: rechazar = aceptar en esfuerzo, cancelar = contratar, nada pre-tildado con costo, urgencia real. → [`patrones-oscuros-etica.md`](patrones-oscuros-etica.md)
- [ ] **ET-02** (S4) Precio total visible antes del pago (envío, impuestos, fees). → [`checkout-ecommerce.md`](checkout-ecommerce.md)

## Pasadas manuales mínimas

1. **Teclado**: el flujo crítico completo solo con teclado.
2. **320 px y 1440 px**: sin scroll horizontal, nada tapado.
3. **Lector de pantalla**: VoiceOver o NVDA en el flujo crítico.
4. **Red lenta y CPU 4×**: estados de carga y feedback.
5. **Fallos forzados**: API caída, tarjeta rechazada, sin resultados, sin permiso, offline.
6. **Primera vez**: cuenta nueva, sin datos.
7. **Datos extremos**: nombres largos, 0 ítems, 10.000 ítems, traducción más larga.

Checklists detallados: accesibilidad `A-01…A-28` en [`accesibilidad.md`](accesibilidad.md), IA `AI-01…AI-12` en [`ux-ia.md`](ux-ia.md), checkout en [`checkout-ecommerce.md`](checkout-ecommerce.md), mobile en [`mobile-touch.md`](mobile-touch.md).

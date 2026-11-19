---
name: frontend-design
description: "Úsala al construir o rediseñar cualquier sitio web, landing, UI de SaaS, dashboard o componente. Use this skill before writing or restyling any website, landing page, SaaS UI, dashboard, or UI component. Elige un estilo, una paleta, una pareja tipográfica, tokens y un layout (grilla, anchos, patrones) del kit Designweb, define la UX (flujo, estados, formularios, accesibilidad, microcopy) con ux/, y revisa anti-patrones/checklist-revision.md, layout/anti-patrones-layout.md y ux/checklist-ux.md antes de dar la UI por terminada."
---

# Diseño frontend

Antes de escribir o retocar UI, decidí con el kit. No arranques por un componente. La UX (que la persona logre la tarea) pesa más que la terminación visual: si hay conflicto, gana la UX. Las rutas de abajo son relativas a la **raíz del clon de Designweb**, no a esta skill.

## Dónde está el kit

- Si el workspace es el clon, la raíz es ese repo.
- Si estás en otro proyecto, usá la ruta absoluta que el usuario indicó (o la de `CLAUDE.md`). Si no hay ruta, pedila. No inventes paletas, fuentes ni tokens.
- `casos/` está vacío. No fabriques casos.

## a) Clasificar

En una frase: tipo de proyecto (SaaS, landing, dashboard, editorial, devtool, comercio, marca) y mood (técnico, editorial, cálido, quieto, expresivo). Si el usuario ya eligió estilo, paleta o tipo, respetalo.

## b) Elegir

Leé los JSON. Una decisión por eje. El detalle vive en el markdown del slug, no lo copies acá.

1. **Estilo.** En `estilos/estilos.json`, un `slug` cuyo `mejor_para` encaje y cuyo `evitar_en` no contradiga el trabajo. Leé `estilos/<slug>.md` (reglas, “cuándo no”, ejemplos). Uno solo. Un acento de otro estilo solo si la ficha lo permite.
2. **Paleta compatible.** En `paletas/paletas.json`, una paleta cuyo array `estilos` incluya ese slug. Usá los roles de `modos.light.tokens` y `modos.dark.tokens` (`bg`, `surface`, `border`, `text`, `muted`, `accent`, `accent-foreground`, `accent-text`, estados). El color de marca existente se respeta: se arma la rampa alrededor, no se reemplaza. Si el acento duda, leé `paletas/evadir-degrade-violeta.md`.
3. **Pareja tipográfica.** Tomá los ids de `fuentes_recomendadas` del estilo y abrí esas fichas en `tipografias/fonts.json` (`nombre`, `licencia`, `snippet_import`, `pareja_recomendada`). Confirmá titular + cuerpo en `tipografias/pairings.md` según el tipo de proyecto. Dos familias; un mono solo si el producto lo pide. Mostrá licencia e import. En producción, autohospedá.
4. **Tokens.** Escalas en `tokens/tokens.json` y `tokens/escalas.md`. Pegá `tokens/tokens.css` o, si el stack es Tailwind v4, `tokens/theme-tailwind-v4.css`. El color sale de la paleta, no de este archivo. Un radio por proyecto. Una familia de sombra (o ninguna).
5. **Layout.** En `layout/layout.json`, tomá la `receta_por_proyecto` del tipo y elegí de `patrones` **un** hero, 2–3 patrones de sección y **un** gesto (split asimétrico, full-bleed, break de grilla o `canvas-grid`). Leé la ficha en `layout/patrones-layout.md` (el campo `ancla`). Fijá:
   - **Anchos:** tres como máximo (`--layout-content` 42rem, `--layout-wide` 72rem, full) con la grilla de líneas con nombre de `layout/grillas.md`. Párrafos a `--measure` (`65ch`; `34rem` si titular y cuerpo usan familias distintas).
   - **Espacio:** densidad (`espaciado.densidad`) y al menos dos paddings de sección distintos de `--space-section*`. Interno < externo.
   - **Jerarquía:** un foco por vista; contraste de escala alto (editorial, marca) o bajo (producto, docs), no el medio tibio.
   - **Responsive:** primitivos (`primitivos`: stack, center, cluster, sidebar, switcher, grid, frame, reel) y `@container` para componentes; breakpoints de tokens solo para la página. Revisá `soporte_css` antes de usar algo que no sea Baseline.
   Las variables `--layout-*`, `--measure*` y `--space-fluid-*` son propuestas: si el proyecto no las tiene, definilas en `:root` con los valores de `layout/README.md`. El detalle (grillas, proporciones, ritmo, Gestalt) está en `layout/*.md`; no lo copies acá.
6. **Componentes.** En `componentes/componentes.json`, los `patrones` que vas a construir (`archivo`, `estilos_afines`, `error_ia`, `terminacion_pro`). Leé `componentes/<archivo>`. Una librería de `bibliotecas` solo si hace falta; el tema default de shadcn no es una estética.
7. **Motion.** En `animaciones/animaciones.json`, una herramienta y solo las `recetas` de la superficie (`archivo`, `duracion_ms`, `easing`). CSS primero. Leé `animaciones/accesibilidad-performance.md` si hay scroll o entrada. `prefers-reduced-motion` apaga la animación.

Íconos, imagen, grano y OG salen de `recursos/README.md`. No uses Lucide por default.

## b2) Definir la UX

Abrí `ux/ux.json` → `problema_a_archivo` y leé solo los archivos que toca el trabajo (`ux/<archivo>.md`). Fijá:

1. **Flujo.** Persona, tarea y contexto en una frase. Pasos con sus salidas: Atrás (estado en la URL), Cancelar, Deshacer. Reversible → hacer + Deshacer; irreversible → confirmación con verbo + objeto (`ux/feedback-notificaciones.md`).
2. **Estados.** Para cada vista con datos, la matriz de `ux/estados.md`: vacío inicial, sin resultados, cargando (umbrales en `ux.json` → `umbrales.indicador_carga_ms`), error con acción, parcial, éxito proporcional y offline si aplica.
3. **Formularios.** Si hay: campos mínimos, label visible, `type`/`inputmode`/`autocomplete`, validación al enviar (+ on blur con contenido), resumen de errores + error por campo, submit con pending y sin `disabled` para indicar errores, login con passkeys/pegar (`ux/formularios-inputs.md`).
4. **Accesibilidad.** HTML semántico primero (`<button>`, `<a href>`, `<dialog>`, `<details>`, `<label>`), foco visible y no tapado, teclado completo, objetivos ≥ 24 px (44 en táctil principal), nada solo al hover, `prefers-reduced-motion` (`ux/accesibilidad.md`, `ux/mobile-touch.md`).
5. **Microcopy.** Botones verbo + objeto; errores y vacíos con qué pasó + qué hacer, en el idioma del producto (`ux/ux-writing-microcopy.md`). Nada de "Algo salió mal".
6. **Casos especiales** solo si aplican: checkout (`ux/checkout-ecommerce.md`), búsqueda y filtros (`ux/busqueda-filtros.md`), onboarding (`ux/onboarding-activacion.md`), datos (`ux/tablas-datos-dashboards.md`), IA o agentes (`ux/ux-ia.md`), cancelaciones/cookies/precios (`ux/patrones-oscuros-etica.md`).

## c) Brief

Escribí esto, corto, **antes** del código:

```
Tipo y mood:
Estilo: <slug> — por qué, y qué evita
Paleta: <slug> — por qué combina con el estilo
Tipo: <titular> + <cuerpo> — licencia e import
Tokens: radio, sombra, duración base
Layout: hero + patrones de sección + gesto; anchos; densidad; foco
UX: tarea y flujo (salidas); estados que aplican; campos y validación; copy clave
Piezas: patrones y motion que sí entran
No entra: el tell más probable de este proyecto y cómo se corta
```

No reabras el menú en cada componente.

## d) Construir

Aplicá el brief. Construí los estados junto con el ideal, no después; usá los snippets de `ux/` como base. Nombres de token (`var(--space-6)`, radio y duración del sistema), no hex, `px` o `duration-1000` sueltos. Un acento sólido. Prueba real cerca del inicio (precio, nombre, horario, captura del producto). Meta, alt, favicon y OG no salen de la plantilla.

## e) Revisar

Pasá `anti-patrones/checklist-revision.md` y el checklist de `layout/anti-patrones-layout.md`. Cada “sí” es un tell. Con tres o más, arreglá antes de cerrar, usando `como_arreglar` en `anti-patrones/catalogo.md`, el slug en `anti-patrones/anti-patrones.json` o el `L-*` en `layout/anti-patrones-layout.md`. Probá a 320 px y a 1440 px: sin scroll horizontal, medida ≤ ~75 caracteres, un foco al desenfocar. No respondas “hacelo más único”.

Después pasá `ux/checklist-ux.md` (ids y severidad 0–4 también en `ux/ux.json` → `checklist`) y los `UX-*` de `ux/anti-patrones-ux.md`. Reportá los ids que fallan con su severidad (`FO-03 ✗ S4`). Un S4 bloquea; con dos o más S3, arreglá antes de cerrar. Probá el flujo crítico solo con teclado y forzá los fallos (API caída, sin resultados, sin permiso).

Salvo brief explícito, no uses Inter, Geist, Roboto, Poppins, Montserrat o Instrument Serif como voz principal, ni índigo, violeta o degradé `from-indigo-* to-purple-*` como identidad. El resto de las prohibiciones está en `anti-patrones/reglas-para-agentes.md`.

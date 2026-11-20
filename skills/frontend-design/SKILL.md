---
name: frontend-design
description: "Úsala al construir, rediseñar, restylear o auditar cualquier sitio web, landing, UI de SaaS, dashboard o componente. Use this skill before writing, restyling or reviewing any website, landing page, SaaS UI, dashboard, or UI component. Tiene tres modos: nuevo (elige estilo, paleta, tipografía, tokens, layout y UX del kit Designweb y construye), restyling (solo lo visual de una UI existente: tokens, tipo, color, espacio, radio, sombra y motion, sin tocar estructura, textos, props ni lógica, con diffs inmediatos) y auditoria (solo revisa contra los checklists y reporta)."
---

# Diseño frontend

Las rutas son relativas a la **raíz del clon de Designweb**, no a esta skill. La UX (que la persona logre la tarea) pesa más que la terminación visual.

## 0. Elegí el modo (antes que nada)

| Modo | Cuándo | Qué entrega |
|---|---|---|
| `nuevo` | Pantalla, página o componente que todavía no existe, o el usuario pide rehacerlo entero | Código nuevo, con el flujo completo de abajo |
| `restyling` | Ya existe y el pedido es visual: "rediseño sin tocar interfaces", "solo lo visual", "que se vea mejor", "pulilo", "cambiale el estilo", "restyling" | **Diffs** en tema, CSS y `className`. Nada de estructura, textos, props, lógica, rutas ni APIs |
| `auditoria` | "Revisá", "auditá", "qué tiene de IA", "qué le falla", sin pedido de cambios | Un reporte con ids y severidad. No edita archivos |

- Si el pedido menciona código existente y duda entre `nuevo` y `restyling`, elegí `restyling`.
- No preguntes el modo: decilo en una línea (`Modo: restyling`) y arrancá. Si el usuario lo nombra, gana el usuario.

## Reglas para los tres modos

- **Kit.** Si el workspace es el clon, la raíz es ese repo. Si no, usá la ruta del usuario o del `CLAUDE.md`. Sin ruta: en `nuevo`, pedila; en `restyling` y `auditoria`, seguí con las reglas de esta skill y avisalo en el reporte.
- **No leas JSON grandes enteros.** `paletas/paletas.json` (~390 KB) y `tipografias/fonts.json` (~135 KB) se consultan con `jq` o `rg` por slug. Para elegir, alcanza con [`indice-rapido.json`](../../indice-rapido.json).
- `casos/` todavía no tiene casos reales. No los inventes. No inventes paletas, fuentes, datos ni testimonios.
- La marca existente (logo, color o fuente que no sea un default) se conserva y se arma alrededor.
- Si el proyecto tiene un `DESIGN.md` en la raíz, leelo primero y respetalo (no cuenta para el límite de archivos del kit). Si no tiene y la sesión fija tokens, proponé crearlo con [`casos/plantilla-design-md.md`](../../casos/plantilla-design-md.md).

## Modo restyling

Procedimiento completo, tabla de "qué es tocar interfaces" y comandos por stack: [`restyling.md`](restyling.md). Resumen:

1. **Kit: máximo 3 archivos.** `indice-rapido.json`, el bloque CSS de una paleta (sección de `paletas/<familia>.md` o `jq` por slug) y `tokens/theme-tailwind-v4.css` o `tokens/tokens.css`.
2. **Stack: máximo 10 lecturas.** Tailwind v3 (`tailwind.config.*`), v4 (`@theme` en el CSS), shadcn (variables en `globals.css`), CSS Modules, styled-components/Emotion (`theme`), MUI/Chakra/Mantine (`createTheme`). Captura de **antes** si el dev server levanta.
3. **Brief de 5 líneas** (modo, dirección, estilo + paleta, tipo, cambios). **No pidas aprobación**: el pedido ya es la aprobación.
4. **Editá enseguida.** Primer diff antes de la llamada a herramienta n.º 20. Pasadas en orden: tokens → tipo → color → espacio → radio/sombra → clases de componentes → pulido de layout → motion. Un commit chico por pasada (`style(tokens): …`).
5. **Verificá.** Build o `tsc --noEmit`, capturas después a 1440 y 390 px, y el diff de `.tsx/.jsx` solo con cambios de clase.
6. **Reportá.** Los checklists visuales, de layout y los ítems visuales de UX se pasan **después** y van como informe. No bloquean. Lo que exige tocar estructura o copy va como sugerencia con archivo y cambio exacto.

**Nunca termines una sesión de restyling sin diffs.** Si algo bloquea, dejá al menos el diff seguro (tokens de color y tipo) y explicá el bloqueo.

## Modo auditoria

1. Abrí la UI (captura si se puede) y los archivos que la renderizan. No edites.
2. Pasá `anti-patrones/checklist-revision.md` (incluye las pasadas en orden), el checklist de `layout/anti-patrones-layout.md` y `ux/checklist-ux.md`.
3. Reportá cada falla con su id (`slug` de `anti-patrones/anti-patrones.json`, `L-*`, `UX-*` o el id del checklist UX), dónde está (archivo y línea), severidad 0–4 y el arreglo en una línea. Cerrá con el triage: **mucho slop** → `nuevo` o restyling completo; **poco** → restyling solo de lo marcado; **nada** → decilo y proponé dos o tres ajustes con valores exactos. El triage sale de [unslop](https://github.com/heydamir/unslop) (CC BY 4.0).

## Modo nuevo

### n1) Clasificar

En una frase: tipo de proyecto (SaaS, landing, dashboard, editorial, devtool, comercio, marca) y mood (técnico, editorial, cálido, quieto, expresivo). Si el usuario ya eligió estilo, paleta o tipo, respetalo.

### n2) Elegir

Elegí con `indice-rapido.json` y después abrí solo la ficha elegida (en `paletas.json` y `fonts.json`, con `jq` por slug). Una decisión por eje. El detalle vive en el markdown del slug, no lo copies acá.

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

### n3) Definir la UX

Abrí `ux/ux.json` → `problema_a_archivo` y leé solo los archivos que toca el trabajo (`ux/<archivo>.md`). Fijá:

1. **Flujo.** Persona, tarea y contexto en una frase. Pasos con sus salidas: Atrás (estado en la URL), Cancelar, Deshacer. Reversible → hacer + Deshacer; irreversible → confirmación con verbo + objeto (`ux/feedback-notificaciones.md`).
2. **Estados.** Para cada vista con datos, la matriz de `ux/estados.md`: vacío inicial, sin resultados, cargando (umbrales en `ux.json` → `umbrales.indicador_carga_ms`), error con acción, parcial, éxito proporcional y offline si aplica.
3. **Formularios.** Si hay: campos mínimos, label visible, `type`/`inputmode`/`autocomplete`, validación al enviar (+ on blur con contenido), resumen de errores + error por campo, submit con pending y sin `disabled` para indicar errores, login con passkeys/pegar (`ux/formularios-inputs.md`).
4. **Accesibilidad.** HTML semántico primero (`<button>`, `<a href>`, `<dialog>`, `<details>`, `<label>`), foco visible y no tapado, teclado completo, objetivos ≥ 24 px (44 en táctil principal), nada solo al hover, `prefers-reduced-motion` (`ux/accesibilidad.md`, `ux/mobile-touch.md`).
5. **Microcopy.** Botones verbo + objeto; errores y vacíos con qué pasó + qué hacer, en el idioma del producto (`ux/ux-writing-microcopy.md`). Nada de "Algo salió mal".
6. **Casos especiales** solo si aplican: checkout (`ux/checkout-ecommerce.md`), búsqueda y filtros (`ux/busqueda-filtros.md`), onboarding (`ux/onboarding-activacion.md`), datos (`ux/tablas-datos-dashboards.md`), IA o agentes (`ux/ux-ia.md`), cancelaciones/cookies/precios (`ux/patrones-oscuros-etica.md`).

### n4) Dirección y brief

Primero la **dirección**, en cinco líneas derivadas del producto, nunca de la moda (formato adaptado de [unslop](https://github.com/heydamir/unslop), Damir Sokolovsky, CC BY 4.0):

- **Producto:** qué hace y para quién, en una frase.
- **Carácter:** dos o tres palabras concretas. "Limpio", "moderno", "elegante" o "premium" no valen: describen cualquier plantilla.
- **Mundo:** el lugar o material del rubro (una farmacia: mostrador, receta, blíster; un monitoreo: instrumentos, guardia nocturna). Tiñe neutros, acento e imagen.
- **Momento:** uno o dos lugares donde va la riqueza (una captura real, un gráfico, un objeto). El resto, quieto.
- **Firma:** un detalle que solo este producto tendría, usado siempre igual.

Después el brief, corto, **antes** del código:

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

Revisá el brief contra el pedido antes de construir: si una línea es lo que harías para cualquier proyecto parecido, cambiala y decí por qué (idea de la skill oficial [`frontend-design` de Anthropic](https://github.com/anthropics/skills/tree/main/skills/frontend-design), Apache 2.0). No reabras el menú en cada componente.

### n5) Construir

Aplicá el brief. Construí los estados junto con el ideal, no después; usá los snippets de `ux/` como base. Nombres de token (`var(--space-6)`, radio y duración del sistema), no hex, `px` o `duration-1000` sueltos. Un acento sólido. Prueba real cerca del inicio (precio, nombre, horario, captura del producto). Meta, alt, favicon y OG no salen de la plantilla. Gastá la audacia en **un** lugar y dejá el resto disciplinado. Cuidá la especificidad del CSS: una clase por tipo de sección y otra por elemento suelen pisarse en paddings y márgenes.

### n6) Revisar

Pasá `anti-patrones/checklist-revision.md` y el checklist de `layout/anti-patrones-layout.md`. Cada "sí" es un tell. Con tres o más, arreglá antes de cerrar, usando `como_arreglar` en `anti-patrones/catalogo.md`, el slug en `anti-patrones/anti-patrones.json` o el `L-*` en `layout/anti-patrones-layout.md`. Probá a 320 px y a 1440 px: sin scroll horizontal, medida ≤ ~75 caracteres, un foco al desenfocar. Antes de entregar, sacá un adorno. No respondas "hacelo más único".

Después pasá `ux/checklist-ux.md` (ids y severidad 0–4 también en `ux/ux.json` → `checklist`) y los `UX-*` de `ux/anti-patrones-ux.md`. Reportá los ids que fallan con su severidad (`FO-03 ✗ S4`). En modo `nuevo`, un S4 bloquea; con dos o más S3, arreglá antes de cerrar. Probá el flujo crítico solo con teclado y forzá los fallos (API caída, sin resultados, sin permiso).

Salvo brief explícito, no uses Inter, Geist, Roboto, Poppins, Montserrat o Instrument Serif como voz principal, ni índigo, violeta o degradé `from-indigo-* to-purple-*` como identidad. El resto de las prohibiciones está en `anti-patrones/reglas-para-agentes.md`.

## Ejemplos de prompt

**Restyling** (listo para pegar; cambiá la ruta del clon y la carpeta):

```
Usá la skill frontend-design en modo restyling. El kit Designweb está en <RUTA_AL_CLON>.
Rediseñá solo lo visual de <CARPETA_O_PANTALLA, p. ej. src/app>: tipografía, colores, espaciado,
radios, sombras, motion y pulido de layout. No cambies la estructura, los textos, las props,
la lógica, las rutas ni las APIs de los componentes.
Leé como máximo 3 archivos del kit (empezá por indice-rapido.json), detectá dónde viven los estilos,
escribí un brief de 5 líneas y aplicá los cambios enseguida en el tema, el CSS global y los className,
con un commit chico por pasada. No me pidas aprobación del brief y no termines sin diffs.
Al final corré el build, sacá capturas a 1440 y 390 px y pasame el checklist como reporte, con lo que
quede fuera de alcance como sugerencias.
```

**Nuevo:** `Usá la skill frontend-design en modo nuevo. El kit Designweb está en <RUTA_AL_CLON>. Armá <la landing / el dashboard> de <producto, para quién>. Seguí el flujo completo y mostrame el brief antes del código.`

**Auditoría:** `Usá la skill frontend-design en modo auditoria sobre <CARPETA>. El kit está en <RUTA_AL_CLON>. No edites nada: reportá cada tell con id, archivo, severidad y arreglo, y cerrá con el triage.`

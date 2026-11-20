# Modo restyling: el procedimiento completo

Este archivo es el detalle del modo `restyling` de [`SKILL.md`](SKILL.md). Las rutas del kit son relativas a la **raíz del clon de Designweb**; las rutas del proyecto, a la raíz del proyecto que se rediseña.

Restyling quiere decir **cambiar cómo se ve sin cambiar qué es**: tipografía, color, espaciado, radio, borde, sombra, motion y pulido de layout. La estructura, los textos y el comportamiento quedan igual. El resultado de una sesión de restyling es **un diff**, no un plan.

## Por qué existe este modo

En noviembre de 2026 un pedido de "rediseño sin tocar ni cambiar las interfaces" terminó en 25 minutos de trabajo y cero cambios. Las causas probables, en orden:

1. **Leer de más.** `paletas/paletas.json` pesa ~390 KB y `tipografias/fonts.json` ~135 KB. Leerlos enteros se come el contexto y el tiempo antes del primer cambio. En restyling se consulta con `jq`/`rg`, nunca entero.
2. **Brief y revisión como portones.** El flujo `nuevo` pide brief, revisión de UX y bloquea con un S4. En restyling el checklist es un **reporte posterior**, no un portón.
3. **Ambigüedad de "no tocar interfaces".** Leída al pie de la letra, impide todo. Acá está definida (ver abajo): las interfaces son la estructura, los textos y las APIs, no los estilos.
4. **Esperar aprobación.** Skills como unslop proponen mostrar la dirección y esperar; en restyling **no se espera**: el pedido ya es la aprobación.
5. **Sin ruta del kit.** Si no hay ruta, se sigue con `tokens/` y reglas generales del proyecto, y se avisa en el reporte. No se frena.

## Qué cuenta como "tocar interfaces"

| Se puede (es estilo) | No se puede (es interfaz) | Zona gris: se decide así |
|---|---|---|
| Valores de tokens y variables CSS (`--primary`, `--radius`, `@theme`) | Agregar, quitar o reordenar elementos, secciones o rutas | Íconos: tamaño, trazo y color sí; cambiar de set o de ícono, no |
| `className` de color, tipo, espaciado, radio, sombra, borde, transición | Cambiar textos, labels, placeholders, `alt` o mensajes | `grid-cols-*`, `flex-*`, `gap`, `max-w-*` dentro del mismo contenedor: sí, si el orden del DOM no cambia |
| Imports y `@font-face` de fuentes; `font-feature-settings`; `text-wrap` | Props, nombres de componentes, exports, tipos, firmas de funciones | Variantes de un componente (`variant="ghost"`): solo si la variante ya existe y la prop ya se usa así |
| Estados visuales: `:hover`, `:focus-visible`, `:active`, `disabled` visual | Lógica, handlers, estado, data fetching, validación | Imágenes: `object-fit`, ratio y recorte sí; reemplazar la imagen, no |
| `prefers-reduced-motion`, duraciones y easings | `aria-*`, roles, orden de tabulación, URLs | Arreglos de accesibilidad visual (contraste, foco visible, tamaño de objetivo) sí; cambios de semántica se anotan como sugerencia |
| Modo oscuro vía variables (`.dark`, `[data-theme]`) | APIs de componentes de librería (no editar `node_modules` ni reescribir `ui/*` de shadcn más allá de clases) | Un wrapper nuevo solo para estilo: no; se resuelve con clases en el elemento existente |

La regla de fondo es la del `polish` de [impeccable](https://github.com/pbakaus/impeccable) (Apache 2.0): pulir es refinar, nunca un rediseño escondido. Si el concepto está mal, se dice y se recomienda `nuevo`; no se cuela un reemplazo.

Si algo del pedido necesita tocar la interfaz (por ejemplo, el hero no se arregla sin mover un bloque), **no lo hagas**: anotalo en el reporte como sugerencia con el archivo y el cambio exacto.

## Presupuesto

| Paso | Tope | Sale con |
|---|---|---|
| 1. Kit | 3 archivos del kit | estilo, paleta y pareja elegidos |
| 2. Stack | 10 lecturas o búsquedas del proyecto | dónde viven los estilos |
| 3. Brief | 5 líneas, sin preguntar | el brief escrito en el chat |
| 4. Editar | primer diff antes de la llamada a herramienta n.º 20 (o ~10 min) | commits pequeños |
| 5. Verificar | 3 renders como máximo | capturas y build OK |
| 6. Reporte | checklist como informe | lista de lo hecho y sugerencias |

Si se acaba el presupuesto de un paso, seguí con lo que tenés. **Nunca termines una sesión de restyling sin diffs.** Si algo bloquea de verdad (no compila, no hay estilos editables), igual dejá el diff mínimo seguro (tokens de color y tipo) y explicá el bloqueo.

## Paso 1. El kit (máximo 3 archivos)

1. [`indice-rapido.json`](../../indice-rapido.json): estilos, paletas y fuentes resumidos (slug, mood, para qué, hex principales). Es el único que se lee entero.
2. El bloque CSS de **una** paleta: `rg -n "^## " paletas/<familia>.md` y después leé solo esa sección, o `jq '.paletas[] | select(.slug=="<slug>") | .modos' paletas/paletas.json`.
3. [`tokens/theme-tailwind-v4.css`](../../tokens/theme-tailwind-v4.css) si el stack es Tailwind v4, si no [`tokens/tokens.css`](../../tokens/tokens.css).

Para la fuente, `jq '.fuentes[] | select(.id=="<id>") | {nombre,licencia,snippet_import}' tipografias/fonts.json` no cuenta como lectura entera. Si el proyecto ya tiene marca (logo, color, fuente que no sea un default), **se conserva**: el color de marca pasa a ser el acento y se arma la rampa alrededor.

## Paso 2. Dónde viven los estilos (por stack)

Primero `cat package.json` y una búsqueda:

```bash
rg -l --hidden -g '!node_modules' -e '@import "tailwindcss"' -e '@tailwind base' -e '@theme' -e 'createTheme' -e 'ThemeProvider' -e 'styled\.' .
ls tailwind.config.* components.json postcss.config.* 2>/dev/null
```

| Stack | Cómo se reconoce | Dónde se edita | Cuidado |
|---|---|---|---|
| Tailwind v3 | `tailwind.config.{js,ts,cjs}`, `@tailwind base` en el CSS global | `theme.extend` (colors, fontFamily, borderRadius, boxShadow, transitionTimingFunction) y el CSS global | No reemplaces `theme` entero: se pierden las clases que ya se usan. Extendé o redefiní solo las claves que usás |
| Tailwind v4 | `@import "tailwindcss"` y `@theme { … }` en `app.css`/`globals.css`, sin config | El bloque `@theme` (`--color-*`, `--font-*`, `--radius-*`, `--shadow-*`, `--ease-*`) | `@theme inline` cuando el token apunta a otra variable (patrón de shadcn v4) |
| shadcn/ui | `components.json`, `components/ui/*`, variables `--background`, `--primary`… en `globals.css` | `:root` y `.dark` en `globals.css`; `--radius` | Ver la tabla de mapeo de abajo. No reescribas los componentes de `ui/`; como mucho ajustá clases |
| CSS Modules | `*.module.css` junto a cada componente | Los **valores** dentro de cada módulo y variables nuevas en `:root` global | Los nombres de clase son API (se importan en el TSX): no los renombres |
| styled-components / Emotion | `ThemeProvider`, `theme.ts`, ``styled.div`…` `` | El objeto `theme` y los literales dentro de los templates, reemplazados por `${({theme}) => theme.…}` | No renombres los componentes exportados ni cambies sus props |
| CSS / SCSS plano | `styles.css`, `_variables.scss`, `:root` | Variables y reglas existentes | Bajá especificidad en vez de sumar `!important` |
| MUI / Chakra / Mantine | `createTheme`, `extendTheme`, `MantineProvider` | `palette`, `typography`, `shape.borderRadius`, `shadows`, `components.*.styleOverrides` | Cambiá el tema, no cada `sx` suelto |

Mapeo de roles del kit a las variables de shadcn/ui (en OKLCH, como usa shadcn desde Tailwind v4):

| Kit | shadcn |
|---|---|
| `bg` | `--background` |
| `text` | `--foreground`, `--card-foreground`, `--popover-foreground` |
| `surface` | `--card`, `--popover`, `--muted`, `--secondary` |
| `muted` | `--muted-foreground` |
| `border` | `--border`, `--input` |
| `accent` / `accent-foreground` | `--primary` / `--primary-foreground`, `--ring` |
| `surface` + `text` | `--accent` / `--accent-foreground` (el "accent" de shadcn es el hover de menú, no la marca) |
| `danger` | `--destructive` |

Antes de editar, levantá el dev server y sacá las capturas de **antes** (ver paso 5). Si no levanta en 2 intentos, seguí sin capturas y anotalo.

Para encontrar lo que no pasa por tokens:

```bash
rg -n --glob '!node_modules' '#[0-9a-fA-F]{3,8}\b' src app components
rg -n --glob '!node_modules' 'from-(indigo|purple|violet)|bg-clip-text|animate-pulse|rounded-(2xl|3xl)|shadow-(xl|2xl)|duration-1000|transition-all' src app components
rg -n --glob '!node_modules' 'font-family|fontFamily|Inter|Geist|Poppins' src app components
```

## Paso 3. Brief de 5 líneas (no se pide aprobación)

```
Modo: restyling — no cambio estructura, textos, props, lógica ni rutas
Dirección: <producto en una frase>; carácter en 2–3 palabras concretas (no "limpio", "moderno", "premium")
Estilo + paleta: <slug> + <slug> (o la marca existente como acento)
Tipo: <titular> + <cuerpo> — licencia; escala y pesos
Cambios: tokens → tipo → color → espacio → radio/sombra → clases → motion; lo que NO entra
```

Escribilo y seguí en el mismo turno. Si el usuario quiere otra dirección, lo dirá sobre el diff.

## Paso 4. Editar en pasadas, con commits pequeños

El orden sigue la lógica de las pasadas de [unslop](https://github.com/heydamir/unslop) (Damir Sokolovsky, CC BY 4.0), recortada a lo que el restyling permite: copy, íconos e imágenes quedan fuera.

1. **Tokens y tema.** Pegá los roles de la paleta y las escalas del kit en el lugar del paso 2. Mapeá a las variables que ya existen; no inventes nombres nuevos si el proyecto ya tiene `--primary`. Commit: `style(tokens): paleta <slug> y escalas`.
2. **Tipografía.** Fuente (import + `font-family` en el tema), escala, dos pesos (400/500, 600 para énfasis raro), interlineado, `text-wrap: balance` en títulos y `pretty` en párrafos, `tabular-nums` en cifras, nada de tracking negativo en texto chico. Commit: `style(type): …`.
3. **Color.** Reemplazá hex sueltos por roles. Un acento sólido; sin degradés de matiz, texto en degradé, glows ni sombras de color. Bordes a 6–10 % del texto. Contraste ≥ 4.5:1 en cuerpo. Commit: `style(color): …`.
4. **Espacio.** Todo en la grilla de 4 px y en la escala; igual cosa, igual medida; adentro < afuera; fuera los `mt-[13px]`. Commit: `style(spacing): …`.
5. **Radio, borde y sombra.** Un radio por tipo de control; radios anidados que suman (radio exterior = interior + padding); una familia de sombra o ninguna; en oscuro, profundidad con superficies, no con sombras. Commit: `style(shape): …`.
6. **Detalles por componente.** Clases de botones, inputs, cards, tablas y navegación: estados hover, `:focus-visible` (2 px, contraste 3:1), `active`, filas de tabla distinguibles. Solo `className`/estilos. Commit: `style(components): …`.
7. **Pulido de layout.** Medida de párrafo (`max-width: 65ch`), anchos, alineación a una columna, alturas de fila iguales, `gap` coherente. Sin mover nodos del DOM. Commit: `style(layout): …`.
8. **Motion.** Una curva de salida del kit, 150–250 ms en UI, sin bounce ni loops, `prefers-reduced-motion` apagando todo lo no esencial; fuera `transition-all`. Commit: `style(motion): …`.

Si no hay git, llevá la lista de archivos tocados por pasada. Si una pasada no tiene nada que cambiar, decilo en una línea y seguí.

## Paso 5. Verificar

```bash
npm run dev            # o pnpm/yarn/bun; anotá la URL (5173 es la de Vite, 3000 la de Next)
npx playwright screenshot --viewport-size="1440,900" http://localhost:5173 antes-1440.png   # antes del paso 4
npx playwright screenshot --viewport-size="390,844"  http://localhost:5173 antes-390.png
# …pasadas…
npx playwright screenshot --viewport-size="1440,900" http://localhost:5173 despues-1440.png
npx playwright screenshot --viewport-size="390,844"  http://localhost:5173 despues-390.png
npm run build || npx tsc --noEmit
```

Comprobá que el diff es solo de estilo:

```bash
git diff --stat
git diff -U0 -- '*.tsx' '*.jsx' '*.vue' '*.svelte' | rg '^[+-][^+-]' | rg -v 'class(Name)?=|className|style=|cn\(|clsx\(|tw`'
```

La segunda línea tiene que salir vacía o casi: cada línea que quede es un cambio que no es de estilo y hay que revisarlo o revertirlo. Mirá las capturas antes y después a 1440 y 390 px (320 si hay tiempo): sin scroll horizontal, sin texto cortado, foco visible.

Opcional, si el proyecto tiene Node: `npx impeccable detect src/` y `npx impeccable detect http://localhost:5173` (detector determinístico de 62 reglas, sin LLM; las de contraste y tamaño necesitan la URL). Sus hallazgos van al reporte; no reabren el trabajo.

## Paso 6. Reporte (el checklist informa, no bloquea)

Pasá, sin frenar el trabajo ya hecho:

- [`anti-patrones/checklist-revision.md`](../../anti-patrones/checklist-revision.md) y el checklist de [`layout/anti-patrones-layout.md`](../../layout/anti-patrones-layout.md).
- De [`ux/checklist-ux.md`](../../ux/checklist-ux.md), solo los ítems visuales: contraste, foco visible, objetivos táctiles, reduced-motion.

Formato del reporte:

```
Hecho: <commits o archivos por pasada>
Tells que quedan: <slug> — por qué no se arregló (necesita tocar estructura/copy)
Sugerencias fuera de alcance: <archivo> — <cambio exacto> — por qué
Verificación: build OK/KO; capturas <rutas>; diff solo-estilo OK/KO
```

## Errores típicos de este modo

- Leer `paletas.json` o `fonts.json` enteros.
- Escribir el brief y quedarse esperando un "dale".
- Reescribir un componente "para que quede más limpio": eso es `nuevo`, no `restyling`.
- Cambiar textos porque el checklist marcó copy de hype: va al reporte como sugerencia.
- Reemplazar un tell por otra moda (vidrio, grano, neón, bento): la dirección sale del producto, no de la tendencia (regla tomada de unslop).
- Terminar con "propuesta de cambios" y ningún archivo modificado.

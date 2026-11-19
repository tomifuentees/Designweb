# Layout: disposición, proporción y composición

Cómo se **arma** una página: grillas, proporciones, espacio, jerarquía, responsive y patrones de sección. Los tokens fijan valores; esta carpeta fija **criterio** para usarlos. Es lo que [`../tokens/escalas.md`](../tokens/escalas.md#lo-que-esta-carpeta-no-resuelve) dice que no resuelve: el muro de tres cards, el hero centrado genérico, el padding igual en todo.

Foto del 19 de noviembre de 2026. Soporte de navegadores tomado de [web-features](https://web-platform-dx.github.io/web-features-explorer/) 3.46.0 y [caniuse](https://caniuse.com/).

## Qué hay acá

| Archivo | Contenido |
|---|---|
| [grillas.md](./grillas.md) | Tipos de grilla (columnas, modular, baseline, asimétrica), 12/8/4, romper la grilla; CSS Grid con líneas con nombre, áreas, subgrid, RAM, `grid-lanes` y quantity queries |
| [proporciones.md](./proporciones.md) | Proporción áurea (evidencia y mito), escalas modulares, medida de línea, anchos de contenedor, ratios de imagen, splits |
| [espaciado-ritmo.md](./espaciado-ritmo.md) | 4/8 pt, proximidad (interno ≤ externo), ritmo vertical, padding de sección, densidad |
| [jerarquia-composicion.md](./jerarquia-composicion.md) | Escala, contraste, agrupación; F, layer-cake y Z con su evidencia; punto focal, alineación, equilibrio, Gestalt |
| [responsive-fluido.md](./responsive-fluido.md) | Diseño intrínseco, `clamp()`, container queries, los primitivos de Every Layout en CSS moderno |
| [patrones-layout.md](./patrones-layout.md) | 19 patrones con wireframe ASCII, proporción, CSS / Tailwind v4 y el error de la IA |
| [anti-patrones-layout.md](./anti-patrones-layout.md) | 18 tells de composición (`L-*`) y checklist de layout |
| [layout.json](./layout.json) | Lo mismo, machine-readable, para la skill |
| [fuentes-investigacion.md](./fuentes-investigacion.md) | Fuentes, con links y fechas |

## Cómo usarlo desde un agente

1. Decidí el **tipo de página** y elegí en `layout.json` → `patrones` un hero, 2–3 patrones de sección y **un** gesto.
2. Fijá **tres anchos** (`content`, `wide`, `full`) y la grilla de página con líneas con nombre ([grillas.md](./grillas.md#21-la-grilla-de-página-con-líneas-con-nombre-full-bleed)).
3. Elegí **densidad** (compacto, cómodo, aireado) y **dos o tres** paddings de sección de `--space-section*`.
4. Decidí la **actitud de escala** (contraste alto o bajo) y el **foco** de cada vista.
5. Construí con primitivos (Stack, Center, Cluster, Sidebar, Switcher, Grid, Frame, Reel) y container queries antes que con breakpoints sueltos.
6. Pasá el checklist de [anti-patrones-layout.md](./anti-patrones-layout.md#checklist-de-layout).

## Propuestas para tokens

Esta carpeta **no modifica** [`../tokens/`](../tokens/README.md). Estas variables se usan en los snippets de acá; si se aprueban, se suman a `tokens.css`, `theme-tailwind-v4.css` y `tokens.json`:

| Variable | Valor | Equivale a | Por qué |
|---|---|---|---|
| `--layout-content` | `42rem` | `--container-2xl` de Tailwind | Columna de contenido (artículo, formularios, FAQ); el párrafo adentro se limita con `--measure` |
| `--layout-wide` | `72rem` | `--container-6xl` | Secciones con grilla |
| `--layout-gutter` | `var(--space-4)` → `var(--space-6)` desde `md` | Margen de M3 (16 / 24) | Margen lateral |
| `--measure` | `65ch` | `max-w-prose` de Tailwind | Medida con una sola familia de texto |
| `--measure-mixed` | `34rem` | ~`34em` de Baymard | Medida cuando titular y cuerpo usan familias distintas |
| `--space-fluid-gutter` | `clamp(1rem, 0.6522rem + 1.7391vw, 2rem)` | 16 → 32 | Gutter fluido (viewport 320–1240) |
| `--space-fluid-block` | `clamp(2rem, 1.3043rem + 3.4783vw, 4rem)` | 32 → 64 | Espacio entre bloques de una sección |
| `--space-fluid-section` | `clamp(4rem, 2.6087rem + 6.9565vw, 8rem)` | 64 → 128 | Padding de sección fluido (alternativa a `--space-section*`) |

Ninguna contradice las escalas existentes: los anchos son pasos de la escala `--container-*` de Tailwind v4 y los pares fluidos interpolan entre pasos de `--space-*`.

## Relación con otras carpetas

- [`../estilos/`](../estilos/README.md): `bento-grids`, `grilla-rota`, `editorial-revista`, `suizo-internacional` y `scrollytelling` son estéticas; acá está la geometría que las sostiene.
- [`../componentes/`](../componentes/README.md): contenido y terminación de hero, pricing, dashboards, FAQ, etc. Acá, su disposición.
- [`../anti-patrones/`](../anti-patrones/README.md): los tells generales; acá, los de composición.

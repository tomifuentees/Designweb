# Grillas

Una grilla no es "12 columnas". Es la decisión de **cuántos anchos distintos existen en la página** y cómo se relacionan. Müller-Brockmann la define como la división de un plano en campos más chicos, iguales o distintos, donde los elementos se ajustan a esos campos ([*Grid Systems in Graphic Design*, 1981, texto en archive.org](https://archive.org/stream/GridSystemsInGraphicDesignJosefMullerBrockmann/Grid%20systems%20in%20graphic%20design%20-%20Josef%20Muller-Brockmann_djvu.txt)). En web, además, la grilla tiene que **ceder**: el ancho no es fijo.

Los valores de espacio salen de [`../tokens/`](../tokens/README.md) (`--space-*`, breakpoints de Tailwind v4). Acá no se inventan pasos nuevos.

## 1. Tipos de grilla y cuándo usar cada una

| Tipo | Qué es | Cuándo | Cuándo no |
|---|---|---|---|
| **Una columna (manuscrito)** | Un bloque de texto con medida controlada | Artículo, docs, legal, changelog | Catálogo, dashboard |
| **Columnas (12 / 8 / 4)** | N columnas iguales con gutter fijo; los bloques ocupan *spans* | Landing, marketing, sitios con muchos tipos de bloque | Cuando todo termina en `span 4` + `span 4` + `span 4` (eso es el tell, no la grilla) |
| **Modular** | Columnas + filas: campos (módulos) | Catálogo, bento, galería, revista | Contenido de altura impredecible |
| **Jerárquica / asimétrica** | Anchos distintos por intención (ej. 5/7, 4/8, 2/10, 1fr 2fr) | Editorial, portfolio, hero con texto + prueba | Formularios largos |
| **Baseline** | Ritmo vertical fijo para el texto | Lectura larga, editorial impreso | UI densa de producto (se rompe con íconos, inputs) |
| **Compuesta** | Dos grillas superpuestas (ej. 12 y 5) | Revista, estudio, dirección de arte | Si no hay director de arte que la sostenga |

### 12 / 8 / 4 en la práctica

El patrón de diseño de sistemas grandes es **4 columnas en móvil, 8 en tablet, 12 (o 16) en desktop**:

- **Material 3** trabaja por *window size classes* y panes, no por columnas: compacto < 600 dp (1 pane, margen 16), medio 600–839 (margen 24), expandido 840–1199 (2 panes, margen y separador 24), grande 1200–1599, extra grande ≥ 1600 ([M3 Breakpoints](https://m3.material.io/foundations/layout/breakpoints)).
- **IBM Carbon** usa la "2x Grid" de 16 columnas: sm 320 px (4 col), md 672 (8), lg 1056 (16), xlg 1312 (16), max 1584 (16) ([Carbon 2x Grid](https://www.carbondesignsystem.com/building-blocks/foundations/2x-grid/overview)).
- **Este kit**: breakpoints de Tailwind v4 (`sm` 40 rem, `md` 48, `lg` 64, `xl` 80, `2xl` 96; ver [`../tokens/escalas.md`](../tokens/escalas.md#breakpoints)). Mapeo sugerido: 4 col < `md`, 8 col `md`–`lg`, 12 col ≥ `lg`. Margen lateral `--space-4` (16 px) en móvil y `--space-6` (24 px) desde `md`, que coincide con M3.

Lo importante no es el número de columnas: es que los *spans* usados sean **pocos y repetidos** (por ejemplo, solo 12, 7/5 y 4/4/4 en toda la landing) y que al menos un bloque los combine de forma no obvia.

### Romper la grilla (con criterio)

El estilo [`grilla-rota`](../estilos/grilla-rota.md) ya lo cubre como estética. Como regla de layout: **rompé una sola cosa por composición** (un titular que entra en el margen, una imagen a sangre, un módulo desplazado) y que la grilla siga siendo visible en el resto. Si todo se sale, no hay grilla que romper.

## 2. CSS Grid: lo que hay que saber en 2026

Soporte (datos de [web-features](https://web-platform-dx.github.io/web-features-explorer/), paquete 3.46.0):

| Feature | Estado |
|---|---|
| `display: grid` | Baseline amplio desde 2020 |
| `gap` en flex | Baseline amplio desde 2023 |
| `subgrid` | Baseline desde 15/09/2023, **amplio desde 15/03/2026** |
| Container queries (`@container`, `cqi`) | Baseline desde 14/02/2023, amplio desde 14/08/2025 |
| `aspect-ratio` | Baseline amplio desde 2024 |
| `:has()` | Baseline amplio desde 19/06/2026 |
| `display: grid-lanes` (masonry) | **Solo Safari 26.4+**; Chrome, Edge y Firefox detrás de flag ([caniuse](https://caniuse.com/css-grid-lanes), [web.dev, marzo 2026](https://web.dev/blog/web-platform-03-2026)) |

### 2.1 La grilla de página con líneas con nombre (full-bleed)

La receta de [Josh Comeau](https://www.joshwcomeau.com/css/full-bleed/), ampliada con una columna "breakout" (patrón de [Ryan Mulligan](https://ryanmulligan.dev/blog/x-scrolling-centered-max-width-container/) y de [MDN, named lines](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Named_grid_lines)). Es la base más útil para landings y artículos: el texto queda en una medida legible y cualquier bloque puede salir a `breakout` o a `full` sin wrappers extra.

```css
.page {
  --gutter: var(--space-4);
  --content: min(var(--layout-content, 42rem), 100% - 2 * var(--gutter));
  --breakout: calc((var(--layout-wide, 72rem) - var(--layout-content, 42rem)) / 2);

  display: grid;
  grid-template-columns:
    [full-start] minmax(var(--gutter), 1fr)
    [breakout-start] minmax(0, var(--breakout))
    [content-start] var(--content) [content-end]
    minmax(0, var(--breakout)) [breakout-end]
    minmax(var(--gutter), 1fr) [full-end];
}
.page > *          { grid-column: content; }
.page > .breakout  { grid-column: breakout; }
.page > .full      { grid-column: full; }
.page > :is(p, ul, ol) { max-inline-size: var(--measure, 65ch); }   /* la columna no es la medida */

@media (width >= 48rem) { .page { --gutter: var(--space-6); } }
```

`--layout-content` y `--layout-wide` son propuestas de token (ver [`README.md`](./README.md#propuestas-para-tokens)).

### 2.2 Grilla de 12 columnas con spans

```css
.grid-12 {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: var(--space-4);
}
@media (width >= 48rem) { .grid-12 { grid-template-columns: repeat(8, minmax(0, 1fr)); gap: var(--space-6); } }
@media (width >= 64rem) { .grid-12 { grid-template-columns: repeat(12, minmax(0, 1fr)); } }

.grid-12 > * { grid-column: 1 / -1; }          /* móvil y tablet: todo a ancho completo */
@media (width >= 64rem) {
  .grid-12 > .span-7 { grid-column: span 7; }
  .grid-12 > .span-5 { grid-column: span 5; }
  .grid-12 > .span-4 { grid-column: span 4; }
}
```

Usá `minmax(0, 1fr)` y no `1fr` a secas: `1fr` es `minmax(auto, 1fr)` y una palabra larga o una imagen puede ensanchar la columna.

Tailwind v4: `grid grid-cols-4 md:grid-cols-8 lg:grid-cols-12 gap-4 md:gap-6` y `lg:col-span-7`.

### 2.3 Áreas con nombre (el mapa se reescribe por breakpoint)

```css
.hero {
  display: grid;
  gap: var(--space-6);
  grid-template-areas:
    "title"
    "proof"
    "copy";
}
@media (width >= 64rem) {
  .hero {
    grid-template-columns: 7fr 5fr;
    grid-template-areas:
      "title proof"
      "copy  proof";
  }
}
.hero h1   { grid-area: title; }
.hero .proof { grid-area: proof; }
.hero .copy  { grid-area: copy; }
```

Ojo: reordenar visualmente con `grid-template-areas` no cambia el orden del DOM ni del foco. Si el orden visual contradice el lógico, falla [WCAG 1.3.2 / 2.4.3](https://www.w3.org/TR/WCAG22/). Mové el DOM, no solo el mapa.

### 2.4 Subgrid: alinear cards entre sí

El problema clásico: tres cards con títulos de distinto largo y los botones quedan a alturas distintas. Con `subgrid` las filas internas se comparten.

```css
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(18rem, 100%), 1fr));
  gap: var(--space-6);
}
.card {
  display: grid;
  grid-row: span 4;                 /* media, título, texto, acción */
  grid-template-rows: subgrid;
  gap: var(--space-3);
}
```

También sirve para que un formulario de dos columnas alinee labels con inputs entre filas (`grid-template-columns: subgrid`). Guía: [web.dev, CSS subgrid](https://web.dev/articles/css-subgrid).

### 2.5 Grilla automática (RAM)

`repeat(auto-fit, minmax(min(16rem, 100%), 1fr))` — "Repeat, Auto, Minmax", de [Una Kravets en web.dev](https://web.dev/articles/one-line-layouts). El `min(…, 100%)` evita el desborde en pantallas angostas (es la versión de [Every Layout Grid](https://every-layout.dev/layouts/grid/)). `auto-fit` colapsa pistas vacías; `auto-fill` las conserva ([CSS-Tricks](https://css-tricks.com/auto-sizing-columns-css-grid-auto-fill-vs-auto-fit/)).

### 2.6 Masonry con `grid-lanes` (mejora progresiva)

```css
.board {
  display: grid;            /* fallback: grilla normal */
  display: grid-lanes;      /* Safari 26.4+ */
  grid-template-columns: repeat(auto-fill, minmax(14rem, 1fr));
  gap: var(--space-4);
}
```

Los prototipos `display: masonry` y `grid-template-rows: masonry` ya no son la spec ([modern-css.com](https://modern-css.com/css-grid-lanes/), [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Grid_lanes)). Safari 27.2 renombró `flow-tolerance` a `fit-tolerance` ([richi.codes, nov. 2026](https://dev.to/richicodes/css-grid-lanes-native-masonry-now-in-safari-b5j)). Ver la [guía de WebKit](https://gridlanes.webkit.org/).

### 2.7 Layout que cambia según la cantidad de hijos

Ahmad Shadeed ([*Solved By Modern CSS: Section Layout*, oct. 2025](https://ishadeed.com/article/modern-css-section-layout/)) combina `:has()` con *quantity queries* para que la sección cambie de layout sola:

```css
/* 4 o más cards: el header de la sección pasa arriba */
.section:has(.card:nth-last-child(n + 4)) { grid-template-columns: 1fr; }

/* 6 o más: la primera card se destaca a ancho completo */
.section:has(.card:nth-last-child(n + 6)) .card:first-child { grid-column: 1 / -1; }
```

Esto mata el "3 cards iguales" de raíz: la cantidad de contenido decide la jerarquía.

## 3. Grilla de baseline (ritmo vertical)

Hoy es viable con `lh` / `rlh` (Baseline amplio desde 21/05/2026, web-features):

```css
:root { line-height: var(--leading-body); }
.prose > * + * { margin-block-start: 1rlh; }   /* una línea de cuerpo */
.prose h2      { margin-block-start: 2rlh; }
```

Límite honesto: un baseline estricto se rompe con imágenes, íconos y tamaños fluidos. En producto, apuntá a **ritmo** (múltiplos de una unidad) y no a "cada línea cae en la misma raya". Detalle en [`espaciado-ritmo.md`](./espaciado-ritmo.md). `text-box-trim` (recortar el aire sobre la cápsula de mayúsculas) todavía no es Baseline.

## 4. Lo que hace mal la IA con las grillas

- Todo es `max-w-7xl mx-auto px-4` + `grid-cols-3`. La grilla existe solo para repartir tres cosas iguales.
- Nunca usa spans asimétricos (7/5, 8/4, 2/10).
- Usa `1fr` sin `minmax(0, …)` y una URL larga rompe la columna.
- Reordena con `order` o `grid-area` y deja el foco del teclado saltando.
- No alinea nada con la grilla de arriba: cada sección tiene su propio `max-w`.

Más en [`anti-patrones-layout.md`](./anti-patrones-layout.md).

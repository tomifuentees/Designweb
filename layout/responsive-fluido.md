# Responsive fluido e intrínseco

En 2026 "responsive" ya no es "tres breakpoints y `hidden md:block`". Es dejar que **el contenido y el contenedor** decidan, con breakpoints solo donde el layout cambia de verdad. Jen Simmons lo llamó *Intrinsic Web Design* (2018): combinar columnas fluidas y fijas, contracción por etapas, y un layout que se adapta sin media queries para cada ancho ([Jen Simmons, *Everything You Know About Web Design Just Changed*](https://www.youtube.com/watch?v=jBwBACbRuGY)). Every Layout lo formalizó en primitivos que no usan `@media` ([every-layout.dev/layouts](https://every-layout.dev/layouts/)).

## 1. Qué usar en cada nivel

| Nivel | Herramienta | Ejemplo |
|---|---|---|
| Página (shell, nav) | `@media` con los breakpoints de [`../tokens/`](../tokens/escalas.md#breakpoints) | Sidebar fija desde `lg` |
| Sección / componente | `@container` + unidades `cqi` | Card horizontal si su contenedor ≥ 28 rem |
| Distribución | Primitivos intrínsecos (flex-wrap, `auto-fit`) | Grilla de logos, botones |
| Tamaño de tipo y espacio | `clamp()` | `--text-*`, pares de espacio |
| Cantidad de hijos | `:has()` + quantity queries | 1 card = destacada; 6+ = la primera a ancho completo |

Soporte (web-features 3.46.0): container queries Baseline amplio desde agosto 2025; `:has()` desde junio 2026; **style queries** (`@container style(--x: y)`) solo Baseline nuevo desde mayo 2026; `round()` / `mod()` Baseline nuevo desde mayo 2024 ([explorer](https://web-platform-dx.github.io/web-features-explorer/)).

## 2. `clamp()` bien usado

`clamp(MIN, PREFERIDO, MAX)`. El preferido mezcla `rem` + `vw` (o `cqi`) para que el zoom del navegador siga funcionando: con `vw` solo, el texto **no escala con el zoom** y se rompe WCAG 1.4.4. El kit ya trae tipo fluido calculado con [Utopia](https://utopia.fyi/type/calculator/) (viewport 320–1240, ver [`../tokens/tokens.css`](../tokens/tokens.css)). No recalcules por componente.

Para espacio, Utopia usa **pares** que interpolan entre dos pasos ("one-up pairs"): `--space-s-m` va de 18 px a 30 px, con mucho más "drama" que `--space-s` solo (18→20) ([Utopia, fluid space calculator](https://utopia.fyi/space/calculator/); [blog](https://utopia.fyi/blog/designing-with-a-fluid-space-palette/)). Propuesta compatible con la escala fija del kit (viewport 320–1240):

```css
:root {
  /* Pares fluidos entre pasos --space-* existentes (misma fórmula que calculateClamp de utopia-core) */
  --space-fluid-gutter:  clamp(1rem, 0.6522rem + 1.7391vw, 2rem);    /* 16 → 32  */
  --space-fluid-block:   clamp(2rem, 1.3043rem + 3.4783vw, 4rem);    /* 32 → 64  */
  --space-fluid-section: clamp(4rem, 2.6087rem + 6.9565vw, 8rem);    /* 64 → 128 */
}
```

Son interpolaciones lineales entre pasos de la escala (16→32, 32→64, 64→128); ver [`README.md`](./README.md#propuestas-para-tokens).

## 3. Container queries

```css
.card-slot { container: card / inline-size; }

.card { display: grid; gap: var(--space-3); }
@container card (width >= 28rem) {
  .card { grid-template-columns: 2fr 3fr; align-items: center; }
}
.card h3 { font-size: clamp(var(--text-h4), 3cqi + 0.5rem, var(--text-h3)); }
```

Tailwind v4 lo trae nativo: `@container` en el padre y `@md:grid-cols-2` en el hijo. Los tamaños de container son la escala `--container-*` (`@xs` 20 rem … `@7xl` 80 rem; tabla en [`proporciones.md`](./proporciones.md#4-anchos-de-contenedor)).

Ahmad Shadeed lleva esto a "Smart Layouts": zonas de layout donde el componente decide según el espacio y la cantidad de hermanos ([CSS Day, junio 2025](https://ishadeed.com/article/smart-layouts-talk-css-day/); [Section Layout, oct. 2025](https://ishadeed.com/article/modern-css-section-layout/); [guía interactiva](https://ishadeed.com/article/css-container-query-guide/)). Un detalle de su artículo: en flex, el ancho mínimo de un ítem es su contenido; si una imagen empuja, poné `min-inline-size: 0`.

## 4. Primitivos de Every Layout (CSS moderno)

[Every Layout](https://every-layout.dev/layouts/) (Heydon Pickering y Andy Bell) define 13 primitivos: Stack, Box, Center, Cluster, Sidebar, Switcher, Cover, Grid, Frame, Reel, Imposter, Icon y Container. Abajo, los diez que más se usan, con tokens del kit. Se componen: un Cover que contiene un Center que contiene un Stack.

### Stack: flujo vertical

```css
.stack { display: flex; flex-direction: column; justify-content: flex-start; }
.stack > * { margin-block: 0; }
.stack > * + * { margin-block-start: var(--stack-space, var(--space-4)); }
/* empujar el resto al fondo: */
.stack > .push { margin-block-end: auto; }
```

Versión con `gap` si no necesitás excepciones: `display: flex; flex-direction: column; gap: var(--space-4)`. Tailwind: `flex flex-col gap-4`. Fuente: [The Stack](https://every-layout.dev/layouts/stack/).

### Box: caja con padding y borde que no desaparece

```css
.box {
  padding: var(--box-pad, var(--space-6));
  border: 1px solid var(--border);
  outline: 1px solid transparent;   /* sigue visible en modo alto contraste */
  outline-offset: -1px;
  background: var(--surface);
  color: var(--text);
}
```

### Center: columna centrada con medida

```css
.center {
  box-sizing: content-box;          /* el padding no come la medida */
  max-inline-size: var(--measure, 65ch);
  margin-inline: auto;
  padding-inline: var(--space-4);
}
```

Tailwind: `mx-auto max-w-prose px-4` (ojo: Tailwind usa `border-box`; el ancho útil queda en 65ch − 2rem).

### Cluster: grupos que envuelven (tags, botones, nav)

```css
.cluster { display: flex; flex-wrap: wrap; gap: var(--space-3); align-items: center; justify-content: flex-start; }
```

Tailwind: `flex flex-wrap items-center gap-3`.

### Sidebar: aside fijo + contenido que crece, sin breakpoint

```css
.with-sidebar { display: flex; flex-wrap: wrap; gap: var(--space-6); }
.with-sidebar > :first-child { flex-basis: 16rem; flex-grow: 1; }          /* el sidebar */
.with-sidebar > :last-child  { flex-basis: 0; flex-grow: 999; min-inline-size: 50%; }
```

Cuando el contenido quedaría más angosto que el 50 %, el sidebar baja solo. Fuente: [The Sidebar](https://every-layout.dev/layouts/sidebar/). Variante con `:has()` en [Piccalilli](https://piccalil.li/blog/a-revisit-of-the-every-layout-sidebar-with-has-and-selector-performance/).

### Switcher: fila ↔ columna según un umbral

```css
.switcher { display: flex; flex-wrap: wrap; gap: var(--space-4); --threshold: 40rem; }
.switcher > * { flex-grow: 1; flex-basis: calc((var(--threshold) - 100%) * 999); }
/* más de 4 hijos: siempre en columna */
.switcher > :nth-last-child(n + 5), .switcher > :nth-last-child(n + 5) ~ * { flex-basis: 100%; }
```

Si el contenedor es más ancho que el umbral, el cálculo da negativo (se trata como 0) y quedan en fila; si es más angosto, da enorme y cada hijo ocupa una fila. Fuente: [The Switcher](https://every-layout.dev/layouts/switcher/).

### Cover: bloque de alto mínimo con un elemento centrado verticalmente

```css
.cover { display: flex; flex-direction: column; min-block-size: 100svh; padding: var(--space-6); }
.cover > * { margin-block: var(--space-4); }
.cover > .principal { margin-block: auto; }
.cover > :first-child:not(.principal) { margin-block-start: 0; }
.cover > :last-child:not(.principal) { margin-block-end: 0; }
```

Usá `svh` (Baseline amplio desde 2025) para que la barra del navegador móvil no tape el CTA. Fuente: [The Cover](https://every-layout.dev/layouts/cover/).

### Grid: grilla automática que no desborda

```css
.auto-grid { display: grid; gap: var(--space-6); grid-template-columns: repeat(auto-fit, minmax(min(var(--min, 16rem), 100%), 1fr)); }
```

Fuente: [The Grid](https://every-layout.dev/layouts/grid/); el patrón RAM en [web.dev](https://web.dev/articles/one-line-layouts).

### Frame: recorte con ratio fijo

```css
.frame { aspect-ratio: var(--ratio, 16 / 9); overflow: hidden; display: flex; justify-content: center; align-items: center; }
.frame > :is(img, video) { inline-size: 100%; block-size: 100%; object-fit: cover; }
```

Fuente: [The Frame](https://every-layout.dev/layouts/frame/). Ratios recomendados en [`proporciones.md`](./proporciones.md#5-ratios-de-imagen).

### Reel: carrusel horizontal nativo

```css
.reel {
  display: flex; gap: var(--space-4);
  overflow-x: auto; overscroll-behavior-inline: contain;
  scroll-snap-type: x mandatory; scroll-padding-inline: var(--space-4);
}
.reel > * { flex: 0 0 var(--item, min(80%, 20rem)); scroll-snap-align: start; }
```

Que el último ítem quede cortado en el borde (el principio de **cierre**) avisa que hay más. Hacé el contenedor enfocable (`tabindex="0"` + `aria-label`) para teclado. Fuente: [The Reel](https://every-layout.dev/layouts/reel/).

## 5. Breakpoints: pocos y por contenido

- Usá los de Tailwind v4 que fija [`../tokens/`](../tokens/escalas.md#breakpoints). No inventes un breakpoint por componente.
- Poné el breakpoint donde **el contenido se rompe**, no donde está un iPhone.
- Material 3 piensa en *window size classes* y en cantidad de **panes** (1 pane < 840 dp, 2 desde 840) ([M3](https://m3.material.io/foundations/layout/breakpoints)). Es buena guía para apps: decidí cuántos paneles, no cuántas columnas.
- Sintaxis de rango moderna: `@media (width >= 64rem)`.

## 6. Trucos de 2025–2026 que vale la pena conocer

- **Apilar con grid sin `position: absolute`:** dos hijos en la misma celda (`grid-area: 1 / 1`) se superponen y siguen en el flujo. Jhey Tompkins lo recordó con subgrid + `position: sticky` ([X, dic. 2025](https://x.com/jh3yy/status/1998097484904849703)).
- **Sidebar que se abre sin JS:** `.layout:has(:popover-open) { grid-template-columns: var(--sidebar-width) 1fr; }` ([Jhey, X, oct. 2025](https://x.com/jh3yy/status/1977517175285154015)).
- **Centrado vertical sin flex ni grid:** `align-content: center` funciona en bloques comunes ([Jhey, X, oct. 2025](https://x.com/jh3yy/status/1978506988293111909)).
- **Subgrid para componentes que antes "no se podían":** Adam Wathan, sobre una biblioteca de libros con subgrid ([X, mayo 2025](https://x.com/adamwathan/status/1920561467150971032)).
- **Masonry nativo:** `display: grid-lanes`, solo Safari 26.4+ por ahora; usalo con fallback (ver [`grillas.md`](./grillas.md#26-masonry-con-grid-lanes-mejora-progresiva)).
- **Titulares sin viudas:** `text-wrap: balance` (Baseline nuevo desde mayo 2024) en headings; `text-wrap: pretty` todavía no es Baseline, sumalo como mejora.

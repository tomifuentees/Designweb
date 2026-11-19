# Patrones de layout

19 disposiciones de página y sección con wireframe, proporciones, código y lo que la IA hace mal. Acá va la **geometría**; el contenido y la terminación de cada pieza (qué copy, qué prueba, qué tipografía) están en [`../componentes/`](../componentes/README.md). Todo usa tokens de [`../tokens/`](../tokens/README.md) y las variables de layout propuestas en [`README.md`](./README.md#propuestas-para-tokens) (`--layout-content` 42 rem, `--layout-wide` 72 rem).

Convenciones del ASCII: `█` foco principal, `▒` apoyo, `·` aire. Las fracciones son de una grilla de 12.

Índice: [hero](#hero) (1–4) · [secciones de producto](#secciones-de-producto) (5–8) · [contenido](#contenido) (9–11) · [aplicación](#aplicación) (12–14) · [conversión](#conversión) (15–18) · [gesto](#gesto) (19)

---

## Hero

### 1. Hero split asimétrico (7/5)

```
┌──────────────────────────────────────────────┐
│ logo                          nav     [CTA]  │
│                                              │
│ ████████████████████████      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒ │
│ TITULAR EN 2–3 LÍNEAS         bajada 2–3 lín │
│ ████████████████████████      [CTA] link     │
│                                              │
│ ┌──────────────── captura real ────────────┐ │
└──────────────────────────────────────────────┘
```

- **Proporción:** 7/5 o 3/5–2/5, alineado **arriba** (no centrado vertical). Es la corrección que hace Steve Schoger al hero centrado de Claude Code ([*Designing with Claude Code*, marzo 2026](https://www.youtube.com/watch?v=lkKGQVHrXzE)).
- **Tailwind v4:** `grid gap-8 lg:grid-cols-12 items-start` → titular `lg:col-span-7`, bajada `lg:col-span-5 lg:pt-3`.
- **CSS:**
  ```css
  .hero { display: grid; gap: var(--space-8); align-items: start; }
  @media (width >= 64rem) { .hero { grid-template-columns: 7fr 5fr; } }
  .hero h1 { font-size: var(--text-display); line-height: var(--leading-display); text-wrap: balance; }
  ```
- **La IA hace:** todo centrado, titular y bajada del mismo ancho, dos botones pill gemelos.

### 2. Hero editorial (titular a ancho completo)

```
┌──────────────────────────────────────────────┐
│ ████████████████████████████████████████████ │
│ TITULAR ENORME QUE OCUPA LAS 12 COLUMNAS     │
│ ────────────────────────────────────────────  │
│ ▒▒ dato    ▒▒ dato     · · ·   bajada 4 col  │
└──────────────────────────────────────────────┘
```

- **Proporción:** titular 12/12 a `--text-display` (o más grande si el estilo lo permite); debajo, una fila de 3/3/·/4 con datos y bajada. Contraste de escala alto (ver [`jerarquia-composicion.md`](./jerarquia-composicion.md#5-contraste-de-escala)).
- **Tailwind:** `grid lg:grid-cols-12 gap-6` → `h1.lg:col-span-12`, metadatos `lg:col-span-3`, bajada `lg:col-start-9 lg:col-span-4`.
- **La IA hace:** titular corto en 3 líneas centradas con `max-w-3xl`.
- **Estilos:** [`editorial-revista`](../estilos/editorial-revista.md), [`suizo-internacional`](../estilos/suizo-internacional.md).

### 3. Hero con producto que sale del contenedor

```
┌──────────────────────────────────────────────┐
│ ████ titular (content)                       │
│ ▒▒ bajada + CTA                              │
│        ┌─────────────────────────────────────┼──→ sangra a la derecha
│        │ captura real del producto           │
└────────┴─────────────────────────────────────┘
```

- **Proporción:** texto en `content`, captura que arranca en la columna 3 y se va a `full-end` (la grilla con nombre de [`grillas.md`](./grillas.md#21-la-grilla-de-página-con-líneas-con-nombre-full-bleed)).
- **CSS:** `.shot { grid-column: content-start / full-end; }` y `aspect-ratio: 16 / 10` con `object-position: left top`.
- **La IA hace:** mockup de MacBook centrado flotando en un degradé (tell #29).

### 4. Hero de prueba (una cifra protagonista)

```
┌──────────────────────────────────────────────┐
│ ▒ titular chico (h2)                          │
│ █████████  48 h                               │
│ █████████  de alta a primer cobro             │
│ ▒ quién lo dice (logo + nombre)    [CTA]     │
└──────────────────────────────────────────────┘
```

- **Proporción:** la cifra a `--text-display` o mayor; titular a `--text-h3`. Una sola cifra.
- **La IA hace:** fila de cuatro stats iguales "10K+ users · 99.9% uptime".

---

## Secciones de producto

### 5. Bento con jerarquía

```
┌──────────────┬───────┬───────┐
│              │ ▒▒▒▒  │ ▒▒▒▒  │
│  █████████   ├───────┴───────┤
│  celda hero  │ ▒▒▒▒▒▒▒▒▒▒▒▒▒ │
├───────┬──────┴───────┬───────┤
│ ▒▒▒▒  │ ▒▒▒▒▒▒▒▒▒▒▒▒ │ ▒▒▒▒  │
└───────┴──────────────┴───────┘
```

- **Proporción:** una celda hero de 2×2; el resto 1×1 y 2×1. 6–9 celdas, gutter único. Reglas completas en [`../estilos/bento-grids.md`](../estilos/bento-grids.md).
- **CSS:**
  ```css
  .bento { display: grid; gap: var(--space-4); grid-template-columns: 1fr; }
  @media (width >= 64rem) {
    .bento {
      grid-template-columns: repeat(4, minmax(0, 1fr));
      grid-auto-rows: minmax(10rem, auto);
      grid-template-areas:
        "hero hero a    b"
        "hero hero c    c"
        "d    e    e    f";
    }
  }
  ```
- **La IA hace:** 3×2 de celdas iguales con ícono + H3 + párrafo.

### 6. Filas de feature (split alternado, con variación)

```
│ ██████ texto 5      ▒▒▒▒▒▒▒▒▒ imagen 7 │
│ ▒▒▒▒▒▒▒▒▒ imagen 7      ██████ texto 5 │
│ ████████ texto a ancho completo + imagen a sangre │
```

- **Proporción:** 5/7, no 6/6. **Rompé el zigzag a la tercera fila**: cambiá de formato (una fila a ancho completo, una lista, una cita). Tres zigzags iguales es el mismo tell que tres cards.
- **Tailwind:** `grid lg:grid-cols-12 gap-8 items-center` → texto `lg:col-span-5`, imagen `lg:col-span-7`; en la fila par `lg:order-first` **solo** en la imagen (el DOM sigue texto → imagen).
- **La IA hace:** zigzag perfecto 6/6 × 4 filas con el mismo padding.

### 7. Lista de features + visual pegajoso (sticky)

```
┌───────────────────┬──────────────────────────┐
│ ▒ feature 1       │                          │
│ ▒ feature 2  →    │   █ visual sticky que    │
│ ▒ feature 3       │     cambia con la lista  │
│ ▒ feature 4       │                          │
└───────────────────┴──────────────────────────┘
```

- **Proporción:** 4/8 o 5/7; la columna visual con `position: sticky; top: var(--space-16)`.
- **CSS:** `.visual { position: sticky; top: var(--space-16); align-self: start; }`. En móvil, desactivá el sticky y poné cada visual debajo de su texto.
- **La IA hace:** cuatro cards con ícono Lucide. Ver también [`../estilos/scrollytelling.md`](../estilos/scrollytelling.md).

### 8. Encabezado de sección lateral (4/8)

```
│ ██ Título de sección   │ ▒ contenido (lista, grilla, FAQ) │
│ ▒ bajada corta         │ ▒                               │
│   (sticky)             │ ▒                               │
```

- **Proporción:** 4/8 o 3/9. El heading en la columna angosta, `position: sticky`. Variante de Shadeed: si hay 4 o más ítems, el header pasa arriba con `:has()` ([Section Layout](https://ishadeed.com/article/modern-css-section-layout/)).
- **La IA hace:** heading centrado + subtítulo centrado + grilla debajo, en todas las secciones.

---

## Contenido

### 9. Artículo con breakout y notas al margen

```
│ · · │ ▒ nota │ █ texto en medida 65ch     │ · · │
│ · · │        │ █                          │ · · │
│ ████████████ imagen full-bleed ██████████████████│
│ · · │  ▒▒▒▒▒ figura breakout ▒▒▒▒▒▒▒▒▒▒▒▒▒ │ · · │
```

- **Proporción:** columna en `--layout-content`, párrafos limitados a `--measure` (`65ch`); breakout hasta `--layout-wide`; full-bleed al 100 %. Notas en la pista izquierda desde `xl`.
- **CSS:** la grilla con nombre de [`grillas.md`](./grillas.md#21-la-grilla-de-página-con-líneas-con-nombre-full-bleed) (Comeau / MDN).
- **La IA hace:** `prose max-w-none` a 1200 px de ancho (100+ caracteres por línea).

### 10. Docs de tres columnas

```
┌────────┬───────────────────────────┬────────┐
│ nav    │ contenido (65–75ch)       │ TOC    │
│ 16rem  │                           │ 14rem  │
└────────┴───────────────────────────┴────────┘
```

- **Proporción:** `16rem minmax(0, 1fr) 14rem`; el TOC desaparece < `xl`, la nav pasa a drawer < `lg`.
- **CSS:** `grid-template-columns: 16rem minmax(0, 1fr) 14rem;` + `.content { max-inline-size: 72ch; }`.
- **La IA hace:** contenido a todo el ancho entre dos sidebars, sin medida.

### 11. Galería / portfolio (masonry progresivo)

- **Proporción:** 2–4 columnas por ancho; ratios mezclados (3/2, 4/5, 1/1) son la gracia.
- **CSS:** `display: grid; display: grid-lanes;` con fallback (ver [`grillas.md`](./grillas.md#26-masonry-con-grid-lanes-mejora-progresiva)). Alternativa sin soporte: `columns: 3 18rem` (orden de lectura vertical).
- **La IA hace:** grilla 3×3 de cuadrados recortados con `object-cover` y hover zoom.

---

## Aplicación

### 12. App shell con sidebar

```
┌────────┬─────────────────────────────────────┐
│ logo   │ topbar: breadcrumb · búsqueda · yo  │
│ nav    ├─────────────────────────────────────┤
│ 15–16  │ contenido (scroll propio)           │
│ rem    │                                     │
└────────┴─────────────────────────────────────┘
```

- **Proporción:** sidebar 15–16 rem (240–256 px), colapsable a ~4 rem de íconos. Topbar 56–64 px.
- **CSS:**
  ```css
  .shell { display: grid; min-block-size: 100dvh; grid-template: "nav top" auto "nav main" 1fr / 16rem minmax(0, 1fr); }
  .shell > nav  { grid-area: nav; position: sticky; top: 0; block-size: 100dvh; overflow-y: auto; }
  .shell > main { grid-area: main; min-inline-size: 0; }
  @media (width < 64rem) { .shell { grid-template: "top" auto "main" 1fr / 1fr; } .shell > nav { display: none; } }
  ```
  Abrir sin JS: `.shell:has(nav:popover-open)` ([Jhey Tompkins, X, oct. 2025](https://x.com/jh3yy/status/1977517175285154015)).
- **La IA hace:** "Welcome back, [Name] ✨" a ancho completo (tell #15) y una sidebar con 14 íconos del mismo peso.

### 13. Dashboard

```
│ ▒ KPI │ ▒ KPI │ ▒ KPI │ (solo los que se accionan)  │
│ ██████████ gráfico principal 8 ██ │ ▒ lista 4     │
│ ▒▒▒▒▒▒▒ tabla a ancho completo ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ │
```

- **Proporción:** KPIs en `Cluster` o `auto-fit` (no siempre 4); gráfico 8/4; tabla 12. Densidad compacta (ver [`espaciado-ritmo.md`](./espaciado-ritmo.md#5-densidad)).
- **La IA hace:** 4 KPIs con flechita verde, 2 gráficos 6/6 iguales, todo en cards con sombra. Contenido en [`../componentes/dashboards.md`](../componentes/dashboards.md).

### 14. Formulario de configuración (etiqueta lateral)

```
│ ▒ Sección       │ label  [input............] │
│   ayuda corta   │ label  [input............] │
```

- **Proporción:** 4/8; dentro, labels e inputs alineados con `subgrid` entre filas.
- **CSS:** `.form { display: grid; grid-template-columns: max-content 1fr; gap: var(--space-3) var(--space-6); } .row { grid-column: 1 / -1; display: grid; grid-template-columns: subgrid; }`.

---

## Conversión

### 15. Pricing

- **Dos o tres planes:** `auto-fit` con `subgrid` para alinear precio, lista y botón entre columnas; el plan recomendado se distingue por **contraste** (fondo invertido o borde de acento), no por `scale-105`.
- **Muchos planes o features:** tabla comparativa con primera columna sticky.
- **CSS:** `.plans { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(18rem, 100%), 1fr)); } .plan { display: grid; grid-row: span 5; grid-template-rows: subgrid; }`.
- **La IA hace:** tres cards, la del medio agrandada con badge "Most popular" y degradé. Contenido en [`../componentes/pricing.md`](../componentes/pricing.md).

### 16. Testimonios: una cita grande + secundarias

```
│ █ "Cita larga, con nombre, cargo y foto real"  8 │ ▒ cita 4 │
│                                                  │ ▒ cita 4 │
```

- **Proporción:** 8/4; la cita principal a `--text-h3`.
- **La IA hace:** carrusel de tres cards iguales con 5 estrellas.

### 17. FAQ con heading lateral

- **Proporción:** 4/8 (patrón 8); `<details>` en la columna ancha, medida ≤ 65ch.
- **La IA hace:** acordeón centrado `max-w-3xl` con heading centrado.

### 18. CTA final y footer

- **CTA:** el único bloque **centrado** de la página puede ser este; padding `--space-section-lg`; un solo botón.
- **Footer:** grilla `auto-fit` de columnas de links + una columna ancha con marca/newsletter (`2fr repeat(3, 1fr)`); los textos legales en una fila aparte.
- **La IA hace:** CTA en card con degradé; footer de 4 columnas idénticas con íconos sociales.

---

## Gesto

### 19. Canvas grid (líneas de grilla visibles)

Bordes verticales y horizontales de 1 px que abrazan los contenedores y se extienden hasta el borde del viewport: estructura arquitectónica sin ilustraciones. Steve Schoger lo usa como terminación en su rediseño con Claude Code ([*Designing with Claude Code*, marzo 2026](https://www.youtube.com/watch?v=lkKGQVHrXzE); [resumen](https://www.yedapo.com/episode/479ceaf7-1088-418a-894a-a835f14337a0/steve-schoger-designing-with-claude-code/insights)).

```css
html { overflow-x: clip; }                      /* las líneas no generan scroll lateral */
.canvas { --line: color-mix(in oklch, var(--text) 10%, transparent); border-inline: 1px solid var(--line); }
.canvas > section { position: relative; }
.canvas > section::after {                       /* línea que sigue hasta el borde de la pantalla */
  content: ""; position: absolute; inset-inline: -100vw; inset-block-end: 0;
  block-size: 1px; background: var(--line);
}
```

Uno por sitio. Si además hay grano, glow y bento, sobra.

---

## Cómo elegir (resumen)

| Si el proyecto es… | Hero | Secciones | Ancho dominante |
|---|---|---|---|
| SaaS / devtool | 1 o 3 | 5, 7, 15 | `--layout-wide` |
| Editorial / blog | 2 | 9, 16 | `--layout-content` |
| Estudio / portfolio | 2 o 3 | 11, 19 | full-bleed |
| Comercio | 3 o 4 | 6, 11, 15 | `--layout-wide` |
| App / dashboard | — | 12, 13, 14 | 100 % con sidebar |
| Docs | — | 10 | `65–75ch` |

Elegí **un** hero, **dos o tres** patrones de sección, y un **gesto** (19, un full-bleed o un break de grilla). Más de eso es collage.

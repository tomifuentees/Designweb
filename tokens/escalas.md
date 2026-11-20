# Escalas y por qué le ganan al default de IA

Cada escala es una decisión cerrada. El modelo, sin ella, elige el valor más común que vio en tutoriales: `p-4` / `p-8` alternados sin ritmo, `rounded-2xl` en todo, `shadow-xl`, `text-5xl font-bold` con `leading-tight` o al revés, `transition-all duration-500`, `z-50` hasta que alguien pone `z-[9999]`.

## Espacio

Base de **4 px (0.25rem)**. Pasos: 0, 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96, 128. El aire entre secciones es `--space-section` (96 px) o `section-sm` / `section-lg`, no un `py-28` improvisado.

En Tailwind v4 una sola variable `--spacing: 0.25rem` genera `p-4`, `gap-6`, etc. Eso está bien como *motor*. El ritmo lo marca usar pocos pasos, siempre los mismos. Un `gap-[18px]` o un `mt-[13px]` es la firma de un componente que nadie revisó.

Por qué le gana al default: un layout con un ritmo único se lee como un sistema. Uno con números sueltos se lee como un ensamble.

## Radio

`none` 0, `sm` 2, `md` 6, `lg` 10, `xl` 16, `full` 9999. Elegí **un default** (`md` en la mayoría de los productos; `none` en suizo, brutal o catálogo). `xl` es para un recorte de media, no para el botón, la card, el input y el badge.

El “todo `rounded-2xl` / `rounded-3xl` + sombra suave” es un tell citado en [Utsubo, junio de 2026](https://www.utsubo.com/blog/built-with-ai-trust-signals-2026) y en [Drop The Hassle, octubre de 2026](https://dropthehassle.com/guides/make-website-look-less-ai).

## Sombra / elevación

Cuatro niveles y un `none` que debería ser el más usado. En SaaS oscuro y en UI casi invisible, el borde de 1 px a bajo contraste (blanco u oscuro al 8–12 %) define el chasis mejor que un `shadow-xl`. El glow de acento no es un nivel de esta escala: si aparece, es un caso (un cursor, un estado activo), no un halo detrás del hero.

## Tipo (fluido)

Escala con `clamp()`, viewport **320–1240 px**, cuerpo de **16 a 18 px**. La receta es la de [Utopia](https://utopia.fyi/type/calculator/): un tamaño mínimo, uno máximo, y una pendiente en `vw`. Pasos: `caption`, `sm`, `body`, `lg`, `h4`, `h3`, `h2`, `h1`, `display`.

```css
--text-body: clamp(1.0000rem, 0.9565rem + 0.2174vw, 1.1250rem);
--text-h1:   clamp(2.5000rem, 2.1522rem + 1.7391vw, 3.5000rem);
```

Por qué le gana al default: la IA salta entre `text-4xl`, `text-5xl` y `text-7xl` según el prompt, y rara vez piensa en el móvil. Una escala fluida unifica las páginas y evita un titular que explota a 390 px o que queda tímido a 1440.

La familia tipográfica no se decide acá. Sale de [`../tipografias/`](../tipografias/README.md).

## Interlineado

Multiplicadores, no píxeles: `display` 1.05, `heading` 1.15, `tight` 1.25 (UI), `body` 1.5, `body-lg` 1.6, `mono` 1.4. El error clásico es `leading-none` en un párrafo o `leading-relaxed` en un display de seis palabras.

## Letter-spacing

`tighter` (−0.03 em) para display, `tight` (−0.02 em) para h1, `normal` para cuerpo, `wide` (0.04 em) y `widest` (0.16 em) para **un** kicker. El label en mayúsculas con tracking enorme arriba de cada heading es un tell ([Drop The Hassle](https://dropthehassle.com/guides/make-website-look-less-ai)).

## Motion

Duraciones: 0, 120, 180, 280, 400 ms. Curvas: `standard` `cubic-bezier(0.2, 0, 0, 1)`, `emphasized` `cubic-bezier(0.3, 0, 0, 1)` (las que Tailwind v4 muestra como `--ease-snappy` y `--ease-fluid` en su anuncio), más `enter` y `exit`. Sin bounce. Sin `ease-in-out` de medio segundo en todo.

`prefers-reduced-motion: reduce` pone las duraciones en 0. Es obligatorio. El fade-and-slide-up en cada sección, el badge con `animate-pulse` y el `transition-all duration-1000` son tells (Desai, Utsubo, Drop The Hassle).

## Breakpoints

Los de Tailwind v4, en rem: `sm` 40, `md` 48, `lg` 64, `xl` 80, `2xl` 96. Un `3xl` de 120 rem es opcional (aparece como ejemplo en las docs de v4) y no es default. No inventes un breakpoint por componente.

## z-index

Capas nombradas: `base` 0, `raised` 10, `dropdown` 20, `sticky` 30, `overlay` 40, `modal` 50, `toast` 60, `max` 70. Si hace falta un slot nuevo, se agrega acá. `z-[9999]` es la forma más rápida de declarar que el sistema no existe.

## Sumado el 20 de noviembre de 2026: escalas de otros sistemas y valores de partida

Lo que sigue salió del minado de repos ([`../recursos/minado-repos.md`](../recursos/minado-repos.md)). Son referencias para comparar y para elegir rápido en modo restyling, no reemplazan la escala de arriba.

### Cuatro sistemas grandes, una misma idea

Las escalas de espaciado de los sistemas que lista [awesome-design-systems](https://github.com/alexpate/awesome-design-systems) (Unlicense) coinciden en lo esencial: pasos chicos de 2 o 4 px adentro de los componentes y saltos grandes entre secciones. Valores verificados en la fuente el 20 de noviembre de 2026:

| Sistema | Escala (px) | Fuente | Qué copiar de la idea |
|---|---|---|---|
| Carbon (IBM) | 2, 4, 8, 12, 16, 24, 32, 40, 48, 64, 80, 96, 160 | [carbondesignsystem.com/elements/spacing](https://carbondesignsystem.com/elements/spacing/overview/) | Los tokens no son responsive; en un breakpoint se baja *un paso* de la escala. |
| Primer (GitHub) | 2, 4, 6, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 64, 80, 96, 112, 128 | [primer/primitives, `size.json5`](https://github.com/primer/primitives/blob/main/src/tokens/base/size/size.json5) | Pasos de 4 hasta 48 para UI densa; después saltos de 16. |
| Polaris (Shopify) | 0, 1, 2, 4, 6, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96, 112, 128 | [Shopify/polaris, `space.ts`](https://github.com/Shopify/polaris/blob/main/polaris-tokens/src/themes/base/space.ts) | El nombre es px × 25 (`space-400` = 16 px) y hay alias semánticos: `space-card-padding` = 16, `space-table-cell-padding` = 6, `space-button-group-gap` = 8. |
| GOV.UK | 0, 5, 10, 15, 20, 25, 30, 40, 50, 60 | [govuk-frontend, `_spacing.scss`](https://github.com/alphagov/govuk-frontend/blob/main/packages/govuk-frontend/src/govuk/settings/_spacing.scss) | Escala responsive: el mismo punto vale menos en móvil (punto 4: 15 → 20 px; punto 9: 40 → 60 px). |

Lección para el kit: la escala de 4 px de arriba alcanza. Lo que vale la pena tomar es la regla de Carbon (bajar un paso en móvil en vez de inventar un valor) y los alias semánticos de Polaris (`--space-card-padding`) cuando un equipo repite siempre el mismo par.

### Guía de espaciado por relación (unslop)

Valores de partida de [unslop](https://github.com/heydamir/unslop) de Damir Sokolovsky ([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), `references/tokens.md`), resumidos:

- adentro de un control: 4 a 12;
- entre ítems relacionados (filas de una lista): 2 a 8;
- entre grupos (un label y su lista, dos cards): 12 a 24;
- entre secciones: 32 a 64; secciones de landing, 80 a 128;
- del nav al titular del hero: 96 a 128 en desktop y 48 a 64 en móvil.

### Medidas de app (unslop)

| Pieza | Medida | Token del kit |
|---|---|---|
| Sidebar | 240 a 280 de ancho | `--size-sidebar` 256 |
| Contenido | fluido, padding 24 a 32, tope 1440 a 1600 | `--size-app-max` 1536 |
| Top bar o page header | 56 a 64 | `--size-topbar` 56 |
| Fila de navegación | 32 a 36, gap 2 a 4 | `--size-control-sm` 32 |
| Control por defecto | 36 | `--size-control-md` 36 |
| Botón de hero o táctil | 44 a 48, padding lateral 16 a 20 | `--size-control-lg` 44 |
| Gráfico principal | al menos 2/3 del ancho, 280 a 360 de alto | sin token |

Los tokens `--size-*` están en [`tokens.css`](tokens.css) y en [`tokens.json`](tokens.json) (grupo `size`).

### Radios anidados

Regla de unslop: **radio interior = radio exterior − padding, nunca menos de 4**. Una card de 16 con padding de 8 lleva hijos con radio 8. Escala orientativa: keycap o tag 4–6, fila/input/botón 8–10, card 12–16, panel 14–20. El incumplimiento es la ficha [`radios-anidados-que-no-suman`](../anti-patrones/catalogo.md#fichas-3159-minadas-de-repos-de-referencia-noviembre-de-2026).

### Rampas neutras para superficies (unslop)

Para apps y dashboards, unslop recomienda una rampa gris (graphite) en todas las superficies; para landings, la rampa cuyo tinte acompaña al mundo de la marca: warm para papel, madera, comida u oficio; ink para noche, agua o lo técnico. Los hex son de unslop (CC BY 4.0). Medí el contraste con el script del kit:

| Rol (oscuro) | Graphite | Warm | Ink |
|---|---|---|---|
| Superficie más profunda (sidebar) | `#0f0f10` | `#12110f` | `#07080d` |
| Fondo de página | `#141415` | `#161513` | `#0b0d14` |
| Card | `#19191b` | `#1c1a18` | `#11141c` |
| Elevada (fila activa, input) | `#232325` | `#262421` | `#1a1e28` |
| Texto principal | `#ededed` | `#efe9de` | `#eef0f5` |
| Texto secundario | `#a1a1a6` | `#aaa398` | `#a3a9b8` |
| Texto apagado e íconos | `#85858b` | `#8a847a` | `#7a8296` |

| Rol (claro) | Graphite | Warm | Ink |
|---|---|---|---|
| Fondo de página | `#fafafa` | `#f7f4ee` | `#f5f7fa` |
| Card | `#ffffff` | `#fdfbf7` | `#ffffff` |
| Elevada | `#f4f4f5` | `#efe9df` | `#eceff4` |
| Texto principal | `#171717` | `#1f1b16` | `#111827` |
| Texto secundario | `#525252` | `#5e554a` | `#4b5565` |
| Texto apagado e íconos | `#737373` | `#7b7266` | `#6b7487` |

Medición del kit (WCAG 2.1 / APCA Lc sobre el fondo de página): el secundario pasa en las seis (6,7–8,3:1). El apagado da 4,9–5,1:1 en oscuro pero solo Lc −35 a −37, y en claro warm e ink quedan en 4,3–4,4:1. Usalo para íconos, metadatos grandes o placeholders, **no para texto de cuerpo**. Ojo: warm claro (`#f7f4ee`) es otro fondo crema; mirá el aviso de [`../paletas/README.md`](../paletas/README.md).

Semánticos de unslop que encajan en las tres rampas: positivo `#4cc38a` (oscuro) / `#16a34a` (claro); negativo `#e5484d` (oscuro) / `#dc2626` (claro). Profundidad: en oscuro, pasos de superficie más un hairline y, como mucho, `inset 0 1px 0 rgb(255 255 255 / 0.12)` arriba de un botón o una fila activa; en claro, `0 1px 2px rgb(0 0 0 / 0.05)` para lo chico y `0 8px 24px rgb(0 0 0 / 0.06)` para lo que flota.

### Easings y sombras de Open Props

[Open Props](https://github.com/argyleink/open-props) de Adam Argyle (MIT) trae curvas numeradas por fuerza. El kit sumó tres que no rebotan:

| Token del kit | Curva | Origen | Uso |
|---|---|---|---|
| `--ease-out-3` | `cubic-bezier(0, 0, 0.3, 1)` | `--ease-out-3` | hover, menú, tooltip |
| `--ease-out-5` | `cubic-bezier(0, 0, 0, 1)` | `--ease-out-5` | panel o drawer que entra |
| `--ease-in-out-3` | `cubic-bezier(0.5, 0, 0.5, 1)` | `--ease-in-out-3` | ida y vuelta (toggle), no entradas |

Quedaron fuera a propósito `--ease-elastic-*`, `--ease-squish-*` y `--ease-spring-*`: son la ficha [`easing-con-rebote`](../anti-patrones/catalogo.md#fichas-3159-minadas-de-repos-de-referencia-noviembre-de-2026).

De las sombras de Open Props vale la técnica, no los valores:

- **Varias capas cortas y tenues** en vez de una sombra grande: se ven físicas sin ensuciar. Es el token `--shadow-layered`.
- **Un color de sombra con tinte** (Open Props usa un gris frío, `220 3% 15%`) y una **fuerza** separada que el modo oscuro sube (de 1 % a 25 %), así el mismo token sirve en los dos temas. En el kit preferimos no usar sombra en oscuro y subir la superficie, pero si tu stack ya tiene sombras, esta es la forma limpia de adaptarlas.
- **Inner shadow como brillo de borde superior** en botones oscuros, la misma idea que el `inset 0 1px 0` de unslop.

## Lo que esta carpeta no resuelve

Los tokens fijan *valores*. No arreglan un muro de tres cards iguales, un hero centrado genérico ni una copy de “Elevate your workflow”. Eso es layout y criterio, y está en [`../anti-patrones/`](../anti-patrones/README.md) y en [`../estilos/`](../estilos/README.md). Motif lo dice claro: una pared de cards en tu paleta sigue siendo una pared de cards.

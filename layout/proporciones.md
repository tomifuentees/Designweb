# Proporciones

Qué proporciones tienen evidencia, cuáles son convención útil y cuáles son mito. La regla del kit: **una proporción vale si se repite en el sistema** (escala, ratio de imagen, ancho de columna). Ninguna vuelve "linda" una página por sí sola.

## 1. Proporción áurea (φ ≈ 1,618): convención, no ley

- **La evidencia de preferencia es débil.** Fechner (1860s) es el estudio que siempre se cita; Markowsky señala que el 76 % eligió alguno de los tres rectángulos de proporción media, no el áureo en particular ([Markowsky, *Misconceptions about the Golden Ratio*, 1992](https://www.researchgate.net/publication/322814290_Misconceptions_about_the_Golden_Ratio); resumen en [EUSci, 2020](https://eusci.org.uk/2020/07/29/myth-busting-the-golden-ratio/)).
- Un experimento con rectángulos encontró que la "preferencia" por el áureo era un **artefacto de la posición del estímulo en el rango** mostrado ([PubMed 4451211](https://pubmed.ncbi.nlm.nih.gov/4451211)).
- Keith Devlin: pocas personas eligen el rectángulo áureo cuando ven una página de rectángulos ([Devlin, MAA, 2007](https://web.archive.org/web/20220225040027/www.maa.org/external_archive/devlin/devlin_05_07.html)).
- La revisión de Green concluye que puede haber efectos psicológicos, pero muy sensibles a errores de método ([Green, *Perception*, 1995](https://journals.sagepub.com/doi/10.1068/p240937)).

**Uso honesto:** φ sirve como *una razón más* para una escala o un split (≈ 62/38). No la uses como argumento de venta ni dibujes espirales sobre logos.

## 2. Escalas modulares

Una escala modular multiplica una base por una razón constante. Tim Brown la propuso para tipo, márgenes y columnas en la web ([*More Meaningful Typography*, A List Apart, 2011](https://alistapart.com/article/more-meaningful-typography/); calculadora en [modularscale.com](https://www.modularscale.com/)). Razones habituales (intervalos musicales):

| Razón | Nombre | Para qué |
|---|---|---|
| 1,125 | segunda mayor | UI densa, dashboards |
| 1,2 | tercera menor | Producto, docs |
| 1,25 | tercera mayor | Marketing equilibrado |
| 1,333 | cuarta justa | Landing con titulares fuertes |
| 1,5 | quinta justa | Editorial, display grande |
| 1,618 | áurea | Solo con pocos pasos; crece muy rápido |

**Qué hace el kit:** la escala de tipo de [`../tokens/`](../tokens/escalas.md#tipo-fluido) no es una progresión geométrica estricta: es fluida (método [Utopia](https://utopia.fyi/type/calculator/)) y ajustada a mano (en el mínimo: 16 → 18 → 20 → 24 → 30 → 40 → 48 px). En la práctica cada paso sube entre 1,125 y 1,33. **No la reemplaces**; si un proyecto pide más dramatismo, subí solo `display` y `h1`, y documentalo en el brief.

La IA tiende a lo contrario: saltos arbitrarios (`text-4xl` → `text-7xl`) en una página y saltos tímidos en otra.

## 3. Medida (largo de línea)

| Fuente | Recomendación |
|---|---|
| Bringhurst, *The Elements of Typographic Style* | 45–75 caracteres; 66 "ideal"; 40–50 en multicolumna (citado en [Rutter, 2024](https://clagnut.com/blog/2432)) |
| Emil Ruder, *Typographie* | 50–60 caracteres (citado por [Baymard](https://baymard.com/research-articles/line-length-readability)) |
| [Baymard, 2022](https://baymard.com/research-articles/line-length-readability) | 50–75 caracteres; sugiere `max-width` ~`70ch` o `34em` |
| [WCAG 2.2, 1.4.8 (AAA)](https://www.w3.org/TR/WCAG22/) | ≤ 80 caracteres (≤ 40 en CJK) |
| Tailwind v4 | `max-w-prose` = `65ch` |

**Matiz con evidencia:** un estudio de 2005 sobre noticias en pantalla midió **mayor velocidad a 95 caracteres** sin cambio en comprensión ([Viget, 2009](https://www.viget.com/articles/the-line-length-misconception)), pero las personas **prefieren y juzgan más fácil** la línea más corta (Mary Dyson, *Legibility*, citada por [Rutter](https://clagnut.com/blog/2432)). Para texto que se quiere leer con gusto (artículo, landing), quedate en 50–75.

**`ch` vs `rem`:** `1ch` es el ancho del "0"; en una fuente condensada o expandida `65ch` no son 65 caracteres reales. Rutter propone fijar la medida en `rem` (ej. `30rem`) cuando hay más de una familia ([Rutter, 2024](https://clagnut.com/blog/2432)). Regla del kit:

```css
.prose { max-inline-size: min(65ch, 100%); }   /* una sola familia de texto */
.prose--mixed { max-inline-size: 34rem; }      /* titular y cuerpo con familias distintas */
```

En móvil la medida la decide el viewport; no fuerces `min-width: 50ch` ([CSS-Tricks](https://css-tricks.com/setting-line-length-in-css-and-fitting-text-to-a-container/)).

## 4. Anchos de contenedor

La escala `--container-*` de Tailwind v4 (verificada en [la doc de max-width](https://tailwindcss.com/docs/max-width) y de [container queries](https://tailwindcss.com/docs/responsive-design)):

| Token | rem | px |
|---|---|---|
| `3xs` | 16 | 256 |
| `2xs` | 18 | 288 |
| `xs` | 20 | 320 |
| `sm` | 24 | 384 |
| `md` | 28 | 448 |
| `lg` | 32 | 512 |
| `xl` | 36 | 576 |
| `2xl` | 42 | 672 |
| `3xl` | 48 | 768 |
| `4xl` | 56 | 896 |
| `5xl` | 64 | 1024 |
| `6xl` | 72 | 1152 |
| `7xl` | 80 | 1280 |

**Tres anchos por proyecto, no siete.** Propuesta del kit (ver [`README.md`](./README.md#propuestas-para-tokens)):

| Rol | Valor | Uso |
|---|---|---|
| `--layout-content` | 42 rem (`2xl`) | Columna de contenido: artículo, formularios, FAQ. El párrafo adentro se limita con `--measure` (`65ch`), porque Baymard asocia ~34 em a ≤ 80 caracteres y 42 rem queda bastante por encima |
| `--layout-wide` | 72 rem (`6xl`) | Secciones con grilla, bento, pricing |
| `--layout-full` | 100 % (con gutter) | Imagen a sangre, bandas de color |

Refactoring UI lo dice simple: no tenés que llenar toda la pantalla; dale a cada elemento el ancho que necesita ([resumen del libro](https://maibuith.com/notes/refactoring-ui); [refactoringui.com](https://refactoringui.com/)).

## 5. Ratios de imagen

Fijalos con `aspect-ratio` (Baseline amplio desde 2024) y `object-fit: cover`. Uno o dos ratios por página.

| Ratio | Uso típico |
|---|---|
| 16 / 9 | Video, capturas de producto apaisadas |
| 3 / 2 | Fotografía (el cuadro de 35 mm) |
| 4 / 3 | Capturas de app, UI con barra |
| 1 / 1 | Avatares, grillas de producto |
| 4 / 5 o 3 / 4 | Retrato, editorial, cards verticales |
| 1200 × 630 | Imagen OG (ver [`../recursos/favicon-og.md`](../recursos/favicon-og.md)) |

```css
.frame { aspect-ratio: var(--ratio, 16 / 9); overflow: hidden; }
.frame > :is(img, video) { inline-size: 100%; block-size: 100%; object-fit: cover; }
```

Es el primitivo **Frame** de [Every Layout](https://every-layout.dev/layouts/frame/). Reserva el espacio y evita saltos de layout (CLS).

## 6. Splits y relaciones de columna

| Split | Sensación | Ejemplo |
|---|---|---|
| 1 : 1 (6/6) | Estable, comparativo | Antes / después, dos planes |
| 7 : 5 | Protagonista + apoyo | Hero texto + captura |
| 2 : 1 (8/4) | Contenido + aside | Artículo + índice |
| 1 : 3 (3/9) | Navegación + trabajo | Docs, app shell |
| ≈ 62 : 38 | "áureo"; casi igual a 8/5 | Cuando querés justificarlo en φ |

El 7/5 y el 8/4 hacen más por romper lo genérico que cualquier efecto: le dan a un lado el rol de protagonista.

## 7. Cuándo importan las proporciones y cuándo no

**Importan (hay evidencia o razón funcional):**
- La **medida** del texto (legibilidad).
- La **consistencia**: Tuch et al. encontraron que la belleza percibida en los primeros 50 ms se asocia a **baja complejidad visual y alta prototipicidad** ([Google Research, 2012](https://research.google/pubs/the-role-of-visual-complexity-and-prototypicality-regarding-first-impression-of-websites-working-towards-understanding-aesthetic-judgments/)); Lindgaard et al. mostraron que ese juicio se forma en 50 ms y se mantiene ([2006](https://doi.org/10.1080/01449290500330448)). Pocas proporciones repetidas bajan la complejidad.
- Los **ratios de imagen** fijos (evitan saltos y collage desparejo).
- El **contraste de escala** entre niveles de jerarquía (ver [`jerarquia-composicion.md`](./jerarquia-composicion.md)).

**No importan tanto (mito o gusto):**
- Que el split sea exactamente φ y no 8/5.
- Espirales áureas sobre composiciones.
- "Regla de los tercios" como ley para UI (es una heurística de fotografía).

Ojo con la prototipicidad: "familiar" ayuda a la primera impresión, pero el kit busca no parecer plantilla. Solución: **estructura familiar** (nav arriba, CTA claro, jerarquía legible) con **decisiones propias** en tipo, color, contenido y un gesto de layout.

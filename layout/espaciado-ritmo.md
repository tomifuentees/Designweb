# Espaciado y ritmo

El espacio es la herramienta de agrupación más barata que existe. Decide qué va con qué antes que cualquier borde, color o card. Los **valores** ya están cerrados en [`../tokens/escalas.md`](../tokens/escalas.md#espacio) (base 4 px, pasos 0–128, `--space-section*`). Este archivo explica **cómo usarlos**.

## 1. Sistema 4 / 8 pt

- El "8-Point Grid" de Bryn Jackson propone múltiplos de 8 para tamaños, padding y márgenes, y un baseline de 4 para el texto; distingue grilla *dura* (todo encaja en celdas de 8) de *blanda* (solo el espacio entre elementos va en pasos de 8) ([spec.fm](https://spec.fm/specifics/8-pt-grid)).
- Material 3 usa márgenes de 16 dp en compacto y 24 dp desde medio ([M3 Breakpoints](https://m3.material.io/foundations/layout/breakpoints)): múltiplos de 8.
- **El kit usa base 4** (`--spacing: 0.25rem` en Tailwind v4) pero el ritmo de layout vive en los pasos **8, 16, 24, 32, 48, 64, 96**. Los pasos 4, 12 y 20 son para el interior de componentes (ícono + label, padding de badge, inputs).

Regla práctica: si un valor de espacio no es un `--space-*`, es un error o una excepción documentada. `gap-[18px]` y `mt-[13px]` son la firma de nadie revisó (ya está en [`../tokens/escalas.md`](../tokens/escalas.md)).

## 2. Proximidad: interno ≤ externo

La ley de proximidad de la Gestalt: lo que está cerca se lee como grupo ([NN/g, Proximity](https://www.nngroup.com/articles/gestalt-proximity/)). En UI se traduce en una regla muy concreta:

> **El espacio dentro de un grupo tiene que ser menor que el espacio entre grupos.** ([Cieden, spacing best practices](https://cieden.com/book/sub-atomic/spacing/spacing-best-practices))

Escalera típica (cada nivel ~1,5–2× el anterior):

| Relación | Paso | Ejemplo |
|---|---|---|
| Ícono ↔ label | `--space-2` (8) | Botón, ítem de menú |
| Label ↔ input; título ↔ su párrafo | `--space-2`–`--space-3` | Formulario, card |
| Ítem ↔ ítem dentro de una lista | `--space-4` (16) | Features, FAQ |
| Bloque ↔ bloque dentro de una sección | `--space-8`–`--space-12` | Heading de sección ↔ grilla |
| Sección ↔ sección | `--space-section` (96) / `-sm` (64) / `-lg` (128) | Landing |

NN/g lo muestra con Spotify: más espacio entre grupos y **menos** entre un heading y su contenido crea la relación jerárquica ([NN/g, Visual Hierarchy](https://www.nngroup.com/articles/visual-hierarchy-ux-definition/)). El error de la IA es el "espacio ambiguo": el título queda a la misma distancia del bloque de arriba que del suyo, y no se sabe a qué pertenece. Refactoring UI lo llama *avoid ambiguous spacing* ([refactoringui.com](https://refactoringui.com/)).

### Espacio antes que cajas

Si el espacio ya agrupa, no hace falta card. Usá **región común** (fondo o borde compartido) solo cuando el espacio no alcanza ([NN/g, Common Region](https://www.nngroup.com/articles/common-region/)), y no para envolver cada párrafo. Ver también [*Spacing Over Cards*](https://smagin.fyi/posts/padding-over-cards/) y el tell 30, "cards dentro de cards", en [`../anti-patrones/catalogo.md`](../anti-patrones/catalogo.md).

## 3. Ritmo vertical

**Ritmo** = el espacio vertical se repite en pocas medidas relacionadas con el interlineado del cuerpo.

```css
/* Flujo de texto: el espacio entre bloques es una línea de cuerpo */
.flow > * + * { margin-block-start: var(--flow-space, 1em); }
.flow :is(h2, h3) { --flow-space: 1.5em; }        /* más aire ANTES del heading… */
.flow :is(h2, h3) + * { --flow-space: 0.5em; }    /* …y menos DESPUÉS (proximidad) */
```

Es el "flow utility" de [Andy Bell / Piccalilli](https://piccalil.li/blog/my-favourite-3-lines-of-css/) y el primitivo **Stack** de [Every Layout](https://every-layout.dev/layouts/stack/). Con `rlh` (Baseline amplio desde mayo de 2026, [web-features](https://web-platform-dx.github.io/web-features-explorer/features/rlh/)) podés atar el espacio al interlineado raíz: `margin-block-start: 1rlh`.

Adam Wathan sugiere en Tailwind v4 fijar el interlineado como paso de la escala de espacio (`text-sm/7`) en lugar de `leading-relaxed`, porque es más predecible ([X, mayo 2025](https://x.com/adamwathan/status/1922049069012160976)). En este kit, el interlineado por rol ya está en `--leading-*`; si un bloque necesita encajar en un ritmo de 4 px, preferí `text-body/6` o `/7` a inventar un multiplicador.

**Baseline estricto vs. ritmo:** el baseline perfecto (cada línea sobre la misma raya en todas las columnas) se rompe con tipo fluido, imágenes e inputs. Para web, apuntá al ritmo.

## 4. Escala de padding de sección

| Token | Valor | Cuándo |
|---|---|---|
| `--space-section-sm` | 64 px | Secciones encadenadas del mismo tema, logos, CTA corto |
| `--space-section` | 96 px | Default de landing |
| `--space-section-lg` | 128 px | Hero, cambio de capítulo, sección "respiro" |

**Variá el padding a propósito.** Todo `py-24` es tan plano como todo `py-8`: una página con ritmo alterna secciones densas y abiertas. Regla: como mínimo dos valores distintos de sección por página, y el más grande alrededor del momento más importante.

Fluido: si querés que el aire crezca con el viewport sin breakpoints, usá un *par* de Utopia (ej. `--space-l-xl`), que interpola entre dos pasos ([Utopia, fluid space](https://utopia.fyi/space/calculator/); [blog](https://utopia.fyi/blog/designing-with-a-fluid-space-palette/)). Detalle y código en [`responsive-fluido.md`](./responsive-fluido.md).

En móvil, reducí el padding de sección a ~60–70 %: `py-16 md:py-24`.

## 5. Densidad

| Nivel | Para qué | Interior de componente | Gap entre ítems | Alto de control |
|---|---|---|---|---|
| **Compacto** | Tablas, dashboards, herramientas pro | `--space-2`/`--space-3` | `--space-2`–`--space-3` | 32 px |
| **Cómodo** (default) | SaaS, formularios, apps | `--space-3`/`--space-4` | `--space-4` | 40 px |
| **Aireado** | Marketing, editorial, onboarding | `--space-6`+ | `--space-6`–`--space-8` | 44–48 px |

- Material define densidad 0, −1, −2, −3: cada paso baja 4 dp la altura del componente ([M2, Applying density](https://m2.material.io/design/layout/applying-density.html); [M3](https://m3.material.io/foundations/layout/grids-spacing/density)).
- Refactoring UI: arrancá con **demasiado** espacio y sacá; la excepción son los dashboards densos a propósito ([texto del capítulo](https://archive.org/stream/RefactoringUIStartWithTooMuchWhiteSpace/Refactoring%20UI%20-%20Start%20with%20too%20much%20white%20space_djvu.txt)).
- **Piso de accesibilidad:** con cualquier densidad, el objetivo táctil mínimo es 24 × 24 px CSS o un círculo de 24 px sin solaparse con otro ([WCAG 2.2, 2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum)). Compacto no puede bajar de ahí.

Una densidad por superficie. Un dashboard compacto con un modal aireado está bien; una tabla con filas de alturas distintas, no.

## 6. Padding desigual (a propósito)

El default de IA es `p-6` en las cuatro caras de todo. Correcciones de oficio:

- **Óptico, no matemático:** un botón con texto en mayúsculas o con ícono a la derecha se ve más equilibrado con un poco más de padding horizontal (`px-4 py-2`, no `p-3`).
- **Cards con media:** la imagen a sangre (padding 0) y el texto con padding; no la imagen "flotando" con el mismo padding que el texto.
- **Radios concéntricos:** si una caja de radio R tiene padding P, el radio interior es R − P (Steve Schoger lo usa para capturas en contenedor, [*Designing with Claude Code*, marzo 2026](https://www.youtube.com/watch?v=lkKGQVHrXzE)).
- **Más aire arriba que abajo en un heading de sección** (proximidad con lo que sigue).

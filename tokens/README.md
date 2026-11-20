# Tokens

Escalas decididas de espacio, radio, sombra, tipo, tracking, leading, motion, breakpoints y z-index, armadas en noviembre de 2026. El color **no** vive acá: vive en [`../paletas/`](../paletas/README.md), con roles. Esta carpeta es lo otro que un modelo improvisa en cada sesión —un `gap-[18px]`, un `rounded-3xl` en todo, un `shadow-xl`, un `text-6xl` con `leading-normal`, un `duration-1000`, un `z-[9999]`— y que, apilado, es una de las razones por las que un frontend de IA se siente ensamblado y no diseñado.

Varios textos de 2025–2026 dicen lo mismo con otras palabras: si el agente no recibe valores fijos, rellena con el promedio. Ver [thanor.ai](https://thanor.ai/blog/design-tokens-for-ai-websites), [Motif](https://motif.asv-labs.com/answers/design-tokens-for-ai-built-frontends/) y el comentario de r/vibecoding del 16 de abril de 2026 que pide un `CLAUDE.md` con tokens, no “un mejor prompt” ([hilo](https://www.reddit.com/r/vibecoding/comments/1rr0dwy/all_ai_websites_and_designs_look_the_same_has/)).

Los archivos de acá siguen el [Design Tokens Format Module 2025.10](https://www.designtokens.org/tr/2025.10/format/) (informe final del Community Group, 28 de octubre de 2025; no es una recomendación W3C) y el `@theme` de [Tailwind CSS v4](https://tailwindcss.com/docs/theme) (v4.0, 22 de enero de 2025).

## Qué hay acá

| Archivo | Contenido |
|---|---|
| [escalas.md](./escalas.md) | El porqué de cada escala, y por qué le gana al default de IA. Desde el 20/11/2026 también compara Carbon, Primer, Polaris y GOV.UK, y suma medidas de app, rampas neutras, radios anidados y easings minados (ver [minado](../recursos/minado-repos.md)) |
| [tokens.css](./tokens.css) | Custom properties listas, con `prefers-reduced-motion`; suma `--ease-out-3/5`, `--ease-in-out-3`, `--shadow-layered` y `--size-*` (medidas de app) |
| [theme-tailwind-v4.css](./theme-tailwind-v4.css) | Bloque `@theme` + `@theme inline` para Tailwind v4 |
| [tokens.json](./tokens.json) | El mismo sistema en formato DTCG 2025.10 |
| [fuentes-investigacion.md](./fuentes-investigacion.md) | Fuentes, con links y fechas |

## Cómo usarlo desde un agente

1. Leé este README y [escalas.md](./escalas.md).
2. Copiá `tokens.css` o el bloque de `theme-tailwind-v4.css`. Pegá **además** los tokens de **una** paleta de [`../paletas/`](../paletas/README.md).
3. En los componentes, usá los nombres (`var(--space-6)`, `rounded-md`, `text-h1`, `duration-[var(--duration-base)]`). No dejes hex, `px` sueltos ni `duration-1000`.
4. Un radio default por proyecto. Una familia de sombras (o ninguna). Una escala de tipo, no `text-4xl` en una página y `text-7xl` en la otra.
5. Respetá `prefers-reduced-motion`. No animes cada sección al scrollear. Ver [`../anti-patrones/`](../anti-patrones/README.md).

La tipografía *de familia* se elige en [`../tipografias/`](../tipografias/README.md); acá solo está la escala de tamaño, el interlineado y el tracking.

La receta de motion (herramientas, microinteracciones, reduced-motion) se desarrolla en [`../animaciones/`](../animaciones/README.md). Esta carpeta solo fija duraciones, easings y la regla de no animar de más.

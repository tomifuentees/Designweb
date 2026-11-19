# Herramientas de paleta (2025–2026)

Herramientas verificadas para construir, previsualizar o exportar paletas con roles, no para pescar cinco hex de un generador y darlos por un sistema. Donde el link respondió, quedó anotado. Donde el crawler falló, está en [fuentes-investigacion.md](./fuentes-investigacion.md).

## Espacio de color y contraste

| Herramienta | Para qué | Link | Notas |
|---|---|---|---|
| OKLCH Color Picker (Evil Martians) | Elegir y convertir OKLCH, con aviso de gamut | [oklch.com](https://oklch.com/) | Open source ([github.com/evilmartians/oklch-picker](https://github.com/evilmartians/oklch-picker)). El punto de partida más sano si vas a escribir `oklch()` a mano. |
| APCA Contrast Calculator (Myndex) | Medir Lc, no solo el ratio WCAG | [apcacontrast.com](https://apcacontrast.com/) | Documentación: [APCA in a Nutshell](https://git.apcacontrast.com/documentation/APCA_in_a_Nutshell.html). Piso útil: Lc 75 para cuerpo, 90 para texto chico exigente, 30 para texto “spot”. Polaridad importa: texto primero, fondo después. |
| WebAIM Contrast Checker | WCAG 2.1 rápido | [webaim.org/resources/contrastchecker](https://webaim.org/resources/contrastchecker/) | Complementa APCA; no lo reemplaza. |
| huekit (Vinod Rajpurohit, 2026) | Hex → OKLCH, rampas 50–950, contraste WCAG/APCA, camino a `@theme` de Tailwind v4 | Anunciado en X, [junio de 2026](https://x.com/doniv01/status/2063469526134427943) | Herramienta chica, zero-dependency, en construcción al momento del anuncio (mix/tailwind/tokens iban llegando). Confirmá el repo/URL actual antes de dependerlo en un pipeline. |

## Sistemas de color ya pensados para UI

| Herramienta | Para qué | Link | Notas |
|---|---|---|---|
| Radix Colors | Rampas de 12 pasos con roles (fondo, componente, borde, sólido, texto) en claro y oscuro | [radix-ui.com/colors](https://www.radix-ui.com/colors) | Escala documentada: 1–2 fondos, 3–5 componentes, 6–8 bordes, 9–10 sólidos, 11–12 texto. El generador de paletas custom trabaja en OKLCH. Mejor punto de partida si necesitás una rampa completa, no solo un acento. |
| Tailwind CSS v4 `@theme` | Definir tokens que se vuelven utilidades | [tailwindcss.com/docs/theme](https://tailwindcss.com/docs/theme) | v4.0 salió el 22 de enero de 2025. Los ejemplos oficiales ya están en OKLCH. Ver también [`../tokens/theme-tailwind-v4.css`](../tokens/theme-tailwind-v4.css). |
| Paleta default de Tailwind | Referencia, no destino | [tailwindcss.com/docs/colors](https://tailwindcss.com/docs/colors) | `indigo-500` es el color que Adam Wathan pidió disculpas por haber puesto en cada botón de Tailwind UI ([7 de agosto de 2025](https://x.com/adamwathan/status/1953510802159219096)). No lo uses como acento por default. |

## Temas para shadcn / productos React

| Herramienta | Para qué | Link | Notas |
|---|---|---|---|
| shadcn/ui Theming | Variables semánticas (`background`, `foreground`, `primary`, `destructive`…) | [ui.shadcn.com/docs/theming](https://ui.shadcn.com/docs/theming) | Con Tailwind v4, shadcn convierte HSL a OKLCH ([docs de Tailwind v4](https://ui.shadcn.com/docs/tailwind-v4)). Partí de acá si el proyecto ya usa shadcn; después cambiale el `primary`. |
| tweakcn | Editor visual de temas para shadcn/ui, exporta CSS, `@theme inline` y CLI | [tweakcn.com](https://tweakcn.com/) | Repo [jnsahaj/tweakcn](https://github.com/jnsahaj/tweakcn/) (Apache-2.0, creado en marzo de 2025). Nace de una observación útil: los sitios con shadcn “se parecen todos”. Usalo para salir del default, no para aplicar un preset violeta y darlo por terminado. |

## Generadores de paleta (con criterio)

| Herramienta | Para qué | Link | Notas |
|---|---|---|---|
| Realtime Colors | Previsualizar texto, fondo, primary, secondary y acento **sobre un sitio de verdad**, con contraste | [realtimecolors.com](https://www.realtimecolors.com/) | Exporta CSS, Tailwind y OKLCH. Lo más útil es la preview, no el “feeling” suelto. |
| Huemint | Paletas por contexto (marca, web, afiche) con un modelo de colorización | [huemint.com](https://huemint.com/) | Sirve para explorar; después formalizá roles y medí contraste. |
| Coolors | Generador rápido, contrast checker, exportes | [coolors.co](https://coolors.co/) | Bien para un puntapié. Mal si te quedás con cinco hex sin roles ni oscuro. La versión Pro agrega extrae-de-imagen y paletas más largas; la base alcanza para explorar. |
| Leonardo (Adobe) | Rampas perceptualmente uniformes, contraste como restricción | [leonardocolor.io](https://leonardocolor.io/) | Útil cuando necesitás una rampa de 10+ pasos que no se “muera” en el medio. |
| Color.js / conversiones | Biblioteca de color del mismo ecosistema CSS Color 4 | [colorjs.io](https://colorjs.io/) | Para scripts, no para “elegir a ojo”. |

## Qué no alcanza

- Un generador de “5 colors for my brand” sin roles, sin modo oscuro y sin contraste.
- Copiar la paleta default de shadcn o de Tailwind y cambiar solo el radio.
- Pedirle a un modelo “una paleta moderna” sin pasarle un estilo de este kit, un acento sacado del tema, y la prohibición explícita del índigo.

Cuando la paleta exista, guardala en tokens (CSS variables +, si el proyecto lo pide, formato DTCG en [`../tokens/tokens.json`](../tokens/tokens.json)) y prohibí hex sueltos en los componentes.

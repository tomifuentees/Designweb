# Recursos

Catálogo de herramientas de terminación, armado en noviembre de 2026. El objetivo no es un dump de “100 tools”: es que un agente deje de resolver cada hueco con el default (Lucide, unDraw en violeta, un MacBook stock, el favicon de Vite, un grain copiado y pegado en el hero) y elija un recurso con licencia, un “cuándo” y un “cuándo no”.

Se lee junto a [`../anti-patrones/`](../anti-patrones/README.md) (Lucide por default, ilustración plástica, mockup genérico, OG de plantilla) y a [`../paletas/herramientas.md`](../paletas/herramientas.md) (color y contraste). Esta carpeta cubre lo que no es paleta ni token: íconos, ilustración, textura, mesh, mockups, placeholders, SVG, capturas y favicon/OG.

Hay **54 recursos** en 9 grupos. Las licencias se anotan con lo que se pudo contrastar; **antes de un uso comercial, confirmá los términos en el sitio**. Varios generadores (fffuel, Haikei, mesh) no son “MIT del asset”: el export suele ser tuyo, pero hay que leer el aviso.

## Qué hay acá

| Archivo | Contenido |
|---|---|
| [iconos.md](./iconos.md) | Phosphor, Tabler, Iconoir, Heroicons, Hugeicons free, Lucide (último recurso), Remix, Radix, Simple Icons, etc. |
| [ilustraciones.md](./ilustraciones.md) | unDraw, Open Peeps, Humaaans, Blush, Storyset, y la prioridad de la foto real |
| [texturas.md](./texturas.md) | fffuel, Haikei, grano CSS, Shader Gradient, Hero Patterns, papeles |
| [gradientes.md](./gradientes.md) | OKLCH picker, mesh, Realtime Colors, Coolors (sin degradé de identidad) |
| [mockups.md](./mockups.md) | shots.so, MockuPhone, Device Frames, Mockuuups, Rotato |
| [imagenes.md](./imagenes.md) | Unsplash, Pexels, Picsum, placehold.co, Dummy Image |
| [svg.md](./svg.md) | SVGOMG, Boxy SVG, Get Waves, Blobmaker, SVG Repo (licencia variable) |
| [capturas.md](./capturas.md) | shots.so, ray.so, Carbon, snappify, Screenzy |
| [favicon-og.md](./favicon-og.md) | RealFaviconGenerator, favicon.io, opengraph.xyz, @vercel/og, OG Playground |
| [recursos.json](./recursos.json) | El mismo catálogo, legible por máquinas |
| [fuentes-investigacion.md](./fuentes-investigacion.md) | Fuentes, con links y fechas |

## Cómo elegir

1. **Un set de íconos por proyecto**, no Lucide por default. Phosphor (duotone) o Tabler cambian la voz con poco esfuerzo. Lo documentó [Om Patel el 7 de marzo de 2026](https://x.com/om_patel5/status/2030310771326861336).
2. **Foto o producto antes que ilustración.** Si ilustrás, un estilo solo, acento de la paleta.
3. **Textura liviana, no un fondo que pelea con el texto.** El grano es un acento del estilo [`grano-ruido`](../estilos/grano-ruido.md).
4. **Mockup de una captura real**, no de una UI inventada.
5. **Favicon y OG hechos**, no los del bundler. Previsualizá el OG.
6. **Leé la licencia.** SVG Repo, Blush, Hugeicons Pro, Storyset y varios generadores no son un MIT universal.

## Cómo usarlo desde un agente

1. Leé este README y el grupo que corresponda.
2. Proponé **un** set de íconos y, si hace falta, **una** fuente de ilustración o textura. No una lista de diez.
3. Advertí la licencia. Si es “varía” o “confirmá términos”, no la des por MIT.
4. No instales Lucide “porque shadcn lo trae” sin avisar que es el default de las UIs AI-coded.

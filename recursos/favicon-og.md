# Favicon y Open Graph

Un favicon de Vite/Next y un OG vacío son tells. Generá un set con RealFaviconGenerator a partir del mark, diseñá el OG con los tokens (Satori / @vercel/og o un PNG) y previsualizalo en opengraph.xyz.

Hay **5 recursos** en este grupo. El catálogo completo está en [`recursos.json`](./recursos.json).

## RealFaviconGenerator

`realfavicongenerator` — [https://realfavicongenerator.net/](https://realfavicongenerator.net/)

**Licencia:** Herramienta (tus assets son tuyos).

**Cuándo usarlo.** Generar el set completo (ICO, apple-touch, android, safari mask, manifest) a partir de un SVG o PNG del mark.

**Cuándo no.** Para ‘inventar’ un isotipo. El input tiene que ser la marca, no un ícono genérico de Lucide.

Sigue siendo la referencia. Un favicon de Vite/Next es un tell (Utsubo / Drop The Hassle).

## favicon.io

`favicon-io` — [https://favicon.io/](https://favicon.io/)

**Licencia:** Herramienta.

**Cuándo usarlo.** Un favicon de texto o un Emoji, para un draft interno, no para una marca seria.

**Cuándo no.** Como isotipo final de un producto (se reconoce, y el emoji como mark es otro tell si se abusa).

Útil en un spike. Después reemplazalo.

## opengraph.xyz

`opengraph-xyz` — [https://www.opengraph.xyz/](https://www.opengraph.xyz/)

**Licencia:** Herramienta de preview.

**Cuándo usarlo.** Inspeccionar cómo se ve el OG de una URL (Twitter/X, Slack, iMessage, LinkedIn) antes de compartir.

**Cuándo no.** Como generador de la imagen: es un previewer.

Obligatorio pasarlo antes de anunciar un lanzamiento.

## @vercel/og + Satori

`vercel-og` — [https://vercel.com/docs/functions/og-image-generation](https://vercel.com/docs/functions/og-image-generation)

**Licencia:** El runtime de Vercel + Satori (licencia del paquete: ver repo).  
**Repo:** https://github.com/vercel/satori

**Cuándo usarlo.** OG dinámicos (título + autor + tema de la paleta) en un sitio Next/Vercel, sin un PNG estático por página.

**Cuándo no.** Si no estás en ese ecosistema y un PNG bien hecho alcanza.

Documentación oficial de Vercel. Diseñá la tarjeta con los tokens del kit, no con el ejemplo violeta.

## OG Image Playground

`og-playground` — [https://og-playground.vercel.app/](https://og-playground.vercel.app/)

**Licencia:** Demo (Satori).

**Cuándo usarlo.** Probar markup de Satori en el browser antes de integrarlo.

**Cuándo no.** Como host de producción de tus OG.

Playground oficial-adyacente del ecosistema Satori.

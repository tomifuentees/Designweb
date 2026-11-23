# Tipografías

Catálogo de tipografías en tendencia y de oficio para diseño web y de producto, armado en noviembre de 2026. El objetivo no es perseguir la moda por la moda: es que un agente de código (o un humano con apuro) deje de abrir un archivo con Inter, Poppins o Montserrat y un degradé violeta, y elija una voz con criterio.

Esta carpeta es la primera pieza de un kit de diseño frontend. Las fichas están pensadas para ser leídas por personas y, también, consumidas por skills de Claude o de otros agentes a través de `fonts.json`.

## Qué hay acá

| Archivo | Contenido |
|---|---|
| [sans-grotesk.md](./sans-grotesk.md) | Grotescas y neo-grotescas (Söhne, Neue Montreal, Cabinet Grotesk, Geist, Mona Sans…) |
| [sans-geometrica.md](./sans-geometrica.md) | Geométricas (Satoshi, Clash Grotesk, Aeonik, Space Grotesk, Cal Sans…) |
| [serif-display.md](./serif-display.md) | Serifs de titular (Fraunces, Editorial New, Signifier, Reckless, Instrument Serif…) |
| [serif-texto.md](./serif-texto.md) | Serifs de lectura (Tiempos Text, Newsreader, Source Serif 4, Literata…) |
| [mono.md](./mono.md) | Monoespaciadas de producto y de código (Geist Mono, JetBrains Mono, Berkeley Mono…) |
| [display-experimental.md](./display-experimental.md) | Display, flares, pixel, lettering e indies (Clash Display, Druk, Obviously, Karrik…) |
| [variable.md](./variable.md) | Fichas variable-first (Recursive, Roboto Flex) y guía de ejes |
| [pairings.md](./pairings.md) | 42 combinaciones titular + cuerpo, con el porqué y el tipo de proyecto (14 sumadas en noviembre de 2026, todas gratis) |
| [fonts.json](./fonts.json) | El mismo catálogo, legible por máquinas |
| [fuentes-investigacion.md](./fuentes-investigacion.md) | Fuentes consultadas, con links |

Hay **122 familias**. 78 son gratis (Google Fonts OFL, Fontshare FFL, GitHub, IBM, repos OFL). 44 son comerciales. 62 tienen corte variable. Las 20 de Google Fonts entraron el 20 de noviembre de 2026 para las parejas nuevas (ver [`../recursos/minado-repos.md`](../recursos/minado-repos.md)); CoFo Friend entró el 23 de noviembre de 2026 (ver [`../novedades/2026-11-23.md`](../novedades/2026-11-23.md)). Cada ficha trae foundry, licencia, link oficial verificado, estilo, usos, pesos, una pareja recomendada y un snippet de import. Si encontramos un sitio real que la usa, también está anotado.

## Cómo elegir una tipografía

1. **Primero el trabajo, después el carácter.** ¿La cara tiene que leerse 40 minutos (cuerpo) o gritarse en un hero (display)? No uses una display como párrafo ni una UI sans como única voz de una marca de lujo.
2. **Dos familias, como máximo tres.** Una para expresión (titular) y una para resistencia (cuerpo, UI, botones). Un mono de acento cuenta como la tercera, y solo si el producto lo pide.
3. **Contrastá roles, no pelees climas.** Una serif editorial + una grotesca quieta funciona. Dos displays gritonas, no.
4. **Si el presupuesto existe, pagá el titular.** Una licencia de Klim, Pangram, Dinamo, Grilli o Commercial Type es de las señales más claras de que el sitio no salió de un prompt. El cuerpo puede ser OFL.
5. **Si el presupuesto no existe, no te quedes en el top de Google Fonts.** Fontshare (Satoshi, Clash, Cabinet, Switzer, Zodiak, Boska), Mona Sans, Bricolage Grotesque, Fraunces, Newsreader o las de Collletttivo rinden mucho más que Poppins.
6. **Probá a 16px y a 72px.** Una geométrica que enamora en el specimen puede fallar en un dashboard. Una serif de alto contraste puede romperse en mobile si no tiene optical size.
7. **Autohospedá.** En producción, serví WOFF2 propio. La API de Fontshare **no garantiza uptime**. La licencia FFL de Fontshare **no permite subsetear ni convertir** el archivo: usá los archivos oficiales tal cual. En Google Fonts (OFL) sí podés subsetear.
8. **Leé la licencia de verdad.** Sobre todo Berkeley Mono, Fontshare FFL y foundries que cobran por tamaño de empresa (Dinamo) o por pageviews (muchas web licenses).

## Reglas anti-IA genérica

Estas caras no están "prohibidas". Varias son excelentes. El problema es usarlas **como default de personalidad**, apiladas con los mismos tics visuales (hero centrado, gradiente violeta o azul, cards de glassmorphism, ilustraciones 3D genéricas).

### Evitá como voz automática de marca

| Familia | Por qué |
|---|---|
| **Inter** | La sans de producto más usada del ciclo 2023-2026. Typewolf la tuvo como #1 en 2023. Emblematic la detecta en decenas de sitios tech. Como UI de apoyo es difícil de superar; como *personalidad* de una PyME argentina, desaparece. |
| **Geist** | Excelente, y por eso ya es el nuevo default de landings de IA y devtools (Vercel, v0, Next.js, Calendly…). Si el producto no es un devtool, no hace falta parecer uno. |
| **Poppins** | Geométrica amable, omnipresente en templates de WordPress, Elementor y en salidas de modelos. Se lee como "la de siempre". |
| **Montserrat** | Inspirada en la señalética de Buenos Aires, irónicamente se volvió la sans genérica global de landings corporativas. |
| **Roboto / Open Sans / Lato / Raleway** | Workhorses de la década anterior. Siguen siendo legibles; ya no dicen nada. Roboto Flex, en cambio, sí puede servir como *motor variable* si el titular tiene carácter. |
| **Playfair Display** | El atajo de "elegante" más gastado de Google Fonts, casi siempre con Inter o Montserrat debajo. Hay mejores serifs: Fraunces, Boska, Zodiak, Editorial, Canela, Signifier. |
| **Instrument Serif** (como cliché) | Bella, gratis, con una itálica memorable. En r/web_design (julio 2026) ya la nombraban como la tendencia que va a envejecer peor. Si la usás, hacelo a propósito y no en la milésima landing "editorial" de un SaaS. |
| **Circular** | Sigue siendo buena, pero mucha gente la lee como "la de Spotify". Licenciarla para parecerse a otra marca no es un atajo inteligente. |

### Gestos que también delatan un diseño de prompt

- Titular en Inter/Poppins Black + un gradiente violeta-azul de fondo.
- Una sola familia para todo, en un solo peso, sin itálica.
- Playfair o Instrument Serif a 80px con tracking apretado y un subtítulo en Inter Regular.
- Geist + Geist Mono en un sitio que no es de software.
- Más de tres pesos cargados "por las dudas".
- Ignorar el optical size cuando la familia lo trae (Fraunces, Newsreader, Source Serif 4, Bricolage).

### Qué hacer en cambio

- Elegí un titular con rareza controlada (Cabinet Grotesk, Bricolage, Fraunces, Clash Display, Syne, Zodiak) y un cuerpo que desaparezca (Satoshi, General Sans, Figtree, Newsreader, Source Serif 4).
- Usá la itálica de verdad, no un bold suelto, para una sola palabra del héroe.
- Si hay presupuesto, una sola cara de foundry (Söhne, Neue Montreal, Signifier, Reckless, Suisse) eleva todo el sistema.
- Dejá que un mono haga de ceja, precio o código, no de párrafo.
- Revisá [pairings.md](./pairings.md) antes de improvisar una pareja.

## Índice de familias

Las 122 fichas, en orden alfabético, con su categoría y tipo de licencia.

| Familia | Categoría | Licencia | Oficial |
|---|---|---|---|
| ABC Arizona Flare | display-experimental | Comercial | https://abcdinamo.com/typefaces/arizona |
| ABC Diatype | sans-grotesk | Comercial | https://abcdinamo.com/typefaces/diatype |
| ABC Oracle | sans-grotesk | Comercial | https://abcdinamo.com/typefaces/oracle |
| Abril Fatface | serif-display | Gratis | https://fonts.google.com/specimen/Abril+Fatface |
| Aeonik | sans-geometrica | Comercial | https://cotypefoundry.com/our-fonts/aeonik |
| Agipo | display-experimental | Comercial | https://radimpesko.com/fonts/agipo |
| Agrandir | sans-geometrica | Comercial | https://pangrampangram.com/products/agrandir |
| Anton | display-experimental | Gratis | https://fonts.google.com/specimen/Anton |
| Aperçu | sans-grotesk | Comercial | https://www.myfonts.com/collections/apercu-font-colophon-foundry |
| Apfel Grotezk | sans-geometrica | Gratis | https://www.collletttivo.it/typefaces/apfel-grotezk |
| Archivo | sans-grotesk | Gratis | https://fonts.google.com/specimen/Archivo |
| Aspekta | sans-geometrica | Gratis | https://github.com/ivodolenc/aspekta |
| Atkinson Hyperlegible | sans-grotesk | Gratis | https://fonts.google.com/specimen/Atkinson+Hyperlegible |
| Atlas Grotesk | sans-grotesk | Comercial | https://commercialtype.com/catalog/atlas |
| Barlow | sans-grotesk | Gratis | https://fonts.google.com/specimen/Barlow |
| Barlow Condensed | display-experimental | Gratis | https://fonts.google.com/specimen/Barlow+Condensed |
| Bebas Neue | display-experimental | Gratis | https://fonts.google.com/specimen/Bebas+Neue |
| Berkeley Mono | mono | Comercial | https://usgraphics.com/products/berkeley-mono |
| Bodoni Moda | serif-display | Gratis | https://fonts.google.com/specimen/Bodoni+Moda |
| Boska | serif-display | Gratis | https://www.fontshare.com/fonts/boska |
| Bricolage Grotesque | sans-grotesk | Gratis | https://fonts.google.com/specimen/Bricolage+Grotesque |
| Cabinet Grotesk | sans-grotesk | Gratis | https://www.fontshare.com/fonts/cabinet-grotesk |
| Cal Sans | sans-geometrica | Gratis | https://cal.com/font |
| Canela | serif-display | Comercial | https://commercialtype.com/catalog/canela |
| Cardinal | serif-display | Comercial | https://productiontype.com/font/cardinal |
| Circular | sans-geometrica | Comercial | https://lineto.com/typefaces/circular |
| Clash Display | display-experimental | Gratis | https://www.fontshare.com/fonts/clash-display |
| Clash Grotesk | sans-geometrica | Gratis | https://www.fontshare.com/fonts/clash-grotesk |
| CoFo Friend | sans-grotesk | Comercial | https://contrastfoundry.com/typeface/cofo-friend |
| Commit Mono | mono | Gratis | https://commitmono.com/ |
| Crimson Pro | serif-texto | Gratis | https://fonts.google.com/specimen/Crimson+Pro |
| Degular | sans-geometrica | Comercial | https://ohnotype.co/fonts/degular |
| Departure Mono | mono | Gratis | https://departuremono.com/ |
| Dia | display-experimental | Comercial | https://www.schick-toikka.com/dia |
| DM Mono | mono | Gratis | https://fonts.google.com/specimen/DM+Mono |
| DM Sans | sans-grotesk | Gratis | https://fonts.google.com/specimen/DM+Sans |
| DM Serif Display | serif-display | Gratis | https://fonts.google.com/specimen/DM+Serif+Display |
| Druk | display-experimental | Comercial | https://commercialtype.com/catalog/druk |
| EB Garamond | serif-texto | Gratis | https://fonts.google.com/specimen/EB+Garamond |
| Editorial New | serif-display | Comercial | https://pangrampangram.com/products/editorial-new |
| Editorial Old | serif-display | Comercial | https://pangrampangram.com/products/editorial-old |
| Epilogue | sans-grotesk | Gratis | https://fonts.google.com/specimen/Epilogue |
| Favorit | sans-grotesk | Comercial | https://abcdinamo.com/typefaces/favorit |
| Feature | serif-display | Comercial | https://commercialtype.com/catalog/feature |
| Figtree | sans-grotesk | Gratis | https://fonts.google.com/specimen/Figtree |
| Fira Code | mono | Gratis | https://fonts.google.com/specimen/Fira+Code |
| Fira Sans | sans-grotesk | Gratis | https://fonts.google.com/specimen/Fira+Sans |
| Founders Grotesk | sans-grotesk | Comercial | https://klim.co.nz/fonts/founders-grotesk/ |
| Fragment Mono | mono | Gratis | https://fonts.google.com/specimen/Fragment+Mono |
| Fraunces | serif-display | Gratis | https://fonts.google.com/specimen/Fraunces |
| Fredoka | display-experimental | Gratis | https://fonts.google.com/specimen/Fredoka |
| Geist | sans-grotesk | Gratis | https://fonts.google.com/specimen/Geist |
| Geist Mono | mono | Gratis | https://fonts.google.com/specimen/Geist+Mono |
| General Sans | sans-grotesk | Gratis | https://www.fontshare.com/fonts/general-sans |
| Gloock | serif-display | Gratis | https://fonts.google.com/specimen/Gloock |
| Graphik | sans-grotesk | Comercial | https://commercialtype.com/catalog/graphik |
| GT Alpina | serif-display | Comercial | https://www.grillitype.com/font/gt-alpina |
| GT America | sans-grotesk | Comercial | https://www.grillitype.com/font/gt-america |
| GT Super | serif-display | Comercial | https://www.grillitype.com/font/gt-super |
| GT Walsheim | sans-geometrica | Comercial | https://www.grillitype.com/font/gt-walsheim |
| Hubot Sans | sans-geometrica | Gratis | https://fonts.google.com/specimen/Hubot+Sans |
| IBM Plex Mono | mono | Gratis | https://fonts.google.com/specimen/IBM+Plex+Mono |
| IBM Plex Sans | sans-grotesk | Gratis | https://fonts.google.com/specimen/IBM+Plex+Sans |
| IBM Plex Serif | serif-texto | Gratis | https://fonts.google.com/specimen/IBM+Plex+Serif |
| Instrument Sans | sans-grotesk | Gratis | https://fonts.google.com/specimen/Instrument+Sans |
| Instrument Serif | serif-display | Gratis | https://fonts.google.com/specimen/Instrument+Serif |
| Inter | sans-grotesk | Gratis | https://rsms.me/inter/ |
| JetBrains Mono | mono | Gratis | https://fonts.google.com/specimen/JetBrains+Mono |
| Jost | sans-geometrica | Gratis | https://fonts.google.com/specimen/Jost |
| Karrik | display-experimental | Gratis | https://gitlab.com/phantomfoundry/karrik_fonts |
| Lexend | sans-geometrica | Gratis | https://fonts.google.com/specimen/Lexend |
| Libre Baskerville | serif-texto | Gratis | https://fonts.google.com/specimen/Libre+Baskerville |
| Libre Bodoni | serif-display | Gratis | https://fonts.google.com/specimen/Libre+Bodoni |
| Literata | serif-texto | Gratis | https://fonts.google.com/specimen/Literata |
| Lora | serif-texto | Gratis | https://fonts.google.com/specimen/Lora |
| Maison Neue | sans-grotesk | Comercial | https://www.myfonts.com/collections/maison-neue-font-milieu-grotesque/ |
| Manrope | sans-grotesk | Gratis | https://fonts.google.com/specimen/Manrope |
| Melodrama | display-experimental | Gratis | https://www.fontshare.com/fonts/melodrama |
| Merriweather | serif-texto | Gratis | https://fonts.google.com/specimen/Merriweather |
| Migra | serif-display | Comercial | https://www.sharptype.co/typefaces/migra |
| Mona Sans | sans-grotesk | Gratis | https://fonts.google.com/specimen/Mona+Sans |
| Monument Grotesk | sans-grotesk | Comercial | https://abcdinamo.com/typefaces/monument-grotesk |
| Necto Mono | mono | Gratis | https://www.collletttivo.it/typefaces/necto-mono |
| Neue Montreal | sans-grotesk | Comercial | https://pangrampangram.com/products/neue-montreal |
| Newsreader | serif-texto | Gratis | https://fonts.google.com/specimen/Newsreader |
| Nunito | sans-geometrica | Gratis | https://fonts.google.com/specimen/Nunito |
| Obviously | display-experimental | Comercial | https://ohnotype.co/fonts/obviously |
| Ogg | serif-display | Comercial | https://www.sharptype.co/typefaces/ogg |
| Onest | sans-geometrica | Gratis | https://fonts.google.com/specimen/Onest |
| Outfit | sans-geometrica | Gratis | https://fonts.google.com/specimen/Outfit |
| Panchang | display-experimental | Gratis | https://www.fontshare.com/fonts/panchang |
| Plus Jakarta Sans | sans-grotesk | Gratis | https://fonts.google.com/specimen/Plus+Jakarta+Sans |
| PP Mori | sans-geometrica | Comercial | https://pangrampangram.com/products/mori |
| Public Sans | sans-grotesk | Gratis | https://fonts.google.com/specimen/Public+Sans |
| Reckless | serif-display | Comercial | https://displaay.net/typeface/reckless/ |
| Recursive | variable | Gratis | https://fonts.google.com/specimen/Recursive |
| Roboto Flex | variable | Gratis | https://fonts.google.com/specimen/Roboto+Flex |
| Roobert | sans-grotesk | Comercial | https://displaay.net/typeface/roobert/ |
| Satoshi | sans-geometrica | Gratis | https://www.fontshare.com/fonts/satoshi |
| Self Modern | serif-display | Comercial | https://www.fonderiebretagne.fr/font/self-modern-regular/ |
| Sentient | serif-texto | Gratis | https://www.fontshare.com/fonts/sentient |
| Shantell Sans | display-experimental | Gratis | https://fonts.google.com/specimen/Shantell+Sans |
| Signifier | serif-display | Comercial | https://klim.co.nz/fonts/signifier/ |
| Sora | sans-geometrica | Gratis | https://fonts.google.com/specimen/Sora |
| Source Sans 3 | sans-grotesk | Gratis | https://fonts.google.com/specimen/Source+Sans+3 |
| Source Serif 4 | serif-texto | Gratis | https://fonts.google.com/specimen/Source+Serif+4 |
| Söhne | sans-grotesk | Comercial | https://klim.co.nz/fonts/soehne/ |
| Space Grotesk | sans-geometrica | Gratis | https://fonts.google.com/specimen/Space+Grotesk |
| Space Mono | mono | Gratis | https://fonts.google.com/specimen/Space+Mono |
| Sprat | display-experimental | Gratis | https://www.collletttivo.it/typefaces/sprat |
| Suisse Int'l | sans-grotesk | Comercial | https://www.swisstypefaces.com/fonts/suisse/ |
| Switzer | sans-grotesk | Gratis | https://www.fontshare.com/fonts/switzer |
| Syncopate | display-experimental | Gratis | https://fonts.google.com/specimen/Syncopate |
| Syne | display-experimental | Gratis | https://fonts.google.com/specimen/Syne |
| Tiempos Headline | serif-display | Comercial | https://klim.co.nz/fonts/tiempos-headline/ |
| Tiempos Text | serif-texto | Comercial | https://klim.co.nz/fonts/tiempos-text/ |
| Topol | display-experimental | Comercial | https://heavyweight-type.com/stuff/topol-poster |
| TWK Lausanne | sans-grotesk | Comercial | https://weltkern.com/typefaces/twk-lausanne |
| Unbounded | display-experimental | Gratis | https://fonts.google.com/specimen/Unbounded |
| Untitled Sans | sans-grotesk | Comercial | https://klim.co.nz/fonts/untitled-sans/ |
| Work Sans | sans-grotesk | Gratis | https://fonts.google.com/specimen/Work+Sans |
| Zodiak | serif-display | Gratis | https://www.fontshare.com/fonts/zodiak |

## Cómo usarlo desde un agente

1. Leé este README y las reglas anti-genéricas.
2. Según el proyecto (SaaS PyME, landing de estudio, dashboard, editorial, lujo, devtool), abrí `fonts.json` o la categoría que corresponda.
3. Proponé **una pareja** (titular + cuerpo), no una lista de diez fuentes.
4. Mostrá el snippet de import y advertí la licencia (sobre todo FFL de Fontshare y comerciales).
5. No presentés Inter, Poppins, Montserrat, Geist o Instrument Serif como primera opción salvo que el brief lo pida o el rol sea de apoyo.

Precios y rankings son una foto de noviembre 2026. Antes de comprar, confirmá la tarifa en la foundry.

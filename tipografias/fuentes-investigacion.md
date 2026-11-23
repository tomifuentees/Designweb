# Fuentes de la investigación

Investigación hecha el 19 de noviembre de 2026 (zona America/Argentina/Salta). Solo se anotaron hechos que se pudieron contrastar: páginas oficiales que respondieron, rankings publicados, hilos de comunidades y detecciones de uso en sitios reales. Donde un dato es aproximado (precios, snapshots de popularidad), queda marcado como tal en la ficha.

Los crawlers no reemplazan una compra: **antes de licenciar, hay que confirmar precio y términos en la foundry**.

## Rankings y observatorios tipográficos

- Typewolf — [Font Usage Data From 2013 to 2026](https://www.typewolf.com/all-fonts). Tops anuales 2024 y 2025 (Söhne, Feature, Neue Montreal, Founders Grotesk, Cardinal, Editorial Old, Signifier, Monument Grotesk, GT Super, Suisse Int'l, Lausanne, Reckless, Tiempos Headline, etc.). El `HEAD` a esta URL a veces no responde; el contenido se obtuvo por GET.
- Typewolf — [Top 10 Most Popular Sans-Serif Fonts of 2026](https://www.typewolf.com/top-10-sans-serif-fonts) (Aperçu aparece primera).
- Typewolf — [Top 10 Most Popular Serif Fonts of 2026](https://www.typewolf.com/top-10-serif-fonts) (Ogg aparece primera).
- Typewolf — portada [What's Trending in Type](https://www.typewolf.com/) (septiembre 2025: Signifier, Switzer, Arizona Flare, Dia, Agipo, Topol, Maison Neue).
- Typewolf — fichas [Feature](https://www.typewolf.com/feature), [Cardinal](https://www.typewolf.com/cardinal), [Editorial Old](https://www.typewolf.com/editorial-old).
- [Fonts In Use](https://fontsinuse.com/) — catálogo de usos documentados (consultado como referencia general; las URLs de uso real de este repo priorizan detecciones de Emblematic y sitios oficiales de foundry).
- [Emblematic: Fonts used by the best-designed websites](https://emblematic.dev/fonts) — detección en sitios reales (Satoshi, Geist, Söhne, Neue Montreal, Suisse Int'l, Graphik, Aperçu, Instrument Sans, Mona/Hubot vía GitHub, TWK Lausanne, Atlas Grotesk, Roobert, IBM Plex Mono, JetBrains Mono, etc.).
- Klim — [Söhne in use](https://klim.co.nz/in-use/all/soehne-collection/).

## Comunidades (Reddit y listados de diseñadores)

- r/webdesign — [Popular fonts for websites in 2025, did I miss anything?](https://www.reddit.com/r/webdesign/comments/1hthj9e/popular_fonts_for_websites_in_2025_did_i_miss/) (enero 2025): Manrope, Urbanist, Satoshi, Aeonik, Plus Jakarta Sans, Space Grotesk, Sora, Cal Sans, Cabinet Grotesk, Geist, Instrument Sans, Switzer, PP Mori, Aspekta, Outfit, etc.
- r/web_design — [Which typography trend do you think will age the worst?](https://www.reddit.com/r/web_design/comments/1upq078/which_typography_trend_do_you_think_will_age_the/) (julio 2026): Instrument Serif y, en general, "todo lo que Claude recomendaría".
- r/typography y r/UXDesign — hilos de recomendaciones de grotescas, superfamilias sans+mono y stacks de producto (2025-2026), usados como contexto, no como única fuente.

X/Twitter se consultó de forma indirecta (Typewolf cita a @typewolf; las foundries anuncian ahí), no como corpus sistemático de posts. No se inventaron tuits.

## Google Fonts y sistemas abiertos

- Fichas de [Google Fonts](https://fonts.google.com/) de cada familia OFL del catálogo (todas las URLs `fonts.google.com/specimen/...` devolvieron 200).
- CSS API de Google Fonts (`fonts.googleapis.com/css2?...`), verificado con GET 200 para Geist, Instrument Serif y Fraunces.
- [Inter, sitio oficial](https://rsms.me/inter/).
- [Geist en GitHub](https://github.com/vercel/geist-font) y ficha en Google Fonts.
- [Mona Sans y Hubot Sans](https://github.blog/news-insights/company-news/introducing-mona-sans-and-hubot-sans/) (GitHub Blog) y specimens en Google Fonts.
- [Instrument Sans](https://github.com/Instrument/instrument-sans).
- [Cal Sans](https://cal.com/font) y [repo calcom/sans](https://github.com/calcom/sans).
- [Aspekta (Ivo Dolenc)](https://github.com/ivodolenc/aspekta).
- [USWDS / Public Sans](https://designsystem.digital.gov/).
- [Atkinson Hyperlegible](https://fonts.google.com/specimen/Atkinson+Hyperlegible) (Braille Institute) y [Atkinson Hyperlegible Next](https://fonts.google.com/specimen/Atkinson+Hyperlegible+Next).

## Fontshare (Indian Type Foundry)

- Catálogo: [Satoshi](https://www.fontshare.com/fonts/satoshi), [Clash Display](https://www.fontshare.com/fonts/clash-display), [Clash Grotesk](https://www.fontshare.com/fonts/clash-grotesk), [General Sans](https://www.fontshare.com/fonts/general-sans), [Cabinet Grotesk](https://www.fontshare.com/fonts/cabinet-grotesk), [Switzer](https://www.fontshare.com/fonts/switzer), [Zodiak](https://www.fontshare.com/fonts/zodiak), [Boska](https://www.fontshare.com/fonts/boska), [Sentient](https://www.fontshare.com/fonts/sentient), [Panchang](https://www.fontshare.com/fonts/panchang), [Melodrama](https://www.fontshare.com/fonts/melodrama). Todas 200.
- Licencia: [ITF Free Font License (FFL)](https://www.fontshare.com/licenses/itf-free-font-license), versión 2.0 del 17 de agosto de 2026. Uso comercial permitido; prohibido modificar, subsetear, convertir o redistribuir el archivo; autohospedaje permitido; API sin garantía de uptime.
- También existe la página de [licencias OFL en Fontshare](https://www.fontshare.com/licenses/sil-ofl) para las familias open source que ellos hostean (este catálogo, en las fichas ITF Originals, asume FFL salvo que la ficha individual diga otra cosa: **confirmalo en cada descarga**).
- CSS API `https://api.fontshare.com/v2/css?f[]=...` verificada (200, devuelve `@font-face` real) para Satoshi, Clash Display y Cabinet Grotesk.
- Popularidad del catálogo: snapshot de agosto 2026 citado por [FontAlternatives (Satoshi)](https://fontalternatives.com/fonts/satoshi/) a partir de la API de Fontshare (Satoshi, Clash Display, General Sans, Cabinet Grotesk, Ranade, Chillax, Clash Grotesk, Switzer). Es un conteo de vistas, no de descargas.

## Foundries comerciales (páginas oficiales)

- Klim Type Foundry — [Söhne](https://klim.co.nz/fonts/soehne/), [Founders Grotesk](https://klim.co.nz/fonts/founders-grotesk/), [Untitled Sans](https://klim.co.nz/fonts/untitled-sans/), [Signifier](https://klim.co.nz/fonts/signifier/), [Tiempos Headline](https://klim.co.nz/fonts/tiempos-headline/), [Tiempos Text](https://klim.co.nz/fonts/tiempos-text/), [FAQs de licencia y precio base (60 USD el primer estilo)](https://klim.co.nz/faqs/). Las URLs antiguas `/retail-fonts/` redirigen a `/fonts/`.
- Pangram Pangram — [catálogo](https://pangrampangram.com/), [Neue Montreal](https://pangrampangram.com/products/neue-montreal), [Editorial New](https://pangrampangram.com/products/editorial-new), [Editorial Old](https://pangrampangram.com/products/editorial-old), [Mori](https://pangrampangram.com/products/mori), [Agrandir](https://pangrampangram.com/products/agrandir). La foundry declara licencias comerciales desde 40 USD.
- Dinamo — [Monument Grotesk](https://abcdinamo.com/typefaces/monument-grotesk), [Favorit](https://abcdinamo.com/typefaces/favorit), [Diatype](https://abcdinamo.com/typefaces/diatype), [Arizona](https://abcdinamo.com/typefaces/arizona), [Oracle](https://abcdinamo.com/typefaces/oracle), [cómo precian](https://abcdinamo.com/news/about-our-pricing), [packs de estudiante](https://abcdinamo.com/students).
- Grilli Type — [GT America](https://www.grillitype.com/font/gt-america), [GT Alpina](https://www.grillitype.com/font/gt-alpina), [GT Super](https://www.grillitype.com/font/gt-super), [GT Walsheim](https://www.grillitype.com/font/gt-walsheim) y shops de cada una (precios de estilo y de familia, 2026).
- Swiss Typefaces — [Suisse](https://www.swisstypefaces.com/fonts/suisse/), [purchase](https://www.swisstypefaces.com/support/purchase/), [licensing](https://www.swisstypefaces.com/licensing/).
- Lineto — [Circular (pricing)](https://lineto.com/typefaces/circular).
- Commercial Type — [Feature](https://commercialtype.com/catalog/feature), [Graphik](https://commercialtype.com/catalog/graphik), [Canela](https://commercialtype.com/catalog/canela), [Druk](https://commercialtype.com/catalog/druk), [Atlas](https://commercialtype.com/catalog/atlas).
- Production Type — [Cardinal](https://productiontype.com/font/cardinal).
- Displaay — [Reckless](https://displaay.net/typeface/reckless/), [Roobert](https://displaay.net/typeface/roobert/), [licencias](https://displaay.net/help/licenses).
- Sharp Type — [Ogg](https://www.sharptype.co/typefaces/ogg), [Migra](https://www.sharptype.co/typefaces/migra). El sitio devolvió **429** (challenge de Vercel) al crawler; no es un 404. Se conservan las URLs canónicas de la foundry, cruzadas con Typewolf.
- CoType Foundry — [Aeonik](https://cotypefoundry.com/our-fonts/aeonik), [licensing](https://cotypefoundry.com/licensing). Precio de Full Family desktop contrastado con el shop (336 GBP, hasta 2 workstations).
- WELTKERN — [TWK Lausanne](https://weltkern.com/typefaces/twk-lausanne).
- U.S. Graphics Company — [Berkeley Mono](https://usgraphics.com/products/berkeley-mono) y tramos de precio del catálogo (Developer 75 USD; comercial por tamaño de empresa).
- Schick Toikka — [Dia](https://www.schick-toikka.com/dia).
- Radim Peško — [Agipo](https://radimpesko.com/fonts/agipo).
- Heavyweight — [Topol Poster](https://heavyweight-type.com/stuff/topol-poster), [foundry](https://heavyweight-type.com/).
- Bretagne Type Foundry — [Self Modern Regular](https://www.fonderiebretagne.fr/font/self-modern-regular/).
- Oh no Type Co. — [Obviously](https://ohnotype.co/fonts/obviously), [Degular](https://ohnotype.co/fonts/degular).
- Colophon Foundry — [sitio](https://www.colophon-foundry.org/) (200). La ficha `/typefaces/apercu` dio **404**; Aperçu se documenta vía [MyFonts / Colophon](https://www.myfonts.com/collections/apercu-font-colophon-foundry).
- Milieu Grotesque — `milieugrotesque.com` redirige a MyFonts. Maison Neue se documenta en [la colección de MyFonts](https://www.myfonts.com/collections/maison-neue-font-milieu-grotesque/).

## Foundries indie y OFL fuera de Google

- Collletttivo — [catálogo](https://www.collletttivo.it/typefaces), [licencia](https://www.collletttivo.it/licensing), [Apfel Grotezk](https://www.collletttivo.it/typefaces/apfel-grotezk), [Sprat](https://www.collletttivo.it/typefaces/sprat), [Necto Mono](https://www.collletttivo.it/typefaces/necto-mono).
- Karrik — repo canónico [gitlab.com/phantomfoundry/karrik_fonts](https://gitlab.com/phantomfoundry/karrik_fonts) (diseño de Jean-Baptiste Morizot y Lucas Le Bihan; OFL). El sitio de [Velvetyne](https://velvetyne.fr/) en noviembre 2026 redirigía las fichas de fuentes a una campaña (`/greve/`); por eso no se usó `velvetyne.fr/fonts/karrik/` como link de ficha. También [type-atlas.xyz/typeface/karrik](https://type-atlas.xyz/typeface/karrik/).
- [Departure Mono](https://departuremono.com/).
- [Commit Mono](https://commitmono.com/).

## Artículos y guías de tendencias 2025-2026

Usados para cruzar *qué se está recomendando*, no como prueba de uso real ni de precio:

- [Font Trends 2026 — Gleam Studio](https://www.gleamstudio.design/blog-post/font-trends-2026) (Fraunces, Instrument Serif, Gloock, Bricolage, Space Grotesk, Syne, Geist, Onest, Figtree, Atkinson, Unbounded, Shantell Sans, etc.).
- [Web Typography Trends 2026 — Made Good Designs](https://madegooddesigns.com/web-typography-trends-2026/) y [Best New Google Fonts of 2026](https://madegooddesigns.com/best-new-google-fonts-2026/).
- [Typography trends 2026 — S Evans Design](https://www.sophie-evans.com/blog/type-trends-worth-keeping).
- [15 Best Free Fonts for Modern UI Design (2026) — Mantlr](https://mantlr.com/blog/15-best-free-fonts-modern-ui-design-2026).
- [Best Web Fonts of 2026 — Fueled by Punch](https://www.fueledbypunch.com/blog/best-web-fonts-2026).
- [Font Pairing Chart for Web design (2026) — Elementor](https://elementor.com/blog/font-pairing-chart/) (se usó con escepticismo: varias parejas son justamente los defaults a evitar).
- [How to pair fonts for a website — Sundry Mill](https://sundrymill.com/blog/font-pairing-website-free-fonts) (Instrument Serif + Satoshi, Fraunces + Karla, Departure Mono + Inter).
- [Best Google Font Pairings for UI Design in 2025 — Matt Medley](https://medley.ltd/blog/best-google-font-pairings-for-ui-design-2025/).
- [Top Google Fonts by usage — StackScan](https://www.stackscan.com/fonts/google-fonts) (Inter, Poppins, Geist, Fraunces, Instrument Serif/Sans, Figtree, etc., como dato de mercado, no como recomendación).
- [BGR sobre Aperçu como sans popular en Typewolf 2026](https://www.bgr.com/2238361/most-popular-web-font-2026/).
- Referencias de precio cruzadas: [typecase.dev (Söhne, Untitled Sans, Suisse Int'l)](https://typecase.dev/), shops de Grilli, Dinamo, Pangram, Displaay, CoType, U.S. Graphics y MyFonts para Aperçu.

## Qué se verificó con curl (y qué no)

- Se hizo `HEAD`/`GET` con redirecciones a las URLs oficiales del catálogo. Se **descartaron** como link de ficha las que dieron 404 (por ejemplo `colophon-foundry.org/typefaces/apercu`) y las que redirigen a otra cosa (Velvetyne `/fonts/karrik/` → `/greve/`).
- Se **conservaron** las de Sharp Type pese al 429: no es un recurso inexistente, es un antibot.
- Typewolf `/all-fonts` a veces no responde al `HEAD`; el contenido se leyó por fetch y se cita igual.
- Los sitios de *uso real* (stripe.com, vercel.com, etc.) se anotan porque una fuente de detección (Emblematic, foundry in-use o el propio dueño de la fuente) los declara. No se inspeccionó el CSS de cada uno en esta pasada: si un sitio cambió de familia, la ficha puede quedar desactualizada. Preferí no inventar usos no soportados.
- No se copió texto largo de specimens ni de sitios de foundry; las descripciones de estilo son síntesis propias a partir de esas fuentes.

## Fecha y límites

- Foto del 19 de noviembre de 2026.
- No es un directorio exhaustivo de todas las tipografías buenas del mundo: es un estante de trabajo para no caer en el default de IA, con sesgo hacia lo que se está viendo en diseño web de EE. UU. y Europa (Typewolf, Reddit, foundries, Google Fonts, Fontshare) y con un puñado de voces indie (Collletttivo, Velvetyne/Karrik, Oh no, Heavyweight, Bretagne).
- Faltan, a propósito o por falta de ficha verificable en esta pasada, varias caras que valdría sumar en una segunda ronda: Basis Grotesque, Untitled Serif, PP Neue Corp, Right Grotesk, Proto Grotesk, Inclusive Sans, Lexend, Hanken Grotesk, Schibsted Grotesk, Gambarino, Ranade, Commit/MD IO, MonoLisa, y más del catálogo vivo de Velvetyne cuando su sitio de fuentes vuelva a servir fichas.

## Novedades del 23 de noviembre de 2026

- [The Font News, archivo](https://www.thefontnews.com/archive) (consultado el 23/11/2026): lanzamientos del 16 al 23 de noviembre de 2026. Se sumó **CoFo Friend** (Contrast Foundry, 18/11/2026) por ser la única pensada explícitamente para interfaces. Ficha oficial: [contrastfoundry.com/typeface/cofo-friend](https://contrastfoundry.com/typeface/cofo-friend) (200 el 23/11/2026). Detalle técnico (cifras tabulares, masters): [D1S1, 18/11/2026](https://d1s1.com/studio/Contrast%20Foundry/cofo-friend-Is-it-the-curves-or-are-we-just-getting-along).
- Vistas y no sumadas (display o editoriales sin ficha web verificada en esta pasada): Reaktor (Nguyen Gobber), KH Meka (KH Type), Costumes (Formagari), Polymode (XYZ Type), Ocote Mono (CocijoType), Haffner Text y Parling (Kent Lew), Conviva (Fincker), Victory (G-Type), BVH Eddi Line. Quedan para una ronda de display/editorial.

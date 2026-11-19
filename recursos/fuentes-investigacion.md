# Fuentes de la investigación

Investigación hecha el 19 de noviembre de 2026 (zona America/Argentina/Salta). Los links se pasaron por una verificación HTTP en esa fecha; el resultado queda más abajo, en la pasada de `curl` del kit.

## Por qué estos recursos (y no Lucide por default)

- Om Patel — [How to make your AI-coded UI actually stand out](https://x.com/om_patel5/status/2030310771326861336), 7 de marzo de 2026: Lucide como default de las UIs AI-coded.
- Listados de 2026 que mencionan Phosphor, Tabler, Hugeicons y Heroicons como alternativas (p. ej. [Terra, 31 de agosto de 2026](https://x.com/terraxezn/status/2094554548098777278)); se usaron como pista, no como autoridad única. Cada set se contrastó con su sitio oficial.
- Utsubo — [The "Built with AI" Tell](https://www.utsubo.com/blog/built-with-ai-trust-signals-2026), 23 de junio de 2026 (ilustración plástica, OG/meta de plantilla).
- Drop The Hassle — [12 fixes](https://dropthehassle.com/guides/make-website-look-less-ai), 1 de octubre de 2026 (dominio y terminación; favicon/OG).

## Sitios oficiales (a verificar con curl)

Phosphor, Tabler, Iconoir, Heroicons, Hugeicons (y [su FAQ de licencia](https://hugeicons.com/docs/faqs/license-questions)), Lucide, Remix Icon, Radix Icons, Simple Icons, Material Symbols, Icônes, unDraw, Open Peeps, Humaaans, Blush, Storyset, Unsplash, Pexels, fffuel, Haikei, Shader Gradient, Hero Patterns, Transparent Textures, oklch.com, whatamesh, CSS Hero Mesher, Realtime Colors, Coolors, shots.so, MockuPhone, Device Frames, Mockuuups, Rotato, Picsum, placehold.co, Dummy Image, SVGOMG, Boxy SVG, Get Waves, Blobmaker, SVG Repo, ray.so, Carbon, snappify, Screenzy, RealFaviconGenerator, favicon.io, opengraph.xyz, docs de [@vercel/og](https://vercel.com/docs/functions/og-image-generation), [OG Playground](https://og-playground.vercel.app/).

## Qué no se pudo verificar o se dejó afuera

- Herramientas muy nuevas citadas en búsquedas de 2026 (Tinapps, ShapeKiln, Wensity noise, Screenshooter de Frontier.sh, bruhgrow) **no se incluyen en el catálogo principal** hasta confirmar URL, licencia y que no son un write-up aislado. Si el `curl` de esta pasada las resuelve bien, se pueden sumar en una segunda ronda.
- Licencias de unDraw, Storyset, Haikei, fffuel y varios generadores: el texto vigente puede cambiar. En las fichas se pide confirmarlo en el sitio, no se finge un MIT.
- El pack Pro de Hugeicons: no es MIT. Solo el free se documenta como MIT, según su FAQ.
- heroicons.dev aparece en listados como mirror; la URL canónica que se cita es [heroicons.com](https://heroicons.com/).

## Verificación HTTP (19 de noviembre de 2026)

- Casi todos los sitios oficiales de este catálogo respondieron **200**.
- [Unsplash](https://unsplash.com/) devolvió **401** al crawler (no es un 404: el sitio existe y bloquea este cliente). Se conserva la URL canónica.
- [opengraph.xyz](https://www.opengraph.xyz/) devolvió **429** (rate limit) en esta pasada, no un 404. Se conserva.
- El ejemplo de Picsum `https://picsum.photos/seed/maat/1600/900` respondió **200** por GET.
- Herramientas 2026 citadas en búsquedas (Tinapps, ShapeKiln, Wensity, Screenshooter, bruhgrow) siguen **afuera** del catálogo principal, a propósito, hasta una segunda ronda de licencia y producto.

# Fuentes de la investigación

Investigación hecha el 19 de noviembre de 2026 (zona America/Argentina/Salta). Solo se anotaron hechos que se pudieron contrastar: páginas oficiales, hilos con fecha, posts de X recuperados con id, y documentación de formatos. No se inventaron tuits ni threads.

## Por qué el violeta / el slop de color

- Adam Wathan — [disculpa por `bg-indigo-500`](https://x.com/adamwathan/status/1953510802159219096), 7 de agosto de 2025, 17:37 UTC (14:37, America/Argentina/Salta). Verificado vía búsqueda en X.
- r/web_design — [AI has a Purple Problem](https://www.reddit.com/r/web_design/comments/1nx0wus/ai_has_a_purple_problem/), 3 de octubre de 2025. Eco en r/webdev: [1nx0y4q](https://www.reddit.com/r/webdev/comments/1nx0y4q/ai_has_a_purple_problem/).
- r/vibecoding — [Why is every vibe coded website purple?](https://www.reddit.com/r/vibecoding/comments/1nx14zc/why_is_every_vibe_coded_website_purple_i_went_to/), octubre de 2025.
- r/webdesign — [Why is every AI website designed the same?](https://www.reddit.com/r/webdesign/comments/1m2om61/why_is_every_ai_website_designed_the_same/).
- r/vibecoding — [Why do all AI generated websites look the same](https://www.reddit.com/r/vibecoding/comments/1o18bb4/why_do_all_ai_generated_websites_look_the_same/), 8 de octubre de 2025.
- r/web_design — [Every Vibecoded websites looks the same](https://www.reddit.com/r/web_design/comments/1uzascg/every_vibecoded_websites_looks_the_same/), 17 de julio de 2026.
- r/vibecoding — [All AI websites look the same, has anyone managed an "anti AI slop design" patterns?](https://www.reddit.com/r/vibecoding/comments/1rr0dwy/all_ai_websites_and_designs_look_the_same_has/), 11 de marzo de 2026. Un comentario del 16 de abril de 2026 insiste en un `CLAUDE.md` con tokens, no en “un mejor prompt”.
- Pranav Desai — [10 tells of a slop ui](https://godobject.dev/blog/10-tells-of-slop/), 27 de septiembre de 2026. Discusión: [Hacker News, 386 puntos](https://news.ycombinator.com/item?id=49867038) (11:41, America/Argentina/Salta).
- prg.sh — [Why Your AI Keeps Building the Same Purple Gradient Website](https://prg.sh/ramblings/Why-Your-AI-Keeps-Building-the-Same-Purple-Gradient-Website), 26 de octubre de 2025.
- Jocelyn Lecamus / Utsubo — [The "Built with AI" Tell: 12 Signals That Drop Trust (2026)](https://www.utsubo.com/blog/built-with-ai-trust-signals-2026), 23 de junio de 2026.
- Drop The Hassle — [Make your website look less AI: 12 fixes](https://dropthehassle.com/guides/make-website-look-less-ai), actualizado el 1 de octubre de 2026.

## Tokens, OKLCH, Tailwind, shadcn

- Tailwind CSS — [v4.0 announcement](https://tailwindcss.com/blog/tailwindcss-v4), 22 de enero de 2025 (CSS-first, `@theme`, ejemplos en OKLCH). Docs: [Theme variables](https://tailwindcss.com/docs/theme), [Functions and directives](https://tailwindcss.com/docs/functions-and-directives).
- Design Tokens Community Group — [Format Module 2025.10](https://www.designtokens.org/tr/2025.10/format/), Final Community Group Report, 28 de octubre de 2025. [Color Module 2025.10](https://www.designtokens.org/tr/2025.10/color/). Anuncio: [“reaches first stable version”](https://www.w3.org/community/design-tokens/2025/10/28/design-tokens-specification-reaches-first-stable-version/).
- shadcn/ui — [Theming](https://ui.shadcn.com/docs/theming), [Tailwind v4](https://ui.shadcn.com/docs/tailwind-v4) (HSL → OKLCH en proyectos nuevos).
- tweakcn — [tweakcn.com](https://tweakcn.com/), repo [jnsahaj/tweakcn](https://github.com/jnsahaj/tweakcn/) (creado el 13 de marzo de 2025, Apache-2.0).
- Radix Colors — [Understanding the scale](https://www.radix-ui.com/colors/docs/palette-composition/understanding-the-scale), [Custom palettes](https://www.radix-ui.com/colors/docs/overview/custom-palettes).
- Evil Martians — [oklch.com](https://oklch.com/), [evilmartians/oklch-picker](https://github.com/evilmartians/oklch-picker).
- Realtime Colors — [realtimecolors.com](https://www.realtimecolors.com/).
- Huemint — [huemint.com](https://huemint.com/).
- Coolors — [coolors.co](https://coolors.co/).
- Leonardo Color — [leonardocolor.io](https://leonardocolor.io/).
- APCA — [apcacontrast.com](https://apcacontrast.com/), [APCA in a Nutshell](https://git.apcacontrast.com/documentation/APCA_in_a_Nutshell.html).
- thanor.ai — [Design tokens for AI-built websites, in the W3C format](https://thanor.ai/blog/design-tokens-for-ai-websites).
- Motif / ASV Labs — [AI Frontends Look Alike? Start With Design Tokens](https://motif.asv-labs.com/answers/design-tokens-for-ai-built-frontends/).
- Vinod Rajpurohit (@doniv01) — [huekit, 7 de junio de 2026](https://x.com/doniv01/status/2063469526134427943) y actualizaciones del 8 de junio. Herramienta anunciada; la URL estable del paquete hay que confirmarla al usarla (ver “Qué no se pudo verificar”).

## Contraste de esta carpeta

Los valores WCAG 2.1 se calcularon con [ColorAide](https://facelessuser.github.io/coloraide/). Los valores APCA-W3, con el paquete oficial [`apca-w3`](https://www.npmjs.com/package/apca-w3) 0.1.9 (algoritmo de Myndex). Las conversiones a OKLCH salen de ColorAide sobre sRGB. Los hex se guardan en minúsculas de 6 dígitos.

## Qué no se pudo verificar

- El aspecto visual pixel a pixel de algunos sitios de referencia (Linear, Raycast, Mercury) en esta pasada: las paletas **no** copian sus hex; se inspiran en la disciplina de “un acento” documentada en las fichas de estilo.
- Una URL canónica estable de huekit como producto instalable (el anuncio en X es real; el repo/paquete puede haber cambiado de nombre o de host).
- El post original de hereticpleb.vercel.app que HN enlazó como espejo de “Tells of a Slop UI”: se cita la versión en [godobject.dev](https://godobject.dev/blog/10-tells-of-slop/), que es la que respondió con el texto completo, y el hilo de HN.
- Un corpus exhaustivo de X más allá de las búsquedas hechas el 19 de noviembre de 2026. No se inventaron tuits; solo se citan posts recuperados con id y fecha.
- Algunas landing de marketing que bloquean crawlers. Si un link de herramienta aparece en [herramientas.md](./herramientas.md), se intentó abrir; el resultado del `curl` queda en la pasada de verificación del kit.

## Verificación HTTP (19 de noviembre de 2026)

Se hizo `HEAD`/`GET` con un UA de browser a los links de esta carpeta.

- La calculadora APCA en `www.myndex.com/APCA` **no resolvió** desde este entorno (fallo de conexión). Se cita en su lugar [apcacontrast.com](https://apcacontrast.com/) (200) y la doc [APCA in a Nutshell](https://git.apcacontrast.com/documentation/APCA_in_a_Nutshell.html) (200; la URL es case-sensitive: `...Nutshell.html`). También respondió [apcaw3.myndex.com](https://apcaw3.myndex.com/).
- El anuncio del DTCG en `w3.org/community/design-tokens/2025/10/28/...` devolvió **403** al crawler. El [Format Module 2025.10](https://www.designtokens.org/tr/2025.10/format/) y el [Color Module](https://www.designtokens.org/tr/2025.10/color/) sí respondieron 200.
- `npmjs.com/package/apca-w3` devolvió **403** al crawler (el paquete se usó en local, versión 0.1.9, para medir Lc).
- Hacker News respondió 405 al `HEAD` y **200** al `GET`.

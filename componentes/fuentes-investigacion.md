# Fuentes de la investigación (componentes)

Investigación hecha el 19 de noviembre de 2026 (zona America/Argentina/Salta). Solo se anotaron hechos contrastables: docs oficiales, repos, posts de X de las cuentas oficiales, changelogs y un puñado de hilos de Reddit. No se inventaron tuits ni stars de GitHub: los números de stars y de “último push” salen de la API pública de GitHub, ese mismo día, y van a cambiar.

## Docs y anuncios oficiales (2025–2026)

- shadcn/ui — [Registry Directory](https://ui.shadcn.com/docs/registry/registry-index), [Namespaces](https://ui.shadcn.com/docs/registry/namespace), [GitHub Registries](https://ui.shadcn.com/docs/registry/github), [registry-item.json](https://ui.shadcn.com/docs/registry/registry-item-json) (GET 200). [July 2026 - Base UI as the Default](https://ui.shadcn.com/docs/changelog/2026-07-base-ui-default) (GET 200): `init` y docs pasan a Base UI; Radix sigue soportado (`-b radix`).
- Base UI — [base-ui.com](https://base-ui.com/) (GET 200). [MUI Update: 2026 and beyond](https://mui.com/blog/2026-and-beyond/) (GET 200): MUI Base deprecado, Base UI estable como dirección fundacional. Changelog del repo [mui/base-ui](https://github.com/mui/base-ui): v1.9.0, 9 de octubre de 2026.
- Radix — [Releases](https://www.radix-ui.com/primitives/docs/overview/releases) (consultado vía búsqueda y docs; el sitio raíz GET 200). Releases listadas hasta el 20 de julio de 2026.
- coss / Origin — [coss.com/ui/docs](https://coss.com/ui/docs), [roadmap](https://coss.com/ui/docs/roadmap), [coss.com/origin](https://coss.com/origin), [cosscom/ui](https://github.com/cosscom/ui) (MIT). [Cal.com v5.8, 15 de octubre de 2025](https://cal.com/blog/calcom-v5-8) (GET 200): lanzamiento de coss ui. El post de lanzamiento todavía advertía early development y Base UI en beta; eso era verdad en octubre de 2025, no en noviembre de 2026 (Base UI ya es estable).
- Kibo — [kibo-ui.com](https://www.kibo-ui.com/) (GET 200). [Shadcnblocks acquires Kibo UI](https://www.shadcnblocks.com/blog/announcing-kibo-ui-acquisition), Rob Austin, 28 de octubre de 2025 (GET 200). Repo [shadcnblocks/kibo](https://github.com/shadcnblocks/kibo), MIT.
- Tremor — [tremor.so](https://www.tremor.so/) (GET 200). [Vercel acquires Tremor](https://vercel.com/blog/vercel-acquires-tremor) (22 de enero de 2025, GET 200). npm `@tremor/react` 3.18.7, 13 de enero de 2025. Repo `tremorlabs/tremor` con push el 10 de octubre de 2025 en esta pasada.
- Magic UI MIT (repo `magicuidesign/magicui`). Pro: [pro.magicui.design/license](https://pro.magicui.design/license). Aceternity Pro: [ui.aceternity.com/licence](https://ui.aceternity.com/licence) (GET 200).
- Animate UI — [LICENSE.md](https://raw.githubusercontent.com/imskyleen/animate-ui/main/LICENSE.md) leída el 19/11/2026: MIT + Commons Clause, copyright 2025 Elliot Sutton.
- Cult UI MIT (repo `nolly-studio/cult-ui`). Motion Primitives MIT (repo `ibelick/motion-primitives`). HeroUI Apache-2.0 (`heroui-inc/heroui`). Park UI: sitio [park-ui.com](https://park-ui.com/) GET 200; no se copió el SPDX en esta pasada, confirmar en el repo antes de un dictamen legal.
- Ark UI [ark-ui.com](https://ark-ui.com/) (MIT, `chakra-ui/ark`). React Aria [react-aria.adobe.com](https://react-aria.adobe.com/) (Apache-2.0, `adobe/react-spectrum`; el path viejo redirige).
- 21st.dev [21st.dev](https://21st.dev/) (GET 200), tratado como directorio, no como librería única.

## Posts de X (cuentas oficiales, no inventados)

- [@coss_com, 10 de octubre de 2025](https://x.com/coss_com/status/1976668768312123777): Origin UI se une a Cal.com y pasa a coss.
- [@peer_rich, 10 de octubre de 2025](https://x.com/peer_rich/status/1976671512305213770): primera acquisition, infraestructura open source.
- [@coss_com, 15 de octubre de 2025](https://x.com/coss_com/status/1978416552266334299): lanzamiento de coss ui / Product Hunt.
- [@shadcn, 16 de enero de 2026](https://x.com/shadcn/status/2012155552064028874): componentes Base UI no son un port automático de Radix; el ecosistema de terceros todavía era, en esa fecha, mayormente Radix.
- [@shadcn, 16 de enero de 2026](https://x.com/shadcn/status/2012267845330038867): descubrir registries y combinar Radix + Base UI vía CLI.
- [@shadcn, 20 de enero de 2026](https://x.com/shadcn/status/2013641788745978276): docs de Base UI en shadcn.
- [@shadcn, 6 de marzo de 2026](https://x.com/shadcn/status/2029974156620517585): shadcn/skills para agentes.
- [@shadcn, 3 de julio de 2026](https://x.com/shadcn/status/2073021588044206483) y [hilo relacionado](https://x.com/shadcn/status/2073021583157837965): Base UI como default.

## Reddit

Hilos ya leídos para la carpeta de estilos, el 19 de noviembre de 2026, y reutilizados acá porque describen el *layout* no solo la tipografía (todos GET 200 en aquella pasada):

- [Every Vibecoded websites looks the same](https://www.reddit.com/r/web_design/comments/1uzascg/every_vibecoded_websites_looks_the_same/) (julio 2026): hero enorme, degradé, tres columnas de features.
- [What makes a ui look AI generated?](https://www.reddit.com/r/web_design/comments/1wkwns6/what_makes_a_ui_look_ai_generated/) (septiembre 2026): happy path, cards para todo, spacing demasiado parejo.
- [What element of AI designs that is overused](https://www.reddit.com/r/web_design/comments/1xa8ug1/what_element_of_ai_designs_that_is_overused/) (octubre 2026): eyebrow, cards iguales, emoji-ícono.
- [What makes an AI-generated website feel generic?](https://www.reddit.com/r/web_design/comments/1wu1yvk/what_makes_an_aigenerated_website_feel_generic/) (septiembre 2026): misma estructura de página (hero, cards, logos, testimonials, pricing, FAQ).

No se usó un hilo como prueba de que una librería esté “muerta” o “sea la mejor”.

## Qué se verificó con curl (y qué no)

GET con redirecciones y User-Agent de Chrome, 19 de noviembre de 2026. Se conservaron 200 y equivalentes de sitio vivo. Stars y `pushed_at` vía API de GitHub el mismo día.

Se **conservaron** con salvedad, no como 404: ninguno crítico de esta carpeta falló por 404. Park UI y 21st.dev resolvieron 200; no se auditó el código de Park UI.

## Qué no se pudo verificar

- Un anuncio oficial de Vercel o Tremor que diga, en 2026, “Tremor está deprecado”. El ritmo bajo (npm de enero de 2025, repo octubre de 2025) está documentado; la interpretación “el trabajo se fue a shadcn” aparece en comunidades y no se tomó como hecho oficial.
- La licencia SPDX de Park UI (el sitio vive; no se leyó el archivo de licencia en esta pasada).
- El número exacto de componentes de Magic UI / Aceternity / Origin en el momento de leer: los “150+” o “600+” de blogs de terceros no se copiaron como cifra propia.
- Tailwind Plus “cerrado a nuevos clientes desde el 9 de septiembre de 2026”: apareció en un comparativo de terceros y **no se verificó** en un anuncio oficial de Tailwind Labs, así que no se documenta como hecho.
- El aspecto visual actual, píxel a píxel, de cada sitio de ejemplo (Stripe, Cal.com, etc.).

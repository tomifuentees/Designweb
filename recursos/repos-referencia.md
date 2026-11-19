# Repositorios de referencia

Lista de repos bien calificados, del mismo tipo que Designweb, para seguir alimentando el kit. **Ninguno de estos estaba ya en los JSON ni en el markdown del kit** (se cruzó por nombre y URL). Los números de estrellas, la fecha de último push y la licencia salen de la API de GitHub, consultada el **19 de noviembre de 2026, 10:45 hora de Salta (UTC-3)**. No están inventados.

Hay **40 repos** agrupados abajo, y **27 candidatos se descartaron** porque ya estaban en Designweb.

El índice machine-readable está en [`repos-referencia.json`](./repos-referencia.json).

## Los 8 para minar primero

Ordenados por qué tan útil es su contenido para las carpetas del kit (no solo por estrellas).

| # | Repo | Estrellas | Qué tomar |
|---|---|---:|---|
| 1 | [anthropics/skills](https://github.com/anthropics/skills) | 197.538 | Contrastar skills/frontend-design de Designweb con la skill oficial y anotar drifts (tipografía, hero, line-length, anti-defaults). No reemplazar la skill propia: enriquecer anti-patrones/ y skills/ con lo que ellos hayan sumado después. |
| 2 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 151.598 | Minar paletas y pairings que Designweb todavía no tenga (tipografias/pairings.md, paletas/, estilos/). Traer reglas UX y anti-patrones nuevos al catálogo, sin copiar el dataset entero. La skill propia debe seguir eligiendo con los JSON de Designweb, no delegar en este pack. |
| 3 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | 128.231 | Adoptar (adaptada) la sección structure de un DESIGN.md para skills/ y para casos/plantilla.md. Extraer patrones recurrentes no-marca (cómo describen spacing o elevation) hacia tokens/ y estilos/. No pegar un DESIGN.md de marca en un proyecto. |
| 4 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | 118.733 | Adaptar la idea de skills por dirección (editorial, brutalista, soft) a estilos/ y a skills/frontend-design, y el flujo de auditoría de un UI existente a anti-patrones/checklist-revision.md. No instalar el pack entero como default: es fácil que el agente copie una estética de moda. |
| 5 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 113.237 | Traducir y fusionar las reglas del detector con anti-patrones/ (hoy hay 30 tells). Sumar a reglas-para-agentes.md comandos de revisión (critique/audit) que el agente de Designweb pueda ejecutar al final de un UI. |
| 6 | [alexpate/awesome-design-systems](https://github.com/alexpate/awesome-design-systems) | 26.400 | Recorrer sistemas que Designweb no documenta (Primer, Carbon, Polaris, GOV.UK) y traer a tokens/ y estilos/ solo escalas y principios (espacio, tipo, color semántico), con link. No copiar componentes ni tokens de marca. |
| 7 | [heydamir/unslop](https://github.com/heydamir/unslop) | 18.518 | Tomar el orden de las pases de revisión para enriquecer anti-patrones/checklist-revision.md y el cierre de la skill de Designweb. Útil como método, no como pack que pise los tokens del kit. |
| 8 | [argyleink/open-props](https://github.com/argyleink/open-props) | 5.581 | Comparar escalas (sombra, easing, gradientes, borders) con tokens/escalas.md y sumar las que Designweb no tenga, sobre todo easings y sombras. No adoptar Open Props entero como default: el kit ya tiene escalas propias. |

## Cómo usar esta lista

1. Empezá por los 8 de arriba.
2. Resumí y adaptá a la carpeta indicada. **No copies** README, SKILL.md, DESIGN.md ni tokens de marca de forma literal.
3. Antes de un uso comercial, reconfirmá la licencia en el repo (el SPDX de GitHub a veces es incompleto).
4. Las estrellas de skills virales de 2025–2026 pueden estar infladas; el criterio es qué se puede integrar al kit, no el ranking.

## Licencias: qué no copiar

- **MIT / Unlicense / CC0 / Apache-2.0:** se puede adaptar con las condiciones de cada una (Apache pide atribución y aviso de cambios). Aunque el wrapper sea MIT, **la identidad de una marca** (paletas, logo, copy, DESIGN.md de Linear, Stripe, etc.) no se reusa.
- **CC-BY-4.0** (unslop): hay que atribuir. Mejor resumir el método y linkear.
- **Sin SPDX / Other / sin LICENSE** (anthropics/skills a nivel repo, google/fonts, DavidHDev/react-bits, animate.css, brabadu/awesome-fonts, wilwaldon, noahbuscher/inspire, design-tokens/community-group): no copies texto ni código hasta abrir el LICENSE del repo o de cada archivo. Linkeá y resumí.
- **Especificaciones DTCG:** se citan, no se reproducen en extenso.

## Fuentes de la pesquisa

- API de GitHub (búsqueda de repos y `GET /repos/{owner}/{repo}`), 19 nov 2026.
- Reddit, 2026: [r/ClaudeCode](https://www.reddit.com/r/ClaudeCode/comments/1s9h0ry/use_designmd_files_to_stop_claude_from_generating/) (awesome-design-md, Impeccable), [r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1vgykci/i_just_opensourced_a_collection_of_designmd_files/) (fudge-design-md), [r/vibedesigns](https://www.reddit.com/r/vibedesigns/comments/1trzdgv/building_an_open_library_of_designmd_files_for/), [r/BestGitHubRepos](https://www.reddit.com/r/BestGitHubRepos/comments/1wz4v19/taste_skill_the_antislop_frontend_framework_for/) (taste-skill), [r/AwesomeGithub](https://www.reddit.com/r/AwesomeGithub/comments/1xkkv0h/unslop_turn_vibecoded_ai_looking_ui_to_designed/) (unslop).
- X, 2026: hilos que agrupan UI/UX Pro Max, awesome-design-md, taste-skill, Impeccable y Open Design (por ejemplo [@Deeen_Codes, 13 nov 2026](https://x.com/Deeen_Codes/status/2121179259611844928) y [@itsKamadh, 28 oct 2026](https://x.com/itsKamadh/status/2115450134045794483)). Las cifras de estrellas que citan esos posts pueden estar desfasadas; acá valen solo las de la API.

## Skills y reglas para agentes

### [anthropics/skills](https://github.com/anthropics/skills) · **Minar primero #1**

- **Estrellas:** 197.538
- **Último push:** 16 nov 2026, 11:22 hora de Salta (UTC-3)
- **Licencia:** sin SPDX en el repo (cada skill trae LICENSE.txt; revisar antes de copiar)
- **Qué tiene:** Repo oficial de Agent Skills de Anthropic. Incluye skills/frontend-design/SKILL.md: dirección estética deliberada, tipografía no default, escala tipográfica y tells de página generada (una palabra en itálica en el titular, all-caps en labels, etc.).
- **Qué tomar y a qué carpeta:** Contrastar skills/frontend-design de Designweb con la skill oficial y anotar drifts (tipografía, hero, line-length, anti-defaults). No reemplazar la skill propia: enriquecer anti-patrones/ y skills/ con lo que ellos hayan sumado después. → `skills/, anti-patrones/`
- **Cuidado con la licencia:** El repo no declara SPDX. La skill frontend-design remite a LICENSE.txt. No copiar el texto de la skill de forma literal hasta confirmar esos términos; sí se puede contrastar la estructura con la skill propia de Designweb.
- **Nota:** Designweb ya tiene una skill propia inspirada en esta idea, pero el repo oficial no estaba listado en el kit local.

### [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) · **Minar primero #2**

- **Estrellas:** 151.598
- **Último push:** 19 nov 2026
- **Licencia:** MIT
- **Qué tiene:** Skill de diseño con datos locales buscables: 80 estilos (51 activos), 194 paletas por tipo de producto, 74 pairings con imports de Google Fonts, 130 guías UX, 25 tipos de chart y 22 stacks. Se instala en Claude Code, Cursor y otros.
- **Qué tomar y a qué carpeta:** Minar paletas y pairings que Designweb todavía no tenga (tipografias/pairings.md, paletas/, estilos/). Traer reglas UX y anti-patrones nuevos al catálogo, sin copiar el dataset entero. La skill propia debe seguir eligiendo con los JSON de Designweb, no delegar en este pack. → `paletas/, tipografias/, estilos/, anti-patrones/, skills/`
- **Nota:** Muy citado en X en 2026 (hilos de skills anti-slop) y en comparativas vs Impeccable (aidesignskills.com, Chase AI).

### [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) · **Minar primero #4**

- **Estrellas:** 118.733
- **Último push:** 8 nov 2026
- **Licencia:** MIT
- **Qué tiene:** Skills portables anti-slop: dirección de arte, imágenes de referencia y chequeo en el browser. Incluye variantes (gpt-tasteskill, redesign, soft, minimalist, brutalist, stitch/DESIGN.md) e instalación con npx skills add.
- **Qué tomar y a qué carpeta:** Adaptar la idea de skills por dirección (editorial, brutalista, soft) a estilos/ y a skills/frontend-design, y el flujo de auditoría de un UI existente a anti-patrones/checklist-revision.md. No instalar el pack entero como default: es fácil que el agente copie una estética de moda. → `skills/, estilos/, anti-patrones/, inspiracion/`
- **Nota:** Trending en Reddit (r/BestGitHubRepos, oct 2026) y en hilos de X de skills anti-slop.

### [pbakaus/impeccable](https://github.com/pbakaus/impeccable) · **Minar primero #5**

- **Estrellas:** 113.237
- **Último push:** 18 nov 2026
- **Licencia:** Apache-2.0
- **Qué tiene:** Vocabulario de diseño para el agente: comandos steer/review/finish (bolder, quieter, typeset, critique, audit, polish) y un detector determinista de slop (62 reglas, sin LLM): Inter everywhere, degradé violeta-azul, cards anidadas, ícono en tile redondeado sobre cada heading, etc.
- **Qué tomar y a qué carpeta:** Traducir y fusionar las reglas del detector con anti-patrones/ (hoy hay 30 tells). Sumar a reglas-para-agentes.md comandos de revisión (critique/audit) que el agente de Designweb pueda ejecutar al final de un UI. → `anti-patrones/, skills/`
- **Cuidado con la licencia:** Apache-2.0 permite uso y adaptación con atribución y aviso de cambios. No copiar el runtime/hooks de forma literal si no hace falta; sí se pueden resumir las 62 reglas.
- **Nota:** Aparecía citado en anti-patrones/fuentes-investigacion.md como detector no confirmado; no estaba catalogado. Ahora el repo está verificado.

### [heydamir/unslop](https://github.com/heydamir/unslop) · **Minar primero #7**

- **Estrellas:** 18.518
- **Último push:** 15 nov 2026
- **Licencia:** CC-BY-4.0
- **Qué tiene:** Skill de Claude que parte de un UI 'vibecoded', lista señales de slop, fija una dirección a partir del producto y corrige por pases (espacio, color, íconos, copy, tipo, layout, detalle, motion).
- **Qué tomar y a qué carpeta:** Tomar el orden de las pases de revisión para enriquecer anti-patrones/checklist-revision.md y el cierre de la skill de Designweb. Útil como método, no como pack que pise los tokens del kit. → `anti-patrones/, skills/`
- **Cuidado con la licencia:** CC-BY-4.0 exige atribución. No copiar SKILL.md ni el texto de las pases de forma literal; resumir el método (audit → direction → pases) y linkear el repo.
- **Nota:** Citado en r/AwesomeGithub (oct 2026).

### [bergside/awesome-design-skills](https://github.com/bergside/awesome-design-skills)

- **Estrellas:** 3.731
- **Último push:** 28 jun 2026
- **Licencia:** MIT
- **Qué tiene:** Registro de 67 skills (SKILL.md + DESIGN.md) para Claude, Cursor, Codex y Google Stitch. Cada carpeta trae tokens, componentes, accesibilidad y quality gates.
- **Qué tomar y a qué carpeta:** Usarlo como índice: elegir 5–8 skills de sistemas reales que no solapen con estilos/ de Designweb y resumir tokens/tipo/color en estilos/ o paletas/. Last push junio 2026: priorizar las entradas que sigan vivas. → `skills/, estilos/, paletas/`
- **Nota:** Last push 28 jun 2026: más índice que repo vivo.

### [plugin87/ux-ui-agent-skills](https://github.com/plugin87/ux-ui-agent-skills)

- **Estrellas:** 3.204
- **Último push:** 18 nov 2026, 04:37 hora de Salta (UTC-3)
- **Licencia:** MIT
- **Qué tiene:** 26 skills de design system para varios agentes: tokens DTCG, WCAG 2.2 AA–AAA, biblioteca de 2.144 design systems y 52 quality gates que fallan el build (no le creen al agente).
- **Qué tomar y a qué carpeta:** Copiar la idea de gates automáticos (contraste, headings, spacing) a skills/ y a tokens/, no el corpus de 2.144 sistemas. Revisar cómo exportan DTCG y contrastarlo con tokens/tokens.json (DTCG 2025.10). → `skills/, tokens/, anti-patrones/`
- **Nota:** Repo muy activo (push 18 nov 2026).

### [wilwaldon/Claude-Code-Frontend-Design-Toolkit](https://github.com/wilwaldon/Claude-Code-Frontend-Design-Toolkit)

- **Estrellas:** 1.321
- **Último push:** 11 abr 2026, 08:57 hora de Salta (UTC-3)
- **Licencia:** sin licencia declarada
- **Qué tiene:** Recopilación personal de skills, plugins, MCP y trucos de CLAUDE.md que al autor le mejoraron el frontend de Claude Code.
- **Qué tomar y a qué carpeta:** Usarlo como mapa de herramientas (varios van a aparecer en esta misma lista). No copiar texto. Last push abr 2026: puede estar desactualizado. → `recursos/, skills/`
- **Cuidado con la licencia:** Sin LICENSE. Tratarlo como índice: linkear, no copiar README ni snippets.
- **Nota:** Last push 11 abr 2026.

### [feimacode/open-design-agent-kit](https://github.com/feimacode/open-design-agent-kit)

- **Estrellas:** 1.156
- **Último push:** 18 nov 2026, 16:45 hora de Salta (UTC-3)
- **Licencia:** MIT
- **Qué tiene:** Kit para hacer posters, posts, slides y landings desde el agente, con 198 design systems, checks y export PDF/PNG/PPT.
- **Qué tomar y a qué carpeta:** Mirar la estructura de checks y los sistemas no-web (slides, poster) solo si se quiere expandir casos/ o un estilo editorial impreso. Baja prioridad frente a skills web. → `estilos/, casos/`
- **Cuidado con la licencia:** MIT cubre el kit; los 198 'design systems' pueden describir marcas de terceros. Resumir patrones, no copiar identidades.

### [superdesigndev/superdesign-skill](https://github.com/superdesigndev/superdesign-skill)

- **Estrellas:** 1.027
- **Último push:** 21 ago 2026
- **Licencia:** MIT
- **Qué tiene:** Design skill para Claude Code, Cursor y otros agentes, posicionada explícitamente como 'stop shipping AI-slop UI'.
- **Qué tomar y a qué carpeta:** Revisar su lista de tells y compararla con anti-patrones/ para no duplicar. Last push ago 2026: chequear si sigue recibiendo reglas nuevas antes de minar en profundidad. → `anti-patrones/, skills/`
- **Nota:** Sin push desde el 21 ago 2026.

### [bitjaru/styleseed](https://github.com/bitjaru/styleseed)

- **Estrellas:** 1.023
- **Último push:** 18 nov 2026, 06:47 hora de Salta (UTC-3)
- **Licencia:** MIT
- **Qué tiene:** Motor de método de diseño: una skill con 22 workflows internos (juicio fijo, gramáticas, paletas semánticas, compilación de referencias y UI verificada con evidencia).
- **Qué tomar y a qué carpeta:** Útil para formalizar el 'cómo elige' la skill de Designweb (más de un estilo, paleta semántica, evidencia). No traer los workflows de una pieza. → `skills/, paletas/, estilos/`
- **Nota:** Activo (push 18 nov 2026).

### [AnxForever/stylekit](https://github.com/AnxForever/stylekit)

- **Estrellas:** 865
- **Último push:** 19 nov 2026, 09:58 hora de Salta (UTC-3)
- **Licencia:** MIT
- **Qué tiene:** 149 estilos web/UI curados con prompts listos para agentes, tokens y recetas de componentes. Sitio en stylekit.top.
- **Qué tomar y a qué carpeta:** Cruzar los 149 estilos con estilos.json (hoy 27) y sumar solo los que no estén (nombre, reglas, un sitio real). Ignorar prompts genéricos que terminen en glassmorphism + indigo. → `estilos/, tokens/, componentes/`
- **Nota:** Muy activo (push el 19 nov 2026).

### [joeseesun/qiaomu-design](https://github.com/joeseesun/qiaomu-design)

- **Estrellas:** 691
- **Último push:** 13 oct 2026, 03:28 hora de Salta (UTC-3)
- **Licencia:** MIT
- **Qué tiene:** Skill 'opinada' para Claude Code: anti-UI genérica, 'probador de estilos' y una librería de 58 design systems de sitios reales. Incluye tipografía china.
- **Qué tomar y a qué carpeta:** El probador de estilos (elegir una dirección y vestir el UI) encaja con estilos/. Los 58 sitios se pueden cruzar con inspiracion/sitios.md. La parte de tipografía china es un hueco del kit actual. → `estilos/, inspiracion/, tipografias/, skills/`
- **Cuidado con la licencia:** Los 58 sistemas de sitios reales describen marcas de terceros: resumir patrones, no clonar identidades.

## Bibliotecas DESIGN.md

### [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) · **Minar primero #3**

- **Estrellas:** 128.231
- **Último push:** 28 oct 2026, 12:45 hora de Salta (UTC-3)
- **Licencia:** MIT
- **Qué tiene:** Colección de DESIGN.md al estilo Google Stitch: un markdown por marca/producto (tema, color, tipo, componentes, layout, elevation, dos/don'ts, responsive y prompts). Sitio: getdesign.md. VoltAgent/awesome-claude-design (4.621 estrellas, last push jun 2026) parece la colección anterior de 68 archivos; priorizar esta.
- **Qué tomar y a qué carpeta:** Adoptar (adaptada) la sección structure de un DESIGN.md para skills/ y para casos/plantilla.md. Extraer patrones recurrentes no-marca (cómo describen spacing o elevation) hacia tokens/ y estilos/. No pegar un DESIGN.md de marca en un proyecto. → `skills/, estilos/, tokens/, casos/`
- **Cuidado con la licencia:** MIT cubre el markdown del repo, no la identidad visual de las marcas analizadas (Claude, Linear, ElevenLabs, etc.). Está bien estudiar la estructura (palette, typography, componentes, dos/don'ts) y linkear. No copiar paletas, logos ni copy de marca a Designweb ni a un proyecto de un cliente.
- **Nota:** Muy mencionado en r/ClaudeCode (1 abr 2026, u/omeraplak) y en hilos de X de 2026.

### [kzhrknt/awesome-design-md-jp](https://github.com/kzhrknt/awesome-design-md-jp)

- **Estrellas:** 1.019
- **Último push:** 18 nov 2026
- **Licencia:** MIT
- **Qué tiene:** Colección DESIGN.md para que un agente arme UI en japonés de forma correcta (tipografía, densidad, convenciones), extendiendo el formato Stitch.
- **Qué tomar y a qué carpeta:** Hay un hueco en Designweb para tipografía y layout CJK / japonés (el kit tiene estilo japones-inspirado, no reglas de typography japonesa real). Extraer solo esas reglas a tipografias/ y estilos/japones-inspirado.md. → `tipografias/, estilos/`
- **Cuidado con la licencia:** Misma precaución de marca que el resto de DESIGN.md.
- **Nota:** Activo (18 nov 2026).

### [scroobius-pip/fudge-design-md](https://github.com/scroobius-pip/fudge-design-md)

- **Estrellas:** 124
- **Último push:** 16 nov 2026
- **Licencia:** MIT
- **Qué tiene:** DESIGN.md generados a partir de sitios reales capturados por Fudge, con tipografía, color, layout, spacing y screenshots. Menos estrellas, pero vivo y discutido en Reddit (r/ClaudeAI, ago 2026).
- **Qué tomar y a qué carpeta:** Comparar cómo documentan sitios reales vs el catálogo de inspiracion/sitios.md. Sumar 3–5 referencias nuevas con un 'porqué', no el markdown completo. → `inspiracion/, estilos/, casos/`
- **Cuidado con la licencia:** Igual que otras colecciones DESIGN.md: el MIT no autoriza a reusar la identidad de los sitios de referencia.
- **Nota:** Señal alta en Reddit pese a pocas estrellas. Push reciente (16 nov 2026).

## Listas awesome

### [alexpate/awesome-design-systems](https://github.com/alexpate/awesome-design-systems) · **Minar primero #6**

- **Estrellas:** 26.400
- **Último push:** 13 nov 2026, 10:47 hora de Salta (UTC-3)
- **Licencia:** Unlicense
- **Qué tiene:** La lista canónica de design systems (Polaris, Primer, Carbon, Spectrum, Lightning, etc.), todavía actualizada en nov 2026.
- **Qué tomar y a qué carpeta:** Recorrer sistemas que Designweb no documenta (Primer, Carbon, Polaris, GOV.UK) y traer a tokens/ y estilos/ solo escalas y principios (espacio, tipo, color semántico), con link. No copiar componentes ni tokens de marca. → `tokens/, estilos/, componentes/`
- **Cuidado con la licencia:** Unlicense es permisiva. Los sistemas linkeados tienen su propia licencia (muchos no son MIT).
- **Nota:** Lista viva (push 13 nov 2026).

### [syxanash/awesome-web-desktops](https://github.com/syxanash/awesome-web-desktops)

- **Estrellas:** 2.155
- **Último push:** 16 nov 2026, 10:58 hora de Salta (UTC-3)
- **Licencia:** CC0-1.0
- **Qué tiene:** Sitios, web apps y portfolios que imitan un sistema operativo de escritorio (win98, mac clásico, XP, webOS). Directorio en simone.computer/webdesktops.
- **Qué tomar y a qué carpeta:** Sumar 4–6 ejemplos a inspiracion/sitios.md y, si encaja, una nota en estilos/ (navegación experimental / retrofuturismo-y2k / anti-diseño). No es un default de producto; es referencia de interfaz lúdica. → `inspiracion/, estilos/`
- **Nota:** Vivo (16 nov 2026).

### [brabadu/awesome-fonts](https://github.com/brabadu/awesome-fonts)

- **Estrellas:** 2.113
- **Último push:** 31 oct 2026, 16:33 hora de Salta (UTC-3)
- **Licencia:** sin licencia declarada
- **Qué tiene:** Lista de fuentes y recursos relacionados (Google Fonts, icon fonts, programming fonts).
- **Qué tomar y a qué carpeta:** Revisar secciones que tipografias/ no cubra (icon fonts ya están en recursos/iconos.md; programming fonts podrían sumar 2–3 alternativas a Geist Mono / Commit Mono). Solo links, no el listado entero. → `tipografias/, recursos/`
- **Cuidado con la licencia:** Sin LICENSE. Usar como índice y linkear; no copiar el README.

### [vkarampinis/awesome-icons](https://github.com/vkarampinis/awesome-icons)

- **Estrellas:** 1.585
- **Último push:** 1 nov 2026, 07:12 hora de Salta (UTC-3)
- **Licencia:** CC0-1.0
- **Qué tiene:** Lista curada de icon fonts y packs SVG.
- **Qué tomar y a qué carpeta:** Buscar 2–3 sets que no estén en recursos/iconos.md y que no sean Lucide-like. Anotar licencia y 'cuándo'. El kit ya tiene Phosphor, Tabler, Iconoir, Heroicons, Hugeicons, Remix, Radix, Simple Icons, etc. → `recursos/`
- **Cuidado con la licencia:** CC0 cubre la lista, no cada set de íconos. Cada set tiene su licencia (confirmar antes de usarlo).

### [Jolg42/awesome-typography](https://github.com/Jolg42/awesome-typography)

- **Estrellas:** 1.554
- **Último push:** 18 nov 2026
- **Licencia:** CC0-1.0
- **Qué tiene:** Lista curada de tipografía digital: foundries, herramientas, artículos, pairings y recursos.
- **Qué tomar y a qué carpeta:** Cruzar foundries, herramientas y pairings con tipografias/ (101 fuentes, 28 pairings). Sumar solo lo que falte (herramientas de hinting, optical size, OpenType features, foundries). → `tipografias/`
- **Nota:** Viva (push 18 nov 2026).

### [noahbuscher/inspire](https://github.com/noahbuscher/inspire)

- **Estrellas:** 1.335
- **Último push:** 15 mar 2024, 07:04 hora de Salta (UTC-3)
- **Licencia:** sin licencia declarada
- **Qué tiene:** Colección clásica de links de frontend y web design.
- **Qué tomar y a qué carpeta:** Baja prioridad. Si se usa, chequear links rotos y cruzar con inspiracion/galerias.md (el kit ya tiene 22 galerías y 55 sitios). → `inspiracion/`
- **Cuidado con la licencia:** Sin LICENSE y sin push desde marzo 2024. Solo como índice histórico; no copiar y verificar que los links sigan vivos.
- **Nota:** Desactualizado (last push 15 mar 2024).

### [sturobson/Awesome-Design-Tokens](https://github.com/sturobson/Awesome-Design-Tokens)

- **Estrellas:** 1.297
- **Último push:** 20 feb 2026, 10:54 hora de Salta (UTC-3)
- **Licencia:** Unlicense
- **Qué tiene:** Lista de recursos sobre design tokens (artículos, tools, casos).
- **Qué tomar y a qué carpeta:** Sumar a tokens/fuentes-investigacion.md las tools y lecturas que falten. Last push feb 2026: contrastar fechas; priorizar links todavía vivos. → `tokens/`
- **Nota:** Last push 20 feb 2026.

### [klaufel/awesome-design-systems](https://github.com/klaufel/awesome-design-systems)

- **Estrellas:** 913
- **Último push:** 10 nov 2026
- **Licencia:** CC0-1.0
- **Qué tiene:** Lista más chica y developer-first: bookmarks, artículos y recursos sobre design systems.
- **Qué tomar y a qué carpeta:** Minar artículos y repos de tokens/herramientas que no estén en tokens/fuentes-investigacion.md. Complemento de alexpate, no un segundo catálogo paralelo. → `tokens/, recursos/`

## Tokens, DTCG y extracción

### [argyleink/open-props](https://github.com/argyleink/open-props) · **Minar primero #8**

- **Estrellas:** 5.581
- **Último push:** 11 oct 2026
- **Licencia:** MIT
- **Qué tiene:** Set de custom properties CSS (color, tipo, sombra, easing, gradients, z-index, media) para arrancar un sistema consistente y adaptativo, de Adam Argyle.
- **Qué tomar y a qué carpeta:** Comparar escalas (sombra, easing, gradientes, borders) con tokens/escalas.md y sumar las que Designweb no tenga, sobre todo easings y sombras. No adoptar Open Props entero como default: el kit ya tiene escalas propias. → `tokens/, animaciones/`
- **Nota:** Pieza de tokens reutilizable, no otra skill viral.

### [Manavarya09/design-extract](https://github.com/Manavarya09/design-extract)

- **Estrellas:** 5.156
- **Último push:** 18 nov 2026, 03:41 hora de Salta (UTC-3)
- **Licencia:** MIT
- **Qué tiene:** CLI/MCP que extrae el design system de un sitio (tokens DTCG primitivos+semánticos+compuestos, Tailwind v4, shadcn, Figma variables, audit CSS/WCAG).
- **Qué tomar y a qué carpeta:** Herramienta para alimentar casos/ (antes/después) y para contrastar tokens de un sitio de inspiracion/sitios.md. Documentar el comando en tokens/ y casos/, no pegar dumps de marcas. → `tokens/, casos/, inspiracion/`
- **Cuidado con la licencia:** MIT cubre la herramienta. Extraer el design system de un sitio de terceros no te da derecho a reusar su identidad. Usar para estudiar y documentar, o sobre sitios propios / con permiso.

### [style-dictionary/style-dictionary](https://github.com/style-dictionary/style-dictionary)

- **Estrellas:** 4.887
- **Último push:** 3 nov 2026
- **Licencia:** Apache-2.0
- **Qué tiene:** Build system canónico para transformar design tokens a CSS, iOS, Android, etc. Antes amzn/style-dictionary; el repo vivo es este. Push nov 2026.
- **Qué tomar y a qué carpeta:** Documentar en tokens/README.md un flujo Style Dictionary a partir de tokens.json (DTCG 2025.10) hacia tokens.css y theme-tailwind-v4.css. Es la pieza de pipeline que el kit todavía no enseña. → `tokens/`
- **Cuidado con la licencia:** Apache-2.0: uso libre con atribución. No hace falta copiar el engine; sí documentar cómo emitir CSS/@theme desde tokens.json.

### [dembrandt/dembrandt](https://github.com/dembrandt/dembrandt)

- **Estrellas:** 4.045
- **Último push:** 19 nov 2026, 10:00 hora de Salta (UTC-3)
- **Licencia:** MIT
- **Qué tiene:** CLI para extraer en segundos logo, colores, tipografía, bordes y más de cualquier sitio, a tokens (y DESIGN.md). Muy activo.
- **Qué tomar y a qué carpeta:** Alternativa más liviana a design-extract para armar un DESIGN.md de un sitio de referencia. Misma regla: no clonar la marca, sí documentar el método en casos/ y tokens/. → `tokens/, casos/, skills/`
- **Cuidado con la licencia:** Igual que design-extract: la herramienta es MIT; la marca extraída no.
- **Nota:** Push el 19 nov 2026.

### [design-tokens/community-group](https://github.com/design-tokens/community-group)

- **Estrellas:** 2.178
- **Último push:** 1 nov 2026, 13:13 hora de Salta (UTC-3)
- **Licencia:** Other (NOASSERTION)
- **Qué tiene:** Repo oficial de la DTCG: sitio y especificación de design tokens. El kit ya trabaja en formato DTCG 2025.10, pero no linkeaba este repo.
- **Qué tomar y a qué carpeta:** Agregar el repo y designtokens.org/TR/drafts/ como fuente canónica en tokens/fuentes-investigacion.md, y revisar si 2025.10 del kit sigue alineado con el draft actual. → `tokens/`
- **Cuidado con la licencia:** Licencia 'Other' / sin SPDX claro. La especificación se consulta y se cita; no copiar el texto normativo de forma extensa.
- **Nota:** El formato DTCG ya está usado en el kit; el repo en sí no estaba listado.

### [zanwei/design-dna](https://github.com/zanwei/design-dna)

- **Estrellas:** 2.141
- **Último push:** 27 ago 2026, 22:58 hora de Salta (UTC-3)
- **Licencia:** MIT
- **Qué tiene:** Pasa UIs de referencia (imagen, screenshot, URL) a un JSON de 'Design DNA' (tokens + estilo cualitativo + efectos) y después genera UI a partir de tu contenido.
- **Qué tomar y a qué carpeta:** La forma del JSON (tokens + cualitativo + efectos) puede inspirar un esquema para casos/ o para que la skill elija estilo con más matices. Last push ago 2026. → `casos/, estilos/, tokens/`
- **Cuidado con la licencia:** MIT del tool; no reusar la identidad de las UIs de referencia.
- **Nota:** Sin push desde el 28 ago 2026.

### [tokens-studio/figma-plugin](https://github.com/tokens-studio/figma-plugin)

- **Estrellas:** 1.631
- **Último push:** 19 nov 2026, 09:52 hora de Salta (UTC-3)
- **Licencia:** MIT
- **Qué tiene:** Plugin oficial Tokens Studio for Figma (antes Figma Tokens). Sigue muy activo.
- **Qué tomar y a qué carpeta:** Documentar en tokens/ el puente Figma → DTCG → Style Dictionary, para cuando un caso/ arranque en Figma. No hace falta vendor lock-in en la skill. → `tokens/, casos/`

## Tipografía (infraestructura)

### [google/fonts](https://github.com/google/fonts)

- **Estrellas:** 20.784
- **Último push:** 19 nov 2026, 07:14 hora de Salta (UTC-3)
- **Licencia:** sin SPDX único (licencias por familia, mayoría OFL/Apache)
- **Qué tiene:** Repo canónico de archivos de Google Fonts e issue tracker público. El kit ya usa el catálogo web, pero no apuntaba a este repo.
- **Qué tomar y a qué carpeta:** Usarlo para bajar/verificar archivos y licencias de las 101 fuentes que salen de Google Fonts, y para detectar familias nuevas. No es un catálogo de tendencias: no pisa tipografias/. → `tipografias/`
- **Cuidado con la licencia:** No hay una licencia única del repo. Cada familia declara la suya (casi siempre OFL o Apache). Confirmar en la carpeta de la fuente antes de distribuir archivos.

### [fontsource/fontsource](https://github.com/fontsource/fontsource)

- **Estrellas:** 6.293
- **Último push:** 9 nov 2026
- **Licencia:** MIT
- **Qué tiene:** Paquetes NPM para self-hostear fuentes open source, sin depender del CDN de Google Fonts.
- **Qué tomar y a qué carpeta:** Agregar Fontsource a tipografias/README.md como método de import preferido cuando se quiera self-host (privacidad, rendimiento, menos CLS). Completar fonts.json con el paquete npm cuando exista. → `tipografias/`
- **Cuidado con la licencia:** MIT cubre el empaquetado. Cada fuente tiene su propia licencia (OFL, SIL, etc.), que es la que hay que respetar al self-hostear.
- **Nota:** El kit ya cita fonts.google.com en muchas fichas, pero no el repo ni el self-host vía Fontsource.

## Paletas y degradés

### [itmeo/webgradients](https://github.com/itmeo/webgradients)

- **Estrellas:** 2.505
- **Último push:** 3 ago 2026, 18:50 hora de Salta (UTC-3)
- **Licencia:** MIT
- **Qué tiene:** 180 degradés CSS/Figma/Sketch/PSD más un dataset JSON pensado también para agentes.
- **Qué tomar y a qué carpeta:** Sumar el JSON como fuente en paletas/ y recursos/gradientes.md, con la regla ya escrita en el kit: un degradé no es identidad. Filtrar y marcar los que caen en violeta-azul (el tell de IA). Preferir los no-indigo para acentos, no para el hero entero. → `paletas/, recursos/`

## Componentes y motion

### [animate-css/animate.css](https://github.com/animate-css/animate.css)

- **Estrellas:** 83.029
- **Último push:** 29 jul 2024, 16:34 hora de Salta (UTC-3)
- **Licencia:** Other (NOASSERTION; históricamente Hijack/custom + código libre; confirmar LICENSE)
- **Qué tiene:** Librería clásica de animaciones CSS (fadeIn, bounce, etc.). Altísimas estrellas, pero desactualizada y muy asociada a UI genérica.
- **Qué tomar y a qué carpeta:** No adoptarla como default de agentes. Como mucho, una nota en animaciones/ de 'qué no usar' (bounce/fadeIn en cada card). Preferir Motion, GSAP, anime.js o CSS nativo (View Transitions, scroll-driven). → `animaciones/, anti-patrones/`
- **Cuidado con la licencia:** SPDX NOASSERTION. Confirmar LICENSE antes de copiar CSS. Además, last push jul 2024.
- **Nota:** Last push 29 jul 2024. Se incluye por ser muy calificado y ausente del kit, con advertencia explícita.

### [juliangarnier/anime](https://github.com/juliangarnier/anime)

- **Estrellas:** 74.900
- **Último push:** 2 nov 2026, 19:25 hora de Salta (UTC-3)
- **Licencia:** MIT
- **Qué tiene:** Motor de animación JS (CSS, SVG, canvas, timelines). Vivo en 2026 (anime.js v4). El kit cubre Motion, GSAP, Lenis, Rive, Lottie, Theatre y AutoAnimate, pero no anime.js.
- **Qué tomar y a qué carpeta:** Ficha en animaciones/herramientas.md y animaciones.json: cuándo usar anime.js vs Motion vs GSAP (peso, SVG, timelines sin React). Sumar 1–2 easings útiles a easing-duracion.md si no están. → `animaciones/`

### [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits)

- **Estrellas:** 52.302
- **Último push:** 19 nov 2026
- **Licencia:** sin SPDX (NOASSERTION)
- **Qué tiene:** Librería grande de componentes React/Next animados e interactivos, 'built for humans and AI agents'. Muy activa.
- **Qué tomar y a qué carpeta:** Catalogarla en componentes/bibliotecas.md como registro de motion (junto a Magic UI / Motion Primitives, que ya están). Advertir el 'cuándo no': usarla como default produce el mismo slop que Magic UI (marquees, glows, particles en cada sección). Elegir 1 gesto por proyecto. → `componentes/, animaciones/`
- **Cuidado con la licencia:** GitHub devuelve NOASSERTION. Confirmar LICENSE del repo antes de copiar un componente. Si no es permisiva, solo linkear.
- **Nota:** No confundir con vasanthk/react-bits (patrones de React, CC-BY-4.0), otro repo.

### [saadeghi/daisyui](https://github.com/saadeghi/daisyui)

- **Estrellas:** 42.906
- **Último push:** 16 nov 2026
- **Licencia:** MIT
- **Qué tiene:** La librería de componentes Tailwind más popular. Temas listos, semántica de clases.
- **Qué tomar y a qué carpeta:** Agregarla a componentes/bibliotecas.md con un 'cuándo no' fuerte: el tema default de daisyUI es otro look genérico (como el Inter + indigo). Si se usa, hay que retokenizar con paletas/ y tokens/ de Designweb, o no usarla. → `componentes/`

### [frankxai/awesome-motion-design-agent-skills](https://github.com/frankxai/awesome-motion-design-agent-skills)

- **Estrellas:** 119
- **Último push:** 19 nov 2026
- **Licencia:** CC0-1.0
- **Qué tiene:** Lista viva de skills de motion para agentes: GSAP, Motion, Remotion, Lottie y Rive (web, video procedural).
- **Qué tomar y a qué carpeta:** Aunque es chica, está actualizada el 19 nov 2026 y apunta a skills de motion que animaciones/ no cataloga como skills (Remotion, skills de GSAP). Revisar y linkear las que no dupliquen herramientas ya listadas. → `animaciones/, skills/`
- **Nota:** Pocas estrellas, alta frescura.

## Workspaces de diseño con agentes

### [nexu-io/open-design](https://github.com/nexu-io/open-design)

- **Estrellas:** 108.449
- **Último push:** 19 nov 2026, 08:01 hora de Salta (UTC-3)
- **Licencia:** Apache-2.0
- **Qué tiene:** Workspace colaborativo local-first de diseño con agentes (motion, prototypes, sites, apps, dashboards, slides, imagen y video). Muy citado en X en 2026 junto a Pro Max, awesome-design-md, taste e Impeccable.
- **Qué tomar y a qué carpeta:** No minar código. Sí vale probarlo como entorno y, si publica agent-skills o design systems reutilizables, revisarlos después. Baja prioridad para alimentar carpetas del kit. → `recursos/`
- **Cuidado con la licencia:** Apache-2.0 del producto. No es material para copiar a Designweb; es una app.
- **Nota:** Es un producto, no un knowledge kit. Se incluye por estrellas, actividad y presencia en X, con el alcance bien delimitado.

## Descartados porque ya estaban en Designweb

Se encontraron y se bajaron **27** candidatos que ya figuraban en el kit (por nombre o URL), para no volver a catalogarlos:

- shadcn-ui/ui — ya en `componentes/`
- magicuidesign/magicui — ya en `componentes/`
- Aceternity UI — ya en `componentes/`
- 21st.dev — ya en `componentes/`
- park-ui — ya en `componentes/`
- cosscom/ui (Origin UI) y origin-space/ui-experiments — ya en `componentes/ (ya catalogado como coss ui)`
- nolly-studio/cult-ui — ya en `componentes/`
- shadcnblocks/kibo — ya en `componentes/`
- ibelick/motion-primitives — ya en `componentes/`
- imskyleen/animate-ui — ya en `componentes/`
- tremorlabs/tremor — ya en `componentes/`
- heroui-inc/heroui — ya en `componentes/`
- radix-ui/primitives — ya en `componentes/`
- chakra-ui/ark — ya en `componentes/`
- adobe/react-spectrum — ya en `componentes/`
- mui/base-ui — ya en `componentes/`
- motiondivision/motion — ya en `animaciones/`
- GSAP — ya en `animaciones/`
- darkroomengineering/lenis — ya en `animaciones/`
- airbnb/lottie-web — ya en `animaciones/`
- rive-app/rive-react — ya en `animaciones/`
- theatre-js/theatre — ya en `animaciones/`
- formkit/auto-animate — ya en `animaciones/`
- evilmartians/oklch-picker — ya en `recursos/, paletas/`
- colorjs — ya en `paletas/herramientas.md`
- utopia.fyi — ya en `tokens/`
- funboy322/avoid-ai-design — ya en `anti-patrones/fuentes-investigacion.md`

Impeccable aparecía solo como mención no confirmada en `anti-patrones/fuentes-investigacion.md` («confirmar el repo antes de dependerlo»). No estaba catalogado, así que **sí entra** en esta lista, ya verificado.

También se dejaron afuera falsos positivos de la búsqueda (listas de system design de entrevistas, frontends de YouTube, wrappers de Font Awesome, etc.) y colecciones DESIGN.md casi vacías de estrellas (por ejemplo `albemala/design-md-library`, 28 estrellas). `VoltAgent/awesome-claude-design` (4.621 estrellas, last push jun 2026) se menciona arriba como predecesor de `awesome-design-md`, no como entrada aparte.

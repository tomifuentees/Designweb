# Librerías visuales

Catálogo de sitios en la línea de [Cult UI](https://www.cult-ui.com/): librerías y registries de componentes visuales y animados que se copian al proyecto (casi siempre React + Tailwind, muchos con Motion y el CLI de shadcn). Armado el 19 de noviembre de 2026, zona America/Argentina/Salta.

El objetivo no es tener 40 kits instalados. Es poder elegir **una** pieza con oficio —un dock, un fondo, un hero, un input de chat— en lugar de dejar que un agente apile el glow de Aceternity, el marquee de Magic UI y el Aurora de React Bits en la misma vista. Eso es, hoy, una de las firmas más reconocibles de UI genérica de IA. Se lee junto a [`../anti-patrones/`](../anti-patrones/README.md), [`../tokens/`](../tokens/README.md) y [`../componentes/`](../componentes/README.md).

Hay **40 sitios**. **8** ya estaban fichados (a nivel librería) en `componentes/`; acá se retoman en breve, con más detalle de instalación y con 3–5 piezas curadas y URL verificada. **32** son nuevos en el kit (React Bits ya estaba solo en [`../recursos/repos-referencia.md`](../recursos/repos-referencia.md)). Las estrellas, el SPDX y el último push salen de la API de GitHub el 19 de noviembre de 2026. Los horarios de push están convertidos a America/Argentina/Salta (UTC−3). Las URLs de cada sitio y de las piezas curadas resolvieron `GET 200` en esa misma pasada, salvo donde se indica lo contrario.

No se copia código de licencias no permisivas: se linkea. Antes de un uso comercial, hay que releer los términos de la pieza (sobre todo Pro, Commons Clause y registries sin SPDX).

## Qué hay acá

| Archivo | Contenido |
|---|---|
| [librerias-visuales.json](./librerias-visuales.json) | El mismo catálogo, legible por máquinas (skills y agentes). |

## Cómo elegir

| Necesidad | Por dónde empezar |
|---|---|
| Microinteracción de producto o UI de agente | Cult UI, Kokonut UI, HextaUI, Animate UI, Motion Primitives |
| Un gesto de landing (uno solo) | Magic UI *o* un bloque de Aceternity *o* una pieza de React Bits, no los tres |
| Texto cinético | Animata (MIT), Fancy Components, React Bits (ojo Commons Clause), Motion Primitives |
| Fondo / shader / WebGL | React Bits (Aurora, Silk), Aceternity (beams, spotlight), Badtz shaders; medir performance y `prefers-reduced-motion` |
| Sección completa de marketing | Launch UI, Tailark, Shadcnblocks, Efferd, craftUI, Shadcn Studio |
| Producto denso (tablas, Gantt, filters) | ReUI, Kibo UI, coss ui, Dice UI, Intent UI |
| Algo que no se vea en todos los demos de 2026 | Skiper UI, Vengeance UI, Fancy Components, 8bitcn (si el look retro es una tesis) |
| Descubrir registries | [Directorio oficial de shadcn](https://ui.shadcn.com/docs/directory), [registry.directory](https://registry.directory/), 21st.dev (como galería, no como sistema) |

Regla práctica: tokens y tipografía del kit **antes** de sumar un registry animado. Una librería por capa (primitivas, un kit de motion, un kit de bloques). Mezclar quince estilos es el camino al look de plantilla.

## Componentes animados

Kits copy-paste de UI animada, el grupo más cercano a Cult UI. Los cinco primeros ya estaban en `componentes/`; el resto es nuevo.

### Cult UI · **ya en componentes/**

- **Oficial:** [www.cult-ui.com](https://www.cult-ui.com/) · Repo: [nolly-studio/cult-ui](https://github.com/nolly-studio/cult-ui) (7.561 estrellas el 19/11/2026, MIT). Último push: 29 de octubre de 2026, 00:57 (America/Argentina/Salta).
- **Stack:** React, Tailwind CSS v4, Motion, shadcn CLI.
- **Instalación:** `npx shadcn@latest add @cult-ui/{name}`
- **Cuándo usarlo:** microinteracciones de producto; patrones de UI para agentes y chat; un gesto animado en controles ya existentes.
- **Cuándo no:** un hero cinematográfico (mejor Magic, Aceternity o React Bits); instalar el catálogo entero.
- **En el kit:** Ya estaba en [`../componentes/`](../componentes/bibliotecas.md).
- **Piezas curadas:** [Toolbar Expandable](https://www.cult-ui.com/docs/components/toolbar-expandable), [Agent Suggest Card Stack](https://www.cult-ui.com/docs/components/agent-suggest-card-stack), [AI Blob Warp](https://www.cult-ui.com/docs/components/ai-blob-warp), [Dynamic Island](https://www.cult-ui.com/docs/components/dynamic-island).
- **Nota:** Ficha base en componentes/. Catálogo más chico y más de producto que Magic UI. El namespace @cult-ui viene en el CLI de shadcn; también se puede pasar la URL https://www.cult-ui.com/r/{name}.json. Descripción oficial del repo: 150+ componentes free, MIT.

### Magic UI · **ya en componentes/**

- **Oficial:** [magicui.design](https://magicui.design/) · Repo: [magicuidesign/magicui](https://github.com/magicuidesign/magicui) (23.376 estrellas el 19/11/2026, MIT (free); Pro con términos propios). Último push: 17 de noviembre de 2026, 09:47 (America/Argentina/Salta).
- **Stack:** React, Tailwind CSS, Motion, shadcn CLI.
- **Instalación:** `npx shadcn@latest add @magicui/{name}`
- **Cuándo usarlo:** un gesto de motion en una landing; marquee, dock, beam o bento, no los cuatro juntos.
- **Cuándo no:** instalar el catálogo entero; dashboards de trabajo; apilar varios efectos 'de Magic' en la misma vista.
- **En el kit:** Ya estaba en [`../componentes/`](../componentes/bibliotecas.md).
- **Piezas curadas:** [Marquee](https://magicui.design/docs/components/marquee), [Dock](https://magicui.design/docs/components/dock), [Animated Beam](https://magicui.design/docs/components/animated-beam), [Shimmer Button](https://magicui.design/docs/components/shimmer-button), [Bento Grid](https://magicui.design/docs/components/bento-grid).
- **Nota:** El kit de marketing más citado del ecosistema shadcn. El default de IA lo pega entero: se ve 'de Magic UI' en tres segundos. Pro no se redistribuye como template.

### Aceternity UI · **ya en componentes/**

- **Oficial:** [ui.aceternity.com](https://ui.aceternity.com/). Sin repo público verificado el 19/11/2026. Términos propios (hay tier free y planes pagos).
- **Stack:** React, Tailwind CSS, Motion, shadcn CLI.
- **Instalación:** `npx shadcn@latest add @aceternity/{name}`
- **Cuándo usarlo:** un hero o una sección memorable; un efecto 3D o de spotlight puntual.
- **Cuándo no:** usarlo como sistema de producto; apilar spotlight + lamp + beams en la misma página.
- **En el kit:** Ya estaba en [`../componentes/`](../componentes/bibliotecas.md).
- **Piezas curadas:** [3D Card Effect](https://ui.aceternity.com/components/3d-card-effect), [Spotlight](https://ui.aceternity.com/components/spotlight), [Lamp Effect](https://ui.aceternity.com/components/lamp-effect), [Background Beams](https://ui.aceternity.com/components/background-beams), [Text Generate Effect](https://ui.aceternity.com/components/text-generate-effect).
- **Nota:** Es el kit que más fácil deja un sitio 'de IA con glow'. Una rareza, no un theme. No se encontró un repositorio público oficial el 19/11/2026.

### Motion Primitives · **ya en componentes/**

- **Oficial:** [www.motion-primitives.com](https://www.motion-primitives.com/) · Repo: [ibelick/motion-primitives](https://github.com/ibelick/motion-primitives) (6.987 estrellas el 19/11/2026, MIT). Último push: 28 de septiembre de 2026, 10:32 (America/Argentina/Salta).
- **Stack:** React, Tailwind CSS, Motion.
- **Instalación:** `npx motion-primitives@latest add {name}` (también hay namespace `@motion-primitives` en el directorio de shadcn).
- **Cuándo usarlo:** componer reveals, morphs y texto animado; microinteracción de producto más sutil que Magic/Aceternity.
- **Cuándo no:** esperar secciones de landing cerradas.
- **En el kit:** Ya estaba en [`../componentes/`](../componentes/bibliotecas.md).
- **Piezas curadas:** [Text Effect](https://www.motion-primitives.com/docs/text-effect).
- **Nota:** Autor @Ibelick. Building blocks, no templates. Hay un sitio Pro aparte.

### Animate UI · **ya en componentes/**

- **Oficial:** [animate-ui.com](https://animate-ui.com/) · Repo: [imskyleen/animate-ui](https://github.com/imskyleen/animate-ui) (5.090 estrellas el 19/11/2026, MIT + Commons Clause). Último push: 15 de noviembre de 2026, 14:23 (America/Argentina/Salta).
- **Stack:** React, Motion, shadcn CLI, Radix / Base UI / React Aria.
- **Instalación:** `npx shadcn@latest add @animate-ui/{name}`
- **Cuándo usarlo:** animar primitivas familiares (drawer, hover card, blur) si la licencia cierra.
- **Cuándo no:** revender o redistribuir los componentes en su forma original; meterlo en un kit que se vende.
- **En el kit:** Ya estaba en [`../componentes/`](../componentes/bibliotecas.md).
- **Piezas curadas:** [Blur](https://animate-ui.com/docs/primitives/animate-ui/blur).
- **Nota:** No es un MIT limpio. El repo de GitHub declara SPDX Other; la ficha de componentes/ ya documentó Commons Clause el 19/11/2026.

### React Bits · **nueva en esta carpeta** (sí estaba en repos-referencia)

- **Oficial:** [www.reactbits.dev](https://www.reactbits.dev/) · Repo: [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) (52.307 estrellas el 19/11/2026, MIT + Commons Clause). Último push: 19 de noviembre de 2026, 11:48 (America/Argentina/Salta).
- **Stack:** React, JS o TS, CSS o Tailwind, GSAP / Motion / Three.js / OGL según el componente, shadcn CLI o jsrepo.
- **Instalación:** `npx shadcn@latest add https://reactbits.dev/r/<Component>-<LANG>-<STYLE>` (ejemplo: `SplitText-JS-CSS`). También hay CLI jsrepo y copy-paste. En el directorio de shadcn aparece el namespace `@react-bits`.
- **Cuándo usarlo:** fondos WebGL o texto cinético en un portfolio o launch; un efecto memorable, no una docena.
- **Cuándo no:** revender los componentes o las tools; usar Aurora/Silk/Split Text en todos los proyectos (ya es una firma reconocible); productos densos de datos.
- **En el kit:** El repo ya figuraba en [`../recursos/repos-referencia.md`](../recursos/repos-referencia.md); acá se documenta como sitio visual, que no estaba en `componentes/`.
- **Licencia, con detalle:** LICENSE.md leída el 2026-11-19, copyright 2026 David Haz. Se puede usar en una app o sitio comercial. No se pueden vender, sublicenciar ni redistribuir los componentes (ni las tools: Background Studio, Texture Lab, etc.) como pack o servicio.
- **Piezas curadas:** [Split Text](https://www.reactbits.dev/text-animations/split-text), [Aurora](https://www.reactbits.dev/backgrounds/aurora), [Silk](https://www.reactbits.dev/backgrounds/silk), [Spotlight Card](https://www.reactbits.dev/components/spotlight-card), [Blur Text](https://www.reactbits.dev/text-animations/blur-text).
- **Nota:** El catálogo free más grande de esta lista. Cuatro variantes de implementación. Ya figuraba en recursos/repos-referencia.md, no en componentes/. El repo se actualizó el mismo 19/11/2026.

### Skiper UI · **nueva en el kit**

- **Oficial:** [skiper-ui.com](https://skiper-ui.com/). Sin repo público verificado el 19/11/2026. Freemium (hay piezas free y un plan pago).
- **Stack:** Next.js, React, Tailwind CSS, shadcn/ui, shadcn CLI.
- **Instalación:** `npx shadcn@latest add @skiper-ui/skiper{N}` (los ítems se identifican por número: skiper1, skiper40, etc.).
- **Cuándo usarlo:** un componente 'un-common' que no está en Magic ni en shadcn core; interacciones raras de hero, hover o scrollbar.
- **Cuándo no:** usar el plan pago sin leer la licencia; tratarlo como un sistema completo.
- **Piezas curadas:** [Anime.js scrollbar (skiper1)](https://skiper-ui.com/v1/skiper1), [Theme toggle btn (skiper26)](https://skiper-ui.com/v1/skiper26), [CssLink (skiper40)](https://skiper-ui.com/v1/skiper40), [ExpandOnHover (skiper52)](https://skiper-ui.com/v1/skiper52), [Quick Start](https://skiper-ui.com/docs/quick-start).
- **Nota:** Se presenta como 'Un-common Components for shadcn/ui'. El sitemap del 19/11/2026 lista las piezas como /v1/skiperN. Varios posts de 2025–2026 (Reddit, X de @orcdev) lo recomiendan cuando se busca algo que no parezca Magic/Aceternity.

### Eldora UI · **nueva en el kit**

- **Oficial:** [www.eldoraui.site](https://www.eldoraui.site/) · Repo: [karthikmudunuri/eldoraui](https://github.com/karthikmudunuri/eldoraui) (1.977 estrellas el 19/11/2026, MIT). Último push: 26 de septiembre de 2026, 14:39 (America/Argentina/Salta).
- **Stack:** React, Tailwind CSS.
- **Instalación:** Copy-paste desde la docs (https://www.eldoraui.site/docs/components); el llms.txt la describe como componentes de landing con React y Tailwind.
- **Cuándo usarlo:** secciones de landing animadas en la línea de Aceternity, con MIT limpio.
- **Cuándo no:** asumir el mismo ritmo de actualización que Magic o React Bits (último push del repo: 26/09/2026); el globo tipo Cobe si el rendimiento duele (comentario frecuente en listas 2025).
- **Piezas curadas:** [Índice de componentes](https://www.eldoraui.site/docs/components).
- **Nota:** Sitio oficial: eldoraui.site (no .com). Útil como alternativa MIT a Aceternity; revisar que la pieza no sea un clon reconocible.

### Hover.dev · **nueva en el kit**

- **Oficial:** [www.hover.dev](https://www.hover.dev/). Sin repo público verificado el 19/11/2026. Freemium (hay componentes free y Hover Pro).
- **Stack:** React, Tailwind CSS, Motion u otras libs de animación según la pieza.
- **Instalación:** Copy-paste desde las fichas del sitio (el home lo presenta así: tomar el código y soltarlo en el proyecto).
- **Cuándo usarlo:** microinteracciones de hover, botones y héroes con carácter; detalles táctiles que no se ven en el default de shadcn.
- **Cuándo no:** usar el botón 'Wet Paint' o el glow índigo de sus demos como identidad; armar toda la landing solo con Hover.
- **Piezas curadas:** [Buttons (incluye Wet Paint, Encrypt, Spotlight)](https://www.hover.dev/components/buttons), [Hero Sections](https://www.hover.dev/components/heros), [Three-D](https://www.hover.dev/components/three-d), [Text](https://www.hover.dev/components/text), [Cards](https://www.hover.dev/components/cards).
- **Nota:** Las páginas de categoría resolvieron 200 el 19/11/2026; las fichas individuales no exponen URL estática fácil de scrapear (se renderizan en el cliente). Verificar términos de Pro antes de un uso comercial.

### Uiverse · **nueva en el kit**

- **Oficial:** [uiverse.io](https://uiverse.io/) · Repo: [uiverse-io/galaxy](https://github.com/uiverse-io/galaxy) (15.047 estrellas el 19/11/2026, MIT). Último push: 2 de septiembre de 2024, 11:32 (America/Argentina/Salta).
- **Stack:** HTML/CSS o Tailwind, funciona fuera de React.
- **Instalación:** Copy-paste desde uiverse.io (elementos de la comunidad, CSS o Tailwind).
- **Cuándo usarlo:** un botón, loader o card CSS aislado, en cualquier stack; inspiración rápida sin atarse a shadcn.
- **Cuándo no:** pegar 20 elementos de autores distintos ( terminación de collage ); asumir que el repo galaxy está al día (último push visto: 2/09/2024); el catálogo vivo es el sitio.
- **Piezas curadas:** [Home / catálogo](https://uiverse.io/).
- **Nota:** No es un registry de shadcn: es la biblioteca comunitaria más grande de elementos CSS. El repo galaxy exporta el código; el producto está en el sitio.

### Indie UI · **nueva en el kit**

- **Oficial:** [ui.indie-starter.dev](https://ui.indie-starter.dev/) · Repo: [alibey-10/indie-ui](https://github.com/alibey-10/indie-ui) (710 estrellas el 19/11/2026, MIT). Último push: 7 de enero de 2026, 10:57 (America/Argentina/Salta).
- **Stack:** React, Tailwind CSS, shadcn, Motion.
- **Instalación:** Copy-paste desde las docs (https://ui.indie-starter.dev/docs). El repo redirige también desde github.com/Ali-Hussein-dev/indie-ui.
- **Cuándo usarlo:** botones con carácter, cards con patrón y bento chicos, con MIT.
- **Cuándo no:** depender de actualizaciones frecuentes (último push del repo: 7/01/2026).
- **Piezas curadas:** [Eye-catching buttons](https://ui.indie-starter.dev/docs/eye-catching-buttons), [Stateful buttons](https://ui.indie-starter.dev/docs/stateful-buttons), [Text animation](https://ui.indie-starter.dev/docs/text-animation), [Cards interactive](https://ui.indie-starter.dev/docs/cards-interactive), [Bento 6](https://ui.indie-starter.dev/docs/bento-6).
- **Nota:** Homepage oficial del repo: ui.indie-starter.dev. El usuario de GitHub es alibey-10; Ali-Hussein-dev/indie-ui redirige al mismo repo.

### SyntaxUI · **nueva en el kit**

- **Oficial:** [syntaxui.com](https://syntaxui.com/) · Repo: [SyntaxUI/syntaxui](https://github.com/SyntaxUI/syntaxui) (991 estrellas el 19/11/2026, MIT). Último push: 18 de mayo de 2026, 02:46 (America/Argentina/Salta).
- **Stack:** React, Tailwind CSS, Motion.
- **Instalación:** Copy-paste desde [syntaxui.com](https://syntaxui.com/). Hay una oferta Pro aparte; el repo público es MIT.
- **Cuándo usarlo:** piezas mínimas y claras, sin el glow de Aceternity.
- **Cuándo no:** esperar un catálogo al ritmo de Magic o React Bits (último push: 18/05/2026).
- **Piezas curadas:** [Home / catálogo](https://syntaxui.com/).
- **Nota:** Las rutas internas de componentes no se expusieron de forma estática en el HTML del 19/11/2026 (sitio muy hidratado). Entrar por la home y elegir.

### SmoothUI · **nueva en el kit**

- **Oficial:** [smoothui.dev](https://smoothui.dev/) · Repo: [educlopez/smoothui](https://github.com/educlopez/smoothui) (1.064 estrellas el 19/11/2026, MIT). Último push: 19 de noviembre de 2026, 09:37 (America/Argentina/Salta).
- **Stack:** React, Tailwind CSS, Motion, shadcn/ui.
- **Instalación:** Según las docs de smoothui.dev (llms.txt disponible). Colección animada pensada para convivir con shadcn.
- **Cuándo usarlo:** secciones de marketing con motion controlado; un orb o gesto 'premium' puntual.
- **Cuándo no:** apilar varios orbs/blobs (el Siri Orb es reconocible).
- **Piezas curadas:** [Siri Orb](https://smoothui.dev/docs/components/siri-orb).
- **Nota:** Repo muy activo el 19/11/2026. Aparece en listas de Reddit y X junto a Kokonut y ReUI.

### Spectrum UI · **nueva en el kit**

- **Oficial:** [ui.spectrumhq.in](https://ui.spectrumhq.in/) · Repo: [arihantcodes/spectrum-ui](https://github.com/arihantcodes/spectrum-ui) (1.543 estrellas el 19/11/2026, Apache-2.0). Último push: 21 de septiembre de 2026, 04:11 (America/Argentina/Salta).
- **Stack:** React, Next.js, Tailwind CSS, Motion, shadcn CLI.
- **Instalación:** CLI de shadcn (el sitio y el llms.txt documentan instalación por CLI). No confundir con Adobe Spectrum.
- **Cuándo usarlo:** botones y cards animados copy-paste, con Apache-2.0; un metal button o hold-to-confirm, no un theme entero.
- **Cuándo no:** confundirlo con React Spectrum / Adobe; dejar el look de demo como identidad.
- **Piezas curadas:** [Metal Button](https://ui.spectrumhq.in/docs/metal-button).
- **Nota:** El propio repo se describe como una colección reutilizable construida usando Aceternity, Magic UI y shadcn. Eso es una señal: revisar originalidad de cada pieza antes de copiarla.

### Fancy Components · **nueva en el kit**

- **Oficial:** [www.fancycomponents.dev](https://www.fancycomponents.dev/) · Repo: [danielpetho/fancy](https://github.com/danielpetho/fancy) (3.312 estrellas el 19/11/2026, MIT). Último push: 14 de marzo de 2026, 07:34 (America/Argentina/Salta).
- **Stack:** React, TypeScript, Tailwind CSS, Motion, shadcn CLI.
- **Instalación:** Agregar el registry en components.json: "@fancy": "https://fancycomponents.dev/r/{name}.json". Después: npx shadcn add @fancy/{component-name}. Las dependencias extra hay que instalarlas a mano (aviso oficial en la docs de instalación).
- **Cuándo usarlo:** microinteracciones raras de texto y hover; un scramble, un morph, un gesto 'weird' bien hecho.
- **Cuándo no:** esperar commits semanales (último push del repo: 14/03/2026); el sitio seguía vivo el 19/11/2026.
- **Piezas curadas:** [Scramble Hover](https://www.fancycomponents.dev/docs/components/text/scramble-hover), [Docs de instalación](https://www.fancycomponents.dev/docs/installation).
- **Nota:** Se vende como 'fun and weird'. Es de las mejores fuentes para no caer en el glow genérico, si se elige una sola pieza y se retoca.

### Kokonut UI · **nueva en el kit**

- **Oficial:** [kokonutui.com](https://kokonutui.com/) · Repo: [kokonut-labs/kokonutui](https://github.com/kokonut-labs/kokonutui) (2.385 estrellas el 19/11/2026, MIT (free); hay un Pro aparte). Último push: 16 de noviembre de 2026, 13:04 (America/Argentina/Salta).
- **Stack:** React, Tailwind CSS, Motion, shadcn/ui, shadcn CLI.
- **Instalación:** `npx shadcn@latest add @kokonutui/{name}`
- **Cuándo usarlo:** inputs y controles de productos AI (prompt, file chips, stop); botones táctiles (command-button, card-flip).
- **Cuándo no:** usar el catálogo Pro sin leer términos; copiar el 'AI prompt' idéntico al de todos los wrappers de chat.
- **Piezas curadas:** [AI Prompt](https://kokonutui.com/docs/components/ai-prompt).
- **Nota:** El sitio se presenta como 'Open-Source AI Components for React'. registry.directory listaba 107 ítems. Muy citado en X en 2026 (@21st_dev, @nectxrz).

### Vengeance UI · **nueva en el kit**

- **Oficial:** [www.vengenceui.com](https://www.vengenceui.com/). Sin repo público verificado el 19/11/2026. El sitio dice que cada componente es open source; conviene verificar los términos en la ficha.
- **Stack:** React, shadcn CLI.
- **Instalación:** `npx shadcn@latest add @vengeanceui/{component}`
- **Cuándo usarlo:** botones y textos con interacción rara (liquid, morph, glitch); cuando Magic/Aceternity ya se sienten vistos.
- **Cuándo no:** usar creepy-button o liquid-metal como identidad de un producto serio; asumir MIT sin leer la página de la pieza.
- **Piezas curadas:** [Liquid Button](https://www.vengenceui.com/components/liquid-button), [Liquid Metal](https://www.vengenceui.com/components/liquid-metal), [Morph Text](https://www.vengenceui.com/components/morph-text), [ASCII Glitch Ripple](https://www.vengenceui.com/components/ascii-glitch-ripple), [Gooey Text Reveal](https://www.vengenceui.com/components/gooey-text-reveal).
- **Nota:** Aparece en threads de r/shadcn (feb 2026) como alternativa 'production-ready' y de interacciones únicas. El dominio se escribe vengence (sin 'a' en el medio).

### useLayouts · **nueva en el kit**

- **Oficial:** [uselayouts.com](https://uselayouts.com/) · Repo: [iurvish/uselayouts](https://github.com/iurvish/uselayouts) (720 estrellas el 19/11/2026, MIT). Último push: 3 de noviembre de 2026, 06:42 (America/Argentina/Salta).
- **Stack:** React, TypeScript, Tailwind CSS, Motion, shadcn / Radix.
- **Instalación:** Copy-paste de un archivo por componente (el home lo presenta así). 69 componentes según el llms.txt del 19/11/2026.
- **Cuándo usarlo:** microinteracciones y layouts animados en un archivo, MIT.
- **Cuándo no:** confundirlo con UI Layouts / ui-layouts (otro autor, Naymur Rahman).
- **Piezas curadas:** [Home / catálogo](https://uselayouts.com/).
- **Nota:** Repo creado en diciembre de 2025. El sitio afirma 69 componentes interactivos.

### BadtzUI · **nueva en el kit**

- **Oficial:** [www.badtz-ui.com](https://www.badtz-ui.com/) · Repo: [badtzx0/badtz-ui](https://github.com/badtzx0/badtz-ui) (269 estrellas el 19/11/2026, NOASSERTION en GitHub (hay plan Pro en el sitio; no se leyó un SPDX claro el 19/11/2026)). Último push: 27 de febrero de 2026, 12:47 (America/Argentina/Salta).
- **Stack:** React, Tailwind CSS, Motion, shadcn.
- **Instalación:** CLI o snippets desde badtz-ui.com/docs. Verificar términos de las piezas Pro.
- **Cuándo usarlo:** dock, particles, shaders y cards con motion, si la licencia de esa pieza cierra.
- **Cuándo no:** asumir MIT; depender de un repo cuyo último push visto es del 27/02/2026.
- **Piezas curadas:** [Dock](https://www.badtz-ui.com/docs/components/dock), [Particles](https://www.badtz-ui.com/docs/components/particles), [Border Beam](https://www.badtz-ui.com/docs/components/border-beam), [Cursor Card](https://www.badtz-ui.com/docs/components/cursor-card), [Pulse Shader](https://www.badtz-ui.com/docs/shaders/pulse-shader).
- **Nota:** El sitio seguía vivo. Varias piezas recuerdan a Magic/Aceternity (border-beam, dock): usarlas con criterio de originalidad.

### Lukacho UI · **nueva en el kit**

- **Oficial:** [ui.lukacho.com](https://ui.lukacho.com/). Sin repo público verificado el 19/11/2026 (tampoco un SPDX). Aparece también en 21st.dev; verificar términos en cada ficha.
- **Stack:** React, animaciones y charts en el catálogo del sitio.
- **Instalación:** Copy-paste desde ui.lukacho.com/components.
- **Cuándo usarlo:** cursores custom, backgrounds de grid/beam, un chart animado puntual.
- **Cuándo no:** usar un custom cursor en un dashboard de trabajo; asumir MIT.
- **Piezas curadas:** [Custom Cursor](https://ui.lukacho.com/components/custom-cursor), [Figma Cursor](https://ui.lukacho.com/components/figma-cursor), [Animated Grid Background](https://ui.lukacho.com/components/animated-grid-background), [Background Grid Beam](https://ui.lukacho.com/components/background-grid-beam), [Animated Chart](https://ui.lukacho.com/components/animated-chart).
- **Nota:** El sitio resolvió 200. Hay menciones antiguas en listas de librerías con Motion. No confundir con forks de GitHub no oficiales (se vio uno a 0 estrellas).

### unlumen UI · **nueva en el kit**

- **Oficial:** [ui.unlumen.com](https://ui.unlumen.com/) · Repo: [leovvx/unlumen-ui-docs](https://github.com/leovvx/unlumen-ui-docs) (82 estrellas el 19/11/2026, MIT en el repo de docs; el sitio distingue componentes open-source y Pro (hay que comprar los Pro)). Último push: 13 de septiembre de 2026, 15:01 (America/Argentina/Salta).
- **Stack:** React, TypeScript, Tailwind CSS, Motion.
- **Instalación:** Según ui.unlumen.com y su llms.txt. No tratar el repo de docs como el source completo de las piezas Pro.
- **Cuándo usarlo:** explorar una librería animada más chica, si se respeta el corte free/Pro.
- **Cuándo no:** copiar piezas Pro o asumir que todo es MIT.
- **Piezas curadas:** [Home / catálogo](https://ui.unlumen.com/).
- **Nota:** El único repo público claro el 19/11/2026 es el de documentación (82 estrellas). El catálogo vive en el sitio.

## Bloques y secciones

Hero, pricing, bento, chat, dashboards: secciones enteras más que átomos. coss ui y Kibo ya estaban en `componentes/`; el resto es nuevo. No confundir **Shadcnblocks** (shadcnblocks.com) con **blocks.so** (otro repo, MIT) ni con el title de blocks.so, que también dice «Shadcn Blocks».

### coss ui (antes Origin UI) · **ya en componentes/**

- **Oficial:** [coss.com/ui/docs](https://coss.com/ui/docs) · Repo: [cosscom/ui](https://github.com/cosscom/ui) (MIT).
- **Stack:** React, Base UI, Tailwind CSS.
- **Cuándo usarlo:** apps de producto; forms y composiciones densas.
- **Cuándo no:** efectos de marketing como sistema.
- **En el kit:** Ya estaba en [`../componentes/`](../componentes/bibliotecas.md).
- **Piezas curadas:** [Documentación de coss ui](https://coss.com/ui/docs).
- **Nota:** Ficha en componentes/. Origin UI se unió a Cal.com (colección legacy en coss.com/origin). No es un kit 'de glow'; es la capa de producto densa.

### Kibo UI · **ya en componentes/**

- **Oficial:** [www.kibo-ui.com](https://www.kibo-ui.com/) · Repo: [shadcnblocks/kibo](https://github.com/shadcnblocks/kibo) (3.985 estrellas el 19/11/2026, MIT). Último push: 4 de mayo de 2026, 03:00 (America/Argentina/Salta).
- **Stack:** React, shadcn/ui, Tailwind CSS.
- **Instalación:** `npx shadcn@latest add @kibo-ui/{name}`
- **Cuándo usarlo:** Gantt, Kanban, editores y componentes avanzados de producto.
- **Cuándo no:** instalarlo como theme de marketing.
- **En el kit:** Ya estaba en [`../componentes/`](../componentes/bibliotecas.md).
- **Piezas curadas:** [Gantt](https://www.kibo-ui.com/components/gantt).
- **Nota:** Creado por Hayden Bleasel. Adquirido por Shadcnblocks el 28 de octubre de 2025. El último push del repo visto el 19/11/2026 es del 4 de mayo de 2026; el sitio seguía vivo.

### Shadcnblocks · **nueva en el kit**

- **Oficial:** [www.shadcnblocks.com](https://www.shadcnblocks.com/) · Repo: [shadcnblocks/shadcn-ui-blocks](https://github.com/shadcnblocks/shadcn-ui-blocks) (418 estrellas el 19/11/2026, NOASSERTION en el repo público (hay bloques free en /blocks/free y planes pagos en el sitio; no se leyó un SPDX claro)). Último push: 9 de octubre de 2025, 17:08 (America/Argentina/Salta).
- **Stack:** React, Next.js, Tailwind CSS, shadcn/ui.
- **Instalación:** Explorar https://www.shadcnblocks.com/blocks y el recorte free en https://shadcnblocks.com/blocks/free. El repo público no parece el catálogo completo (último push: 9/10/2025).
- **Cuándo usarlo:** secciones de marketing (hero, bento, pricing, careers) sobre shadcn; cuando hace falta un bloque completo, no un átomo.
- **Cuándo no:** armar un sitio entero con bloques stock sin retocar tipo y color; confundirlo con blocks.so, que es otro proyecto.
- **Piezas curadas:** [Bento](https://www.shadcnblocks.com/blocks/bento), [Background pattern](https://www.shadcnblocks.com/blocks/background-pattern), [Banner](https://www.shadcnblocks.com/blocks/banner), [Book a demo](https://www.shadcnblocks.com/blocks/book-a-demo), [Chart card](https://www.shadcnblocks.com/blocks/chart-card).
- **Nota:** Muy citado por @orcdev como la librería de bloques más consistente. También es el dueño actual de Kibo UI. Verificar licencia de cada bloque (free vs Pro).

### Tailark · **nueva en el kit**

- **Oficial:** [tailark.com](https://tailark.com/). Sin repo público de componentes verificado el 19/11/2026 (solo repos auxiliares como tailark/pro-images). Freemium según el sitio y listas de 2026.
- **Stack:** React, Tailwind CSS, shadcn/ui.
- **Instalación:** Desde tailark.com (bloques y temas). Confirmar términos del plan.
- **Cuándo usarlo:** landings de conversión con un lenguaje visual más cohesivo que un collage de registries.
- **Cuándo no:** asumir que todo es MIT y publicable como pack.
- **Piezas curadas:** [Home](https://tailark.com/), [Bloque Quartz](https://tailark.com/blocks/quartz).
- **Nota:** Autor citado en X como @MeschacIrung. Aparece en casi todas las listas de 'top shadcn block libraries' de 2025–2026 (OrcDev lo tenía alto en octubre de 2025).

### Efferd · **nueva en el kit**

- **Oficial:** [efferd.com](https://efferd.com/) · Repo: [shabanwtf/efferd-ui](https://github.com/shabanwtf/efferd-ui) (150 estrellas el 19/11/2026, NOASSERTION en GitHub; el sitio se presenta para agentes que colocan y themean bloques. Verificar términos.). Último push: 10 de diciembre de 2025, 09:53 (America/Argentina/Salta).
- **Stack:** React, shadcn/ui.
- **Instalación:** Desde efferd.com (hay docs MCP, incluido Cursor: https://efferd.com/docs/mcp/cursor).
- **Cuándo usarlo:** que un agente arme una landing a partir de bloques ya nombrados (hero-1, hero-2, …).
- **Cuándo no:** tratar el repo público (último push 10/12/2025, homepage legacy.efferd.com) como la fuente actual; el producto vive en efferd.com.
- **Piezas curadas:** [Hero (familia de bloques)](https://efferd.com/blocks/hero).
- **Nota:** Citado por @21st_dev en septiembre de 2026 junto a Kokonut, HextaUI, ReUI y Cult. Pensado para agentes, no solo para copy-paste humano.

### craftUI · **nueva en el kit**

- **Oficial:** [www.craftui.space](https://www.craftui.space/). Sin repo público verificado el 19/11/2026 (`hardimpactdev/craft-ui` devolvió 404). El llms.txt del sitio describe bloques shadcn/ui; verificar términos ahí.
- **Stack:** React, shadcn/ui, Tailwind CSS.
- **Instalación:** Desde craftui.space (el sitio y su llms.txt listan secciones, bloques e ilustraciones).
- **Cuándo usarlo:** secciones de SaaS/landing sobre shadcn, si la licencia de esa pieza cierra.
- **Cuándo no:** asumir MIT o un repo oficial que hoy no aparece.
- **Piezas curadas:** [Home / catálogo](https://www.craftui.space/).
- **Nota:** craftui.space redirige a www.craftui.space. GET 200 el 19/11/2026. No inventar un GitHub que no se pudo confirmar.

### Launch UI · **nueva en el kit**

- **Oficial:** [www.launchuicomponents.com](https://www.launchuicomponents.com/) · Repo: [launch-ui/launch-ui](https://github.com/launch-ui/launch-ui) (875 estrellas el 19/11/2026, MIT (el repo es un kit/template; hay recorte Pro en el sitio)). Último push: 4 de noviembre de 2026, 08:11 (America/Argentina/Salta).
- **Stack:** React, shadcn/ui, Tailwind CSS, Radix.
- **Instalación:** Copy/paste o partir del template del repo (es template de GitHub). Docs: https://www.launchuicomponents.com/docs/getting-started/installation
- **Cuándo usarlo:** armar una landing completa (navbar, hero, bento, pricing, social proof) con un solo lenguaje; un starter, no un átomo suelto.
- **Cuándo no:** dejar el look de Launch UI sin cambiar tipo, radio y acento.
- **Piezas curadas:** [Hero](https://www.launchuicomponents.com/docs/sections/hero), [Bento Grid](https://www.launchuicomponents.com/docs/sections/bento-grid), [Navbar](https://www.launchuicomponents.com/docs/sections/navbar), [Pricing](https://www.launchuicomponents.com/docs/sections/pricing), [Glow (componente)](https://www.launchuicomponents.com/docs/components/glow).
- **Nota:** Se describe como landing page kit copy/paste. El repo público está activo en noviembre de 2026.

### Shadcn Studio · **nueva en el kit**

- **Oficial:** [shadcnstudio.com](https://shadcnstudio.com/) · Repo: [shadcnstudio/shadcn-studio](https://github.com/shadcnstudio/shadcn-studio) (1.995 estrellas el 19/11/2026, MIT + Commons Clause (y cláusula de no competir)). Último push: 20 de agosto de 2026, 07:38 (America/Argentina/Salta).
- **Stack:** React, shadcn/ui, Motion (variantes animadas), theme generator, MCP, builder.
- **Instalación:** Copy-paste, CLI y herramientas del sitio (theme generator, MCP, builder). El recorte open-source está en el repo; hay capas premium.
- **Cuándo usarlo:** variantes de componentes y bloques shadcn, más un theme generator; cuando se necesita un ecosistema (Figma, MCP, templates), no un solo átomo.
- **Cuándo no:** redistribuir las piezas como librería o clonar el producto; dejar el theme default.
- **Licencia, con detalle:** LICENSE.md leída el 2026-11-19: MIT, más restricción de no vender/redistribuir los componentes sin modificación, y de no usarlo para un producto que compita con shadcn/studio.
- **Piezas curadas:** [Home](https://shadcnstudio.com/), [Intro de docs](https://shadcnstudio.com/docs/getting-started/introduction).
- **Nota:** Muy presente en listas de X 2025–2026 (Ajay Patel / @ajaypatel_aj es el autor más citado). El repo público tiene último push del 20/08/2026; el sitio seguía vivo.

### ReUI · **nueva en el kit**

- **Oficial:** [reui.io](https://reui.io/) · Repo: [keenthemes/reui](https://github.com/keenthemes/reui) (4.197 estrellas el 19/11/2026, MIT). Último push: 16 de octubre de 2026, 07:15 (America/Argentina/Salta).
- **Stack:** React, Tailwind CSS, shadcn/ui, Radix y Base UI, TanStack Table.
- **Instalación:** `npx shadcn@latest add` (registry de ReUI). El llms.txt del 19/11/2026 habla de 27 primitivas propias y 1.265 ejemplos free, más un recorte premium.
- **Cuándo usarlo:** product UI densa: data grid, kanban, filtros, gantt, calendar, file upload; pasar de primitivas shadcn a pantallas reales.
- **Cuándo no:** usarlo como kit de marketing con glow; instalar 1.200 ejemplos 'porque están'.
- **Piezas curadas:** [Catálogo de componentes](https://reui.io/components).
- **Nota:** Keenthemes. El sitio se presenta en clave anti-default de IA. Buen par de Kibo/coss para producto, no para un hero de partículas.

### Intent UI · **nueva en el kit**

- **Oficial:** [intentui.com](https://intentui.com/) · Repo: [irsyadadl/intentui](https://github.com/irsyadadl/intentui) (1.978 estrellas el 19/11/2026, MIT). Último push: 19 de noviembre de 2026, 06:09 (America/Argentina/Salta).
- **Stack:** React, React Aria Components, Tailwind CSS, shadcn CLI (namespace @intentui).
- **Instalación:** `npx shadcn@latest add @intentui/{name}` ([registry.directory](https://registry.directory/intentui/intentui) listaba 582 ítems). Usar [intentui.com](https://intentui.com/); `www.intentui.com` tenía el certificado SSL vencido el 19/11/2026.
- **Cuándo usarlo:** una librería accesible copy-paste sobre React Aria, no sobre Radix/Base UI; cuando se quiere dueñar el código con WAI-ARIA sólido.
- **Cuándo no:** sumarlo a un proyecto que ya está en shadcn + Base UI / Radix (son dos familias de primitivas).
- **Piezas curadas:** [Home](https://intentui.com/).
- **Nota:** Activo el 19/11/2026. No es 'otro Magic UI': es un kit de producto accesible que además publica registry shadcn.

### HextaUI · **nueva en el kit**

- **Oficial:** [hextaui.com](https://hextaui.com/) · Repo: [preetsuthar17/hextaui](https://github.com/preetsuthar17/hextaui) (167 estrellas el 19/11/2026, MIT). Último push: 16 de noviembre de 2026, 11:06 (America/Argentina/Salta).
- **Stack:** React, shadcn/ui, Base UI.
- **Instalación:** `npx shadcn@latest add https://hextaui.com/r/{name}.json`
- **Cuándo usarlo:** bloques de productos AI (chat thread, prompt input, subagents, diff review) con estados loading/error/empty.
- **Cuándo no:** usarlo como librería de marketing genérica.
- **Piezas curadas:** [Chat Thread](https://hextaui.com/blocks/chat-thread), [Chat Sidebar](https://hextaui.com/blocks/chat-sidebar), [Prompt Input](https://hextaui.com/blocks/prompt-input), [Subagents](https://hextaui.com/blocks/subagents), [Diff Review](https://hextaui.com/blocks/diff-review).
- **Nota:** Repo relativamente nuevo (creado el 25/09/2026) y ya activo en noviembre. Complementa a Cult/Kokonut en el nicho de UI para agentes.

### Dice UI · **nueva en el kit**

- **Oficial:** [diceui.com](https://diceui.com/). Sin repo público verificado el 19/11/2026 (se probaron rutas habituales y no resolvieron). Verificar términos en el sitio.
- **Stack:** React, TypeScript, Tailwind CSS, shadcn/ui, variantes Base UI y Radix.
- **Instalación:** Desde las docs: https://diceui.com/docs/components (hay árboles /docs/components/base/* y /docs/components/radix/*).
- **Cuándo usarlo:** componentes de producto menos comunes (query builder, command stack, data grid, scroll spy, marquee).
- **Cuándo no:** asumir un SPDX que no se pudo leer.
- **Piezas curadas:** [Query Builder](https://diceui.com/docs/components/base/query-builder), [Data Grid](https://diceui.com/docs/components/base/data-grid), [Command Stack](https://diceui.com/docs/components/base/command-stack), [File Upload](https://diceui.com/docs/components/base/file-upload), [Marquee](https://diceui.com/docs/components/base/marquee).
- **Nota:** Aparece en listas de Reddit (dic 2025) y en posts de 'librerías que sí se sienten pulidas'. www.diceui.com redirige a diceui.com.

### blocks.so · **nueva en el kit**

- **Oficial:** [blocks.so](https://blocks.so/) · Repo: [ephraimduncan/blocks](https://github.com/ephraimduncan/blocks) (1.865 estrellas el 19/11/2026, MIT). Último push: 30 de octubre de 2026, 16:48 (America/Argentina/Salta).
- **Stack:** React, Tailwind CSS, shadcn/ui.
- **Instalación:** Desde blocks.so y el repo (el sitio se presenta como 60+ bloques free). No confundir con shadcnblocks.com.
- **Cuándo usarlo:** un set MIT, más chico, de bloques shadcn.
- **Cuándo no:** confundir el nombre 'Shadcn Blocks' del title del sitio con la marca shadcnblocks.com.
- **Piezas curadas:** [Home / catálogo](https://blocks.so/).
- **Nota:** Autor ephraimduncan; se anunció en un comentario de r/webdev (nov 2025). Título del sitio el 19/11/2026: 'Shadcn Blocks - 60+ Free shadcn/ui Components for React'.

### 8bitcn/ui · **nueva en el kit**

- **Oficial:** [www.8bitcn.com](https://www.8bitcn.com/) · Repo: [TheOrcDev/8bitcn-ui](https://github.com/TheOrcDev/8bitcn-ui) (2.083 estrellas el 19/11/2026, MIT). Último push: 5 de noviembre de 2026, 17:29 (America/Argentina/Salta).
- **Stack:** React, shadcn/ui.
- **Instalación:** Desde https://www.8bitcn.com/docs/components (registry shadcn del propio OrcDev).
- **Cuándo usarlo:** un producto que realmente quiere look retro/8-bit; salir del default 'SaaS índigo' con una decisión de estilo.
- **Cuándo no:** usarlo 'un poquito' en una app corporativa (el look es una tesis, no un acento).
- **Piezas curadas:** [Componentes](https://www.8bitcn.com/docs/components), [Blocks](https://www.8bitcn.com/docs/blocks).
- **Nota:** De @orcdev, autor de muchas de las listas de X citadas en esta investigación. Es un estilo, no un cajón de efectos.

### shadcn.io · **nueva en el kit**

- **Oficial:** [www.shadcn.io](https://www.shadcn.io/). Sin repo público verificado el 19/11/2026. Verificar en el sitio (hay recorte free y planes). astrae.design redirigió a este dominio el 19/11/2026.
- **Stack:** React, shadcn/ui.
- **Instalación:** Explorar bloques y átomos en shadcn.io (hay /hero-block, /chat-block, /background, /text, etc.).
- **Cuándo usarlo:** un catálogo grande de bloques para agentes y landings, cuando se elige poco y se tokeniza.
- **Cuándo no:** pegar bloques de 10 categorías distintas; asumir que astrae.design sigue siendo un producto aparte: el 19/11/2026 redirigía acá.
- **Piezas curadas:** [Hero Block](https://www.shadcn.io/hero-block), [Chat Block](https://www.shadcn.io/chat-block), [Background](https://www.shadcn.io/background), [Text](https://www.shadcn.io/text), [Pricing Block](https://www.shadcn.io/pricing-block).
- **Nota:** Algunas listas de 2026 todavía hablan de Astrae (astrae.design). Comprobar siempre el dominio final.

## Fondos y efectos

No hay un sitio que sea *solo* fondos. Las piezas buenas viven dentro de librerías ya fichadas. Elegir una y retocar color, grano y velocidad; el Aurora, el beam y el spotlight ya son un cliché de 2026.

| Pieza | Librería | URL |
|---|---|---|
| Aurora | React Bits | [reactbits.dev/backgrounds/aurora](https://www.reactbits.dev/backgrounds/aurora) |
| Silk | React Bits | [reactbits.dev/backgrounds/silk](https://www.reactbits.dev/backgrounds/silk) |
| Background Beams | Aceternity UI | [ui.aceternity.com/components/background-beams](https://ui.aceternity.com/components/background-beams) |
| Spotlight | Aceternity UI | [ui.aceternity.com/components/spotlight](https://ui.aceternity.com/components/spotlight) |
| Particles | BadtzUI | [badtz-ui.com/docs/components/particles](https://www.badtz-ui.com/docs/components/particles) |
| Pulse Shader | BadtzUI | [badtz-ui.com/docs/shaders/pulse-shader](https://www.badtz-ui.com/docs/shaders/pulse-shader) |
| Animated Grid Background | Lukacho UI | [ui.lukacho.com/components/animated-grid-background](https://ui.lukacho.com/components/animated-grid-background) |
| Background Grid Beam | Lukacho UI | [ui.lukacho.com/components/background-grid-beam](https://ui.lukacho.com/components/background-grid-beam) |
| Background (catálogo) | shadcn.io | [shadcn.io/background](https://www.shadcn.io/background) |
| Backgrounds (categoría) | 21st.dev | [21st.dev/community/components/s/background](https://21st.dev/community/components/s/background) |

Ver también Magic UI (beams, particles) y Animata. En producto, conviene un fondo quieto del kit de [`../tokens/`](../tokens/README.md) y [`../recursos/texturas.md`](../recursos/texturas.md).

## Efectos de texto

Una animación de título puede dar carácter. Ocho a la vez, no. Animata es la ficha principal de este grupo porque su catálogo y su guía de 2026 están centrados en texto, con MIT limpio.

### Animata · **nueva en el kit**

- **Oficial:** [animata.design](https://animata.design/) · Repo: [codse/animata](https://github.com/codse/animata) (3.003 estrellas el 19/11/2026, MIT). Último push: 3 de noviembre de 2026, 13:01 (America/Argentina/Salta).
- **Stack:** React, Tailwind CSS v4, shadcn CLI, WAAPI en varios textos.
- **Instalación:** `npx shadcn add https://animata.design/r/{category}/{name}.json` (ejemplo: `https://animata.design/r/container/marquee.json`). El registry se lanzó en abril de 2026.
- **Cuándo usarlo:** presets de texto (gradient, blur, glitch, counter, split); botones y widgets animados MIT, sin Commons Clause.
- **Cuándo no:** aplicar 8 presets de texto en un mismo hero.
- **Piezas curadas:** [Animated Gradient Text](https://animata.design/docs/text/animated-gradient-text), [Guía de text effects 2026](https://animata.design/docs/guides/animated-react-text-effects), [Guía de botones animados 2026](https://animata.design/docs/guides/animated-react-buttons).
- **Nota:** El llms.txt habla de ~130 primitivas. Buena opción cuando se quiere motion de texto con MIT limpio.

Otras piezas curadas en librerías ya descritas:

| Pieza | Librería | URL |
|---|---|---|
| Split Text | React Bits | [reactbits.dev/text-animations/split-text](https://www.reactbits.dev/text-animations/split-text) |
| Blur Text | React Bits | [reactbits.dev/text-animations/blur-text](https://www.reactbits.dev/text-animations/blur-text) |
| Text Generate Effect | Aceternity UI | [ui.aceternity.com/components/text-generate-effect](https://ui.aceternity.com/components/text-generate-effect) |
| Text Effect | Motion Primitives | [motion-primitives.com/docs/text-effect](https://www.motion-primitives.com/docs/text-effect) |
| Scramble Hover | Fancy Components | [fancycomponents.dev/docs/components/text/scramble-hover](https://www.fancycomponents.dev/docs/components/text/scramble-hover) |
| Morph Text | Vengeance UI | [vengenceui.com/components/morph-text](https://www.vengenceui.com/components/morph-text) |
| Gooey Text Reveal | Vengeance UI | [vengenceui.com/components/gooey-text-reveal](https://www.vengenceui.com/components/gooey-text-reveal) |
| Text animation | Indie UI | [ui.indie-starter.dev/docs/text-animation](https://ui.indie-starter.dev/docs/text-animation) |
| Text (categoría) | Hover.dev | [hover.dev/components/text](https://www.hover.dev/components/text) |

## 3D y WebGL

Útil en un hero o un poster. Caro en una app de trabajo. Probar en un teléfono, respetar `prefers-reduced-motion` ([`../animaciones/accesibilidad-performance.md`](../animaciones/accesibilidad-performance.md)) y no mezclar Three/OGL de React Bits con el 3D card de Aceternity y el globo de Eldora en la misma página.

| Pieza | Librería | URL |
|---|---|---|
| 3D Card Effect | Aceternity UI | [ui.aceternity.com/components/3d-card-effect](https://ui.aceternity.com/components/3d-card-effect) |
| Aurora / Silk (fondos WebGL) | React Bits | [Aurora](https://www.reactbits.dev/backgrounds/aurora), [Silk](https://www.reactbits.dev/backgrounds/silk) |
| Three-D (categoría) | Hover.dev | [hover.dev/components/three-d](https://www.hover.dev/components/three-d) |
| 3D Wrapper | BadtzUI | [badtz-ui.com/docs/components/3d-wrapper](https://www.badtz-ui.com/docs/components/3d-wrapper) |
| Pulse Shader | BadtzUI | [badtz-ui.com/docs/shaders/pulse-shader](https://www.badtz-ui.com/docs/shaders/pulse-shader) |
| ASCII Glitch Ripple | Vengeance UI | [vengenceui.com/components/ascii-glitch-ripple](https://www.vengenceui.com/components/ascii-glitch-ripple) |

React Bits declara GSAP, Motion, Three.js u OGL *según el componente*. Hay que mirar las dependencias de esa ficha, no asumir un único motor.

## Registries y directorios

No son librerías de look: son el mapa del ecosistema. 21st.dev ya estaba en `componentes/`.

### 21st.dev · **ya en componentes/**

- **Oficial:** [21st.dev](https://21st.dev/). Sin repo público verificado el 19/11/2026. Varía por pieza.
- **Stack:** mixto, shadcn registries, MCP y CLI propios.
- **Instalación:** Explorar y copiar, o instalar vía shadcn CLI / MCP (https://21st.dev/mcp). El paquete @21st-dev/magic es alias del MCP actual.
- **Cuándo usarlo:** descubrir piezas y librerías de la comunidad; que un agente busque e instale un registry.
- **Cuándo no:** pegar 15 estilos distintos en un mismo producto; tratarlo como un design system.
- **En el kit:** Ya estaba en [`../componentes/`](../componentes/bibliotecas.md).
- **Piezas curadas:** [Componentes populares](https://21st.dev/community/components/popular), [Text Animation (categoría)](https://21st.dev/community/components/s/text-animation), [Backgrounds (categoría)](https://21st.dev/community/components/s/background), [AI Chat (categoría)](https://21st.dev/community/components/s/ai-chat), [Hero Sections (categoría)](https://21st.dev/community/components/s/hero).
- **Nota:** El llms.txt oficial del 19/11/2026 habla de 12.000+ piezas. No es una librería única. Fundado por Serafim Korablev y Sergey Bunas.

### registry.directory · **nueva en el kit**

- **Oficial:** [registry.directory](https://registry.directory/). Sin repo público verificado el 19/11/2026. No aplica (directorio; la licencia es la de cada registry).
- **Stack:** explorador del ecosistema de registries shadcn.
- **Instalación:** No instala componentes propios. Sirve para descubrir namespaces y comandos `npx shadcn@latest add @ns/item`.
- **Cuándo usarlo:** comparar registries (Kokonut, Intent, etc.) y copiar el comando de instalación; investigar qué hay publicado antes de sumar otra lib.
- **Cuándo no:** instalar 'todo lo que aparece'.
- **Piezas curadas:** [Home](https://registry.directory/), [kokonut/ui](https://registry.directory/kokonut-labs/kokonutui), [Intent UI](https://registry.directory/intentui/intentui).
- **Nota:** Se presenta como 'The explorer for the shadcn registry ecosystem'. Complementa el directorio oficial de shadcn.

### Registry Directory oficial de shadcn · **ya se mencionaba en componentes/**

- **Oficial:** [ui.shadcn.com/docs/directory](https://ui.shadcn.com/docs/directory) · Repo: [shadcn-ui/ui](https://github.com/shadcn-ui/ui) (MIT (el proyecto shadcn/ui; cada registry listado tiene la suya)).
- **Stack:** directorio oficial de namespaces y registries.
- **Instalación:** Leer https://ui.shadcn.com/docs/registry/namespace y https://ui.shadcn.com/docs/registry/registry-index. Instalar con `npx shadcn@latest add @namespace/item`.
- **Cuándo usarlo:** la fuente canónica de namespaces (@magicui, @cult-ui, @react-bits, @kibo-ui, etc.); antes de inventar una URL de registry.
- **Cuándo no:** saltarlo y copiar registries de tweets sin mirar si siguen listados.
- **Piezas curadas:** [Directory](https://ui.shadcn.com/docs/directory), [Registry index (docs)](https://ui.shadcn.com/docs/registry/registry-index), [Namespaces](https://ui.shadcn.com/docs/registry/namespace).
- **Nota:** Ya se menciona en componentes/bibliotecas.md. Acá queda como ficha de descubrimiento, no como librería visual en sí.

## Fuentes de esta pasada

- Sitios oficiales (GET 200 el 19/11/2026) y, cuando existían, sus `llms.txt` o sitemaps.
- API de GitHub: estrellas, SPDX o lectura de `LICENSE.md` (React Bits, Shadcn Studio) y fecha de último push.
- Reddit: [7 shadcn-based libraries that actually look good in 2026](https://www.reddit.com/r/shadcn/comments/1rdwh1k/7_shadcnbased_libraries_that_actually_look_good/) (r/shadcn, 24/02/2026), [Shadcn-compatible UI libraries](https://www.reddit.com/r/Frontend/comments/1rgfrvf/shadcncompatible_ui_libraries_worth_exploring/) (r/Frontend, 27/02/2026), [Top 20 Shadcn based React UI libraries](https://www.reddit.com/r/shadcn/comments/1pjrhcl/these_are_the_top_20_shadcn_based_react_ui/) (11/12/2025) y hilos de noviembre de 2025 en r/shadcn y r/webdev.
- X, de junio de 2025 a noviembre de 2026: listas de [@orcdev](https://x.com/orcdev/status/1979112824656818183), [@21st_dev](https://x.com/21st_dev/status/2103324298027085942), [@naymur_dev](https://x.com/naymur_dev/status/1987111926833508635), entre otras.
- No se tomaron como verdad los números de posts o blogs (estrellas desactualizadas, conteos de componentes). Donde hay cifra de estrellas, salió de GitHub el 19/11/2026.

Lo que no entró: primitivas headless (shadcn, Base UI, Radix, Ark, React Aria) y sistemas empaquetados (HeroUI, Park UI, Tremor), que ya están en [`../componentes/bibliotecas.md`](../componentes/bibliotecas.md). Herramientas de motion (GSAP, Motion, Rive, Lottie) están en [`../animaciones/`](../animaciones/README.md).

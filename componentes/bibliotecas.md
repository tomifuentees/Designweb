# Librerías y registries

Foto del 19 de noviembre de 2026. Las URLs de esta ficha resolvieron con `GET` (o antibot, no 404) desde este entorno. Los datos de licencia y de “último push” salen de los repos oficiales o de npm; donde el estado es incierto, queda marcado.

La pregunta útil no es “¿cuál es la mejor librería?”. Es: **¿necesito primitivas headless, un flujo copy-paste, un kit de marketing o un bloque de producto avanzado?** Mezclar las cuatro capas sin criterio es como se llega al look de plantilla.

## Primitivas y el flujo shadcn

### shadcn/ui

- **Oficial:** [ui.shadcn.com](https://ui.shadcn.com/) · Repo: [shadcn-ui/ui](https://github.com/shadcn-ui/ui) (MIT, activo el 19/11/2026).
- **Stack:** React, Tailwind CSS, primitivas de **Base UI** (default en proyectos nuevos desde julio de 2026) o **Radix** (`shadcn init -b radix`).
- **Qué es:** no es una dependencia runtime. Es un flujo: copiás el código a tu repo y lo duele. El CLI instala ítems desde registries con namespaces (`@shadcn/button`, `@kibo-ui/…`, `owner/repo/item`). Docs del registry: [Registry Directory](https://ui.shadcn.com/docs/registry/registry-index), [Namespaces](https://ui.shadcn.com/docs/registry/namespace), [GitHub Registries](https://ui.shadcn.com/docs/registry/github).
- **Cambio de 2026:** el 3 de julio de 2026, shadcn anunció que Base UI es el default de `init`, de `shadcn/create` y de la documentación. Radix **no está deprecado**. La nota oficial: [July 2026 - Base UI as the Default](https://ui.shadcn.com/docs/changelog/2026-07-base-ui-default). El post de [X de @shadcn, 3 de julio de 2026](https://x.com/shadcn/status/2073021588044206483) lo resume. En marzo de 2026 también publicó [shadcn/skills](https://x.com/shadcn/status/2029974156620517585) para que los agentes respeten el sistema y el registry.
- **Cuándo usarlo:** casi cualquier app React/Tailwind que quiera dueñar el código. **Cuándo no:** si necesitás un tema Material/Ant completo ya resuelto, o si el equipo no va a retocar tokens: ahí el default se ve igual en todos lados.
- **Oficio:** cambiá tipografía (el kit está en [`../tipografias/`](../tipografias/README.md)), radio, acento y densidad *antes* de sumar un registry animado. shadcn es infraestructura, no personalidad.

### Base UI

- **Oficial:** [base-ui.com](https://base-ui.com/) · Repo: [mui/base-ui](https://github.com/mui/base-ui) (MIT, activo el 19/11/2026). Cuenta: [@base_ui](https://x.com/base_ui).
- **Stack:** React, sin CSS bundled. Funciona con Tailwind, CSS Modules, CSS-in-JS o CSS plano, y con Motion o transiciones CSS.
- **Qué es:** primitivas unstyled de los creadores de Radix, Floating UI y Material UI. MUI lo presenta como su dirección de largo plazo para componentes fundacionales; MUI Base (el paquete viejo) está deprecado. Fuente: [MUI Update: 2026 and beyond](https://mui.com/blog/2026-and-beyond/). Changelog del repo: v1.9.0 el 9 de octubre de 2026.
- **Versus Radix (según la propia home de Base UI):** APIs cercanas a propósito, para migrar. Base UI trae piezas más complejas (Combobox, Autocomplete), más soporte de edge cases (scrubbing, dialogs anidados, menús en hover) y un equipo full-time de 7 personas. shadcn, en julio de 2026, lo citaba en 1.6.0 con 6M+ descargas semanales.
- **Cuándo usarlo:** proyectos nuevos con shadcn, o un design system propio que quiera una base activa. **Cuándo no:** no reescribas una app Radix estable “porque ahora es el default”.

### Radix Primitives

- **Oficial:** [radix-ui.com](https://www.radix-ui.com/) · Repo: [radix-ui/primitives](https://github.com/radix-ui/primitives) (MIT). Último push visto en esta pasada: 14 de octubre de 2026. Releases documentadas hasta el 20 de julio de 2026 (fixes de Dialog, Toast, Tooltip, tree-shaking y subpaths `radix-ui/accordion`).
- **Stack:** React, unstyled, accesible.
- **Estado:** vivo y soportado. No está abandonado ni deprecado. Es, todavía, la base de muchísimos registries y de apps en producción. El ritmo de innovación visible está más en Base UI, y el ecosistema de bloques de terceros todavía es, en parte, Radix (el propio shadcn lo admitió en [X, 16 de enero de 2026](https://x.com/shadcn/status/2012155552064028874)).
- **Cuándo usarlo:** proyectos que ya lo tienen, o `shadcn init -b radix` si el equipo lo prefiere. **Cuándo no:** como “la opción moderna” en un greenfield de finales de 2026, salvo que haya una razón concreta.

### Ark UI

- **Oficial:** [ark-ui.com](https://ark-ui.com/) · Repo: [chakra-ui/ark](https://github.com/chakra-ui/ark) (MIT, activo el 19/11/2026).
- **Stack:** headless, **multi-framework** (React, Solid, Vue, Svelte). El paquete `@ark-ui/react` seguía publicándose en 2026 (se vio 5.40.0 listado en npm el 29 de octubre de 2026; confirmar siempre la versión actual). Lo mantiene el equipo de Chakra UI. Encima de Ark está [Park UI](https://park-ui.com/) (GET 200), un kit estilado con Panda CSS.
- **Cuándo usarlo:** design system multi-framework, o si ya vivís en el ecosistema Chakra/Panda. **Cuándo no:** un proyecto Next/Tailwind que ya está en shadcn + Base UI no gana nada sumando otra primitiva.

### React Aria (Adobe)

- **Oficial:** [react-aria.adobe.com](https://react-aria.adobe.com/) (el path histórico `react-spectrum.adobe.com/react-aria/` redirige acá). Repo: [adobe/react-spectrum](https://github.com/adobe/react-spectrum) (Apache-2.0, activo el 19/11/2026).
- **Stack:** React, hooks y componentes headless de alto nivel de a11y (internacionalización, comportamiento de teclado, ARR). Parte de React Spectrum.
- **Cuándo usarlo:** producto con requisitos fuertes de accesibilidad, i18n o un design system de empresa que no quiere Tailwind como contrato. **Cuándo no:** para “salir rápido” una landing: la curva es más alta que shadcn.

## Kits copy-paste y registries (encima de shadcn o Base UI)

### Magic UI

- **Oficial:** [magicui.design](https://magicui.design/) · Repo: [magicuidesign/magicui](https://github.com/magicuidesign/magicui) (MIT en los componentes free; Pro tiene [términos propios](https://pro.magicui.design/license)). Cuenta: [@magicuidesign](https://x.com/magicuidesign).
- **Stack:** React, Tailwind, Motion. Se instala con el CLI de shadcn. Hay MCP oficial para editores.
- **Para qué:** texto animado, number tickers, marquees, fondos y mockups de device en páginas de marketing. **Oficio:** un par de piezas, no un tour de efectos. El Pro no se redistribuye ni se revende como template.

### Aceternity UI

- **Oficial:** [ui.aceternity.com](https://ui.aceternity.com/). Componentes free instalables por shadcn CLI; planes Pro/lifetime para bloques y landings. Licencia Pro: [ui.aceternity.com/licence](https://ui.aceternity.com/licence) (GET 200): uso en productos finales y trabajo para clientes, sin revender el source ni armar un kit competidor.
- **Stack:** React, Tailwind, Motion (ex Framer Motion).
- **Para qué:** un hero o una sección que tenga que frenar el scroll (spotlight, lamp, 3D cards, parallax). **Oficio:** es el kit que más fácil convierte un sitio en “landing de IA con glow”. Usalo como *una* rareza, no como sistema. Para un look de producto, no compite con coss ni con shadcn bien tokenizado.

### coss ui (antes Origin UI)

- **Oficial:** [coss.com/ui/docs](https://coss.com/ui/docs) · Roadmap: [coss.com/ui/docs/roadmap](https://coss.com/ui/docs/roadmap) · Colección legacy: [coss.com/origin](https://coss.com/origin) · Repo: [cosscom/ui](https://github.com/cosscom/ui) (MIT, activo el 18/11/2026). Cuenta: [@coss_com](https://x.com/coss_com).
- **Hechos:** el 10 de octubre de 2025, Origin UI anunció que se unía a Cal.com y pasaba a ser coss ([post de @coss_com](https://x.com/coss_com/status/1976668768312123777); [Peer Richelsen el mismo día](https://x.com/peer_rich/status/1976671512305213770)). El 15 de octubre de 2025 lanzaron coss ui en Product Hunt ([anuncio](https://x.com/coss_com/status/1978416552266334299); [blog de Cal.com v5.8](https://cal.com/blog/calcom-v5-8)). Lo siguen Pasquale Vitiello ([@pacovitiello](https://x.com/pacovitiello), Director of Design Engineering en Cal/coss) y el equipo de Cal.com.
- **Stack actual:** Base UI + Tailwind, copy-paste, pensado para apps de verdad (Cal.com). El Origin original era Radix/shadcn-style y queda como snapshot con soporte limitado. El roadmap habla de primitivas, *particles* (patrones de más nivel) y, más adelante, *atoms* con integraciones.
- **Para qué:** base limpia de producto, forms y composiciones densas, no efectos de marketing. **Oficio:** es de las mejores alternativas al “shadcn se ve igual en todos lados”, porque nace de un producto real. Ojo: en el lanzamiento de octubre de 2025 todavía se advertía early/breaking; en noviembre de 2026 el repo sigue activo, pero conviene leer el roadmap antes de apostar el design system entero.

### Kibo UI

- **Oficial:** [kibo-ui.com](https://www.kibo-ui.com/) · Repo: [shadcnblocks/kibo](https://github.com/shadcnblocks/kibo) (MIT; el `license.md` del repo, 2026, figura a nombre de shadcnblocks). Se instala con `npx shadcn add @kibo-ui`.
- **Hechos:** lo creó Hayden Bleasel ([@haydenbleasel](https://x.com/haydenbleasel)). El 28 de octubre de 2025, Shadcnblocks anunció la adquisición: [Shadcnblocks acquires Kibo UI](https://www.shadcnblocks.com/blog/announcing-kibo-ui-acquisition) (Rob Austin). En ese anuncio: 41 componentes y 1.000+ variantes, sigue open source, el registry `@kibo-ui` no cambia en lo inmediato.
- **Stack:** React, shadcn/ui, Tailwind. Piezas avanzadas de *app*: Gantt, Kanban, editores, no un kit de glow.
- **Para qué:** cuando shadcn no trae el componente difícil. **Oficio:** instalá lo que vas a usar. No es un theme.

### Cult UI

- **Oficial:** [cult-ui.com](https://www.cult-ui.com/) · Repo: [nolly-studio/cult-ui](https://github.com/nolly-studio/cult-ui) (MIT, copyright Jordan-Gilliam).
- **Stack:** React, TypeScript, Tailwind, Motion, encima de shadcn. Controles con microinteracción (docks, paneles, expandibles) más que secciones de marketing.
- **Para qué:** un producto que quiere motion de oficio en la UI, no un hero cinematográfico. Catálogo más chico que Magic UI.

### Motion Primitives

- **Oficial:** [motion-primitives.com](https://www.motion-primitives.com/) · Repo: [ibelick/motion-primitives](https://github.com/ibelick/motion-primitives) (MIT, copyright 2024 ibelick). Autor: [@Ibelick](https://x.com/Ibelick).
- **Stack:** React, Tailwind, Motion. Son *building blocks* (reveal, morph, text effects, transiciones) para componer, no landings cerradas.
- **Para qué:** cuando querés motion a medida sin pelearte con la API cruda. Complementa [`../animaciones/`](../animaciones/README.md).

### Animate UI

- **Oficial:** [animate-ui.com](https://animate-ui.com/) · Repo: [imskyleen/animate-ui](https://github.com/imskyleen/animate-ui).
- **Licencia (leída en [LICENSE.md](https://raw.githubusercontent.com/imskyleen/animate-ui/main/LICENSE.md), copyright 2025 Elliot Sutton):** MIT + **Commons Clause**. Podés usarlo, modificarlo y publicarlo *como parte de una aplicación, sitio o producto*, incluso comercial. **No podés vender ni redistribuir los componentes en su forma original, solos o en un bundle.** No es un MIT limpio: no lo metas en un registry o un kit que revendés.
- **Stack:** React, shadcn CLI, Motion. Versiones animadas de componentes familiares.
- **Para qué:** si la licencia te cierra y querés primitivas ya animadas. Si no, Motion Primitives o CSS nativo suelen bastar.

### Tremor

- **Oficial:** [tremor.so](https://www.tremor.so/) · Repo: [tremorlabs/tremor](https://github.com/tremorlabs/tremor) (Apache-2.0). npm `@tremor/react` latest **3.18.7**, publicado el **13 de enero de 2025**; el repo tenía push el 10 de octubre de 2025 en esta pasada, no actividad reciente comparable a Base UI o shadcn.
- **Hechos:** Vercel anunció la adquisición el 22 de enero de 2025: [Vercel acquires Tremor](https://vercel.com/blog/vercel-acquires-tremor). El sitio sigue en pie (GET 200). En comunidades de 2026 se repite que el trabajo nuevo del equipo fue hacia shadcn/ui; **no encontré un anuncio oficial de “Tremor está deprecado”**, así que lo documentamos como **vivo, pero en ritmo bajo / incierto**.
- **Stack:** React + Tailwind, copy-paste, charts y dashboards. No es un registry shadcn estricto, pero convive bien.
- **Para qué:** un dashboard que necesita charts ya resueltos. **Oficio:** confirmá en npm y en el repo si el paquete cubre tu versión de React antes de usarlo en un proyecto nuevo. Alternativas: primitivas de gráfico propias, o bloques de Kibo / shadcn charts.

## Otras bases (no shadcn-first, pero vigentes)

### HeroUI (antes NextUI)

- **Oficial:** [heroui.com](https://heroui.com/) (`www.heroui.com` redirige) · Repo: [heroui-inc/heroui](https://github.com/heroui-inc/heroui) (Apache-2.0, activo el 18/11/2026).
- **Stack:** React, Tailwind, librería completa (no copy-paste dueñado al estilo shadcn). Útil si el equipo quiere un sistema con tema y paquetes, no archivos en `/components`. El riesgo es el mismo de siempre: se ve “de HeroUI” si no lo personalizás.

### Park UI

- **Oficial:** [park-ui.com](https://park-ui.com/) (GET 200). Encima de Ark + Panda CSS, del entorno Chakra. Encaja si ya estás en Panda, no como agregado a un proyecto Tailwind/shadcn.

### 21st.dev

- **Oficial:** [21st.dev](https://21st.dev/) (GET 200). No es una librería única: es un directorio / marketplace de componentes y registries de la comunidad, útil para descubrir, peligroso para pegar 15 estilos distintos en un mismo producto. Tratalo como galería de piezas, no como sistema.

## Cómo no mezclarlos

| Necesidad | Por dónde empezar |
|---|---|
| App React nueva, 2026 | shadcn + Base UI, tokens propios, tipo del kit |
| App ya en Radix/shadcn | No migres. Seguí en Radix |
| Design system multi-framework | Ark (o Park si hay Panda) |
| A11y / i18n de empresa | React Aria |
| Landing con un gesto de motion | Magic UI *o* un bloque de Aceternity, no ambos a lo loco |
| Componentes densos de producto | coss ui (y Origin legacy si ya lo usás) |
| Gantt, Kanban, editor | Kibo |
| Charts / dashboard | Tremor con la salvedad de ritmo, o charts dueñados |
| Microinteracción de UI | Motion Primitives o Cult UI; ver [`../animaciones/`](../animaciones/README.md) |

La terminación pro no sale del registry. Sale de **elegir poco, tokenizar y diseñar estados**. Los patrones de esta carpeta arrancan de esa idea.

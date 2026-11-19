# Reglas para agentes (pegá esto en CLAUDE.md o AGENTS.md)

Bloque reutilizable. Está escrito para que un agente lo siga en cada sesión, no como prosa para leer de corrido. Complementalo con las rutas de este kit (ajustá el path si el repo vive en otro lado) y con **una** paleta, **un** estilo y **una** pareja tipográfica del proyecto.

```md
## Diseño frontend (obligatorio)

Leé, antes de diseñar o de tocar UI, el kit de este repo:
- tipografias/README.md y tipografias/fonts.json
- estilos/README.md y estilos/estilos.json
- paletas/README.md, paletas/evadir-degrade-violeta.md y paletas/paletas.json
- tokens/escalas.md, tokens/tokens.css (o tokens/theme-tailwind-v4.css)
- anti-patrones/README.md, anti-patrones/checklist-revision.md y anti-patrones/catalogo.md
- recursos/README.md (íconos, texturas, OG; no Lucide por default)

### Decisiones, no adjetivos
1. Elegí un estilo del catálogo (uno, o uno + un acento). Respetá su “cuándo no”.
2. Elegí una pareja tipográfica del catálogo. Mostrá licencia e import. Autohospedá en producción.
3. Elegí una paleta del catálogo (o construí roles alrededor de un color de marca). Pegá claro y oscuro. No inventes hex en los componentes.
4. Usá las escalas de tokens (espacio, radio, sombra, tipo fluido, motion, z-index). Un radio default por proyecto.

### Prohibido salvo brief explícito
- Inter, Geist, Roboto, Poppins, Montserrat o Instrument Serif como familia principal.
- Índigo, violeta o degradés from-indigo-* to-purple-* / #667eea–#764ba2 como identidad. Tampoco texto en degradé (bg-clip-text) ni halo/glow detrás del hero.
- Una fila de tres cards idénticas con ícono + párrafo como sección de features.
- Hero centrado con titular genérico y CTAs “Get started” / “Learn more”.
- El orden fijo hero → logos → 3 features → testimonials → pricing → CTA.
- Glassmorphism como tema; cards anidadas; fingernail cards; rounded-2xl/3xl + shadow-xl en todo.
- Lucide como set de íconos por default. Emojis como ícono, bullet o saludo de dashboard.
- animate-pulse en badges; fade/slide-up en cada sección; duration-1000; transition-all; flecha en cada botón; kicker en versales o 01/02/03 en cada heading.
- Ilustraciones 3D de stock, retratos de IA genéricos o mockups de notebook en lugar del producto.
- Copy de hype: Elevate, Seamless, Next-Generation, Supercharge, Unleash, Empower, cutting-edge, “build the future of…”, “Welcome to your Dashboard ✨”.
- Copy que recicla el chat (“Built with…”, “written in Neovim”, “no mocks”).
- Hex, px o duraciones sueltos cuando existe un token. z-[9999].

### Pisos
- Contraste de cuerpo y de accent-foreground sobre accent: al menos WCAG 4.5:1. Muted por debajo de 4.5 no se usa como párrafo.
- prefers-reduced-motion: las animaciones se apagan.
- Meta, alt, favicon y OG no salen de la plantilla.
- Cerca del inicio tiene que haber prueba real: un precio, un horario, un nombre, una captura o un dato que solo este producto tiene.

### Al cerrar una UI
Pasá anti-patrones/checklist-revision.md. Si hay tres o más tells, arreglalos antes de dar por terminado el trabajo. No respondas “hacelo más único”: aplicá las decisiones de arriba.
```

Si el proyecto todavía no copió el kit, dejá estas reglas y un path claro a `tokens.css` y a la paleta elegida. Un modelo sin valores fijos vuelve al promedio en la sesión siguiente (lo documentan [thanor.ai](https://thanor.ai/blog/design-tokens-for-ai-websites), [Motif](https://motif.asv-labs.com/answers/design-tokens-for-ai-built-frontends/) y [Alex Madrazo, 12 de agosto de 2026](https://x.com/alextechhub/status/2087643439382864025)).

# Reglas para agentes (pegá esto en CLAUDE.md o AGENTS.md)

Bloque reutilizable. Está escrito para que un agente lo siga en cada sesión, no como prosa para leer de corrido. Complementalo con las rutas de este kit (ajustá el path si el repo vive en otro lado) y con **una** paleta, **un** estilo y **una** pareja tipográfica del proyecto.

```md
## Diseño frontend (obligatorio)

Modo: si el pedido es solo visual sobre una UI que ya existe ("rediseño sin tocar interfaces", "que se vea mejor"), es restyling: leé como máximo 3 archivos del kit (indice-rapido.json primero), escribí un brief de 5 líneas sin pedir aprobación y editá tema, CSS y className enseguida. No cambies estructura, textos, props, lógica ni rutas. Nunca termines sin diffs. Detalle: skills/frontend-design/restyling.md.

Leé, antes de diseñar UI nueva, el kit de este repo:
- indice-rapido.json (estilos, paletas y fuentes resumidos: para elegir alcanza)
- tipografias/README.md; de tipografias/fonts.json solo la ficha elegida (jq por id; el archivo pesa ~135 KB)
- estilos/README.md y estilos/estilos.json
- paletas/README.md y paletas/evadir-degrade-violeta.md; de paletas/paletas.json solo la paleta elegida (jq por slug; ~390 KB)
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
- Fondo crema + serif display + acento terracota (#D97757) por reflejo; casi negro + un acento ácido; look de diario en algo que no es de lectura.
- Una palabra del titular en itálica o color; serif itálica gigante en el hero; pastilla "Nuevo ✨" arriba del H1; ícono en cuadradito arriba de cada card.
- Glows y sombras de color; borde fino + sombra ancha en toda una fila; fondos de grilla o rayas decorativos; marquee en loop; bordes que giran o brillan en loop (border beam); cursor parpadeante; easing con rebote.
- Copy de segunda generación: tira de cifras, titulares "X. Y.", "no es X, es Y" repetido, palabras de virtud (honesto, cuidado, de verdad), cifras o clientes inventados, signos de exclamación.

### Pisos
- Contraste de cuerpo y de accent-foreground sobre accent: al menos WCAG 4.5:1. Muted por debajo de 4.5 no se usa como párrafo.
- prefers-reduced-motion: las animaciones se apagan.
- Meta, alt, favicon y OG no salen de la plantilla.
- Texto funcional ≥ 11 px, cuerpo ≥ 14 px, leading de párrafo ≥ 1.5, text-wrap: balance en títulos, tabular-nums en cifras, radio interior = exterior − padding.
- El contenido es visible sin JS; ninguna animación decide si existe.
- Cerca del inicio tiene que haber prueba real: un precio, un horario, un nombre, una captura o un dato que solo este producto tiene.

### Al cerrar una UI
Pasá anti-patrones/checklist-revision.md (incluye el orden de las pasadas). En restyling es un reporte, no un portón. Si hay tres o más tells, arreglalos antes de dar por terminado el trabajo. No respondas “hacelo más único”: aplicá las decisiones de arriba.
```

Si el proyecto todavía no copió el kit, dejá estas reglas y un path claro a `tokens.css` y a la paleta elegida. Un modelo sin valores fijos vuelve al promedio en la sesión siguiente (lo documentan [thanor.ai](https://thanor.ai/blog/design-tokens-for-ai-websites), [Motif](https://motif.asv-labs.com/answers/design-tokens-for-ai-built-frontends/) y [Alex Madrazo, 12 de agosto de 2026](https://x.com/alextechhub/status/2087643439382864025)).

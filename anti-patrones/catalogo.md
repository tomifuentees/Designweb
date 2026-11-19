# Catálogo de anti-patrones (AI slop / vibe-coded UI)

Lista de **30 tells** documentados en 2025–2026. No es una estética personal: cada entrada cita hilos o artículos reales (Desai y Hacker News, el tuit de Wathan, Reddit, Utsubo, Drop The Hassle, posts de X recuperados con id). El objetivo es que un agente —o una pasada humana— pueda nombrar lo que está viendo y cortarlo.

Una sola de estas cosas, elegida a propósito, no hace un sitio “de IA”. Tres o cuatro apiladas, sí: es el promedio de un primer draft sin dirección. Varios comentarios del hilo de HN lo dicen: el problema no es usar un modelo, es shippear la primera salida sin oficio.

La versión machine-readable está en [`anti-patrones.json`](./anti-patrones.json). El bloque para pegar en `CLAUDE.md` está en [`reglas-para-agentes.md`](./reglas-para-agentes.md). La pasada rápida, en [`checklist-revision.md`](./checklist-revision.md).

## 1. Degradé índigo–violeta como identidad

`degrade-violeta-de-identidad`

**Síntoma.** El hero, el fondo o el CTA viven en un degradé from-indigo-500 to-purple-600, #667eea → #764ba2, o un bg-indigo-500 sin que la marca lo pida.

**Por qué pasa.** Es el promedio de los tutoriales de Tailwind UI. El 7 de agosto de 2025 Adam Wathan se disculpó en público por haber puesto bg-indigo-500 en cada botón de Tailwind UI, 'leading to every AI generated UI on earth also being indigo'. Los modelos repiten lo que más vieron.

**Cómo arreglarlo.** Elegí un acento que salga del tema y usalo sólido, con roles. Prohibí el degradé como marca de la página. Ver ../paletas/evadir-degrade-violeta.md.

**Regla para el agente.** No uses índigo, violeta ni degradés from-indigo-* to-purple-* (ni #667eea–#764ba2, ni violet-600) como identidad, salvo que el brief lo pida de forma explícita. Un acento sólido, sacado de la paleta del proyecto.

Fuentes: [fuente](https://x.com/adamwathan/status/1953510802159219096), [fuente](https://godobject.dev/blog/10-tells-of-slop/), [fuente](https://www.reddit.com/r/web_design/comments/1nx0wus/ai_has_a_purple_problem/), [fuente](https://dropthehassle.com/guides/make-website-look-less-ai), [fuente](https://www.utsubo.com/blog/built-with-ai-trust-signals-2026)

## 2. Titular con una palabra (o todo el H1) en degradé

`texto-en-degrade`

**Síntoma.** Un word del heading va con bg-clip-text y un degradé, o el H1 entero es un degradé.

**Por qué pasa.** Es un truco de landing 2021–2023 que los modelos copian para 'dar vida' al título cuando no tienen una voz tipográfica.

**Cómo arreglarlo.** El titular se lee en el color de texto (o, como mucho, en el acento sólido). La personalidad la pone la familia tipográfica, no un shader sobre la letra.

**Regla para el agente.** No uses bg-clip-text ni texto en degradé en headings. Si hace falta énfasis, cambiale el peso, la familia o el color sólido de un segmento, no un degradé.

Fuentes: [fuente](https://dropthehassle.com/guides/make-website-look-less-ai)

## 3. Halo o glow de acento detrás del hero

`halo-glow-detras-del-hero`

**Síntoma.** Un blur violeta, índigo o neón detrás del titular o del mockup, tipo shadow-indigo-500/40 o un div absoluto con blur-3xl.

**Por qué pasa.** Es la forma más barata de 'profundidad' en landings de SaaS que el modelo vio mil veces. En las fichas de estilo de este kit ya se marca como error de SaaS oscuro.

**Cómo arreglarlo.** Sacalo. Si hay glow, que sea de un estado activo real (un cursor, un foco), no un fondo.

**Regla para el agente.** No pongas un halo, blur o glow de acento detrás del hero, del titular o de un mockup genérico.

Fuentes: [fuente](https://dropthehassle.com/guides/make-website-look-less-ai), [fuente](https://www.utsubo.com/blog/built-with-ai-trust-signals-2026)

## 4. Rainbow vomit (colores sin rol)

`rainbow-vomit`

**Síntoma.** Cada bloque, dato o card tiene un color distinto. No hay 70-30-10. La pantalla parece un tablero de stickers.

**Por qué pasa.** El modelo distingue 'campos' pintándolos de colores distintos, sin una paleta con roles. Desai lo llama rainbow vomit en su lista del 27 de septiembre de 2026.

**Cómo arreglarlo.** Una paleta con roles. Un acento. Neutros para el resto. Ver ../paletas/README.md.

**Regla para el agente.** No asignes un color distinto a cada card o dato. Usá los tokens de rol de la paleta del proyecto. Un acento, no un arcoíris.

Fuentes: [fuente](https://godobject.dev/blog/10-tells-of-slop/)

## 5. Badges que pulsan (y que nunca se apagan)

`badges-pulsantes`

**Síntoma.** Un chip con animate-pulse que dice 'Active', 'Live', 'Verified' o 'New' en un estado que no cambia nunca.

**Por qué pasa.** Está en los datos de entrenamiento (onboarding, marketing). Desai describe un 'active student' que no puede estar inactivo: si lo está, la app te desloguea. Es información redundante más un movimiento que no dice nada.

**Cómo arreglarlo.** Un badge solo si el estado puede ser otro. Sin pulse, salvo que el pulso comunique algo que se actualiza de verdad.

**Regla para el agente.** No uses animate-pulse en badges. No agregues chips 'Active', 'Verified' o 'Live' si ese estado no puede no cumplirse.

Fuentes: [fuente](https://godobject.dev/blog/10-tells-of-slop/)

## 6. Fingernail cards (raya de acento a la izquierda)

`fingernail-cards`

**Síntoma.** Toda card trae una franja vertical de color en el borde izquierdo. Desai las llama fingernail cards: nadie se sentó a pedirlas, y están en casi todo UI vibe-coded.

**Por qué pasa.** Es un patrón de 'card con énfasis' que los modelos aplican por default, a todas por igual, y entonces no enfatiza nada.

**Cómo arreglarlo.** Si una card necesita énfasis, cambiá el peso del título, un dato o el orden, no una uña de color en cada una.

**Regla para el agente.** No le pongas una franja de acento al borde izquierdo de cada card.

Fuentes: [fuente](https://godobject.dev/blog/10-tells-of-slop/)

## 7. Emoji slop (como ícono, bullet o saludo)

`emoji-como-icono-o-bullet`

**Síntoma.** 🍞🚀💜 en las feature cards, 'Welcome to your Dashboard ✨', bullets con emojis en un producto serio.

**Por qué pasa.** Los modelos aman los emojis, escribe Desai, y Drop The Hassle y Utsubo lo listan como señal de draft. Sirven en un chat, no como sistema de íconos.

**Cómo arreglarlo.** Un set de íconos consistente (no Lucide por default: ver ../recursos/iconos.md). En un producto, el saludo no lleva confetti.

**Regla para el agente.** No uses emojis como íconos de features, ni en títulos, ni en saludos de dashboard. Un set de íconos del proyecto, de una sola familia.

Fuentes: [fuente](https://godobject.dev/blog/10-tells-of-slop/), [fuente](https://dropthehassle.com/guides/make-website-look-less-ai), [fuente](https://www.utsubo.com/blog/built-with-ai-trust-signals-2026)

## 8. Elementos sueltos desalineados

`desalineacion-de-elementos-sueltos`

**Síntoma.** SVG, ASCII, un ícono o una lista que no comparte línea de base ni columna con el texto de al lado. Se nota sobre todo en bloques que no van dentro de una caja.

**Por qué pasa.** Desai lo marca como tell estable: el modelo 'casi siempre' desalinea lo que no está en un box. Los comentarios de HN coinciden en que hay que hacer una pasada humana.

**Cómo arreglarlo.** Una grilla, un baseline, y una revisión visual. No confíes en que el modelo vea el desalineado.

**Regla para el agente.** Todo ícono, cifra o marca al lado de un texto comparte línea de base o centro, y una columna de la grilla. Revisá SVG y listas sueltas antes de dar por cerrado un bloque.

Fuentes: [fuente](https://godobject.dev/blog/10-tells-of-slop/), [fuente](https://news.ycombinator.com/item?id=49867038)

## 9. Inter, Geist o una sola sans por default

`inter-geist-para-todo`

**Síntoma.** Todo el sitio en Inter (o Geist, o Roboto, o Poppins) en un solo peso. Si es un proyecto 'de devs', JetBrains Mono en cada caption.

**Por qué pasa.** Son las familias más presentes en el entrenamiento. Este kit las documenta como default a evadir en ../tipografias/. Utsubo y Drop The Hassle las listan como tell visual.

**Cómo arreglarlo.** Una pareja del catálogo de tipografías, con un peso de titular y un cuerpo. Geist e Inter pueden ser apoyo, no la primera opción.

**Regla para el agente.** No uses Inter, Geist, Roboto, Poppins, Montserrat ni Instrument Serif como primera opción, salvo que el brief lo pida. Elegí una pareja de ../tipografias/fonts.json y declarala en los tokens.

Fuentes: [fuente](https://godobject.dev/blog/10-tells-of-slop/), [fuente](https://www.utsubo.com/blog/built-with-ai-trust-signals-2026), [fuente](https://dropthehassle.com/guides/make-website-look-less-ai)

## 10. Separadores // de 'tech'

`doble-slash-tecnico`

**Síntoma.** Kicker del tipo '// features' o '01 // overview' en cuanto el tema roza lo técnico.

**Por qué pasa.** Desai lo señala: el modelo agrega // siempre que algo suena a programación. Es un adorno, no una jerarquía.

**Cómo arreglarlo.** Un kicker tipográfico (mayúsculas o mono, una vez), o nada. El // no aporta dato.

**Regla para el agente.** No uses // como adorno de sección o kicker, aunque el producto sea técnico.

Fuentes: [fuente](https://godobject.dev/blog/10-tells-of-slop/)

## 11. Lucide en todos lados

`lucide-por-default`

**Síntoma.** Todos los íconos son Lucide (el set por default de shadcn y de casi cualquier app 'AI-coded').

**Por qué pasa.** Om Patel lo escribió el 7 de marzo de 2026: 'lucide react is basically the default icon set for ai coded apps… which is exactly why every ai generated interface ends up looking the same.' El post tuvo más de mil likes.

**Cómo arreglarlo.** Phosphor (incluye duotone), Tabler, Iconoir, Heroicons o Hugeicons, uno solo por proyecto. Ver ../recursos/iconos.md.

**Regla para el agente.** No uses Lucide como set por default. Elegí un set de ../recursos/iconos.md (Phosphor, Tabler, Iconoir, Heroicons o Hugeicons) y quedate con ese.

Fuentes: [fuente](https://x.com/om_patel5/status/2030310771326861336)

## 12. La copy huele al prompt

`fuga-del-prompt`

**Síntoma.** Frases como 'Built with Hugo. Written from Neovim', 'Real services, no mocks', 'Your files never leave your browser' dichas como slogan, o un 'One campus. One app.' que se entiende solo si escuchaste la reunión. Desai lo llama redundant text due to chat context. En HN varios dijeron que es el tell más nuevo.

**Por qué pasa.** El modelo recicla el contexto de la conversación o una instrucción negativa ('no hagas X') y la convierte en copy visible.

**Cómo arreglarlo.** La copy se escribe para el usuario, no para el chat. Revisá cada string que suene a justificación técnica o a eco del brief interno.

**Regla para el agente.** No vuelques al UI ni al README el contexto del chat ('built with…', 'written in…', 'no mocks', 'no HTML'). La copy habla del producto y del usuario, no de cómo se construyó.

Fuentes: [fuente](https://godobject.dev/blog/10-tells-of-slop/), [fuente](https://news.ycombinator.com/item?id=49867038)

## 13. Glassmorfismo como tema (y brutalismo de plantilla)

`glassmorfismo-como-tema`

**Síntoma.** Todo es un panel translúcido con blur y borde blanco, o un 'brutalismo' idéntico al de la landing de al lado (borde grueso, sombra dura, amarillo, la misma card).

**Por qué pasa.** Desai: el modelo ama el glass y, si no, cae en un brutalismo que 'all of them look the EXACT same'. Este kit documenta ambos como acento o nicho, no como tema.

**Cómo arreglarlo.** Vidrio solo en un recorte (un panel sobre una foto). Brutalismo como acento, con una paleta propia (ver brutal-amarillo), no como skin de una landing de SaaS.

**Regla para el agente.** No uses glassmorphism como tema de la página. Un blur, como mucho, en un panel. No apliques un skin 'brutalist' genérico a un SaaS o a una PyME que no lo pidió.

Fuentes: [fuente](https://godobject.dev/blog/10-tells-of-slop/)

## 14. Taglines de hype (Elevate, Seamless, Unleash…)

`taglines-de-hype`

**Síntoma.** Cada H1 trae un subtítulo gris: 'Experience the power of task management with our cutting-edge intuitive interface.' Palabras fetiche: Elevate, Seamless, Next-Generation, Supercharge, Unleash, Empower, cutting-edge.

**Por qué pasa.** Desai y Utsubo lo documentan. El modelo trata cada pantalla como una landing y rellena con el promedio de los slogans de SaaS.

**Cómo arreglarlo.** Decí qué hace el producto, con un dato (precio, horario, nombre, cifra). Drop The Hassle lo muestra con una panadería: 'Sourdough out of the oven at 6:00' vs 'Elevate your mornings'.

**Regla para el agente.** Prohibidas como muleta: Elevate, Seamless, Next-Generation, Supercharge, Unleash, Empower, cutting-edge, intuitive interface, 'build the future of…'. La copy tiene que decir algo que solo este producto puede decir.

Fuentes: [fuente](https://godobject.dev/blog/10-tells-of-slop/), [fuente](https://www.utsubo.com/blog/built-with-ai-trust-signals-2026), [fuente](https://dropthehassle.com/guides/make-website-look-less-ai)

## 15. Welcome to your Dashboard, [Name] ✨

`dashboard-welcome-sparkles`

**Síntoma.** Un producto interno o un dashboard arranca como landing: saludo con sparkles, un subtítulo de 'Revolutionise your workflow', tres stats tiles inútilmente grandes.

**Por qué pasa.** Desai: el modelo trata cada pantalla como una landing en vez de como una herramienta.

**Cómo arreglarlo.** Un dashboard empieza por la tarea (qué hay que hacer hoy), no por un welcome. Los stats, si existen, son los que alguien usa.

**Regla para el agente.** En dashboards y herramientas, no empieces con 'Welcome to your Dashboard' ni con un tagline de marketing. Empezá por la tarea o por el dato útil.

Fuentes: [fuente](https://godobject.dev/blog/10-tells-of-slop/)

## 16. Hero centrado que le serviría a cualquiera

`hero-centrado-generico`

**Síntoma.** Texto centrado, un H1 que podría encabezar otra empresa, un CTA 'Get started' y otro 'Learn more', a veces un mockup de notebook abajo.

**Por qué pasa.** Es la estructura media de cada plantilla de SaaS con la que se entrenaron los modelos (Utsubo, Drop The Hassle, hilos de Reddit de 2025–2026).

**Cómo arreglarlo.** Alineación a un lado (salvo que el estilo pida centro: un póster, un look editorial específico). Un titular que nombre el producto o la promesa concreta. Un solo CTA principal.

**Regla para el agente.** No armes un hero centrado con un titular genérico, dos CTAs 'Get started / Learn more' y un mockup de notebook. Alineá, sé específico, un CTA.

Fuentes: [fuente](https://www.utsubo.com/blog/built-with-ai-trust-signals-2026), [fuente](https://dropthehassle.com/guides/make-website-look-less-ai), [fuente](https://www.reddit.com/r/web_design/comments/1uzascg/every_vibecoded_websites_looks_the_same/)

## 17. Tres cards idénticas de features

`tres-cards-identicas`

**Síntoma.** Tres columnas, la misma altura, el mismo radio, el mismo ícono-en-tile, el mismo párrafo de dos líneas. A veces 01 / 02 / 03.

**Por qué pasa.** Es el layout más repetido de las landings de SaaS (prg.sh, Utsubo, Drop The Hassle, Reddit). 'Three boxes with icons arranged in a grid.'

**Cómo arreglarlo.** Una grilla bento con jerarquía, un stack editorial, una lista con prueba real (precios, nombres, captures). Si hay features, que no midan todas lo mismo.

**Regla para el agente.** No uses una fila de tres cards idénticas con ícono y un párrafo como sección de features. Variá el tamaño, o reemplazala por prueba real o por un recorte del producto.

Fuentes: [fuente](https://www.utsubo.com/blog/built-with-ai-trust-signals-2026), [fuente](https://dropthehassle.com/guides/make-website-look-less-ai), [fuente](https://prg.sh/ramblings/Why-Your-AI-Keeps-Building-the-Same-Purple-Gradient-Website), [fuente](https://www.reddit.com/r/web_design/comments/1uzascg/every_vibecoded_websites_looks_the_same/)

## 18. El orden de plantilla (hero → logos → 3 cards → testimonials → pricing → CTA)

`orden-de-template-saas`

**Síntoma.** Todas las landings del proyecto siguen esa secuencia, con las mismas alturas y el mismo padding.

**Por qué pasa.** Drop The Hassle lo lista como el 'template order' de los builders (Lovable, Bolt, v0). Es seguro, y por eso se reconoce.

**Cómo arreglarlo.** Reordená según lo que el usuario necesita probar primero. Una PyME puede empezar por precios y horarios. Un devtool, por la demo.

**Regla para el agente.** No uses por default la secuencia hero, logo strip, tres features, testimonials, pricing, CTA. El orden lo define el trabajo de la página.

Fuentes: [fuente](https://dropthehassle.com/guides/make-website-look-less-ai)

## 19. Un radio enorme y la misma sombra suave en todo

`un-radio-y-sombra-para-todo`

**Síntoma.** Botones, cards, inputs, badges e imágenes comparten rounded-2xl o rounded-3xl y un shadow-xl de 10 % de opacidad.

**Por qué pasa.** Utsubo y Drop The Hassle lo marcan. El modelo elige un radio 'moderno' y lo aplica a cada caja.

**Cómo arreglarlo.** Dos radios (controles vs. media), o uno solo chico, o ninguno. Poca sombra. Ver ../tokens/escalas.md.

**Regla para el agente.** No apliques rounded-2xl/3xl ni shadow-xl a todos los elementos. Usá los radios y sombras de ../tokens/. Un default; xl solo para media.

Fuentes: [fuente](https://www.utsubo.com/blog/built-with-ai-trust-signals-2026), [fuente](https://dropthehassle.com/guides/make-website-look-less-ai)

## 20. Fade-and-slide-up en cada sección (y motion sin propósito)

`fade-up-en-cada-seccion`

**Síntoma.** Cada bloque aparece con un fade + translate-y al scrollear. A veces duration-1000. A veces también un bounce o un pulse.

**Por qué pasa.** Es la primera animación que los tutoriales enseñan, y la que el modelo pega en todas partes (Utsubo: 'Motion With No Purpose'; Drop The Hassle lo lista entre los 12 fixes).

**Cómo arreglarlo.** Una o dos animaciones con sentido (un recorte de producto, un dato). Duraciones del kit (120–280 ms). prefers-reduced-motion obligatorio.

**Regla para el agente.** No animes cada sección con fade/slide-up al scrollear. No uses duration-1000 ni transition-all. Motion de ../tokens/, y solo donde aporta. Respetá prefers-reduced-motion.

Fuentes: [fuente](https://www.utsubo.com/blog/built-with-ai-trust-signals-2026), [fuente](https://dropthehassle.com/guides/make-website-look-less-ai)

## 21. Flecha en cada botón

`flecha-en-cada-boton`

**Síntoma.** Todos los CTA terminan en → o en un ícono arrow-right, incluidos los que no 'van' a ningún lado narrativo.

**Por qué pasa.** Drop The Hassle lo incluye en la lista de adornos de plantilla. Una flecha deja de significar 'continuar' si está en todos lados.

**Cómo arreglarlo.** Flecha solo en un link de continuar o en un 'ver más' puntual. El CTA principal puede no llevar ícono.

**Regla para el agente.** No le pongas una flecha a todos los botones. Como máximo, al CTA de continuar o a un 'ver más' puntual.

Fuentes: [fuente](https://dropthehassle.com/guides/make-website-look-less-ai)

## 22. Label en versales (y 01 / 02 / 03) encima de cada heading

`kicker-versalas-en-cada-heading`

**Síntoma.** Cada H2 trae un kicker con letter-spacing enorme: 'OUR FEATURES'. O una numeración 01 02 03 en cosas que no son una secuencia.

**Por qué pasa.** Es un adorno de jerarquía que, usado en todos los bloques, los aplana. Documentado por Drop The Hassle.

**Cómo arreglarlo.** Un kicker, como mucho, en la sección que realmente lo necesita. Numeración solo en pasos reales.

**Regla para el agente.** No pongas un label en versales con tracking enorme encima de cada heading, ni 01/02/03 en contenido que no es una secuencia.

Fuentes: [fuente](https://dropthehassle.com/guides/make-website-look-less-ai)

## 23. Ilustración 3D plástica o imagen de IA genérica

`ilustracion-plastica-ia`

**Síntoma.** Personajes 3D de stock, 'friendly robots', hands-with-phones, o un render que podría ilustrar cualquier SaaS. Utsubo lo llama the plastic AI illustration.

**Por qué pasa.** Es barata de generar y está en todos los builders. El ojo ya la asocia a 'default de IA', no a una marca.

**Cómo arreglarlo.** Foto real, recorte del producto, ilustración de un estilo elegido (ver ../recursos/ilustraciones.md y el estilo ilustrado-humano). Un solo criterio, no un mix de renders.

**Regla para el agente.** No uses ilustraciones 3D de stock ni imágenes genéricas de IA como hero o features. Preferí foto real, captura del producto o un estilo ilustrado coherente y humano.

Fuentes: [fuente](https://www.utsubo.com/blog/built-with-ai-trust-signals-2026)

## 24. No hay prueba que solo esta marca podría tener

`sin-prueba-real`

**Síntoma.** No hay precios, horarios, nombres, fotos del equipo, captures reales del producto. En su lugar, tres features con ícono.

**Por qué pasa.** Utsubo ('No Real Proof') y Drop The Hassle: lo que saca a una página del promedio es lo que no se puede copiar con un prompt genérico.

**Cómo arreglarlo.** Precios, horarios, nombres, una captura, un testimonio atribuido. Aunque el resto del layout sea simple.

**Regla para el agente.** Incluí prueba real (precios, horarios, nombres, fotos o capturas del producto) cerca del inicio. No la reemplaces por tres features genéricas.

Fuentes: [fuente](https://www.utsubo.com/blog/built-with-ai-trust-signals-2026), [fuente](https://dropthehassle.com/guides/make-website-look-less-ai)

## 25. Copy de modelo: em-dash a granel, openers de stock, hedging

`copy-de-modelo`

**Síntoma.** Casi cada frase tiene un em-dash. Arranques tipo 'In today's fast-paced world' o 'a rich tapestry of'. Mucho 'might', 'can help', y bullets con emoji. Utsubo lo parte en varios tells de escritura.

**Por qué pasa.** Es la prosodia media de los LLM. El em-dash no es el problema (es puntuación legítima); la densidad sí.

**Cómo arreglarlo.** Frases más cortas, verbos concretos, menos conectores. Una pasada solo de copy, sin tocar el layout.

**Regla para el agente.** No escribas con em-dash en casi cada oración, ni con openers de stock ('In today's fast-paced world', 'a rich tapestry'), ni con hedging inútil. Copy concreta, atribuible, sin confetti.

Fuentes: [fuente](https://www.utsubo.com/blog/built-with-ai-trust-signals-2026)

## 26. Meta, alt y OG de plantilla

`meta-y-og-de-plantilla`

**Síntoma.** Title y description genéricos, alt='image' o alt='hero image', OG por default del builder, favicon de Vite o de Next.

**Por qué pasa.** Utsubo lo lista como tell de código/SEO. También debilita la búsqueda. Drop The Hassle insiste en el dominio propio frente a tuapp.lovable.app.

**Cómo arreglarlo.** Title específico, description que se pueda citar, alt que describa, un OG y un favicon hechos (ver ../recursos/favicon-og.md).

**Regla para el agente.** No dejes title/description genéricos, alt vacío o 'image', ni el favicon/OG por default del bundler o del builder. Escribí meta específica y generá favicon y OG.

Fuentes: [fuente](https://www.utsubo.com/blog/built-with-ai-trust-signals-2026), [fuente](https://dropthehassle.com/guides/make-website-look-less-ai)

## 27. Tokens inventados en cada sesión

`tokens-inventados-en-cada-sesion`

**Síntoma.** Cada chat vuelve a elegir colores, radios, tamaños y duraciones. Alex Madrazo lo resumió el 12 de agosto de 2026: 'Every AI-generated UI looks the same because every agent invents its own tokens each session.'

**Por qué pasa.** Sin un archivo que sobreviva al chat, el modelo vuelve al promedio. Motif y thanor.ai dicen lo mismo: los tokens no garantizan buen diseño, pero cortan la deriva.

**Cómo arreglarlo.** Un archivo de tokens (../tokens/ + una paleta) y una regla de 'sin hex sueltos'. CLAUDE.md o AGENTS.md que lo apunten. El bloque está en reglas-para-agentes.md.

**Regla para el agente.** No inventes colores, radios, tamaños ni duraciones en el componente. Usá los tokens del proyecto (este kit o el archivo del repo). Si no existen, crealos primero y reutilizalos.

Fuentes: [fuente](https://x.com/alextechhub/status/2087643439382864025), [fuente](https://thanor.ai/blog/design-tokens-for-ai-websites), [fuente](https://motif.asv-labs.com/answers/design-tokens-for-ai-built-frontends/)

## 28. Grises que no contrastan (sobre todo en oscuro)

`gris-que-no-contrasta`

**Síntoma.** Texto muted #777 sobre #111, o un zinc-500 como cuerpo. Se ve 'premium' en el monitor del diseñador y no se lee en el del usuario. Los comentarios de HN del hilo de Desai lo contrastan con Bootstrap, que sí partía de un piso WCAG.

**Por qué pasa.** El modelo prioriza 'suavidad' visual sobre un piso de contraste. Este kit lo marca en las fichas de SaaS oscuro y en cada paleta.

**Cómo arreglarlo.** Medí WCAG y APCA. El cuerpo pide 4.5:1 y un Lc alto. Muted por debajo de 4.5 no va en párrafo.

**Regla para el agente.** No uses grises de 'look premium' que no lleguen a 4.5:1 para cuerpo. Medí texto, muted y acento sobre fondo y superficie (WCAG y, si podés, APCA). Ver ../paletas/.

Fuentes: [fuente](https://news.ycombinator.com/item?id=49867038), [fuente](https://apcacontrast.com/)

## 29. Mockup de MacBook genérico en lugar del producto

`mockup-de-notebook-generico`

**Síntoma.** Un template de notebook o iPhone con una UI inventada o un screenshot borroso, en vez del producto real.

**Por qué pasa.** Las fichas de SaaS oscuro de este kit ya lo listan como error. Utsubo y Drop The Hassle piden prueba real.

**Cómo arreglarlo.** Una captura o una demo del producto. Si todavía no existe, un recorte fiel, no un mockup stock.

**Regla para el agente.** No uses un mockup genérico de notebook o teléfono como héroe de un producto. Preferí una captura o una demo real.

Fuentes: [fuente](https://www.utsubo.com/blog/built-with-ai-trust-signals-2026)

## 30. Cards dentro de cards

`cards-dentro-de-cards`

**Síntoma.** Una card con borde y sombra envuelve otras cards con borde y sombra. El 23 de octubre de 2026, un post en X lo resumía: 'Inter font, purple-to-blue gradient, cards inside cards.'

**Por qué pasa.** El modelo 'encaja' cada bloque en una card porque es el componente que más vio. Anidarlas no crea jerarquía: crea ruido.

**Cómo arreglarlo.** Una superficie por grupo. El anidado, si existe, se resuelve con espacio y tipografía, no con otra caja.

**Regla para el agente.** No anides cards con borde y sombra dentro de otras cards. Un nivel de caja por grupo; el resto, aire y tipo.

Fuentes: [fuente](https://x.com/jimmyyangrz/status/2113722648744304914)


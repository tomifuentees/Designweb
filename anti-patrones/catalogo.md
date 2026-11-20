# Catálogo de anti-patrones (AI slop / vibe-coded UI)

Lista de **59 tells** documentados en 2025–2026 (las fichas 31–59 se sumaron el 20 de noviembre de 2026 desde repos de referencia, con atribución). No es una estética personal: cada entrada cita hilos o artículos reales (Desai y Hacker News, el tuit de Wathan, Reddit, Utsubo, Drop The Hassle, posts de X recuperados con id). El objetivo es que un agente —o una pasada humana— pueda nombrar lo que está viendo y cortarlo.

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

---

## Fichas 31–59: minadas de repos de referencia (noviembre de 2026)

Resumidas y adaptadas al español de [impeccable](https://github.com/pbakaus/impeccable) (Apache 2.0), la skill oficial [`frontend-design` de Anthropic](https://github.com/anthropics/skills/tree/main/skills/frontend-design) (Apache 2.0), [taste-skill](https://github.com/Leonxlnx/taste-skill) (MIT) y [unslop](https://github.com/heydamir/unslop) de Damir Sokolovsky (CC BY 4.0). Qué se tomó de cada uno: [`../recursos/minado-repos.md`](../recursos/minado-repos.md).

## 31. Fondo crema 'con gusto' por reflejo

`crema-por-reflejo`

**Síntoma.** Fondo beige o crema cálido (cerca de #F4F1EA) con un serif display de alto contraste y un acento terracota o arcilla (cerca de #D97757), sin que el rubro lo pida.

**Por qué pasa.** Es la salida 'elegante' que encontraron los modelos para escapar del índigo. La skill oficial de Anthropic lo nombra como el primer cluster de diseño generado, y aclara que #D97757 es el acento de la propia interfaz de Claude, así que en un brief ajeno se lee como firma de IA. impeccable lo detecta como 'cream-palette'.

**Cómo arreglarlo.** Sacá el fondo de la dirección (mundo y material del producto), no del 'tono seguro'. Probá un blanco frío, un gris tintado hacia el acento o un fondo de color pleno. Si el rubro sí es papel o materia, que sea una decisión escrita en el brief.

**Regla para el agente.** No uses un fondo crema o beige cálido con serif display y acento terracota como default. Si el brief no habla de papel, materia o editorial, elegí otro fondo y justificá el que uses.

Fuentes: [anthropics/skills](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md), [pbakaus/impeccable](https://github.com/pbakaus/impeccable)

## 32. Casi negro con un solo acento ácido o neón

`negro-con-acento-acido`

**Síntoma.** Fondo #0B0B0B o #111 con un único acento verde ácido, bermellón o cian brillante en botones, cifras y bordes.

**Por qué pasa.** Es el segundo cluster que describe Anthropic y el 'cyan-on-dark' que impeccable marca como paleta de IA. Parece técnico sin decidir nada sobre el producto.

**Cómo arreglarlo.** Si el producto es técnico, que el acento salga del mundo del producto y viva en un lugar chico (selección, una cifra clave). El botón primario puede ser un blanco roto de la rampa con texto oscuro. Usá negro real o un neutro tintado con intención.

**Regla para el agente.** No armes la identidad con casi negro + un acento ácido o neón. Si es oscuro, el acento se usa poco y se justifica en el brief.

Fuentes: [anthropics/skills](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md), [pbakaus/impeccable](https://github.com/pbakaus/impeccable)

## 33. Diario de plantilla (filetes, radio 0, columnas densas)

`broadsheet-de-plantilla`

**Síntoma.** Layout tipo periódico en cualquier rubro: filetes finos por todos lados, border-radius 0, columnas apretadas y metadatos en mono.

**Por qué pasa.** Tercer cluster de la skill oficial de Anthropic. Es la respuesta del modelo a 'hacelo editorial', aplicada aunque el contenido no sea de lectura.

**Cómo arreglarlo.** Usá el estilo editorial solo cuando hay contenido largo de verdad (ver ../estilos/editorial-revista.md). Si no, elegí la densidad y el radio por el tipo de producto.

**Regla para el agente.** No apliques el look de diario (filetes, radio 0, columnas densas) si el producto no es de lectura. Editorial es una decisión del brief, no un escape del default.

Fuentes: [anthropics/skills](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md)

## 34. Cromo de plantilla: 'A · B · C', 'PALABRA — fragmento' y mono para etiquetas

`metadatos-con-punto-medio`

**Síntoma.** Metadatos unidos con punto medio, etiquetas armadas como 'PALABRA — fragmento' con raya espaciada, y una mono chiquita para cada dato menor, en cualquier tema.

**Por qué pasa.** La skill oficial de Anthropic lo lista como 'template chrome' que aparece sin importar el tema. Son tics de formato, no decisiones.

**Cómo arreglarlo.** Escribí los metadatos como texto normal o en una tabla chica. Una mono solo si el producto es de código o datos. Separadores de un solo tipo y solo donde ordenan.

**Regla para el agente.** No unas metadatos con ' · ' ni armes etiquetas 'PALABRA — fragmento' por costumbre. La mono para etiquetas solo si el producto es técnico.

Fuentes: [anthropics/skills](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md)

## 35. Una sola palabra del titular en itálica, negrita u otro color

`una-palabra-acentuada`

**Síntoma.** 'Diseñá *más rápido*': una palabra o frase del H1 en itálica serif, en el color de acento o subrayada a mano.

**Por qué pasa.** La skill oficial de Anthropic la nombra como el tell tipográfico más común. Es la versión 'sobria' del texto en degradé.

**Cómo arreglarlo.** Que el titular funcione entero en un solo tratamiento. El énfasis va en la escala, el peso del bloque o la composición.

**Regla para el agente.** No resaltes una sola palabra del titular con itálica, color o subrayado decorativo, salvo que el brief lo pida.

Fuentes: [anthropics/skills](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md)

## 36. Serif itálica gigante como titular de hero

`serif-italica-de-hero`

**Síntoma.** Hero con un titular enorme en serif itálica (Fraunces, Recoleta, Playfair, Newsreader italic) en una startup que no es editorial.

**Por qué pasa.** impeccable lo marca como el hero universal de startup de IA: parece gusto aislado, pero ya es el promedio.

**Cómo arreglarlo.** Romana en vez de itálica, o un display sans con carácter. En una revista o un sello editorial puede quedar: que sea una decisión.

**Regla para el agente.** No uses una serif itálica gigante como titular del hero salvo que el registro sea editorial y esté en el brief.

Fuentes: [pbakaus/impeccable](https://github.com/pbakaus/impeccable)

## 37. Chip o pastilla 'Nuevo ✨' encima del titular

`chip-eyebrow-en-hero`

**Síntoma.** Una pastilla chica con texto en versales o 'New ✨ Presentamos…' justo arriba del H1 del hero.

**Por qué pasa.** impeccable lo detecta como 'hero-eyebrow-chip', el hero default de SaaS generado. unslop pide sacar los badges 'PRO', 'New ✨' o 'Beta 🚀' salvo que el producto los necesite.

**Cómo arreglarlo.** Borrala. Si la novedad importa, integrala al titular o al subtítulo, o usá un breadcrumb real.

**Regla para el agente.** No pongas una pastilla o eyebrow arriba del titular del hero. Si el dato importa, va en el texto.

Fuentes: [pbakaus/impeccable](https://github.com/pbakaus/impeccable), [heydamir/unslop](https://github.com/heydamir/unslop/blob/main/skills/unslop/SKILL.md)

## 38. Ícono en un cuadradito redondeado arriba de cada título

`icono-en-cuadradito`

**Síntoma.** Cada card de features empieza con un ícono dentro de un cuadrado redondeado de color suave, y abajo el título.

**Por qué pasa.** impeccable lo llama la plantilla universal de feature card: todos los generadores sacan esa forma exacta.

**Cómo arreglarlo.** Ícono al lado del título y en el color del texto, o sin contenedor. Mejor todavía, un recorte real del producto en lugar del ícono.

**Regla para el agente.** No apiles un ícono en un cuadradito de color sobre cada título de card. Ícono en línea, del color del texto, o un recorte del producto.

Fuentes: [pbakaus/impeccable](https://github.com/pbakaus/impeccable)

## 39. Sombras de color y glows en botones y cards

`glow-de-color-en-sombras`

**Síntoma.** box-shadow o text-shadow de color con offset cero (un halo), o sombras de color difusas sobre fondo oscuro, en botones, cards e inputs.

**Por qué pasa.** impeccable lo marca como el look 'cool' default de las UIs generadas. Complementa al halo detrás del hero (ficha 3): acá el brillo está en cada componente.

**Cómo arreglarlo.** Sombras neutras y cortas, o ninguna. En oscuro, profundidad con pasos de superficie y bordes finos.

**Regla para el agente.** No uses sombras de color ni glows de acento en componentes. Elevación neutra o superficies escalonadas.

Fuentes: [pbakaus/impeccable](https://github.com/pbakaus/impeccable), [heydamir/unslop](https://github.com/heydamir/unslop/blob/main/skills/unslop/SKILL.md)

## 40. Borde finito más sombra ancha en toda la fila

`borde-fino-y-sombra-ancha`

**Síntoma.** Todas las cards de una fila llevan un borde de 1 px y además una sombra amplia y difusa.

**Por qué pasa.** impeccable lo registra como firma recurrente de UI generada: un panel flotante puede tener las dos cosas; una fila entera, no.

**Cómo arreglarlo.** Elegí una: borde definido o elevación suave, para toda la fila.

**Regla para el agente.** No combines borde fino y sombra ancha en todas las cards de una fila. Una sola señal de borde por familia de componentes.

Fuentes: [pbakaus/impeccable](https://github.com/pbakaus/impeccable)

## 41. Fondo de grilla de líneas o de rayas decorativas

`fondo-de-grilla-o-rayas`

**Síntoma.** Un fondo de cuadrícula finita hecha con linear-gradient repetido, o rayas con repeating-gradient, detrás de secciones que no son un canvas ni un plano.

**Por qué pasa.** impeccable los marca como firmas recurrentes de UI generada ('codex-grid-background', 'repeating-stripes-gradient'): textura sin significado.

**Cómo arreglarlo.** Reservá la grilla para superficies que miden algo (canvas, mapa, plano). En el resto, superficie lisa o una textura deliberada de ../recursos/texturas.md.

**Regla para el agente.** No uses fondos de grilla ni rayas como decoración. Solo en superficies que miden o dibujan.

Fuentes: [pbakaus/impeccable](https://github.com/pbakaus/impeccable)

## 42. Marquee que se desplaza solo

`marquee-automatico`

**Síntoma.** Una cinta de logos, testimonios o palabras que se mueve en loop sin que nadie la toque.

**Por qué pasa.** impeccable lo marca: pide atención que no ganó y esconde la mitad del contenido en todo momento. Además rompe WCAG 2.2.2 si no se puede pausar.

**Cómo arreglarlo.** Fila estática o grilla. Si queda, que se pueda pausar y que se apague con prefers-reduced-motion.

**Regla para el agente.** No uses marquees en loop. Si el brief lo exige, con pausa y apagado en prefers-reduced-motion.

Fuentes: [pbakaus/impeccable](https://github.com/pbakaus/impeccable)

## 43. Cursor que parpadea en un hero que no es un input

`cursor-parpadeante-decorativo`

**Síntoma.** Un titular que se 'tipea' solo, con un cursor parpadeando, sin ningún campo editable.

**Por qué pasa.** impeccable lo marca como estética de devtool usada de adorno: simula una entrada que no existe.

**Cómo arreglarlo.** Sacalo. Si el producto es una terminal, mostrá una sesión real o una captura.

**Regla para el agente.** No simules tipeo ni cursores parpadeantes fuera de un campo real.

Fuentes: [pbakaus/impeccable](https://github.com/pbakaus/impeccable)

## 44. Easing con rebote o elástico

`easing-con-rebote`

**Síntoma.** Botones, modales o cards que entran con bounce o elastic (cubic-bezier con valores > 1).

**Por qué pasa.** impeccable lo marca como fechado: los objetos reales desaceleran suave. unslop pide una sola curva y nada de motion que rebote.

**Cómo arreglarlo.** Una curva de salida del kit (../tokens/tokens.json → easing.standard o enter). Elastic solo para un juego o un personaje.

**Regla para el agente.** No uses easings con rebote o elásticos en UI. Una curva de salida del sistema.

Fuentes: [pbakaus/impeccable](https://github.com/pbakaus/impeccable), [heydamir/unslop](https://github.com/heydamir/unslop/blob/main/skills/unslop/SKILL.md)

## 45. Ilustración armada con formas primitivas

`ilustracion-de-formas-primitivas`

**Síntoma.** Un SVG grande en el hero, hecho con un montón de círculos, rectángulos y blobs que intentan ser una escena.

**Por qué pasa.** impeccable lo marca: se lee como clip art de relleno. Es lo que dibuja un modelo cuando no tiene imagen.

**Cómo arreglarlo.** Una foto, una captura real, una ilustración hecha de verdad o nada. Los íconos, logos y gráficos de datos están bien a su escala.

**Regla para el agente.** No armes la imagen principal con formas SVG primitivas. Foto, captura o ilustración real.

Fuentes: [pbakaus/impeccable](https://github.com/pbakaus/impeccable)

## 46. Una oración entera en tamaño display

`h1-oracion-gigante`

**Síntoma.** El H1 es una frase larga (dos o tres líneas) a tamaño display y se come el viewport.

**Por qué pasa.** impeccable lo marca: el display va bien con una o dos palabras; una oración larga necesita otro tamaño o menos texto.

**Cómo arreglarlo.** Achicá el tamaño o el texto. Usá text-wrap: balance y medí que el CTA quede arriba del pliegue a 390 px.

**Regla para el agente.** Si el titular tiene más de ~8 palabras, no lo pongas en tamaño display. Achicá el tamaño o la frase.

Fuentes: [pbakaus/impeccable](https://github.com/pbakaus/impeccable)

## 47. Contenido que nunca aparece (reveal fallido)

`contenido-invisible-en-reposo`

**Síntoma.** Buena parte del texto queda en opacity 0 o visibility hidden porque la animación de entrada no se disparó (JS que falló, observer que no corre, captura headless).

**Por qué pasa.** impeccable lo detecta como firma de reveal fallido. Pasa cuando la animación gobierna si el contenido existe.

**Cómo arreglarlo.** Contenido visible por defecto; JS solo mejora la entrada. Probá con JS apagado y con prefers-reduced-motion.

**Regla para el agente.** Nunca escondas contenido por defecto esperando una animación. Visible sin JS; la animación es una mejora.

Fuentes: [pbakaus/impeccable](https://github.com/pbakaus/impeccable)

## 48. Texto diminuto, tracking abierto en cuerpo o interlineado apretado

`texto-diminuto-o-apretado`

**Síntoma.** Labels de 9–10 px, cuerpo con letter-spacing amplio, párrafos con line-height por debajo de 1.3, texto largo en versales o justificado sin cortes.

**Por qué pasa.** impeccable los marca como fallas de legibilidad, no de estilo: texto funcional por debajo de 11 px, tracking > 0.05em en cuerpo, leading < 1.3. unslop agrega: nunca tracking negativo en texto chico.

**Cómo arreglarlo.** Cuerpo 16 px (14 como mínimo en UI densa), funcional ≥ 11 px, leading 1.5–1.7 en párrafos, tracking 0 en cuerpo, alineado a la izquierda.

**Regla para el agente.** Nada funcional por debajo de 11 px; cuerpo ≥ 14 px; leading de párrafo ≥ 1.5; sin tracking abierto ni negativo en texto chico; sin justificar sin guiones.

Fuentes: [pbakaus/impeccable](https://github.com/pbakaus/impeccable), [heydamir/unslop](https://github.com/heydamir/unslop/blob/main/skills/unslop/SKILL.md)

## 49. Viudas y titulares desbalanceados

`viudas-y-titulos-desparejos`

**Síntoma.** Párrafos que terminan con una sola palabra en la última línea; titulares cuya última línea es una palabra suelta.

**Por qué pasa.** impeccable lo marca como aviso ('straggler', 'unbalanced-heading'). Hoy se arregla con una línea de CSS.

**Cómo arreglarlo.** text-wrap: balance en títulos y text-wrap: pretty en párrafos. Si el navegador no lo soporta, un espacio duro entre las dos últimas palabras.

**Regla para el agente.** Poné text-wrap: balance en headings y text-wrap: pretty en párrafos.

Fuentes: [pbakaus/impeccable](https://github.com/pbakaus/impeccable)

## 50. Cards pegadas al borde de un carrusel o panel

`cards-cortadas-en-el-scroller`

**Síntoma.** En un scroller horizontal o un tab panel, la primera card toca el borde y se le cortan las esquinas, mientras del otro lado hay margen.

**Por qué pasa.** impeccable lo detecta ('edge-flush-cards'): el panel es más ancho que su caja de recorte.

**Cómo arreglarlo.** Mismo inset de los dos lados (scroll-padding y padding-inline iguales).

**Regla para el agente.** En scrollers y paneles, el mismo inset a los dos lados; ninguna card cortada en reposo.

Fuentes: [pbakaus/impeccable](https://github.com/pbakaus/impeccable)

## 51. Radios anidados que no suman

`radios-anidados-que-no-suman`

**Síntoma.** Una card con rounded-2xl tiene adentro una imagen o un botón con el mismo radio, y las esquinas se ven 'hinchadas' o desparejas.

**Por qué pasa.** unslop lo pone en su checklist: el radio interior tiene que ser el exterior menos el padding.

**Cómo arreglarlo.** radio interior = radio exterior − padding (con un mínimo de 0). Un radio por tipo de control.

**Regla para el agente.** En elementos anidados, el radio interior es el exterior menos el padding. Los botones comparten el radio de control.

Fuentes: [heydamir/unslop](https://github.com/heydamir/unslop/blob/main/skills/unslop/SKILL.md)

## 52. Números en formatos mezclados y sin cifras tabulares

`cifras-en-formatos-mezclados`

**Síntoma.** '$48.210' al lado de '$124,860.40', porcentajes con y sin decimales, columnas de números que bailan.

**Por qué pasa.** unslop lo marca: el modelo escribe cada número por separado.

**Cómo arreglarlo.** Un solo formato por pantalla (Intl.NumberFormat con el locale del producto) y font-variant-numeric: tabular-nums en cifras y tablas.

**Regla para el agente.** Un formato numérico por pantalla, con el locale del producto, y tabular-nums en cifras.

Fuentes: [heydamir/unslop](https://github.com/heydamir/unslop/blob/main/skills/unslop/SKILL.md)

## 53. Signos de exclamación y punto final en labels

`exclamaciones-y-puntos-en-labels`

**Síntoma.** '¡Guardado con éxito!', '¡Empezá ya!', títulos y botones que terminan en punto.

**Por qué pasa.** unslop lo pide fuera: la interfaz no grita, y los strings cortos no llevan punto final.

**Cómo arreglarlo.** Sin exclamaciones en la interfaz. Títulos, labels, botones y captions sin punto; los párrafos sí.

**Regla para el agente.** Sin signos de exclamación en la UI. Sin punto final en títulos, botones, labels y captions.

Fuentes: [heydamir/unslop](https://github.com/heydamir/unslop/blob/main/skills/unslop/SKILL.md)

## 54. Tira de cifras bajo el hero

`tira-de-cifras`

**Síntoma.** Una fila de tres o cuatro números grandes con una etiqueta de una palabra ('10k+ usuarios · 99,9 % uptime · 24/7').

**Por qué pasa.** taste-skill (copy-tells) la llama 'the strip of figures': aparece en casi todas las páginas de modelo. La skill de Anthropic también avisa que 'número grande + label chico + acento' es el tratamiento default.

**Cómo arreglarlo.** Cada número en la oración que prueba. Una tira solo con datos reales del brief (precio, horario, cantidad).

**Regla para el agente.** No armes una tira de cifras con etiquetas de una palabra. Cada dato en la frase que lo prueba, y solo si es real.

Fuentes: [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill/blob/main/skills/taste-skill/references/copy-tells.md), [anthropics/skills](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md)

## 55. Titulares 'X. Y.' y pares numéricos

`titulos-en-dos-fragmentos`

**Síntoma.** 'Doce habitaciones. Tres formas de quedarse.' o 'Cuatro proyectos, cuatro problemas distintos.' en varias secciones.

**Por qué pasa.** taste-skill los cuenta como tells de segunda generación: parecen buena copy, por eso pasan la revisión. Una vez está bien; el patrón es la señal.

**Cómo arreglarlo.** Otras formas de título: un nombre con una afirmación debajo, un verbo y la cosa, una oración simple que diga qué tiene la sección.

**Regla para el agente.** Como mucho un titular de dos fragmentos ('X. Y.') por página y ningún par numérico ('cuatro X, cuatro Y').

Fuentes: [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill/blob/main/skills/taste-skill/references/copy-tells.md)

## 56. Contrastes fabricados y aforismos

`contrastes-fabricados`

**Síntoma.** 'No es una herramienta. Es una plataforma.', 'Sin formularios, sin vueltas.', 'en lugar de…', 'sin el…' cerrando varias secciones.

**Por qué pasa.** impeccable lo detecta como 'aphoristic-cadence' y taste-skill como 'contrast frames' y 'negation runs': si se prohíbe 'no X sino Y', vuelve como 'en lugar de'.

**Cómo arreglarlo.** Decí el hecho positivo solo. Una negación queda si cada ítem es algo que la persona puede verificar.

**Regla para el agente.** Como mucho dos contrastes ('no X, sino Y', 'en lugar de', 'sin…') por página, y nunca para cerrar secciones.

Fuentes: [pbakaus/impeccable](https://github.com/pbakaus/impeccable), [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill/blob/main/skills/taste-skill/references/copy-tells.md)

## 57. Palabras de virtud sobre uno mismo

`palabras-de-virtud`

**Síntoma.** La página se describe como 'honesta', 'tranquila', 'cuidada', 'de verdad', 'pensada', 'confiable'.

**Por qué pasa.** taste-skill las prohíbe cuando hablan de la propia marca: una página nunca se llama honesta, lo muestra.

**Cómo arreglarlo.** Reemplazá cada virtud por el hecho que la prueba (una política, un plazo, un dato).

**Regla para el agente.** No describas el producto con palabras de virtud (honesto, tranquilo, cuidado, de verdad). Mostralo con un hecho.

Fuentes: [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill/blob/main/skills/taste-skill/references/copy-tells.md)

## 58. Detalles específicos inventados

`especificos-inventados`

**Síntoma.** 'Lote N.º 047', 'a las 6:12 desde la ventana de la habitación 9', '38 % menos reintentos', '10x más rápido', 'Más de 10.000 equipos' sin fuente.

**Por qué pasa.** taste-skill lo prohíbe: el modelo produce detalle de adorno porque el detalle convence. unslop pide sacar o confirmar cada afirmación que no se puede verificar.

**Cómo arreglarlo.** Solo los datos del brief o del cliente. Sin ellos, una frase más simple. Listá en el reporte las afirmaciones a confirmar.

**Regla para el agente.** No inventes cifras, nombres, horarios, lotes ni clientes. Si un dato no está en el brief, no va o se marca para confirmar.

Fuentes: [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill/blob/main/skills/taste-skill/references/copy-tells.md), [heydamir/unslop](https://github.com/heydamir/unslop/blob/main/skills/unslop/SKILL.md)

## 59. Remate ingenioso, firma de footer y origen de plantilla

`cierre-ingenioso-y-firma-de-footer`

**Síntoma.** Párrafos que terminan con un chiste seco, un footer 'Hecho en Salta, horneado a 220 °C', o una historia 'En 2019, Ana y Luis encontraron una vieja ferretería…' sin que el brief la cuente.

**Por qué pasa.** taste-skill los lista como tells de segunda generación: la misma voz cálida e ingeniosa para cualquier cliente.

**Cómo arreglarlo.** Cerrá con información. El footer lleva la fila legal y de contacto. La historia, solo si es la real.

**Regla para el agente.** No cierres secciones con remates, no firmes el footer con una frase y no inventes la historia de origen.

Fuentes: [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill/blob/main/skills/taste-skill/references/copy-tells.md)

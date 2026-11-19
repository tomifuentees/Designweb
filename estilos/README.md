# Estilos visuales

Catálogo de estilos visuales para web y producto, armado en noviembre de 2026. El objetivo no es perseguir la moda por la moda: es que un agente de código (o un humano con apuro) deje de abrir un archivo con un hero centrado, un degradé violeta-índigo, tres cards idénticas con sombra suave e Inter, y elija un lenguaje visual con criterio.

Esta carpeta es la segunda pieza del kit de diseño frontend, pensada para leerse junto a [`../tipografias/`](../tipografias/README.md). Las fichas están escritas para personas y, también, para que una skill de Claude o de otro agente las consuma a través de `estilos.json`.

Hay **27 estilos**. Cada ficha trae cuándo usarlo y cuándo no, reglas concretas (grilla, espaciado, radios, bordes, sombras, color y tipografía del catálogo), al menos tres sitios reales con link verificado, errores comunes y un snippet mínimo en HTML + Tailwind (CDN) o CSS. La tipografía recomendada sale de [`../tipografias/fonts.json`](../tipografias/fonts.json); los links relativos apuntan a la categoría correspondiente.

No todos están “en auge”. Algunos son el default de 2026 (bento, tipo cinética, SaaS oscuro). Otros son contrapesos útiles (editorial, orgánico, anti-diseño). Un par —neo-brutalismo de página completa, claymorfismo, glassmorfismo como tema— están en enfriamiento o en nicho, y se documentan para usarlos con oficio, no por default.

## Qué hay acá

| Archivo | Contenido |
|---|---|
| [bento-grids.md](./bento-grids.md) | Grillas bento: jerarquía por tamaño de mosaico |
| [neo-brutalismo.md](./neo-brutalismo.md) | Neo-brutalismo: borde grueso, sombra dura, acento más que look completo |
| [suizo-internacional.md](./suizo-internacional.md) | Estilo suizo / internacional: grilla, sans neutra, jerarquía clara |
| [editorial-revista.md](./editorial-revista.md) | Editorial / revista: serif, crema, ritmo de lectura |
| [saas-oscuro-premium.md](./saas-oscuro-premium.md) | SaaS oscuro premium: un acento, mucho aire, producto al frente |
| [estilo-linear.md](./estilo-linear.md) | Estilo Linear: el producto es la demo, etiquetas técnicas, bento |
| [ui-casi-invisible.md](./ui-casi-invisible.md) | UI casi invisible: pelo de línea, tipografía como cromo |
| [retrofuturismo-y2k.md](./retrofuturismo-y2k.md) | Retrofuturismo / Y2K: cromo, neón, nostalgia del 2000 |
| [organico-terroso.md](./organico-terroso.md) | Orgánico / terroso: paleta de tierra, formas blandas, calor |
| [maximalismo.md](./maximalismo.md) | Maximalismo: capas, saturación, tipografía que grita |
| [minimalismo-monocromo.md](./minimalismo-monocromo.md) | Minimalismo monocromo: una familia, poco color, mucho aire |
| [grano-ruido.md](./grano-ruido.md) | Grano y ruido: textura liviana contra el pulido de IA |
| [tipografia-kinetica.md](./tipografia-kinetica.md) | Tipografía cinética: el tipo se mueve, una sola vez y bien |
| [anti-diseno.md](./anti-diseno.md) | Anti-diseño / brutalismo anti-grilla: crudeza deliberada |
| [claymorfismo.md](./claymorfismo.md) | Claymorfismo: inflado, suave, nicho estable (no default 2026) |
| [espacial-3d.md](./espacial-3d.md) | Espacial / 3D: WebGL, producto orbitando, profundidad |
| [japones-inspirado.md](./japones-inspirado.md) | Inspiración japonesa: ma, cruce vertical/horizontal, contención |
| [dopamina-saturado.md](./dopamina-saturado.md) | Dopamina / paletas saturadas: color alto, marcas jóvenes |
| [scrollytelling.md](./scrollytelling.md) | Scrollytelling: el scroll cuenta, no secuestra |
| [glassmorfismo.md](./glassmorfismo.md) | Glassmorfismo: vidrio mate como acento, no como tema |
| [catalogo-tecnico.md](./catalogo-tecnico.md) | Catálogo técnico: ficha de producto, captions mono, fondo neutro |
| [ilustrado-humano.md](./ilustrado-humano.md) | Ilustrado / hecho a mano: contrapeso a la imagen de IA |
| [navegacion-experimental.md](./navegacion-experimental.md) | Navegación experimental: explorar antes que el menú de siempre |
| [risografia-impreso.md](./risografia-impreso.md) | Risografía / impreso: paleta corta, grano de tinta, registro imperfecto |
| [expresivo-minimo.md](./expresivo-minimo.md) | Minimalismo expresivo: limpieza + una sola rareza |
| [realismo-tactil.md](./realismo-tactil.md) | Realismo táctil: materia, papel, irregularidad creíble |
| [grilla-rota.md](./grilla-rota.md) | Grilla rota / layouts orgánicos: asimetría controlada |
| [estilos.json](./estilos.json) | El mismo catálogo, legible por máquinas |
| [fuentes-investigacion.md](./fuentes-investigacion.md) | Fuentes consultadas, con links |

## Cómo elegir un estilo según el tipo de proyecto

1. **Primero el trabajo, después el look.** ¿Hay que vender un producto, leer un artículo, operar un dashboard o impresionar en un portfolio? El estilo sale de esa tarea, no de un moodboard suelto.
2. **Uno, no una ensalada.** Elegí un idioma visual y un acento. Mezclar bento + glass + neo-brutalismo + tipografía cinética + grano en la misma landing es otra forma de parecer una plantilla.
3. **Si el producto es de confianza (plata, salud, trámites), bajá el volumen.** UI casi invisible, suizo, editorial contenido o catálogo técnico. El maximalismo y el Y2K quedan para moda, música, belleza y campañas.
4. **Si el presupuesto de motion es bajo, no prometas WebGL.** Un tipo bien elegido y una grilla rara rinden más que un canvas a 20 fps.

### SaaS / producto de software

Los caminos que hoy se leen como “de oficio” son el [SaaS oscuro premium](./saas-oscuro-premium.md), el [estilo Linear](./estilo-linear.md) (si de verdad el producto puede ser la demo), la [UI casi invisible](./ui-casi-invisible.md) y el [bento](./bento-grids.md) en la sección de features —no en todo el sitio. El [catálogo técnico](./catalogo-tecnico.md) y el [minimalismo expresivo](./expresivo-minimo.md) evitan que el clon de Linear se note. Evitá neo-brutalismo de página completa, Y2K, claymorfismo y glass por todos lados. Ojo: copiar el púrpura de Linear + Inter Display ya es un default nuevo.

### Landing de PyME

Acá el riesgo no es “verse poco tech”. Es verse como la milésima landing de IA. Funcionan el [minimalismo expresivo](./expresivo-minimo.md), lo [editorial](./editorial-revista.md) si hay historia que contar, lo [orgánico](./organico-terroso.md) si el oficio es físico (comida, bienestar, oficio local) y un [bento](./bento-grids.md) corto para servicios. No clones Linear ni uses Geist si no vendés software. Un color sacado del local, una foto real y una serif o grotesca del catálogo alcanzan.

### E-commerce

La dirección la marca la mercadería. Lujo callado: [minimalismo monocromo](./minimalismo-monocromo.md), [editorial](./editorial-revista.md), [inspiración japonesa](./japones-inspirado.md). Belleza y juventud: [dopamina](./dopamina-saturado.md), [Y2K](./retrofuturismo-y2k.md), [maximalismo](./maximalismo.md). Comida, cuerpo, campo: [orgánico](./organico-terroso.md), [realismo táctil](./realismo-tactil.md). El bento sirve para destacar categorías; el 3D, solo si el producto se entiende mejor girándolo.

### Portfolio / estudio / cultural

Hay más permiso para [grilla rota](./grilla-rota.md), [tipo cinética](./tipografia-kinetica.md), [navegación experimental](./navegacion-experimental.md), [anti-diseño](./anti-diseno.md), [risografía](./risografia-impreso.md) o un momento [3D](./espacial-3d.md). El [estilo suizo](./suizo-internacional.md) sigue siendo una base impecable para estudios de arquitectura y diseño. La regla: una firma, no cinco efectos.

### Dashboard / app densa

Priorizá [UI casi invisible](./ui-casi-invisible.md), [suizo](./suizo-internacional.md) y tipografías de UI del catálogo (Switzer, Mona Sans, Figtree, Atkinson Hyperlegible si hay requisito de lectura). El color es semántico, no decorativo. No uses glass sobre tablas, neo-brutalismo en formularios, tipo cinética sobre datos ni cards envueltas en cards.

## Señales de diseño genérico de IA

Estas cosas no están prohibidas. Varias son útiles. El problema es usarlas **como default de personalidad**, apiladas, sin una decisión de marca. El diagnóstico sale de hilos de r/web_design de 2026 (en particular [What makes a ui look AI generated?](https://www.reddit.com/r/web_design/comments/1wkwns6/what_makes_a_ui_look_ai_generated/), [Every Vibecoded websites looks the same](https://www.reddit.com/r/web_design/comments/1uzascg/every_vibecoded_websites_looks_the_same/), [What element of AI designs is overused](https://www.reddit.com/r/web_design/comments/1xa8ug1/what_element_of_ai_designs_that_is_overused/) y [What makes an AI-generated website feel generic?](https://www.reddit.com/r/web_design/comments/1wu1yvk/what_makes_an_aigenerated_website_feel_generic/)), cruzados con lo que ya está en [`../tipografias/README.md`](../tipografias/README.md).

| Señal | Por qué delata | Cómo escapar |
|---|---|---|
| Degradé violeta / índigo de fondo o en el titular | Es el “seguro” del training data y de v0 / Lovable / Bolt. | Sacá la paleta del mundo real de la marca (un azulejo, un logo viejo, un producto). Un solo acento, plano o casi. |
| Inter (o Geist, Poppins, Montserrat) como voz de marca | Inter es la sans de producto 2023-2026; Geist ya es el default de landings de IA y devtools. | Elegí una pareja del [catálogo](../tipografias/README.md). Inter puede quedar de apoyo en UI densa, no de personalidad. |
| Cards idénticas, bien redondeadas, con sombra suave | Nadie decidió una jerarquía: cada bloque se envolvió en el mismo contenedor. | Variá tamaño y peso. Un bloque sin caja. Bordes de 0, 4 o 20 px a propósito, no todos en `rounded-xl`. |
| Íconos emoji (o Lucide / Heroicons mezclados) sobre cada feature | Atajo de “esto parece diseñado”. Los sets no coinciden en trazo. | Un solo set, un solo peso. Mejor: un número, una foto real o nada. |
| Hero centrado + tres feature cards + tira de logos + testimonials + pricing + FAQ | Es la plantilla estadística de “SaaS moderno”. | Borrá la mitad de las secciones. Agrandá la que sí importa. Que el contenido real dicte la forma. |
| Glassmorfismo en todos lados | El blur barato + púrpura es de los combos más citados como “AI look”. | Vidrio solo en un header sticky o un modal, con texto de contraste real. Ver [glassmorfismo](./glassmorfismo.md). |
| Eyebrow (“The future of…”) arriba de cada H2 | Ritmo mecánico, copy intercambiable. | Un eyebrow, o ninguno. El titular tiene que decir algo que solo esta marca puede decir. |
| Copy genérica (“Unlock your potential”, “Seamlessly manage your workflow”) | El diseño no tiene a qué responder, entonces cae en el default visual. | Escribí el texto de verdad antes de maquetar. Números reales, nombres reales, estados vacíos. |
| Fade-in al scroll en cada sección, badges neón, ilustraciones 3D de stock / IA | Ornamento sin punto de vista. Las imágenes de IA ya se reconocen al toque (Creative Boom, 2026, citado por Bubble). | Una sola firma (un titular cinético, un grano, una foto). Ilustración propia o fotografía. |
| Padding matemáticamente uniforme en toda la página | Nada atrae la mirada. | Rompé la escala a propósito: un bloque con el doble de aire, otro más denso. |

Lo que sí conviene conservar, aunque la IA también lo use: un titular que diga qué hacés en palabras simples, un botón primario obvio, contraste decente, tamaños de lectura en mobile y espacio para respirar. Eso no es genérico: es oficio. El punto de vista está en la excepción, no en romper las reglas básicas.

## Índice de estilos

| Estilo | Vigencia en 2026 | Mood | Mejor para |
|---|---|---|---|
| [Bento grids](./bento-grids.md) | Establecido / casi default en features | Modular, ordenado, producto | SaaS, landings, categorías de e-commerce |
| [Neo-brutalismo](./neo-brutalismo.md) | En enfriamiento como look completo; vivo como acento | Ruidoso, gráfico, directo | Campañas, consumer, un CTA dentro de un sistema calmado |
| [Suizo / internacional](./suizo-internacional.md) | Perenne, con revival de catálogo técnico | Preciso, objetivo, tipográfico | Estudios, instituciones, finanzas, editorial de datos |
| [Editorial / revista](./editorial-revista.md) | Contrapeso en auge frente al SaaS oscuro | Literario, cálido, autoritativo | Medios, agencias, marcas con historia, landings con lectura |
| [SaaS oscuro premium](./saas-oscuro-premium.md) | Dominante en software de diseño liderado | Técnico, premium, contenido | Devtools, B2B, product-led |
| [Estilo Linear](./estilo-linear.md) | Muy copiado; ya hay que usarlo con distancia | Especificación, demo viva | Productos donde la UI *es* el argumento |
| [UI casi invisible](./ui-casi-invisible.md) | Emergente | Quieto, confiable, tipográfico | Dashboards, fintech, plataformas de datos |
| [Retrofuturismo / Y2K](./retrofuturismo-y2k.md) | Nicho estable, visible en lifestyle | Nostálgico, cromado, lúdico | Moda, música, belleza, microsites |
| [Orgánico / terroso](./organico-terroso.md) | Emergente (“nature distilled”) | Cálido, físico, cercano | Comida, bienestar, sustentabilidad, PyMEs de oficio |
| [Maximalismo](./maximalismo.md) | En auge como contrapeso al minimalismo genérico | Denso, ruidoso, memorable | Marcas de actitud, cultura, campañas |
| [Minimalismo monocromo](./minimalismo-monocromo.md) | Perenne, vigente en lujo y fintech sobria | Callado, caro, disciplinado | Lujo, banca, moda, portfolios serios |
| [Grano y ruido](./grano-ruido.md) | Establecido como técnica, no como “estilo de página” | Táctil, analógico, anti-IA | Acento sobre editorial, oscuro, riso, anti-diseño |
| [Tipografía cinética](./tipografia-kinetica.md) | Establecido; mejor como un solo gesto | Expresivo, dirigido, memorable | Heroes, lanzamientos, portfolios |
| [Anti-diseño](./anti-diseno.md) | Establecido como contrapeso al bento pulido | Crudo, deliberadamente feo, indie | Estudios, cultura, editoriales experimentales |
| [Claymorfismo](./claymorfismo.md) | Nicho estable, no es tendencia de 2026 | Blando, juguetón, “de juguete” | Onboarding, kids, fintech amable. No tablas. |
| [Espacial / 3D](./espacial-3d.md) | En auge cuando el producto lo pide | Inmersivo, material, demo | Producto físico, fashion 3D, portfolios de motion |
| [Inspiración japonesa](./japones-inspirado.md) | Vivo en cultura, retail y estudios | Contención, ritmo, vacío | Editorial, retail, cultura, marcas que bancan el silencio |
| [Dopamina / saturado](./dopamina-saturado.md) | En auge en lifestyle y beauty | Alegre, alto contraste, energético | Juventud, belleza, wellness lúdico, F&B |
| [Scrollytelling](./scrollytelling.md) | Establecido | Narrativo, guiado, cinematográfico | Lanzamientos, long-form, producto físico |
| [Glassmorfismo](./glassmorfismo.md) | Revivido (Liquid Glass), sobreusado como tema | Vítreo, espacial, frágil | Acento en headers/modales. Nunca como sistema completo. |
| [Catálogo técnico](./catalogo-tecnico.md) | Visible en hardware y devtools | Manual, preciso, documental | Hardware, APIs, industrial, marcas “built, not decorated” |
| [Ilustrado / humano](./ilustrado-humano.md) | Emergente como reacción a la imagen de IA | Cercano, dibujado, imperfecto | Educación, wellness, marcas con personaje |
| [Navegación experimental](./navegacion-experimental.md) | Citada como tendencia; de alto riesgo | Exploratoria, espacial, memorable | Portfolios, cultural, campañas. Cuidado en e-commerce y SaaS. |
| [Risografía / impreso](./risografia-impreso.md) | Nicho editorial, vigente | Tinta, granulado, limitado | Editoriales independientes, café, cultura, zines |
| [Minimalismo expresivo](./expresivo-minimo.md) | El “mínimo” que sí aguanta 2026 | Limpio con una rareza | PyMEs, SaaS que no quieren parecer Linear, estudios |
| [Realismo táctil](./realismo-tactil.md) | Establecido | Material, irregular, creíble | Comida, belleza, craft, cualquier marca que venda materia |
| [Grilla rota](./grilla-rota.md) | En auge como reacción a la grilla 12 | Asimétrico, compuesto, editorial | Portfolios, agencias, landings culturales |

## Cómo usarlo desde un agente

1. Leé este README y la tabla anti-genérica.
2. Según el tipo de proyecto, proponé **un estilo** (o un estilo + un acento, por ejemplo “editorial con un poco de grano”). No una lista de diez.
3. Abrí la ficha y `estilos.json`. Respetá “cuándo no” y las reglas de radio, sombra y paleta.
4. Elegí tipografía solo del [catálogo](../tipografias/fonts.json), con la pareja que recomiende la ficha o [`../tipografias/pairings.md`](../tipografias/pairings.md). Advertí la licencia.
5. No presentes Inter + degradé violeta + tres cards + glass como primera opción, salvo que el brief lo pida de forma explícita.
6. Si el usuario pide “que se vea como Linear”, avisá que ese look ya está muy copiado y ofrecé una variante (otra grotesca, otro acento, UI casi invisible, catálogo técnico).

La vigencia es una foto de noviembre de 2026. Un estilo “en auge” hoy puede ser el cliché del año que viene —el bento ya está cerca de ese punto en landings de SaaS.


# Checklist de revisión (antes de shippear)

Pasada corta, pensada para un humano o para un agente que ya armó una UI. Si marcás tres o más “sí”, volvé al [catálogo](./catalogo.md) y a las reglas antes de mergear. Una sola cosa, elegida a propósito, puede quedar.

## Color y forma

- [ ] ¿Hay un degradé índigo–violeta (o `bg-indigo-500` / `violet-600`) usado como identidad?
- [ ] ¿Hay un heading con `bg-clip-text` o un halo/glow detrás del hero?
- [ ] ¿Cada bloque tiene un color distinto, sin una paleta de roles?
- [ ] ¿Todas las cajas comparten un `rounded-2xl`/`3xl` y la misma sombra suave?
- [ ] ¿Hay “fingernail cards” (raya de acento a la izquierda en cada card)?
- [ ] ¿Hay glassmorphism como tema, o un brutalismo de plantilla que no se pidió?
- [ ] ¿El cuerpo o el muted fallan 4.5:1 (sobre todo en oscuro)?

## Layout y motion

- [ ] ¿El hero está centrado, con un titular que le serviría a cualquiera y dos CTAs genéricos?
- [ ] ¿Hay una fila de tres cards idénticas con ícono + párrafo?
- [ ] ¿La página sigue el orden hero → logos → 3 features → testimonials → pricing → CTA sin una razón?
- [ ] ¿Hay cards anidadas dentro de cards?
- [ ] ¿Cada sección entra con fade/slide-up, o hay badges con `animate-pulse`?
- [ ] ¿Cada botón lleva una flecha, y cada H2 un kicker en versales o un 01 / 02 / 03?

## Tipo, ícono e imagen

- [ ] ¿La única familia es Inter, Geist, Poppins, Montserrat o Roboto?
- [ ] ¿Los íconos son Lucide “porque sí”?
- [ ] ¿Hay emojis haciendo de ícono, bullet o saludo de dashboard?
- [ ] ¿La imagen es un render 3D de stock, un retrato de IA o un MacBook genérico?
- [ ] ¿Falta prueba real (precios, horarios, nombres, captura del producto)?

## Copy y resto

- [ ] ¿Aparecen Elevate, Seamless, Supercharge, Unleash, Empower, cutting-edge, “build the future of…”?
- [ ] ¿Un dashboard arranca con “Welcome to your Dashboard, [Name] ✨”?
- [ ] ¿Hay frases que huelen al prompt (“Built with…”, “no mocks”, justificación técnica)?
- [ ] ¿La prosa está llena de em-dash, openers de stock o hedging?
- [ ] ¿El title, el alt, el OG o el favicon son los de la plantilla o del bundler?
- [ ] ¿Hay hex, radios o duraciones sueltos, distintos a los tokens del proyecto?

## Señales agregadas en noviembre de 2026 (fichas 31–59)

Minadas de impeccable, de la skill oficial de Anthropic, de taste-skill y de unslop. Detalle en [`../recursos/minado-repos.md`](../recursos/minado-repos.md).

**Color, superficie y forma**
- [ ] ¿Fondo crema/beige con serif display y acento terracota, sin que el rubro lo pida? (`crema-por-reflejo`)
- [ ] ¿Casi negro con un solo acento ácido o neón como identidad? (`negro-con-acento-acido`)
- [ ] ¿Sombras de color o glows en botones, cards o inputs? (`glow-de-color-en-sombras`)
- [ ] ¿Toda una fila de cards con borde fino **y** sombra ancha? (`borde-fino-y-sombra-ancha`)
- [ ] ¿Fondo de grilla de líneas o de rayas sin que la superficie mida nada? (`fondo-de-grilla-o-rayas`)
- [ ] ¿Radios anidados iguales, que no restan el padding? (`radios-anidados-que-no-suman`)

**Tipo y estructura**
- [ ] ¿Una sola palabra del titular en itálica, color o subrayado? (`una-palabra-acentuada`)
- [ ] ¿Serif itálica gigante como titular del hero en algo que no es editorial? (`serif-italica-de-hero`)
- [ ] ¿Pastilla o eyebrow arriba del H1? (`chip-eyebrow-en-hero`)
- [ ] ¿Ícono en un cuadradito de color arriba de cada título de card? (`icono-en-cuadradito`)
- [ ] ¿Una oración larga en tamaño display? (`h1-oracion-gigante`)
- [ ] ¿Metadatos 'A · B · C', etiquetas 'PALABRA — fragmento' o mono para cada dato menor? (`metadatos-con-punto-medio`)
- [ ] ¿Look de diario (filetes, radio 0, columnas densas) en un producto que no es de lectura? (`broadsheet-de-plantilla`)
- [ ] ¿Texto funcional < 11 px, cuerpo con tracking abierto, leading < 1.3 o justificado? (`texto-diminuto-o-apretado`)
- [ ] ¿Títulos sin `text-wrap: balance` o párrafos con viudas? (`viudas-y-titulos-desparejos`)
- [ ] ¿Números en formatos mezclados o sin `tabular-nums`? (`cifras-en-formatos-mezclados`)
- [ ] ¿Cards cortadas contra el borde de un scroller? (`cards-cortadas-en-el-scroller`)

**Motion e imagen**
- [ ] ¿Marquee en loop? ¿Cursor parpadeante sin input? ¿Easing con rebote? (`marquee-automatico`, `cursor-parpadeante-decorativo`, `easing-con-rebote`)
- [ ] ¿Contenido en `opacity: 0` hasta que una animación lo revela? Probalo sin JS. (`contenido-invisible-en-reposo`)
- [ ] ¿La imagen principal es un SVG de formas primitivas? (`ilustracion-de-formas-primitivas`)

**Copy de segunda generación** (parece buena, por eso pasa la revisión)
- [ ] ¿Tira de 3–4 cifras con etiquetas de una palabra? (`tira-de-cifras`)
- [ ] ¿Más de un titular "X. Y." o un par "cuatro X, cuatro Y"? (`titulos-en-dos-fragmentos`)
- [ ] ¿Más de dos "no es X, es Y" / "en lugar de" / "sin…"? (`contrastes-fabricados`)
- [ ] ¿La página se llama a sí misma honesta, tranquila o cuidada? (`palabras-de-virtud`)
- [ ] ¿Cifras, lotes, horarios o clientes que no están en el brief? (`especificos-inventados`)
- [ ] ¿Remates ingeniosos, firma poética en el footer o historia de origen inventada? (`cierre-ingenioso-y-firma-de-footer`)
- [ ] ¿Signos de exclamación en la UI o punto final en botones y títulos? (`exclamaciones-y-puntos-en-labels`)
- [ ] ¿Algún borde que gira o brilla en loop (border beam, conic-gradient animado)? (`borde-giratorio-beam`)

## Cómo pasar la revisión (orden y método)

**1. Dos miradas separadas.** Primero el juicio de diseño (¿se entiende? ¿se ve hecho para este producto?), después la evidencia medible (contraste, tamaños, overflow, foco, el detector). No mezcles las dos hasta el final: la lista de un detector "ancla" el juicio. Idea tomada del `critique` de [impeccable](https://github.com/pbakaus/impeccable) (Apache 2.0), que corre las dos evaluaciones en subagentes aislados. Detector opcional, sin LLM: `npx impeccable detect src/` y `npx impeccable detect http://localhost:5173` (las reglas de contraste y tamaño necesitan la página renderizada).

**2. Triage antes de arreglar** (de [unslop](https://github.com/heydamir/unslop), CC BY 4.0): con mucho slop (color, tipo, íconos y copy a la vez) va el flujo completo; con poco, solo se arregla lo marcado y se conserva paleta, tipo y layout; sin slop, se dice y se proponen dos o tres ajustes con valores exactos. No se cambia una pantalla buena solo para que sea distinta.

**3. Clasificá cada desvío** (del `polish` de impeccable): falta un token, implementación suelta que debería usar un componente compartido, desajuste de concepto (flujo o jerarquía distintos al resto del producto) o defecto local. Arreglá la causa en el nivel más chico correcto.

**4. Arreglá por capas, en este orden** (de unslop): espacio → color → íconos → copy → tipo → layout → detalles → visuales → motion. El espacio va primero porque todo se lee distinto con el ritmo bien; la copy antes que el tipo porque el largo del titular decide su tamaño; visuales y motion al final, sobre una pantalla que ya funciona sin ellos. En modo `restyling` se saltean íconos (salvo tamaño y color), copy y visuales.

**5. Cerrá con tres pruebas:** (a) **plantilla**: si cambiás el nombre del producto por otro, ¿la pantalla sigue sirviendo? Si sí, empujá la dirección en la copy, el visual y la firma (unslop); (b) **un adorno menos**: antes de entregar, sacá uno (la skill de Anthropic cita el consejo de Chanel); (c) **renders**: como mucho tres por pasada, a 1440 y 390 px.

Si el proyecto todavía no tiene tokens, paleta ni pareja tipográfica, **empezá por ahí**. Sin eso, el checklist se va a poner rojo en cada pasada.

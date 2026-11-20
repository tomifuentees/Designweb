# Dirección por rubro

Antes de elegir un estilo, decidí **qué tipo de negocio es** y qué puede mostrar. Esta ficha junta tres ideas minadas en noviembre de 2026 y las aterriza en los slugs de Designweb:

- De [taste-skill](https://github.com/Leonxlnx/taste-skill) (MIT): **el tipo de negocio decide todo**. Un lugar al que la gente va (café, farmacia, gimnasio) no se diseña como un software.
- De [unslop](https://github.com/heydamir/unslop) (Damir Sokolovsky, CC BY 4.0): la **dirección en cinco líneas** sale del producto, nunca de la moda.
- De [ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) (MIT): la idea de un índice **rubro → estilo → paleta → tipografía**. Sus valores concretos (azul de confianza, Inter, glassmorphism para SaaS) **no** se copiaron: son justamente los defaults que este kit evita. Las recomendaciones de abajo son propias.

## 1. Cuatro tipos de negocio

Resumen adaptado de la tabla de taste-skill; las reglas son orientativas, el brief manda.

| Tipo | Ejemplos | Qué lidera la página | Qué no va |
|---|---|---|---|
| **Lugar** | café, panadería, farmacia, gimnasio, hotel chico, tienda | Fotos reales del lugar y de lo que se vende; dirección y horario en la segunda pantalla; una acción principal por pantalla | Shaders, escenas 3D, grano, degradés, loops. Fondos planos |
| **Servicio** | clínica, estudio jurídico, agencia, oficio | Las personas, el trabajo y los casos, en foto; quién atiende y cómo se contrata | Iconografía de stock (balanzas, estetoscopios); ilustración genérica |
| **Producto** | ropa, cosmética, muebles, comida envasada | El producto grande y entero; una foto distinta por sección; cada promesa del titular, mostrada | El producto chico en un panel gris; la misma vista dos veces |
| **Software o tech** | SaaS, devtool, fintech, hardware, juego | La interfaz real del producto, en HTML vivo y con datos plausibles; como mucho **un** efecto y uno o dos momentos | Un dashboard genérico; solo fragmentos sueltos; violeta |

Dos reglas que valen para los cuatro (también de taste-skill): **un objeto no carga con toda la página** (el producto lidera el hero y, como mucho, dos secciones más) y **los activos del cliente tienen lugar** (si hay fotos, video o capturas, cada uno tiene su marco).

## 2. La dirección en cinco líneas

Escribila antes de abrir el catálogo (formato de unslop, CC BY 4.0):

```
Producto: qué hace y para quién, en una frase
Carácter: 2–3 palabras concretas (no "limpio", "moderno", "elegante", "premium")
Mundo: el lugar o material del rubro; tiñe neutros, acento e imagen
Momento: 1–2 lugares donde va la riqueza (foto, gráfico, objeto); el resto, quieto
Firma: un detalle que solo este producto tendría, siempre igual
```

Ejemplo para una farmacia de barrio: *Producto:* farmacia con turnos de guardia y obras sociales, para vecinos del barrio. *Carácter:* claro, cercano, puntual. *Mundo:* mostrador, receta, cruz verde de la vidriera. *Momento:* el cartel de la guardia de hoy, grande y con horario. *Firma:* el horario siempre en mono tabular, como en el cartel de la puerta.

## 3. Rubro → estilo, paleta y pareja

Las paletas sugeridas combinan con al menos uno de los estilos de la fila (campo `estilos` de [`../paletas/paletas.json`](../paletas/paletas.json)). La pareja es titular + cuerpo de [`../tipografias/fonts.json`](../tipografias/fonts.json). Es un punto de partida, no una receta: si el brief o la marca dicen otra cosa, ganan.

| Rubro | Tipo | Estilos | Paletas | Pareja | Qué mostrar |
|---|---|---|---|---|---|
| Farmacia o salud de barrio | lugar | [`expresivo-minimo`](./expresivo-minimo.md), [`suizo-internacional`](./suizo-internacional.md) | `oceano-profundo`, `nordico-hielo`, `jardin-botanico` | Lexend + Source Sans 3 | Mostrador, receta, horario de turno. El dato real (horario, guardia, obras sociales) va arriba; nada de stock de médicos sonriendo. |
| Clínica o salud digital | servicio | [`ui-casi-invisible`](./ui-casi-invisible.md), [`suizo-internacional`](./suizo-internacional.md) | `oceano-profundo`, `monocromo-frio` | Lexend + Atkinson Hyperlegible | Confianza por claridad: turnos, profesionales con nombre y matrícula, sin violeta 'wellness'. |
| Back-office, caja, inventario | software | [`denso-de-datos`](./denso-de-datos.md) | `lima-mercurio`, `carbon-menta`, `monocromo-frio` | Fira Sans + Fira Code | Neutros grises, cifras tabulares, filas de 28–32 px. El color es estado, no marca. |
| SaaS B2B | software | [`estilo-linear`](./estilo-linear.md), [`saas-oscuro-premium`](./saas-oscuro-premium.md) | `lima-mercurio`, `rayo-rojo`, `oceano-profundo` | Mona Sans + JetBrains Mono | La interfaz real del producto, en HTML vivo y con datos plausibles, es el hero. |
| Devtools | software | [`catalogo-tecnico`](./catalogo-tecnico.md), [`estilo-linear`](./estilo-linear.md) | `cian-terminal`, `carbon-menta` | Mona Sans + JetBrains Mono | Mostrá lo que la herramienta toca (un diff, un log), no un dashboard genérico. |
| Cafetería, panadería, restaurante | lugar | [`organico-terroso`](./organico-terroso.md), [`risografia-impreso`](./risografia-impreso.md) | `hora-dorada`, `cafe-leche`, `teja-mar` | Abril Fatface + Merriweather | Fotos del lugar y del plato mandan; dirección y horario en la segunda pantalla. Sin efectos ni shaders. |
| Cervecería o bodegón | lugar | [`risografia-impreso`](./risografia-impreso.md), [`maximalismo`](./maximalismo.md) | `hora-dorada`, `poster-tinta` | Abril Fatface + Crimson Pro | Tipografía de cartel para el nombre, menú con precios reales. |
| Moda o lujo | producto | [`editorial-revista`](./editorial-revista.md), [`minimalismo-monocromo`](./minimalismo-monocromo.md) | `rosa-desierto`, `vino-noche`, `suizo-neutro` | Bodoni Moda + Jost | El producto grande y entero en cada sección, una foto distinta por sección. |
| Cosmética o estética | producto | [`expresivo-minimo`](./expresivo-minimo.md), [`organico-terroso`](./organico-terroso.md) | `rosa-desierto`, `durazno-tinta` | Bodoni Moda + Jost | Texturas reales del producto; nada de ilustración 3D plástica. |
| Estudio jurídico o contable | servicio | [`suizo-internacional`](./suizo-internacional.md), [`editorial-revista`](./editorial-revista.md) | `monocromo-frio`, `crema-cobalto` | Public Sans + Source Serif 4 | Personas con nombre, áreas y casos; sin martillos ni balanzas de stock. |
| Educación o universidad | servicio | [`editorial-revista`](./editorial-revista.md), [`bauhaus`](./bauhaus.md) | `crema-cobalto`, `bauhaus-primario` | Crimson Pro + Atkinson Hyperlegible | Fechas de inscripción y planes de estudio arriba; bauhaus solo para escuelas de arte o diseño. |
| Kids o juguetes | producto | [`memphis`](./memphis.md), [`claymorfismo`](./claymorfismo.md) | `memphis-pastel`, `dopamina-coral` | Fredoka + Nunito | Color en formas y patrones, nunca debajo del texto; el padre o la madre es quien compra. |
| Eventos o festivales | servicio | [`memphis`](./memphis.md), [`tipografia-kinetica`](./tipografia-kinetica.md), [`neo-brutalismo`](./neo-brutalismo.md) | `memphis-pastel`, `brutal-amarillo` | Bebas Neue + Source Sans 3 | Fecha, lugar y precio de la entrada en el primer viewport. |
| Deportes o gimnasio | lugar | [`dopamina-saturado`](./dopamina-saturado.md), [`suizo-internacional`](./suizo-internacional.md) | `dopamina-coral`, `brutal-amarillo` | Barlow Condensed + Barlow | Horarios de clases y precios reales; fotos del lugar, no de bancos de imágenes. |
| Cultura o museo | lugar | [`bauhaus`](./bauhaus.md), [`editorial-revista`](./editorial-revista.md) | `bauhaus-primario`, `suizo-neutro` | Outfit + General Sans | Agenda y entradas; las formas codifican salas o ciclos. |
| Vivero o herboristería | lugar | [`organico-terroso`](./organico-terroso.md), [`ilustrado-humano`](./ilustrado-humano.md) | `jardin-botanico`, `matcha-carbon` | Fraunces + Manrope | Plantas reales, nombres científicos y precio; nada de hojas vectoriales genéricas. |
| Logística o transporte | software | [`denso-de-datos`](./denso-de-datos.md), [`suizo-internacional`](./suizo-internacional.md) | `oceano-profundo`, `acero-seguridad` | Barlow Condensed + Barlow | Estados de envío legibles en movimiento; números grandes y tabulares. |
| Fintech o banca | software | [`ui-casi-invisible`](./ui-casi-invisible.md), [`saas-oscuro-premium`](./saas-oscuro-premium.md) | `grafito-oro`, `monocromo-frio` | IBM Plex Sans + IBM Plex Mono | Montos con formato del país, tabular-nums; sin cifras inventadas en el hero. |
| Lectura, notas o documentación | software | [`papel-e-ink`](./papel-e-ink.md) | `suizo-neutro`, `monocromo-frio` | Literata + Atkinson Hyperlegible | Una columna de 65ch, cero motion decorativo. |
| Industria o hardware | producto | [`catalogo-tecnico`](./catalogo-tecnico.md), [`espacial-3d`](./espacial-3d.md) | `acero-seguridad`, `lima-mercurio` | IBM Plex Sans + IBM Plex Mono | Fotos o render del equipo cuando el brief lo pide; ficha técnica real. |
| Inmobiliaria o arquitectura | servicio | [`minimalismo-monocromo`](./minimalismo-monocromo.md), [`suizo-internacional`](./suizo-internacional.md) | `suizo-neutro`, `monocromo-calido` | Archivo + IBM Plex Mono | La foto grande manda; filtros claros y precios visibles. |
| Turismo u hotelería | lugar | [`editorial-revista`](./editorial-revista.md), [`japones-inspirado`](./japones-inspirado.md) | `teja-mar`, `japon-sumi`, `rosa-desierto` | Libre Bodoni + Public Sans | La región y el lugar en foto; reserva y precio por noche sin vueltas. |

## 4. Antes de cerrar: la prueba de plantilla

Cambiá el nombre del producto por el de otro del mismo rubro. Si la pantalla sigue sirviendo, la dirección es débil: empujala en la copy, en la imagen y en la firma (prueba tomada de unslop).

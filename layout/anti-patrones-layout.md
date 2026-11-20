# Anti-patrones de layout + checklist

Tells de **composición** que delatan una UI generada sin criterio. Complementa el catálogo general de [`../anti-patrones/catalogo.md`](../anti-patrones/catalogo.md) (59 tells); los que ya están ahí se citan por número y no se repiten. Slugs con prefijo `L-` para que la skill los pueda nombrar.

## Catálogo

| Slug | Tell | Por qué pasa | Arreglo |
|---|---|---|---|
| `L-todo-centrado` | Cada bloque centrado: hero, headings de sección, párrafos, CTA. | Es el promedio de las landings de entrenamiento ([Orlume, oct. 2026](https://orlume.site/guides/how-to-make-an-ai-website-not-look-generic); [X, nov. 2026](https://x.com/nurnabidesigner/status/2119729679968137244)). Catálogo #16. | Alineá a la izquierda por defecto; centrá **un** bloque corto (el CTA final). Hero split 7/5 ([patrón 1](./patrones-layout.md#1-hero-split-asimétrico-75)). |
| `L-fila-de-tres-iguales` | Tres cards del mismo tamaño, una y otra vez. | La "regla de los impares" + `grid-cols-3`. Catálogo #17. | Una principal + dos de apoyo, una lista, o bento con jerarquía ([patrón 5](./patrones-layout.md#5-bento-con-jerarquía)). Quantity queries con `:has()`. |
| `L-padding-uniforme` | `py-24` en todas las secciones y `p-6` en todos los componentes. | Un valor "seguro" repetido. | Mínimo dos tamaños de sección; más aire alrededor del foco ([espaciado](./espaciado-ritmo.md#4-escala-de-padding-de-sección)). |
| `L-espacio-ambiguo` | El heading está a la misma distancia del bloque anterior que del suyo. | Se usa `space-y-*` igual para todo. | Interno < externo: más aire antes del heading, menos después ([proximidad](./espaciado-ritmo.md#2-proximidad-interno--externo)). |
| `L-sin-medida` | Párrafos de 100+ caracteres por línea (`max-w-none`, `max-w-7xl` en texto). | El contenedor de la sección se usa también para el texto. | `max-inline-size: 65ch` o `--layout-content` ([proporciones](./proporciones.md#3-medida-largo-de-línea)). |
| `L-sin-ejes` | Cada sección tiene su propio `max-w-*` y su propio borde izquierdo. | Secciones generadas por separado. | Dos o tres anchos (`content`, `wide`, `full`) y una grilla de página con líneas con nombre ([grillas](./grillas.md#21-la-grilla-de-página-con-líneas-con-nombre-full-bleed)). |
| `L-zigzag-infinito` | Filas texto/imagen alternadas 6/6 × 4 o más. | Patrón "feature rows" de plantilla. | 5/7, y cortá el ritmo a la tercera fila ([patrón 6](./patrones-layout.md#6-filas-de-feature-split-alternado-con-variación)). |
| `L-orden-de-plantilla` | hero → logos → 3 cards → testimonios → pricing → CTA. | Catálogo #18. | Ordená por la pregunta del usuario: qué es → prueba → cómo funciona → objeciones → precio. |
| `L-todo-en-cards` | Cada grupo envuelto en una card con borde y sombra; cards dentro de cards. | Catálogo #30. | Agrupá con espacio; región común solo si el espacio no alcanza ([NN/g](https://www.nngroup.com/articles/common-region/)). |
| `L-dos-focos` | Dos CTAs primarios, dos celdas hero, dos titulares display en la misma vista. | Falta de decisión. | Un foco por vista ([jerarquía](./jerarquia-composicion.md#3-punto-focal)). |
| `L-escala-tibia` | Saltos de tamaño chicos y parejos en todo (`text-4xl`/`text-xl`/`text-base`). | Clases de tutorial. | Elegí contraste alto (editorial) o bajo (producto) y sostenelo ([jerarquía](./jerarquia-composicion.md#5-contraste-de-escala)). |
| `L-breakpoint-por-componente` | `md:` y `lg:` distintos en cada componente, o `min-[913px]:`. | Se arregla cada caso por separado. | Container queries para componentes; breakpoints del kit solo para la página ([responsive](./responsive-fluido.md#1-qué-usar-en-cada-nivel)). |
| `L-reorden-visual` | `order-*` o `grid-area` que cambia el orden visual y deja el foco del teclado saltando. | Se reordena con CSS en lugar del DOM. | El DOM manda; WCAG 1.3.2 y 2.4.3 ([WCAG 2.2](https://www.w3.org/TR/WCAG22/)). |
| `L-columna-que-desborda` | Una URL o una tabla rompe la grilla; scroll horizontal en móvil. | `1fr` sin `minmax(0, …)`; falta `min-inline-size: 0` en flex. | `minmax(0, 1fr)`, `min-inline-size: 0`, `overflow-wrap: anywhere` en contenido de usuario. |
| `L-imagen-sin-ratio` | Imágenes de alturas distintas en una fila; saltos de layout al cargar. | No se fija `aspect-ratio`. | Primitivo Frame con uno o dos ratios por página ([proporciones](./proporciones.md#5-ratios-de-imagen)). |
| `L-hero-100vh` | Hero con `h-screen` que en móvil esconde el CTA bajo la barra del navegador o deja medio viewport vacío. | `100vh` por costumbre. | `min-block-size: 100svh` solo si el contenido lo justifica; si no, alto natural. |
| `L-densidad-mezclada` | Una tabla con filas de alturas distintas; un dashboard compacto con controles de 48 px. | Componentes de librerías distintas. | Una densidad por superficie ([densidad](./espaciado-ritmo.md#5-densidad)); objetivo táctil ≥ 24 px ([WCAG 2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum)). |
| `L-romper-todo` | Overlaps, rotaciones y desplazamientos en todas las secciones. | "Hacelo menos genérico" mal entendido. | Rompé **una** regla por composición ([grillas](./grillas.md#romper-la-grilla-con-criterio); [`grilla-rota`](../estilos/grilla-rota.md)). |

## Checklist de layout

Pasalo junto con [`../anti-patrones/checklist-revision.md`](../anti-patrones/checklist-revision.md). Cada **sí** es un tell; con tres o más, arreglá antes de entregar.

### Estructura
- [ ] ¿Más de la mitad de los bloques están centrados?
- [ ] ¿Hay una fila de tres (o cuatro) elementos idénticos?
- [ ] ¿El orden de secciones es el de plantilla (#18)?
- [ ] ¿Cada sección usa un `max-w-*` distinto, sin ejes compartidos?
- [ ] ¿Hay más de tres anchos de contenedor en la página?

### Espacio
- [ ] ¿Todas las secciones tienen el mismo padding vertical?
- [ ] ¿Algún heading está tan cerca del bloque anterior como del suyo?
- [ ] ¿Hay valores de espacio fuera de `--space-*` (`gap-[18px]`, `mt-[13px]`)?
- [ ] ¿Hay cards dentro de cards, o cards que solo envuelven un párrafo?

### Jerarquía
- [ ] Con la captura desenfocada 10 px, ¿no se distingue un solo foco?
- [ ] ¿Hay dos CTAs primarios en la misma vista?
- [ ] ¿Se usan más de cuatro tamaños de tipo en una pantalla?

### Medida y proporción
- [ ] ¿Algún párrafo pasa de ~75 caracteres por línea en desktop?
- [ ] ¿Las imágenes de una misma fila tienen ratios distintos sin intención?
- [ ] ¿Los splits son todos 6/6?

### Responsive
- [ ] ¿Hay scroll horizontal accidental a 320 px?
- [ ] ¿Algún componente tiene breakpoints propios que no son los del kit?
- [ ] ¿El orden visual en móvil difiere del orden del DOM?
- [ ] ¿El CTA del hero queda fuera de la primera pantalla en un móvil de 390 × 844?
- [ ] ¿Algún objetivo táctil mide menos de 24 × 24 px sin espacio alrededor?

### Gesto
- [ ] ¿No hay **ningún** gesto propio (split asimétrico, full-bleed, break de grilla, canvas grid)?
- [ ] ¿Hay **más de dos** gestos compitiendo?

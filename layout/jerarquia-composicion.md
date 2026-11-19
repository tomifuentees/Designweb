# Jerarquía y composición

Componer es decidir **qué se ve primero, segundo y tercero**, y hacer que el ojo llegue ahí sin esfuerzo. La IA no decide: reparte el mismo peso en todo (centrado, tres cards iguales, mismo padding). Este archivo es el criterio; los patrones concretos están en [`patrones-layout.md`](./patrones-layout.md).

## 1. Las tres palancas de la jerarquía

NN/g resume la jerarquía visual en **color/contraste, escala y agrupación** ([NN/g, Visual Hierarchy](https://www.nngroup.com/articles/visual-hierarchy-ux-definition/)):

1. **Escala.** No más de tres tamaños protagonistas por vista (chico, mediano, grande). El kit tiene nueve pasos de tipo, pero en una pantalla se usan tres o cuatro.
2. **Contraste.** No más de tres variaciones de contraste en un diseño complejo: "si todo contrasta, nada se destaca". Lo que crea jerarquía es la diferencia de valor y saturación respecto del contexto, no el color en sí.
3. **Agrupación.** Proximidad y región común (ver [`espaciado-ritmo.md`](./espaciado-ritmo.md)).

Refactoring UI agrega dos herramientas de oficio: **des-enfatizar** lo secundario en lugar de agrandar lo principal, y usar **peso y color** antes que tamaño ([refactoringui.com](https://refactoringui.com/); [resumen](https://maibuith.com/notes/refactoring-ui)).

### Test del entrecerrado (squint test)

Desenfocá la captura 5–10 px. Si no se distinguen los grupos y un solo foco, la jerarquía falla. NN/g muestra que a 20 px de blur aparece la jerarquía *no intencional* (un ítem con color fuerte que roba el foco) ([NN/g](https://www.nngroup.com/articles/visual-hierarchy-ux-definition/)).

## 2. Patrones de lectura: F, Z y lo que dice la evidencia

- **Patrón F:** NN/g lo documentó en 2006 (232 usuarios, eyetracking) y lo reconfirmó en 2017. Aparece cuando el texto **no tiene estructura** (sin subtítulos, bullets, negritas); es **malo** para usuarios y negocio, y el buen formato lo evita ([NN/g, 2017](https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/); [original](https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content-discovered/)).
- **Hay otros patrones:** *layer-cake* (se leen los headings y se saltea el cuerpo, el más eficiente), *spotted*, *marking* (más en móvil), *bypassing*, *commitment* ([NN/g, Text Scanning Patterns](https://www.nngroup.com/articles/text-scanning-patterns-eyetracking/); [Layer-cake](https://www.nngroup.com/articles/layer-cake-pattern-scanning/)). En idiomas de derecha a izquierda la F se espeja.
- **Patrón Z:** es una heurística de composición de landings (logo → nav → diagonal → CTA), **no** un hallazgo de eyetracking de NN/g. Usalo como guía para páginas con poco texto, no como ley.

**Conclusión de diseño:** no "diseñes para la F". Diseñá para el *layer-cake*: headings que dicen algo, primeras palabras con carga, bullets, y lo importante arriba y a la izquierda (en LTR).

## 3. Punto focal

Un punto focal por vista. Se crea con **una** de estas diferencias, no con todas:

- Tamaño (el titular display, la captura grande).
- Contraste (el único bloque oscuro en una página clara; el único acento).
- Aislamiento (espacio vacío alrededor).
- Dirección (miradas, flechas, líneas de la grilla que convergen).
- Movimiento (solo si [`../animaciones/`](../animaciones/README.md) lo justifica).

Si hay dos focos que pelean (dos CTAs primarios, dos celdas "hero" en un bento), no hay jerarquía. Ya está como error en [`../estilos/bento-grids.md`](../estilos/bento-grids.md).

## 4. Alineación

- **Pocas líneas de alineación.** Cada borde izquierdo nuevo es una línea más que el ojo tiene que registrar. Una página de calidad tiene dos o tres ejes verticales que se repiten de sección en sección.
- **Alineado a la izquierda por defecto** para texto de más de dos líneas: el centrado obliga a buscar el inicio de cada línea. Centrá solo bloques cortos (un titular de 1–2 líneas, un CTA final).
- **Alineación óptica:** íconos, comillas y letras redondas (O, C) se ven corridas si se alinean matemáticamente; corré a ojo 1–2 px o usá `hanging-punctuation` donde haya soporte.
- **Anclá el texto a la grilla de arriba.** El párrafo de la sección 3 debería empezar en la misma columna que el titular del hero.

Steve Schoger, rediseñando una landing con Claude Code, reemplaza el hero centrado por un split 3/5–2/5 alineado arriba: titular a la izquierda, bajada y CTA a la derecha ([*Designing with Claude Code*, marzo 2026](https://www.youtube.com/watch?v=lkKGQVHrXzE); [resumen](https://www.yedapo.com/episode/479ceaf7-1088-418a-894a-a835f14337a0/steve-schoger-designing-with-claude-code/insights)).

## 5. Contraste de escala

La diferencia entre "plantilla" y "diseñado" suele ser la **distancia** entre niveles. Un `h1` de 40 px sobre un cuerpo de 16 es una razón 2,5:1; un display de 72 px sobre cuerpo de 18 es 4:1. Elegí una de dos actitudes:

- **Contraste alto** (display enorme + cuerpo chico, mucho aire): editorial, marca, portfolio.
- **Contraste bajo** (pasos chicos, más peso y color): producto, dashboard, docs.

Lo que no funciona es el medio tibio en todo: `text-4xl` + `text-lg` + `text-base` sin que nada mande.

## 6. Espacio en blanco

El espacio vacío es **activo**: aísla el foco y agrupa. Refactoring UI: empezá con demasiado y reducí ([capítulo](https://archive.org/stream/RefactoringUIStartWithTooMuchWhiteSpace/Refactoring%20UI%20-%20Start%20with%20too%20much%20white%20space_djvu.txt)). Pero el aire **uniforme** también es un tell: en r/web_design se cita el espaciado "demasiado parejo, donde nada atrae la mirada" como señal de IA (ver [`../estilos/grilla-rota.md`](../estilos/grilla-rota.md)). El blanco tiene que tener **ritmo**: más alrededor de lo importante, menos entre lo relacionado.

## 7. Equilibrio

- **Simétrico:** formal, estable, institucional. Funciona en un CTA final o una página de precios comparativa.
- **Asimétrico:** un bloque pesado (imagen, titular) balanceado por varios livianos o por espacio vacío. Más tensión, más editorial. Es el default recomendado para heros.
- **Peso visual** sube con: tamaño, oscuridad/saturación, textura, aislamiento, posición alta. Un bloque chico pero muy oscuro equilibra uno grande y claro.

## 8. Regla de los impares (y por qué no es ley)

La "regla de los impares" (3 o 5 elementos se ven más dinámicos que 2 o 4) viene de fotografía y composición pictórica. **No encontramos evidencia empírica sólida para UI**; tomala como heurística. Además, en web es justamente la que produce el tell de **tres cards idénticas** ([`../anti-patrones/catalogo.md`](../anti-patrones/catalogo.md), #17). Si usás tres, que no pesen lo mismo: una principal y dos de apoyo, o una lista en lugar de cards.

## 9. Gestalt aplicada a UI

| Principio | En UI | Error típico |
|---|---|---|
| **Proximidad** | Espacio interno < externo ([NN/g](https://www.nngroup.com/articles/gestalt-proximity/)) | Heading equidistante de dos bloques |
| **Región común** | Fondo o borde compartido agrupa ([NN/g](https://www.nngroup.com/articles/common-region/)) | Card en cada párrafo; cards dentro de cards |
| **Similitud** | Mismo estilo = misma función (todos los links iguales) | Botón secundario que parece primario |
| **Continuidad** | Elementos alineados en una línea se leen como secuencia | Pasos de un proceso que zigzaguean |
| **Cierre** | El ojo completa formas; un carrusel cortado sugiere "hay más" | Scroll horizontal sin pista de que sigue |
| **Figura / fondo** | Modal, popover, sticky sobre contenido | Overlay sin contraste suficiente |
| **Destino común** | Lo que se mueve junto, va junto | Animaciones de entrada sin relación con la agrupación |

NN/g también tiene un resumen de los cinco principios de diseño visual en UX (escala, jerarquía, equilibrio, contraste, Gestalt) ([NN/g](https://www.nngroup.com/articles/principles-visual-design/)).

## 10. Primera impresión

La impresión de belleza se forma en ~50 ms y se mantiene estable ([Lindgaard et al., 2006](https://doi.org/10.1080/01449290500330448)); las páginas **simples** (baja complejidad) y **prototípicas** (que se parecen a lo que se espera de su categoría) salen mejor puntuadas ([Tuch et al., Google, 2012](https://research.google/pubs/the-role-of-visual-complexity-and-prototypicality-regarding-first-impression-of-websites-working-towards-understanding-aesthetic-judgments/)).

Traducción para este kit: **la estructura** puede ser convencional (nav, hero, prueba, CTA en lugares esperables); **la diferencia** va en el tipo, el color, el contenido real y un gesto de composición. Ser raro en la estructura cuesta comprensión; ser genérico en todo cuesta identidad.

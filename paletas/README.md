# Paletas

Catálogo de paletas con tokens de rol, armado en noviembre de 2026. El objetivo no es un moodboard de colores lindos: es que un agente de código deje de improvisar un degradé índigo-violeta, un `bg-indigo-500` y un gris “que más o menos contrapone”, y trabaje con **roles** (fondo, superficie, borde, texto, muted, acento, estados) en claro y en oscuro, con valores en OKLCH y hex, y con el contraste medido.

Esta carpeta se lee junto a [`../estilos/`](../estilos/README.md) y [`../tipografias/`](../tipografias/README.md). Las escalas de espacio, radio, sombra y tipo están en [`../tokens/`](../tokens/README.md). Las señales de “AI slop” que estas paletas ayudan a cortar están en [`../anti-patrones/`](../anti-patrones/README.md).

Hay **41 paletas** (35 originales y 6 sumadas el 20 de noviembre de 2026; ver [`../recursos/minado-repos.md`](../recursos/minado-repos.md)). Cada una trae modo claro y oscuro, tokens de rol (incluido `accent-text` para links), contraste WCAG 2.1 y APCA-W3, estilos del catálogo con los que combina y un bloque CSS listo para pegar. Ninguna usa el degradé violeta-índigo como identidad. Una sola —[cera suave](./culturales.md)— tiene un violeta sólido, y está marcada como nicho de claymorfismo, no como default.

> **Ojo con el crema.** 19 de las 35 paletas originales tienen en modo claro un fondo cálido crema o beige. En noviembre de 2026 la skill oficial de Anthropic e [impeccable](https://github.com/pbakaus/impeccable) marcan ese fondo (sobre todo con serif display y acento terracota) como el nuevo default de IA. Usalas cuando el rubro es papel, materia o editorial, no por reflejo (ver `crema-por-reflejo` en [`../anti-patrones/catalogo.md`](../anti-patrones/catalogo.md)). Las 6 paletas nuevas no usan fondo crema. Para elegir por rubro, mirá [`../estilos/direccion-por-rubro.md`](../estilos/direccion-por-rubro.md).

## Qué hay acá

| Archivo | Contenido |
|---|---|
| [saas-producto.md](./saas-producto.md) | 7 paletas de producto: lima, rojo de comando, cian de terminal, oro, señal, menta, océano profundo |
| [editoriales.md](./editoriales.md) | 5 paletas de papel y tinta: crema, diario, riso, pergamino, cobalto de sello |
| [organicas.md](./organicas.md) | 7 paletas de materia: terracota, oliva, café, cobre, matcha, jardín botánico, hora dorada |
| [monocromas.md](./monocromas.md) | 4 paletas quietas: suizo neutro, cálido, frío, hueso y ocre |
| [expresivas.md](./expresivas.md) | 6 paletas altas: brutal amarillo, dopamina coral, Y2K cromo, póster, bauhaus primario, memphis pastel |
| [culturales.md](./culturales.md) | 12 paletas de nicho: sumi, nórdico, vino, bosque, arcilla, durazno, acero, arena, teja, niebla, cera, rosa del desierto |
| [herramientas.md](./herramientas.md) | Generadores y pickers verificados en 2025–2026 (OKLCH, Radix, tweakcn, shadcn, Huemint, etc.) |
| [evadir-degrade-violeta.md](./evadir-degrade-violeta.md) | Por qué la IA cae en el índigo y cómo no dejarla |
| [paletas.json](./paletas.json) | El mismo catálogo, legible por máquinas |
| [fuentes-investigacion.md](./fuentes-investigacion.md) | Fuentes consultadas, con links y fechas |

## Cómo está armada cada paleta

Roles (los que pide un sistema de producto, no una lista de cinco hex sueltos):

- `bg`, `surface`, `border`
- `text`, `muted`
- `accent` (relleno sólido: botones, chips) y `accent-foreground` (el texto/ícono encima)
- `accent-text` (el mismo matiz, calibrado para usarse como link o texto sobre el fondo)
- `success`, `warn`, `danger` (como color de texto/ícono sobre `bg`; si los usás en sólido, chequeá el foreground)

Valores en **OKLCH** (el espacio que adoptaron Tailwind CSS v4, el 22 de enero de 2025, y shadcn/ui al pasar de HSL a OKLCH) y en **hex** de respaldo. El contraste se midió de dos maneras:

- **WCAG 2.1** contraste relativo, con 4.5:1 como piso para cuerpo y para `accent-foreground` sobre `accent`.
- **APCA-W3** (Lc). El cuerpo de estas fichas cumple |Lc| ≥ 60; el objetivo de lectura seguida es 75 o más (90 para texto chico exigente, según la documentación de APCA). APCA es sensible a la polaridad: un número negativo es texto claro sobre fondo oscuro.

Si `accent` no llega a 4.5:1 como texto sobre el fondo (pasa seguido con amarillos, naranjas y rojos de botón), la ficha lo dice: el botón usa `accent` + `accent-foreground`, el link usa `accent-text`.

## Cómo elegir una paleta

1. **Primero el trabajo, después el color.** ¿Es un SaaS oscuro, una editorial, una PyME local, un zine, un catálogo técnico? Empezá por el [estilo](../estilos/README.md) y recién ahí abrí el grupo de paletas que le corresponde.
2. **Un acento, no un arcoíris.** La regla 70-30-10: el fondo y la superficie son el 70, los neutros de apoyo el 30, el acento el 10. “Rainbow vomit” es uno de los tells de slop más citados en 2026 ([Desai, 27 de septiembre](https://godobject.dev/blog/10-tells-of-slop/)).
3. **Sacá el acento del tema, no de Tailwind.** Una panadería no pide índigo; pide corteza. Un devtool puede pedir lima o cian, no un halo violeta detrás del hero. Ver [evadir el degradé violeta](./evadir-degrade-violeta.md).
4. **Medí el contraste, no lo adivines.** Un gris “bonito” sobre `#111` suele fallar. Muted por debajo de 4.5:1 no va en cuerpo.
5. **El modo oscuro no es invertir el claro.** El acento sólido en oscuro a menudo hay que oscurecerlo para que el texto blanco cumpla APCA; el link (`accent-text`) se aclara. Por eso vienen los dos.
6. **No uses esta carpeta como un menú de diez opciones para el usuario.** Proponé una paleta (o una + un acento alternativo) y explicá por qué.

## Cómo usarlo desde un agente

1. Leé este README y [evadir-degrade-violeta.md](./evadir-degrade-violeta.md).
2. Según el estilo elegido en [`../estilos/estilos.json`](../estilos/estilos.json), abrí el grupo o `paletas.json` y proponé **una** paleta.
3. Pegá los tokens CSS (claro + `.dark`). Mapealos a las escalas de [`../tokens/`](../tokens/README.md). No inventes hex sueltos en los componentes.
4. No presentes índigo, violeta ni un degradé `#667eea → #764ba2` (o `from-indigo-500 to-purple-600`) como primera opción, salvo que el brief lo pida de forma explícita.
5. Si el usuario ya tiene un color de marca, no lo reemplaces: construí una rampa de roles alrededor (herramientas en [herramientas.md](./herramientas.md), empezando por el picker OKLCH de Evil Martians o por Radix Colors).

La vigencia es una foto del 19 de noviembre de 2026. Un acento “distinto” hoy puede ser el cliché de mañana: el cream + terracota pastel ya está en esa frontera.

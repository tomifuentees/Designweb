# Memphis

El Grupo Memphis (Milán, 1981, Ettore Sottsass y compañía) dejó patrones de squiggles, confeti, laminados de colores imposibles y formas que no se toman en serio. En web vuelve en marcas jóvenes, eventos, kids, música y campañas, casi siempre como **patrón y acento** sobre una base calma. [ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) (MIT) lo tiene catalogado como estilo activo; esta ficha es propia.

## Cuándo usarlo y cuándo no

**Usalo** en eventos, festivales, marcas de golosinas o juguetes, educación infantil, música, campañas de temporada y portfolios de ilustración.

**No lo uses** en salud, finanzas, legal, B2B ni en formularios largos. Tampoco como fondo detrás de texto de lectura: el patrón se come la legibilidad.

## Reglas concretas

- **Grilla:** convencional por debajo. Lo loco es la superficie, no la estructura.
- **Espaciado:** generoso; el patrón necesita aire alrededor para no volverse ruido.
- **Radios:** mezcla deliberada de formas (círculo, medialuna, rectángulo), cada una con su radio fijo.
- **Bordes:** negro de 2–3 px en formas y stickers.
- **Sombras:** dura y sin blur si hay, como en el neo-brutalismo; o ninguna.
- **Color:** pasteles saturados (rosa chicle, menta, amarillo pollito, celeste) con negro y uno o dos tonos fuertes. Texto siempre sobre fondo liso.
- **Patrones:** squiggles, confeti, grilla de puntos, zigzag. Uno o dos por página, en SVG propio, nunca detrás de párrafos.
- **Tipografía:** display redonda o geométrica con humor; cuerpo calmo.
  - Titular: [Unbounded](../tipografias/display-experimental.md), [Syne](../tipografias/display-experimental.md) o [Clash Display](../tipografias/display-experimental.md).
  - Cuerpo / UI: [DM Sans](../tipografias/sans-geometrica.md) o [Outfit](../tipografias/sans-geometrica.md).
  - Acento manuscrito: [Shantell Sans](../tipografias/display-experimental.md).

## Sitios reales

- [memphis-milano.com](https://memphis-milano.com/) — la casa original (respondió 202 al verificar; puede pedir JS).
- [camillewalala.com](https://www.camillewalala.com/) — Camille Walala, murales y espacios en clave Memphis contemporánea.
- [nathaliedupasquier.com](https://www.nathaliedupasquier.com/) — Nathalie Du Pasquier, una de las autoras de los patrones del grupo.
- [adamnathanielfurman.com](https://www.adamnathanielfurman.com/) — posmodernismo de color, pariente directo.

## Errores comunes

- Patrón detrás del texto. Siempre fondo liso bajo la copy.
- Seis pasteles con el mismo peso: sin un negro y un tono fuerte, todo se aplana.
- Squiggles de stock genéricos o SVG armados con formas primitivas sin oficio (ver `ilustracion-de-formas-primitivas` en ../anti-patrones/catalogo.md).
- Aplicarlo a la app entera: va en marketing y en momentos, no en la tabla de pedidos.

## Snippet

```html
<section class="relative overflow-hidden bg-[#fff7ec] px-8 py-20 font-[DM_Sans]">
  <svg class="pointer-events-none absolute -right-6 top-6 w-48" viewBox="0 0 200 40" aria-hidden="true">
    <path d="M0 20 Q 12.5 0 25 20 T 50 20 T 75 20 T 100 20 T 125 20 T 150 20 T 175 20 T 200 20" fill="none" stroke="#111" stroke-width="5"/>
  </svg>
  <span class="absolute bottom-10 right-24 size-16 rounded-full border-[3px] border-[#111] bg-[#ff8fb1]" aria-hidden="true"></span>
  <div class="relative max-w-xl rounded-none bg-[#fff7ec]">
    <h1 class="font-[Unbounded] text-5xl font-bold leading-tight text-[#111]">Feria del juguete, 6 y 7 de diciembre</h1>
    <p class="mt-4 text-lg text-[#2a2a2a]">Plaza 9 de Julio, de 16 a 21. Entrada libre.</p>
    <a href="#programa" class="mt-8 inline-block border-[3px] border-[#111] bg-[#7fe0c3] px-6 py-3 font-semibold shadow-[5px_5px_0_0_#111] focus-visible:outline-4 focus-visible:outline-[#111]">Ver el programa</a>
  </div>
</section>
```

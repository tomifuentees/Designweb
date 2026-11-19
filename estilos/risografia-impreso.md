# Risografía / impreso

filtercoffee.dev lo lista entre los estilos vivos: grano de tinta, paletas cortas (dos o tres tintas de riso), registro un poco corrido, sabor a fanzine y a imprenta pequeña. Es un nicho editorial, no una tendencia de mass SaaS, pero en 2026 gana sentido como contrapeso al pulido de IA: la mancha es un rasgo, no un defecto. Convive con [grano](./grano-ruido.md), con [anti-diseño](./anti-diseno.md) y con lo [ilustrado](./ilustrado-humano.md). Byline y otras piezas “dial-up” (Wix) a veces rozan este clima, aunque vengan de otro lado (early web, no taller).

No es un filtro Instagram “riso” sobre una foto de stock. Es una paleta limitada y una lógica de capas (una tinta, otra tinta, un overlap).

## Cuándo usarlo y cuándo no

**Usalo** en editoriales independientes, cafés, cultura, música, zines, portfolios de gráfica, campañas de un evento.

**No lo uses** en un producto de datos, en un checkout, ni si vas a simularlo con un overlay sucio sobre Inter y un layout de tres cards.

## Reglas concretas

- **Grilla:** Puede ser de afiche (un titular enorme, un márgen de taller) o de interior de libro (dos columnas, un folio). El registro “corrido” es un acento (1–2 px), no un layout entero desalineado.
- **Espaciado:** Tipo taller: márgenes irregulares pero repetidos. Un folio (número de página) visible queda bien.
- **Radios:** 0. La esquina viva es de papel cortado, no de card.
- **Bordes:** Pueden no existir, o ser un filete de una sola tinta.
- **Sombras:** No. La superposición de tintas (multiply) hace el trabajo.
- **Color:** Dos o tres tintas planas, típicas de riso: un rosa flúo, un azul, un negro, un mostaza. Fondos papel (`#f3ecd9`). Superposición con `mix-blend-mode: multiply`. Evitá degradés suaves y el índigo de UI kit.
- **Tipografía:** Un poco tosca o de taller.
  - [Karrik](../tipografias/display-experimental.md), [Sprat](../tipografias/display-experimental.md), [Obviously](../tipografias/display-experimental.md), [Zodiak](../tipografias/serif-display.md), [Bricolage Grotesque](../tipografias/sans-grotesk.md).
  - Folio y ficha: [Space Mono](../tipografias/mono.md).

## Sitios reales

No todas las editoriales independientes tienen un “look riso” literal en la web; se citan referentes de clima impreso / tinta, no un directorio de imprentas:

- [www.itsnicethat.com](https://www.itsnicethat.com/) — editorial de diseño, cercana al mundo de la gráfica y la imprenta.
- [www.bylinebyline.com](https://www.bylinebyline.com/) — cultura impresa / early web, paleta y actitud de zine más que de producto.
- [basement.studio](https://basement.studio/) — a menudo trabaja campañas con textura y tipo de afiche.
- [www.graza.co](https://www.graza.co/) — gráfica de envase y de tinta, paleta corta, no un UI kit.

## Errores comunes

- Un filtro de “halftone” a 40% sobre una foto de Unsplash y un botón de Tailwind.
- Seis tintas “porque queda más rico”: deja de ser riso.
- Texto en overlap multiply que ya no se lee.
- Aplicarlo a un form de signup con validaciones: el usuario necesita claridad, no taller.

## Snippet

Dos tintas en multiply, Zodiak + Space Mono, papel.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=zodiak@600&display=swap">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Space+Mono&display=swap" rel="stylesheet">
  <style>
    body { font-family: "Zodiak", serif; background: #f3ecd9; color: #1a1a1a; }
    .tinta { mix-blend-mode: multiply; }
    .folio { font-family: "Space Mono", ui-monospace, monospace; }
  </style>
</head>
<body class="min-h-screen px-8 py-10">
  <p class="folio text-xs">nº 07 · taller</p>
  <div class="relative mt-8 max-w-3xl">
    <h1 class="text-6xl md:text-8xl leading-[0.9] font-semibold">Tinta sobre tinta.</h1>
    <div class="tinta absolute -top-4 right-4 w-40 h-40 rounded-full bg-[#ff5ca8]"></div>
    <div class="tinta absolute top-16 right-16 w-40 h-40 rounded-full bg-[#2f5cff]"></div>
  </div>
  <p class="folio mt-24 max-w-sm text-sm">Dos tintas, un overlap, papel. El registro puede correrse un milímetro, no un layout entero.</p>
</body>
</html>
```

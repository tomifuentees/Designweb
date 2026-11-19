# Neo-brutalismo

El neo-brutalismo web toma del brutalismo la franqueza (bordes visibles, tipografía gruesa, poco modelado) y le suma color alto, stickers y una sombra dura, sin blur, desplazada unos píxeles. The Plus Addons, en 2026, lo describe con precisión: como *look de página completa* está en enfriamiento fuera de marcas consumer y creator, porque el ruido trabaja en contra de categorías que convierten por confianza. Como *acento*, en cambio, está vivo: un solo CTA con borde grueso y sombra hard-offset dentro de un sistema convencional.

Listas de enero de 2026 (NeoBrutalism Blog) todavía apuntan a Gumroad, Feastables o Roze Bunker. Antes de copiar uno, mirá el estado actual del sitio: son referentes de un ciclo que ya no es el default.

## Cuándo usarlo y cuándo no

**Usalo** en campañas, snacks, música, educación informal, portfolios con actitud, o como un único botón / badge dentro de un layout calmado (un dashboard puede tener *un* CTA brutalista).

**No lo uses** en salud, banca, trámites, legal, ni en un SaaS B2B que necesita parecer sólido. Tampoco como tema de un dashboard o de un formulario largo: la fatiga visual llega rápido. Si la marca ya es ruidosa en el logo y en la foto, el UI no tiene que gritar el doble.

## Reglas concretas

- **Grilla:** Puede ser rígida y visible (columnas con gap gordo) o un poco desprolija, pero las cajas se alinean. El caos total es anti-diseño, no neo-brutalismo.
- **Espaciado:** Gutters grandes y parejos (20–32 px). El peso está en el borde, no en el aire infinito.
- **Radios:** 0 px, o un radio chico y constante (4–8 px) tipo sticker. Nada de pills en todos los botones.
- **Bordes:** 2–4 px sólidos, casi siempre negro o un color muy oscuro. El borde es ornamento y estructura.
- **Sombras:** `box-shadow: 4px 4px 0 0 #111` (o 6–8 px). Cero blur. En hover, la caja se “aprieta” hacia su sombra (trasladás 2 px y acortás el offset), no se eleva con una sombra suave.
- **Color:** Paletas cortas y saturadas, a menudo planas: un amarillo, un rosa, un azul eléctrico, un negro y un crema. Evitá degradés violetas: no es el idioma.
- **Tipografía:** Display tosca o una grotesca con carácter, a menudo en boxy y con tracking apretado.
  - Titular: [Clash Display](../tipografias/display-experimental.md), [Bricolage Grotesque](../tipografias/sans-grotesk.md), [Syne](../tipografias/display-experimental.md), [Unbounded](../tipografias/display-experimental.md) o [Karrik](../tipografias/display-experimental.md).
  - Cuerpo / UI: [Space Grotesk](../tipografias/sans-geometrica.md) o [Cabinet Grotesk](../tipografias/sans-grotesk.md).
  - Acento: [Space Mono](../tipografias/mono.md).
  - [GT Maru](https://gt-maru.com/) (Grilli, comercial, no está en el catálogo del kit) aparece en el circuito neo-brutalista como specimen; no la inventes en un snippet gratis.

## Sitios reales

- [gumroad.com](https://gumroad.com/) — ejemplo clásico, todavía listado en enero de 2026. Confirmá el estado visual actual antes de tomarlo como foto fiel.
- [feastables.com](https://feastables.com/) — NeoBrutalism Blog lo cita por botones chunky y gráficos tipo sticker, apuntado a una audiencia joven.
- [rozebunker.nl](https://rozebunker.nl/) — marca de bebidas, neón y layout bold (GET 202, sitio vivo).
- [gt-maru.com](https://gt-maru.com/) — specimen de GT Maru; sirve como referencia de tipo + color, no como “producto SaaS brutalista”.

## Errores comunes

- Aplicarlo a *todas* las superficies de un producto serio y después “suavizarlo” con sombras blur: queda un híbrido barato.
- Más de cuatro colores saturados + stock stickers + emoji. El estilo pide paleta corta y gráficos propios.
- Sombra con blur “para que se lea mejor”. Si tiene blur, ya no es este idioma.
- Contraste flojo (amarillo sobre blanco, o neón sobre neón): el estilo es ruidoso, no inaccesible.
- Copiar Gumroad para una fintech o una farmacia.

## Snippet

Un bloque de campaña con CTA de acento. La sombra es dura; el hover la aprieta.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&family=Space+Grotesk:wght@400;500&display=swap" rel="stylesheet">
  <style>
    body { font-family: "Space Grotesk", sans-serif; background: #f6f1e8; }
    h1 { font-family: "Bricolage Grotesque", sans-serif; }
    .hard { box-shadow: 6px 6px 0 0 #111; transition: transform .12s, box-shadow .12s; }
    .hard:hover, .hard:focus-visible { transform: translate(3px, 3px); box-shadow: 3px 3px 0 0 #111; }
  </style>
</head>
<body class="min-h-screen p-6 md:p-12 text-neutral-900">
  <main class="max-w-3xl mx-auto border-4 border-neutral-900 bg-[#ffd84a] p-8 md:p-12 hard">
    <p class="text-sm font-medium uppercase tracking-wide">Campaña · no un dashboard</p>
    <h1 class="mt-4 text-5xl md:text-7xl leading-[0.95] font-extrabold">Borde grueso. Sombra dura. Un color que se banca el grito.</h1>
    <p class="mt-6 text-lg max-w-md">Si todo el sitio grita, no queda acento. Este bloque sirve como excepción, no como tema.</p>
    <a href="#" class="inline-block mt-8 border-4 border-neutral-900 bg-[#ff5c8a] px-6 py-3 text-lg font-bold hard">Pedir uno</a>
  </main>
</body>
</html>
```

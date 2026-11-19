# Editorial / revista

Toimi describe en 2026 una bifurcación clara: de un lado el SaaS techno-futurista (oscuro, acento, bento, shaders); del otro, el contrapeso editorial (crema, serif, calor, whitespace de lectura). El estilo revista no es “poner Instrument Serif a 80 px sobre un hero de startup”. Es jerarquía de publicación: un titular que ocupa el ancho, una bajada, una imagen con pie, columnas de lectura, un ritmo entre pasajes cortos y largos.

filtercoffee.dev apunta a The Gentlewoman y It's Nice That. En r/web_design ya advierten que Instrument Serif, usada como atajo “editorial” de un SaaS, es de las tendencias que peor van a envejecer.

## Cuándo usarlo y cuándo no

**Usalo** en medios, agencias, marcas con historia, lujo callado, landings donde hay algo para leer (un manifiesto, casos, un ensayo) y e-commerce que vende con relato (moda, comida, objetos).

**No lo uses** en un dashboard, en un onboarding de cinco pasos o en un SaaS que no tiene texto de verdad. Tampoco como disfraz: un pricing de tres columnas con una serif arriba sigue siendo una plantilla de IA.

## Reglas concretas

- **Grilla:** Más cercana a una revista que a un UI kit: 2 o 3 columnas, o una columna de lectura (62–75 caracteres) con una marginalia. Los titulares pueden romper la columna y ocupar el ancho.
- **Espaciado:** El ritmo lo marca la lectura. Más aire arriba de un H1 que entre párrafos. No todas las secciones miden lo mismo.
- **Radios:** 0–4 px en imágenes y reglas. Las fotos se recortan con criterio, no con `rounded-3xl`.
- **Bordes:** Filetes finos, a veces en un color de tinta (negro cálido, marrón, rojo de revista). Separadores tipográficos (una línea, un número de sección) antes que cards.
- **Sombras:** Casi no. Si hay, es la de un papel (muy corta, cálida), no un drop shadow de Tailwind por default.
- **Color:** Fondos crema, papel, arena (`#f4efe6`, `#f7f3ec`), tinta oscura cálida (no un gris frío `#111`). Un acento de tinta: rojo, verde oscuro, azul de imprenta. Evitá el violeta de SaaS.
- **Tipografía:** Una serif de titular y una serif de texto *o* una grotesca quieta para UI y captions.
  - Titular: [Fraunces](../tipografias/serif-display.md) (mejor con optical size), [Zodiak](../tipografias/serif-display.md), [Boska](../tipografias/serif-display.md), [Editorial New](../tipografias/serif-display.md), [Signifier](../tipografias/serif-display.md), [Reckless](../tipografias/serif-display.md) o [Tiempos Headline](../tipografias/serif-display.md).
  - Cuerpo: [Newsreader](../tipografias/serif-texto.md), [Source Serif 4](../tipografias/serif-texto.md), [Tiempos Text](../tipografias/serif-texto.md) o [Literata](../tipografias/serif-texto.md).
  - UI / nav: [Switzer](../tipografias/sans-grotesk.md), [Söhne](../tipografias/sans-grotesk.md) o [Untitled Sans](../tipografias/sans-grotesk.md).
  - Instrument Serif solo si el brief lo pide, y no en una landing de software. Ver las reglas anti-genéricas de [tipografías](../tipografias/README.md).

## Sitios reales

- [thegentlewoman.co.uk](https://thegentlewoman.co.uk/) — filtercoffee.dev lo cita como referencia de jerarquía revista (tipo + fotografía).
- [www.itsnicethat.com](https://www.itsnicethat.com/) — publicación de diseño, ritmo entre titular, imagen y cuerpo.
- [www.wired.com](https://www.wired.com/) — editorial digital contemporánea; el catálogo de tipografías la asocia a Aperçu.
- [www.kinfolk.com](https://www.kinfolk.com/) — revista / lifestyle con paleta papel y fotografía contenida (el dominio desnudo redirige a `www`).

## Errores comunes

- Instrument Serif o Playfair a tamaño hero + Inter en la bajada + un degradé. Es el cliché que el kit existe para evitar.
- Envolver cada párrafo en una card.
- Medir todas las secciones igual, como un landing page builder.
- Cuerpo en display de alto contraste a 16 px en mobile: ilegible. Usá una serif de texto, o optical size.
- Fondos blanco óptico y negros azulados: se pierde el calor de “papel”.

## Snippet

Apertura de artículo: Fraunces + Newsreader sobre crema, un filete, sin cards.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Newsreader:opsz,wght@6..72,400;6..72,500&display=swap" rel="stylesheet">
  <style>
    body { font-family: "Newsreader", serif; background: #f4efe6; color: #241e18; }
    h1 { font-family: "Fraunces", serif; font-optical-sizing: auto; }
  </style>
</head>
<body class="min-h-screen">
  <article class="max-w-3xl mx-auto px-6 py-16 md:py-24">
    <p class="text-xs tracking-[0.2em] uppercase text-[#7a3b2e]">Ensayo · Nº 14</p>
    <h1 class="mt-4 text-5xl md:text-7xl leading-[1.05] font-medium">La página se lee, no se recorre como un pricing.</h1>
    <p class="mt-8 text-xl md:text-2xl leading-snug text-[#3a3128]">Una bajada de una o dos líneas. Después, el cuerpo a un ancho de lectura y una foto con pie, no con sombra.</p>
    <hr class="mt-10 mb-10 border-[#241e18]/20">
    <p class="text-lg leading-8">El contrapeso editorial existe porque el SaaS oscuro se volvió un dialecto. Si hay historia, dejá que la tipografía y el papel la lleven. Si no hay texto de verdad, este estilo no tiene nada que hacer.</p>
    <figure class="mt-12">
      <div class="aspect-[16/9] bg-[#d9cfc0]"></div>
      <figcaption class="mt-3 text-sm text-[#5a5046]">Pie de foto. El archivo, el lugar, la fecha — no un caption genérico.</figcaption>
    </figure>
  </article>
</body>
</html>
```

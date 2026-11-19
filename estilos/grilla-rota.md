# Grilla rota / layouts orgánicos

Envato, en marzo de 2026, lo pone junto a la tipo cinética como uno de los gestos del año: salir de la grilla de 12 columnas que, de tan usada, hace que los sitios se parezcan aunque el contenido no. Habla de composiciones asimétricas, overlaps, formas irregulares, diagonales, spacing inesperado — no de caos por el caos, sino de una composición *considerada*. Es distinto del [anti-diseño](./anti-diseno.md) (que exhibe crudeza) y del [bento](./bento-grids.md) (que es una grilla, solo que de mosaicos). Acá la grilla puede existir por debajo, y una pieza se sale, se monta, o desobedece una columna.

En r/web_design, una de las señales de UI de IA es justamente lo contrario: un spacing *demasiado* parejo, donde nada atrae la mirada.

## Cuándo usarlo y cuándo no

**Usalo** en portfolios, agencias, landings culturales, editoriales, héroes de campaña, una sección (no necesariamente todo el sitio).

**No lo uses** en un checkout, en un dashboard o en un artículo largo de 4000 palabras (la lectura larga pide una columna estable). En mobile, la ruptura se simplifica: overlap de dos piezas, no de seis.

## Reglas concretas

- **Grilla:** Partí de una grilla real (12 o 8) y rompé *una* regla por composición: un titular que entra en negativo, una foto que pisa al tipo, un módulo desplazado `translateY`. Si rompés todas, no se lee como composición.
- **Espaciado:** Dos ritmos, no quince. El “inesperado” funciona porque el resto es predecible.
- **Radios:** Pueden mezclarse (una foto a vivo, un recorte irregular) si hay un criterio. Evitá el radio uniforme de card.
- **Bordes / sombras:** Al servicio de las capas (un filete, una superposición). Nada de `shadow-xl` en cada pieza, que las aplana otra vez en “cards sueltas”.
- **Color:** El de la marca. La ruptura es formal, no un arcoíris.
- **Tipografía:** Display o serif que aguanten el tamaño y el overlap.
  - [Editorial New](../tipografias/serif-display.md), [Fraunces](../tipografias/serif-display.md), [Syne](../tipografias/display-experimental.md), [Bricolage Grotesque](../tipografias/sans-grotesk.md), [Clash Display](../tipografias/display-experimental.md), [Reckless](../tipografias/serif-display.md).
  - Cuerpo, cuando aparece: [Newsreader](../tipografias/serif-texto.md) o [Satoshi](../tipografias/sans-geometrica.md).

## Sitios reales

- [basement.studio](https://basement.studio/) — composiciones de estudio, tipo e imagen en capas, no una grilla de 12 dócil.
- [locomotive.ca](https://locomotive.ca/) — Envato / Figma lo sitúan en el lote de motion y layouts que no se sienten de template.
- [drinkghia.com](https://drinkghia.com/) — frames, type recortado, piezas que se pisan; composición más que sección-de-SaaS.
- [thegentlewoman.co.uk](https://thegentlewoman.co.uk/) — editorial que desplaza foto y titular con criterio de revista, no de UI kit.
- [starface.world](https://starface.world/) — stickers y composiciones fuera de la grilla de e-commerce genérica, con un flujo de compra que igual se entiende.

## Errores comunes

- “Romper la grilla” = `position: absolute` en todo, y en mobile un desastre de overlaps ilegibles.
- Un hero asimétrico y, debajo, las tres cards de siempre. La ruptura tiene que ser una decisión de *página*, o al menos de un capítulo entero.
- Texto debajo de una foto sin un fondo o un contraste de reserva: se pisa y no se lee.
- Confundirlo con no tener grilla. Los estudios que lo hacen bien miden, y después desobedecen.

## Snippet

Un titular que se mete sobre una mancha, una nota desplazada. En mobile, se apila.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700&family=Newsreader:opsz,wght@6..72,400&display=swap" rel="stylesheet">
  <style>
    body { font-family: "Newsreader", serif; background: #f7f4ef; color: #161616; }
    h1 { font-family: "Bricolage Grotesque", sans-serif; }
  </style>
</head>
<body class="min-h-screen px-6 py-16">
  <main class="max-w-5xl mx-auto relative">
    <div class="hidden md:block absolute right-[8%] top-8 w-[42%] aspect-[4/5] bg-[#d9c7a8] -z-0"></div>
    <h1 class="relative text-5xl md:text-7xl font-bold leading-[0.95] max-w-xl">La grilla existe. Una pieza se sale a propósito.</h1>
    <p class="relative mt-10 md:mt-16 md:ml-[45%] max-w-sm text-lg leading-8 bg-[#f7f4ef] md:p-2">En mobile, se apila y se lee. En desktop, la foto queda atrás del titular. Una desobediencia, no diez.</p>
  </main>
</body>
</html>
```

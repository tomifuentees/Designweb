# Realismo táctil

Bubble lo da por establecido en 2026 y pone de ejemplo el sitio de Graza: grano, rayas de film, irregularidad física como señal de que una persona hizo el trabajo, en un momento en que lo “clean and competent” se lee como genérico. Advierte el costo: texturas pesadas y sin comprimir frenan la página. La implementación buena es liviana (un tile, un shader chico, un CSS de papel), no un fotograma de 4K. Es cercano al [grano](./grano-ruido.md) —el grano es la herramienta—, pero acá el objetivo es *materia*: papel, tela, aceite, cerámica, metal, no solo un overlay de ruido sobre un UI plano.

Envato y Wix, desde otro ángulo (lo orgánico, lo “nature distilled”), empujan al mismo lugar: que lo digital no parezca plástico.

## Cuándo usarlo y cuándo no

**Usalo** en comida, belleza, craft, moda, hospitalidad, cualquier marca que venda un objeto que se toca.

**No lo uses** en un dashboard de métricas o en un form largo (ensucia la lectura). No lo uses si la única materia que tenés es una textura de stock de “paper dust” a 200% de opacidad.

## Reglas concretas

- **Grilla:** Editorial o de producto, no de cards iguales. La foto del material puede ir a sangre.
- **Espaciado:** Un poco irregular ayuda (2–4 px de diferencia), sin romper la alineación de lectura.
- **Radios:** Recortes que parezcan de papel o de etiqueta (un radio chico, o un corte recto). Evitá el `rounded-3xl` de UI kit, que es lo contrario de lo táctil.
- **Bordes:** Un filete de tinta, o el borde real de una etiqueta fotografiada. No un border-token gris.
- **Sombras:** Cálidas, cortas, como de objeto sobre una mesa. Nunca un glow.
- **Color:** Paleta del material (el aceite, el algodón, el barro). Fondos papel. Ver también [orgánico](./organico-terroso.md).
- **Performance:** Tile de ruido de 100–200 px, imágenes comprimidas, nada de autoplay 4K de “textura”.
- **Tipografía:** Serifs y grotescas con cuerpo, que aguanten parecer impresas.
  - [Signifier](../tipografias/serif-display.md), [Reckless](../tipografias/serif-display.md), [Tiempos Headline](../tipografias/serif-display.md) / [Tiempos Text](../tipografias/serif-texto.md), [Founders Grotesk](../tipografias/sans-grotesk.md), [Fraunces](../tipografias/serif-display.md), [Zodiak](../tipografias/serif-display.md).
  - Gratis: Fraunces + [Newsreader](../tipografias/serif-texto.md) o [Cabinet Grotesk](../tipografias/sans-grotesk.md).

## Sitios reales

- [www.graza.co](https://www.graza.co/) — el ejemplo que cita Bubble para tactile realism.
- [seed.com](https://seed.com/) — Bubble lo cita como nature-inspired; comparte materia y calor, útil como vecino.
- [usa.spell.co](https://usa.spell.co/) — textil, campaña, materia fotografiada, no un render.
- [www.patagonia.com](https://www.patagonia.com/) — prenda y paisaje como materia, no como stock genérico de “aventura”.

## Errores comunes

- Un overlay de ruido al 40% que tapa el tipo y tumba el contraste.
- Texturas de 3 MB por sección.
- Skeuomorfismo ingenuo (un botón que parece cuero de 2009). Táctil en 2026 es *señal de materia*, no un UI que finge ser un objeto.
- Combinarlo con glass y con un degradé: se anulan.

## Snippet

Papel, una etiqueta, Fraunces, ruido liviano. Sombra de mesa, no de card.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Newsreader:opsz,wght@6..72,400&display=swap" rel="stylesheet">
  <style>
    body { font-family: "Newsreader", serif; background: #e8dcc8; color: #2a2218; }
    h1 { font-family: "Fraunces", serif; }
    .paper {
      background: #f3ead8;
      box-shadow: 2px 3px 0 rgba(80, 50, 20, .12);
      position: relative;
    }
    .paper::after {
      content: ""; position: absolute; inset: 0; pointer-events: none; opacity: .06;
      background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='140' height='140'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.8' numOctaves='2' stitchTiles='stitch'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>");
    }
  </style>
</head>
<body class="min-h-screen flex items-center justify-center p-8">
  <article class="paper max-w-md p-10">
    <p class="text-xs tracking-[0.16em] uppercase text-[#7a4a28]">Etiqueta · 500 ml</p>
    <h1 class="relative z-10 mt-3 text-5xl leading-tight">Se tiene que sentir como una cosa, no como una UI.</h1>
    <p class="relative z-10 mt-6 text-lg leading-8">Papel, una sombra corta, un poco de grano. La foto del material, si hay, va a sangre — no en un rounded-3xl.</p>
  </article>
</body>
</html>
```

# Ilustrado / hecho a mano

Envato, Figma y Bubble coinciden en un contrapunto de 2026: frente a la imagen de IA —ya reconocible, y en retirada como default, según una encuesta de diseñadores citada por Bubble vía Creative Boom—, las marcas vuelven a lo dibujado, a lo escrito a mano, a lo imperfecto. Wix lo venía registrando en 2025 (ilustración handmade, lettering) y en 2026 lo hace evolucionar hacia “nature distilled”; acá se documenta el polo *ilustrativo*, no el terroso. Headspace lleva años con un mundo de personajes. Graza y Ghia, cada una a su modo, se apoyan en gráfica propia, no en un render genérico.

El oficio está en un sistema de ilustración (una mano, una paleta, un trazo), no en un pack de “cute doodles” de un UI kit o en un “dibujo” salido de un modelo.

## Cuándo usarlo y cuándo no

**Usalo** en educación, wellness, productos para personas, marcas con un personaje, onboarding, PyMEs que tienen un ilustrador (aunque sea para tres spots).

**No lo uses** si la única ilustración disponible es de un generador o de un set de stock que también usa medio Twitter. No lo uses en un banco institucional o en un panel de datos, salvo un empty state muy contenido.

## Reglas concretas

- **Grilla:** La ilustración puede romper la caja (un personaje que se asoma, un trazo que cruza un titular). El texto, en una columna predecible.
- **Espaciado:** Dejá que el dibujo tenga un escenario, no lo encares en una card de 80 px sobre un heading.
- **Radios:** Blandos si el trazo es blando; rectos si el dibujo es de tinta. Que el UI no pelee con la mano.
- **Bordes / sombras:** Mínimos. Un trazo dibujado puede hacer de borde, mejor que un `border-gray-200`.
- **Color:** La paleta sale de la ilustración, no al revés. Pocos tintas, como en un riso o en un cuaderno.
- **Tipografía:** Una grotesca humana o una serif, y a lo sumo un acento “escrito”.
  - [Bricolage Grotesque](../tipografias/sans-grotesk.md), [Cabinet Grotesk](../tipografias/sans-grotesk.md), [Fraunces](../tipografias/serif-display.md) (itálica), [Karrik](../tipografias/display-experimental.md).
  - Acento manuscrito: [Shantell Sans](../tipografias/display-experimental.md), nunca en un párrafo largo ni en un form.

## Sitios reales

- [www.headspace.com](https://www.headspace.com/) — mundo ilustrado propio, citado por Figma en el lote de paletas vivas; el personaje es de marca, no un doodle de set.
- [drinkghia.com](https://drinkghia.com/) — ilustración y type recortado, gráfica de campaña.
- [www.graza.co](https://www.graza.co/) — identidad gráfica propia (el squiggle, el objeto) en lugar de un render genérico de botella.
- [www.glossier.com](https://www.glossier.com/) — beauty con voz propia, tipo e imagen de campaña, no stock de “mujer con textura suave” de IA.

## Errores comunes

- Iconos “hand-drawn” de un kit mezclados con Lucide en la misma fila.
- Una ilustración de IA con “style: pencil” y un prompt de wellness: es justo lo que está en retirada.
- Shantell Sans en todo el sitio, incluidos los legales.
- Poner el dibujo en un círculo con sombra suave, como un avatar de card de features.

## Snippet

Titular en Bricolage, una nota en Shantell, un campo para un dibujo real (no un emoji).

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600&family=Shantell+Sans:ital,wght@1,500&display=swap" rel="stylesheet">
  <style>
    body { font-family: "Bricolage Grotesque", sans-serif; background: #fbf6ea; color: #2a2418; }
    .hand { font-family: "Shantell Sans", cursive; }
  </style>
</head>
<body class="min-h-screen px-6 py-16">
  <main class="max-w-5xl mx-auto grid md:grid-cols-2 gap-12 items-center">
    <div>
      <p class="hand text-lg text-[#c45c26]">hecho a mano, de verdad</p>
      <h1 class="mt-3 text-5xl md:text-6xl leading-[1.05] font-semibold">El dibujo es de alguien. Si no, no está.</h1>
      <p class="mt-5 text-lg text-[#4a4336]">Un sistema de trazo, tres tintas, un lugar fijo para el personaje. Nada de doodles de UI kit ni de “pencil style” de un modelo.</p>
    </div>
    <div class="aspect-square bg-[#f0e2c5] flex items-center justify-center hand text-[#c45c26] text-xl">acá va el dibujo</div>
  </main>
</body>
</html>
```

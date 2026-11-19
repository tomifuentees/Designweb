# Maximalismo

Figma lo incluye entre las tendencias de 2026: el minimalismo no se va, pero el maximalismo pide más espacio —colores ricos, visuals superpuestos, tipos bold, composiciones densas—. Cita a Spotify y a Liquid Death como marcas que lo usan para sorprender. Es la respuesta ruidosa a la fatiga de “clean and competent”. No es lo mismo que desorden: un buen maximalismo tiene un sistema (una paleta corta pero alta, un tipo display que se repite, capas con un ritmo) y un mal maximalismo es una landing a la que le dejaron todos los efectos encendidos.

Convive bien con [dopamina](./dopamina-saturado.md) y a veces con [Y2K](./retrofuturismo-y2k.md) o [neo-brutalismo](./neo-brutalismo.md). Pelea con la UI casi invisible y con el suizo clásico.

## Cuándo usarlo y cuándo no

**Usalo** en marcas de actitud (bebidas, música, streetwear, entretenimiento, campañas). Un portfolio puede tener *una* página maximalista.

**No lo uses** en productos de confianza, en dashboards, ni como “personalidad” de un SaaS B2B que no la tiene. Si todo grita, no hay acento, y la conversión de un checkout se resiente.

## Reglas concretas

- **Grilla:** Capas, overlap, tipo que se sale del margen, a veces dos sistemas (una grilla de contenido + una capa de stickers / type). En mobile, simplificá las capas; no apilés overlap ilegible.
- **Espaciado:** Más apretado de lo “premium”. El maximalismo llena, pero tiene que dejar un camino para el ojo (un titular, un CTA).
- **Radios:** Libres, siempre que sean deliberados (un sticker recortado, un marco duro). Evitá el radio medio de card de SaaS, que aplaca el ruido.
- **Bordes:** Pueden ser gruesos, invertidos, o no haber y que la capa de tipo haga de borde.
- **Sombras:** Duras o multiplicadas, o ninguna. La sombra suave homogénea lo vuelve “UI kit ruidoso”, no maximalismo.
- **Color:** Alto contraste, pocos colores usados a lo grande (un amarillo a sangre, un negro, un blanco sucio) antes que un arcoíris de tokens.
- **Tipografía:** Una display que ocupe de verdad + una grotesca o mono que aguante.
  - [Druk](../tipografias/display-experimental.md), [Clash Display](../tipografias/display-experimental.md), [Agrandir](../tipografias/sans-geometrica.md), [Obviously](../tipografias/display-experimental.md), [Syne](../tipografias/display-experimental.md), [Melodrama](../tipografias/display-experimental.md).
  - Soporte: [Bricolage Grotesque](../tipografias/sans-grotesk.md) o [Space Grotesk](../tipografias/sans-geometrica.md).

## Sitios reales

- [liquiddeath.com](https://liquiddeath.com/) — Figma lo cita; negro, blanco, imagen y copy en mayúsculas, volumen alto.
- [starface.world](https://starface.world/) — color, stickers, composiciones llenas, comercio que todavía se entiende.
- [drinkghia.com](https://drinkghia.com/) — blocking de color, type recortado, frames; vecino maximalista / artístico.
- [newsroom.spotify.com](https://newsroom.spotify.com/) — se cita la marca (Figma) por campañas maximalistas. El sitio de marketing `spotify.com` redirige al player; esta es la URL que resolvió acá como propiedad de la marca.

## Errores comunes

- Activar grano + cinética + 3D + cinco displays distintas. Eso no es maximalismo: es un accidente.
- Perder el CTA o el precio en la capa decorativa.
- Usar Inter en el titular “para que se lea” y dejar el display solo en un detalle: se apaga el idioma.
- No tener una versión quieta para `prefers-reduced-motion` si hay motion de más.

## Snippet

Titular que se sale, paleta corta de alto contraste, Clash Display.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=clash-display@700&display=swap">
  <style>
    body { font-family: "Clash Display", sans-serif; background: #0a0a0a; color: #f4f400; }
  </style>
</head>
<body class="min-h-screen overflow-x-hidden">
  <main class="px-4 py-10 md:py-16">
    <p class="text-black bg-[#f4f400] inline-block px-2 text-sm font-bold uppercase">Volumen alto</p>
    <h1 class="mt-4 text-[22vw] leading-[0.8] font-bold tracking-tighter uppercase">
      Más<br>no menos
    </h1>
    <p class="mt-8 max-w-md text-lg text-[#f4f400]/80">Una paleta de dos colores, un tipo que ocupa la pantalla y un solo lugar donde hacer clic. El resto, que sobre.</p>
    <a href="#" class="inline-block mt-8 bg-[#f4f400] text-black px-6 py-3 text-xl font-bold uppercase">Abrir</a>
  </main>
</body>
</html>
```

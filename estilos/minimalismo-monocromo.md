# Minimalismo monocromo

Una familia, una paleta de grises (o de un solo tinte), mucho aire, fotografía o producto como único acontecimiento. Es perenne en lujo, moda y fintech sobria. En 2026 sigue vigente precisamente porque el “minimalismo” de plantilla (blanco, cards, un acento violeta) se volvió genérico: el monocromo bien hecho se siente como una decisión, no como una falta de ideas. Mercury aparece en Toimi en el lote de estética monocroma de lujo; The Row es un referente de retail callado. No confundir con la [UI casi invisible](./ui-casi-invisible.md) (eso es producto / datos) ni con el [suizo](./suizo-internacional.md) (eso es grilla y tipo internacional, que puede llevar un acento rojo).

## Cuándo usarlo y cuándo no

**Usalo** en lujo, moda, banca privada, arquitectura, portfolios serios, marcas que venden menos y más caro.

**No lo uses** en productos que necesitan semántica de color (estados de un dashboard), en marcas infantiles o de dopamina, ni como excusa para no definir jerarquía: el monocromo exige *más* escala tipográfica, no menos.

## Reglas concretas

- **Grilla:** Simétrica o casi, márgenes anchos, pocas columnas. Un objeto por vista, siempre que se pueda.
- **Espaciado:** El más generoso del kit. El lujo está en lo que no se pone.
- **Radios:** 0, o muy pocos (2–4 px). Las fotos a menudo van a vivo, sin marco.
- **Bordes:** Hairline negro o gris. A veces ni eso: solo el contraste del tipo sobre el campo.
- **Sombras:** No.
- **Color:** Negro, blanco, un rango de grises. Un “casi negro” cálido o frío, elegido. Si hay un acento, aparece una vez (un punto, un link al pasar).
- **Tipografía:** Una sola familia para casi todo, o una grotesca + una serif de titular en un único tamaño hero.
  - [Neue Montreal](../tipografias/sans-grotesk.md), [Söhne](../tipografias/sans-grotesk.md), [TWK Lausanne](../tipografias/sans-grotesk.md), [Suisse Int'l](../tipografias/sans-grotesk.md).
  - Lujo con serif: [Canela](../tipografias/serif-display.md) o [Signifier](../tipografias/serif-display.md).
  - Gratis: [Switzer](../tipografias/sans-grotesk.md), [General Sans](../tipografias/sans-grotesk.md).

## Sitios reales

- [mercury.com](https://mercury.com/) — Toimi lo cita por una estética monocroma, casi de lujo, en fintech.
- [www.therow.com](https://www.therow.com/) — retail de moda callada, foto y tipo, poco color.
- [www.vitsoe.com](https://www.vitsoe.com/) — sistema y producto sobre campo neutro, casi un manual.
- [www.nendo.jp](https://www.nendo.jp/) — galería blanca, labels chicos, el trabajo ocupa el color que el UI no usa.

## Errores comunes

- Gris sobre gris sin contraste AA.
- Meter un degradé “sutil” o un botón azul de sistema “para que se vea el CTA”. El CTA puede ser un subrayado negro o un invert.
- Usar Inter + mucho padding y llamarlo monocromo de lujo.
- Doce pesos de una variable “porque queda fino”. Con dos alcanza.

## Snippet

Campo blanco, Switzer, un titular y una ficha, sin color.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=switzer@400,500&display=swap">
  <style>body { font-family: "Switzer", sans-serif; }</style>
</head>
<body class="bg-white text-neutral-900 min-h-screen">
  <main class="max-w-4xl mx-auto px-6 py-24">
    <p class="text-xs tracking-[0.22em] uppercase text-neutral-500">Colección 06</p>
    <h1 class="mt-6 text-5xl md:text-7xl font-medium tracking-tight leading-[1.02]">Una familia. Cero color. La foto hace el resto.</h1>
    <div class="mt-16 aspect-[3/2] bg-neutral-200"></div>
    <p class="mt-6 text-sm text-neutral-500 max-w-sm">Si hace falta un acento, que sea un único gesto: un link, un punto, un invert al pasar.</p>
  </main>
</body>
</html>
```

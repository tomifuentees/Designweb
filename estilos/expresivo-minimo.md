# Minimalismo expresivo

Varias guías de 2026 (Envato, vikilinks, el “quiet” de Bubble) describen el mismo deseo: sitios limpios que no se sientan vacíos ni genéricos. La receta no es “más ornaments”. Es **una limpieza seria más una sola rareza** —una itálica de Fraunces, un acento de color sacado del local, un filete inesperado, un grain en el hero, un titular desalineado un módulo—. Es, en la práctica, el estilo más útil para una PyME o para un SaaS que no quiere parecer Linear ni una plantilla de v0.

Si el minimalismo monocromo es disciplina de lujo y la UI casi invisible es disciplina de producto, este es el de “una voz, y el resto en orden”.

## Cuándo usarlo y cuándo no

**Usalo** en landings de PyME, estudios chicos, SaaS que todavía no tienen una demo cinematográfica, profesionales, restaurants, servicios.

**No lo uses** si la “rareza” son cinco: cinética + grano + 3D + una display gritona + un bento de 9. Ahí ya no es expresivo, es una ensalada. Tampoco si no hay nada que decir: el estilo no suplanta el copy.

## Reglas concretas

- **Grilla:** Clara, de 12 o de 8, con una excepción (un titular que se mete en el margen, una imagen que se sale).
- **Espaciado:** Generoso y regular, salvo en el gesto (un bloque con el doble de aire).
- **Radios:** Un radio chico y constante (4–8 px) o 0. No un `rounded-2xl` de plantilla.
- **Bordes:** Un filete, no una card en cada sección.
- **Sombras:** No, o una sola y corta en el objeto que es el gesto.
- **Color:** Un neutro (crema o gris cálido) y **un** acento que no sea violeta de UI kit. El acento sale del mundo de la marca.
- **Tipografía:** Una pareja con contraste de rol.
  - Titular con carácter: [Cabinet Grotesk](../tipografias/sans-grotesk.md), [Fraunces](../tipografias/serif-display.md) (una itálica), [Bricolage Grotesque](../tipografias/sans-grotesk.md), [Clash Display](../tipografias/display-experimental.md) en una sola línea, [Zodiak](../tipografias/serif-display.md).
  - Cuerpo: [Satoshi](../tipografias/sans-geometrica.md), [Switzer](../tipografias/sans-grotesk.md), [Newsreader](../tipografias/serif-texto.md) o [Figtree](../tipografias/sans-grotesk.md).
  - Ver también [`../tipografias/pairings.md`](../tipografias/pairings.md).

## Sitios reales

El expresivo-mínimo se reconoce más por lo que *no* hace. Referentes de una voz clara y poco cromo:

- [cal.com](https://cal.com/) — producto y marketing contenidos, una tipografía de marca (Cal Sans), sin circus.
- [stripe.com](https://stripe.com/) — sistema limpio con un carácter propio (ilustración y color puntuales), no un template.
- [thegentlewoman.co.uk](https://thegentlewoman.co.uk/) — pocas piezas, una voz tipográfica fuerte, nada de UI de más.
- [www.vitsoe.com](https://www.vitsoe.com/) — objeto, tipo, silencio; una rareza de oficio más que de efecto.

## Errores comunes

- “Mínimo” = Inter, mucho padding, un botón pill índigo.
- Agregar un segundo y un tercer gesto porque “si no se ve poco”.
- Usar Instrument Serif en el hero de un SaaS y creer que eso basta (r/web_design, julio 2026: de las tendencias que peor van a envejecer).
- Tres cards de features “porque tiene que haber features”. Si hay tres servicios, pueden ser una lista tipográfica.

## Snippet

Crema, un acento óxido, Fraunces itálica en una sola palabra, Satoshi en el cuerpo.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=satoshi@400,500,600&display=swap">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@1,9..144,500&display=swap" rel="stylesheet">
  <style>
    body { font-family: "Satoshi", sans-serif; background: #f5f1ea; color: #1f1b16; }
    em { font-family: "Fraunces", serif; font-style: italic; font-weight: 500; }
  </style>
</head>
<body class="min-h-screen">
  <main class="max-w-3xl mx-auto px-6 py-24">
    <p class="text-xs tracking-[0.18em] uppercase text-[#9a4a2a]">Oficio · una sola rareza</p>
    <h1 class="mt-4 text-5xl md:text-6xl font-medium tracking-tight leading-[1.08]">Un sitio limpio, con <em>una</em> palabra que se sale.</h1>
    <p class="mt-6 text-lg text-neutral-600 max-w-xl">El resto: un acento sacado de la marca, un filete, un botón claro. Sin tres cards, sin degradé, sin Inter por default.</p>
    <a href="#" class="inline-block mt-10 border-b-2 border-[#9a4a2a] text-[#9a4a2a] pb-0.5 font-medium">Escribir</a>
  </main>
</body>
</html>
```

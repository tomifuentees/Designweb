# Retrofuturismo / Y2K

Figma incluye el retrofuturismo entre las tendencias de 2026: la visión vintage del futuro —cromo, neón, pixel, degradés de ciencia ficción y de la web temprana— aplicada con intención. Lo emparenta con las paletas saturadas y la nostalgia Y2K que también alimentan el “dopamine design”. Wix suma el “dial-up design”: memes, WordArt, MySpace, lo lo-fi de Geocities, y cita sitios de cultura de internet como Byline y Boys Club (la gráfica de *Brat* aparece como referente de actitud, no como un sitio para calcar). The Plus Addons lo marca como **nicho estable**, no como default: texto recortado en degradé, sparkles, `clip-path`. Sirve cuando esa nostalgia es parte del mundo de la audiencia (música, beauty, streetwear), no como decoración de una marca ajena.

Hay dos polos: el **cromo futurista** (brillos, metal, aurora) y el **early web / dial-up** (más tosco, más meme). No los mezcles sin querer.

## Cuándo usarlo y cuándo no

**Usalo** en moda joven, música, belleza, snacks, campañas y microsites. Una landing de lanzamiento lo banca mejor que un sitio institucional permanente.

**No lo uses** donde la conversión depende de confianza (salud, banca, legal, B2B sobrio). Tampoco como tema de un dashboard. Cuidado con el contraste de los degradés sobre texto.

## Reglas concretas

- **Grilla:** Puede romper la de 12: diagonales, stickers superpuestos, un hero que se sale. En el checkout o en el form, volvé a algo predecible.
- **Espaciado:** Más denso y “pegoteado” que un SaaS. El aire infinito pelea con el mood.
- **Radios:** Pills, círculos, o recortes raros (`clip-path`). Evitá el `rounded-xl` uniforme de Tailwind UI.
- **Bordes:** Cromo (degradé metálico de 1–2 px), o un pixel-border negro. A veces un glow, pero localizado.
- **Sombras:** Destellos y inner-shadows metálicos, no la sombra suave de card de SaaS.
- **Color:** Plata, celeste hielo, fucsia, lima, un negro lustroso. Degradés sí, pero *no el violeta-índigo de plantilla*. Un degradé de cromo o un duotono de campaña es otra cosa.
- **Tipografía:** Display geométrica o techno + un mono pixel o de máquina.
  - [Clash Display](../tipografias/display-experimental.md), [Panchang](../tipografias/display-experimental.md), [Unbounded](../tipografias/display-experimental.md), [Syne](../tipografias/display-experimental.md), [Space Grotesk](../tipografias/sans-geometrica.md).
  - Acento: [Space Mono](../tipografias/mono.md) o [Departure Mono](../tipografias/mono.md).
  - Wix menciona Orbitron y similares; no están en este catálogo, no las inventes como si lo estuvieran.

## Sitios reales

- [starface.world](https://starface.world/) — Figma lo cita entre las marcas de paleta alta y espíritu Y2K / dopamine (parches en forma de estrella, color, sticker). Atención: `starface.com` es otra empresa (telefonía).
- [www.bylinebyline.com](https://www.bylinebyline.com/) — citado por Wix en “dial-up design”.
- [boysclub.vip](https://boysclub.vip/) — citado por Wix en el mismo lote de cultura de internet.
- [drinkghia.com](https://drinkghia.com/) y [feastables.com](https://feastables.com/) — consumer con gráfica alta, útil como vecindario visual, aunque no sean “Y2K de libro”.

## Errores comunes

- Hacer un degradé violeta, poner Inter y llamarlo Y2K.
- Sparkles de CSS en cada título, cada botón y el cursor. Un destello, no una nevada.
- Texto sobre cromo sin respaldo (sin overlay, sin trazo): no se lee.
- Traer el estilo al flujo de compra completo y perder claridad.
- Usar `starface.com` como referencia de la marca de beauty: no lo es.

## Snippet

Titular con degradé metálico (no violeta), Clash Display, un destello contenido.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=clash-display@600,700&display=swap">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400&display=swap" rel="stylesheet">
  <style>
    body { font-family: "Clash Display", sans-serif; background: #07070c; color: #f4f0ff; }
    .chrome {
      background: linear-gradient(105deg, #b8c0cc, #ffffff 35%, #e7b0ff 50%, #8ad7ff 70%, #d0d5dd);
      -webkit-background-clip: text; background-clip: text; color: transparent;
    }
    .pill { box-shadow: 0 0 24px rgba(231, 176, 255, .35), inset 0 1px 0 rgba(255,255,255,.5); }
  </style>
</head>
<body class="min-h-screen flex items-center justify-center p-6">
  <main class="text-center max-w-2xl">
    <p class="font-['Space_Mono'] text-xs tracking-[0.2em] text-fuchsia-300 mb-4">Y2K · no un degradé índigo de plantilla</p>
    <h1 class="chrome text-6xl md:text-8xl font-bold leading-[0.9]">FUTURO<br>YA ERA</h1>
    <p class="mt-6 text-sm text-zinc-400 font-['Space_Mono']">Cromo, un glow y una paleta de campaña. El checkout, después, se tiene que poder leer.</p>
    <a href="#" class="pill inline-block mt-8 rounded-full px-6 py-2 text-sm bg-white/10 border border-white/40 backdrop-blur">Entrar</a>
  </main>
</body>
</html>
```

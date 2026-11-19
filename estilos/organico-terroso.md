# Orgánico / terroso

Wix llama “nature distilled” a una dirección de 2026: paletas que vienen de la piel, la madera y la tierra, texturas de papel o piedra, y una sofisticación baja de volumen. Lo vincula al Pantone Color of the Year 2026 (Cloud Dancer). Bubble lo marca como tendencia *emergente* (nature-inspired) y pone de ejemplo el sitio de Seed: verdes de bosque y terracota en lugar de primarios saturados o neutros estériles. Es un contrapeso explícito a las interfaces SaaS frías y a la imagen de IA. filtercoffee.dev describe un vecindario “bohemian” con SPELL (foto de campaña, tierra, oficio).

No es poner una hoja de palmera en PNG sobre un layout de tres cards. El color, el tipo y el recorte de las fotos tienen que parecer materia.

## Cuándo usarlo y cuándo no

**Usalo** en comida, vino, bienestar, cosmética, turismo, sustentabilidad, oficio (cerámica, textil, agricultura) y PyMEs cuyo mundo es físico.

**No lo uses** en un devtool, un exchange o un dashboard de ops: va a parecer disfraz. Tampoco si la única “naturaleza” que tenés es un stock de Unsplash o una imagen de IA de “hojas suaves”.

## Reglas concretas

- **Grilla:** Puede ser más suelta que un SaaS: bloques de foto a sangre, texto en una columna cálida, formas con esquinas blandas o recortes irregulares. Sigue habiendo alineación, no collage aleatorio.
- **Espaciado:** Generoso y un poco irregular (no todos los márgenes idénticos). Como una mesa servida, no como un design system de 8 px exhibido.
- **Radios:** 12–24 px, o recortes orgánicos (`border-radius` distinto en cada esquina, con mesura). Evitá el círculo perfecto de pill en todos los botones.
- **Bordes:** Finos, en tinta marrón o verde oscuro al 20%. A veces un trazo que parece lápiz, no un hairline de UI.
- **Sombras:** Cálidas, cortas, de baja opacidad (como si la luz fuera de tarde). Nada de sombras negras estándar de Tailwind.
- **Color:** Terracota, oliva, arena, crema, óxido, un verde profundo. Fondos `#f3eadf`, `#efe6d6`. Evitá el púrpura y los neones. Cloud Dancer (un blanco cálido) puede ser fondo, no “blanco de Figma”.
- **Tipografía:** Una serif con cuerpo y una grotesca humana, o una display un poco irregular.
  - Titular: [Fraunces](../tipografias/serif-display.md), [Boska](../tipografias/serif-display.md), [Sentient](../tipografias/serif-texto.md), [Zodiak](../tipografias/serif-display.md).
  - Cuerpo: [Newsreader](../tipografias/serif-texto.md) o [Source Serif 4](../tipografias/serif-texto.md).
  - UI: [Cabinet Grotesk](../tipografias/sans-grotesk.md) o [Bricolage Grotesque](../tipografias/sans-grotesk.md).
  - Un acento escrito a mano: [Shantell Sans](../tipografias/display-experimental.md), nunca como cuerpo largo.

## Sitios reales

- [seed.com](https://seed.com/) — el ejemplo de nature-inspired que cita Bubble.
- [usa.spell.co](https://usa.spell.co/) — SPELL, Byron Bay; filtercoffee.dev lo usa como referencia “bohemian” / organica (también está [aus.spell.co](https://aus.spell.co/)).
- [www.patagonia.com](https://www.patagonia.com/) — retail de outdoor, paleta tierra, foto de lugar y de materia.
- [www.graza.co](https://www.graza.co/) — aceite de oliva; Bubble lo cita más bien como realismo táctil, pero comparte paleta y mundo físico (útil como vecino).
- [www.aesop.com](https://www.aesop.com/) — referente habitual de retail botánico / editorial. El GET desde este entorno devolvió 403 (antibot, no 404); confirmar visualmente en el navegador.

## Errores comunes

- Stock de “mujer en un campo” + Inter + botones verde menta. Sigue pareciendo plantilla.
- Ilustraciones de plantas generadas por IA (Creative Boom, 2026, citado por Bubble: ya se reconocen).
- Más de seis colores “tierra” sin un dominante: queda sucio, no orgánico.
- Sombras negras y radios de card de SaaS sobre un fondo crema.

## Snippet

Hero en papel, Fraunces, un acento terracota, forma un poco irregular.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Source+Serif+4:opsz,wght@8..60,400&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=cabinet-grotesk@500&display=swap">
  <style>
    body { background: #efe6d6; color: #2a2218; font-family: "Source Serif 4", serif; }
    h1 { font-family: "Fraunces", serif; }
    .ui { font-family: "Cabinet Grotesk", sans-serif; }
    .blob { border-radius: 40% 60% 50% 50% / 50% 40% 60% 50%; }
  </style>
</head>
<body class="min-h-screen">
  <main class="max-w-5xl mx-auto px-6 py-16 md:py-24 grid md:grid-cols-2 gap-12 items-center">
    <div>
      <p class="ui text-xs tracking-[0.18em] uppercase text-[#8a4330]">Cosecha · 2026</p>
      <h1 class="mt-3 text-5xl md:text-6xl leading-[1.05] font-medium">La paleta sale de la tierra, no de un degradé.</h1>
      <p class="mt-6 text-lg leading-8 text-[#4a3f32]">Terracota, oliva, papel. Una foto real del oficio. El botón puede esperar.</p>
      <a href="#" class="ui inline-block mt-8 bg-[#8a4330] text-[#efe6d6] px-5 py-3 text-sm">Ver la línea</a>
    </div>
    <div class="blob bg-[#c4b196] aspect-square"></div>
  </main>
</body>
</html>
```

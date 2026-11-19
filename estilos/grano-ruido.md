# Grano y ruido

No es tanto un “estilo de página” como una técnica de 2026 que aparece en varios idiomas (editorial, oscuro, riso, anti-diseño, táctil). Bubble lo vincula al realismo táctil: grano, rayas de film, irregularidad física como señal de que alguien hizo el trabajo, frente a lo “clean and competent” que ahora se lee como genérico. La advertencia es de performance: el grano bien hecho es un SVG, un PNG chico en repeat, o un gradiente + `filter`, no un JPG de 4 MB a pantalla completa.

Sirve como **acento** sobre otro estilo del catálogo. Si el único gesto del sitio es un overlay de ruido, todavía hace falta una decisión de tipo y de paleta.

## Cuándo usarlo y cuándo no

**Usalo** para sacar el plastificado de un fondo plano, de una foto demasiado retocada o de un dark mode que parece un UI kit. Queda bien en héroes, en un capítulo, en una tapa.

**No lo uses** en un dashboard denso (cansa la vista y ensucia los números), ni sobre texto chico (mata el contraste), ni como capa 60% opaca que deja todo gris. Evitá animar el grano en loop: puede ser un problema de accesibilidad y de batería.

## Reglas concretas

- **Grilla / radios / bordes:** Los hereda el estilo base (editorial, oscuro, riso). El grano no pide una grilla propia.
- **Espaciado:** Sin cambios. El grano no reemplaza al aire.
- **Sombras:** Si hay, que también tengan un poco de suciedad (no un blur perfecto).
- **Color:** El ruido puede ser monocromo (opacidad 4–8%) o duotono (una tinta). Sobre oscuro, un ruido claro al 5–7% alcanza.
- **Implementación liviana:** un pseudo-elemento `pointer-events: none` con `background-image` de un tile de 100–200 px, `background-repeat: repeat`, `opacity: .06`. Alternativa CSS: `filter: url(#noise)` o un `repeating-linear-gradient` cruzado, más barato todavía.
- **Tipografía:** La del estilo anfitrión. Queda especialmente bien con [Reckless](../tipografias/serif-display.md), [Signifier](../tipografias/serif-display.md), [Karrik](../tipografias/display-experimental.md), [Monument Grotesk](../tipografias/sans-grotesk.md) o [Zodiak](../tipografias/serif-display.md).

## Sitios reales

El grano aparece como capa, no como “marca de un solo sitio”. Referentes donde la textura es parte del clima:

- [www.graza.co](https://www.graza.co/) — Bubble lo cita como ejemplo de realismo táctil (grano e irregularidad frente al pulido de IA).
- [basement.studio](https://basement.studio/) — estudio con acabado de campaña, a menudo con textura y tipo pesado.
- [www.cosmos.so](https://www.cosmos.so/) — archivo visual oscuro, materia y curaduría, clima de “objeto” más que de UI plana.
- [bruno-simon.com](https://bruno-simon.com/) — portfolio 3D con un acabado que no es UI kit; el grano / la materia aparecen en el vecindario de lo espacial.

(No se cita un sitio *solo* por tener un overlay: se eligieron referentes donde la textura sostiene el tono.)

## Errores comunes

- Un PNG enorme, sin tile, sobre todo el `body`.
- Opacidad alta que ensucia el texto y tumba el contraste AA.
- Grano animado en un `setInterval` de canvas, sin respetar `prefers-reduced-motion`.
- Sumarlo a glass + degradé violeta: no “artesaniza” un default de IA, lo ensucia.

## Snippet

Tile de ruido en CSS puro (sin imagen), sobre un hero oscuro.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=zodiak@500,600&display=swap">
  <style>
    body { font-family: "Zodiak", serif; background: #161410; color: #efe8dc; }
    .noise { position: relative; isolation: isolate; }
    .noise::after {
      content: "";
      position: absolute; inset: 0; pointer-events: none; z-index: 2;
      opacity: .07;
      background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='160' height='160'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>");
    }
  </style>
</head>
<body class="min-h-screen">
  <section class="noise min-h-screen flex items-center px-8">
    <div class="relative z-10 max-w-3xl">
      <p class="text-xs tracking-[0.18em] uppercase text-[#efe8dc]/50">Capa · no un JPG de 4 MB</p>
      <h1 class="mt-4 text-5xl md:text-7xl leading-[1.05] font-medium">Un poco de suciedad saca el plastificado.</h1>
      <p class="mt-6 text-lg text-[#efe8dc]/70 max-w-md">Opacidad baja, tile chico, texto que sigue contrastando. El grano es un acento, no un tema.</p>
    </div>
  </section>
</body>
</html>
```

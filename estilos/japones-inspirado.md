# Inspiración japonesa

No es un “theme sakura”. Lo que se puede sostener en 2026 es un conjunto de decisiones: *ma* (el vacío como materia), jerarquía callada, a menudo el cruce de vertical y horizontal cuando hay japonés y latín, fotografía o vídeo de estación / de materia, motion contenido. El case de Shinpaku (KEI inc.) lo dice con claridad: tipografía vertical en japonés y horizontal en inglés que se cruzan al scroll, ritmo de poema, veinticuatro estaciones. nendo trabaja en blanco, labels chicos, el proyecto como pieza de galería. MUJI, del lado retail, sigue siendo el referente de contención (en esta pasada `muji.com` no respondió; sí lo hizo `muji.eu`).

Este kit **no incluye tipografías japonesas**. Si el sitio está en japonés, hace falta una familia adecuada (Noto Sans JP, una grotesca japonesa licenciada, o la del sistema) *además* de la pareja latina del catálogo. No intentes cubrir japonés con Inter.

## Cuándo usarlo y cuándo no

**Usalo** en cultura, retail de objeto, editorial, gastronomía, hospitality, estudios, marcas que bancan el silencio y el ritmo lento.

**No lo uses** como “asian flair” en una marca que no tiene nada que ver (ilustraciones de onda, ramo de sakura de stock, kanji decorativo). Tampoco en un flujo denso de dashboard: el *ma* se come la densidad que el producto necesita.

## Reglas concretas

- **Grilla:** Columnas anchas de vacío. Un módulo de contenido y mucho campo. Si hay japonés, prever un eje vertical (writing-mode) que no rompa el layout latino.
- **Espaciado:** Más del que un SaaS “premium” ya usaría. El vacío es el gesto, no un padding de más en una card.
- **Radios:** 0 o muy pocos. Las fotos, a menudo a vivo o con un filete fino.
- **Bordes:** Hairlines. Un sello o un índice (un número, una estación) en lugar de un badge.
- **Sombras:** No.
- **Color:** Blanco, tinta, un rojo o un índigo puntuales, a veces un papel un poco cálido. Paleta corta. Evitá neones y el violeta de plantilla.
- **Tipografía (latina, del catálogo):**
  - [Neue Montreal](../tipografias/sans-grotesk.md), [Suisse Int'l](../tipografias/sans-grotesk.md), [Monument Grotesk](../tipografias/sans-grotesk.md), [Untitled Sans](../tipografias/sans-grotesk.md), [Söhne](../tipografias/sans-grotesk.md).
  - Gratis: [Switzer](../tipografias/sans-grotesk.md) o [Mona Sans](../tipografias/sans-grotesk.md), en pesos livianos, tracking un poco abierto en caps.
  - Para japonés: declaralo explícitamente fuera de este catálogo. No lo improvises.

## Sitios reales

- [shinpaku.co](https://shinpaku.co/) — el sitio del proyecto; el case está en [kei-inc.jp/projects/shinpaku](https://kei-inc.jp/projects/shinpaku/).
- [www.nendo.jp](https://www.nendo.jp/) — estudio, galería blanca, labels mínimos.
- [www.muji.eu](https://www.muji.eu/) — retail de contención. `www.muji.com` no respondió (timeout) desde este entorno; se usa la URL europea que dio 200.
- [www.teamlab.art](https://www.teamlab.art/) — lo inmersivo, el ritmo y la estación como contenido, no como stock “Japan”.

## Errores comunes

- Sakura de stock, kanji de adorno, una brush font falsa.
- Llenar el *ma* con tres cards de features porque “si no parece vacío”.
- Inter a 16 px sobre blanco y un ícono de montaña Fuji.
- Animaciones rápidas tipo SaaS: el idioma pide otra temporalidad (y reduced-motion igual).

## Snippet

Mucho vacío, un índice, Switzer, un filete. Sin ornamentación “japonesa” de stock.

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
<body class="bg-[#f7f6f2] text-neutral-900 min-h-screen">
  <main class="min-h-screen grid md:grid-cols-12 px-8 py-16">
    <p class="md:col-span-3 text-xs tracking-[0.22em] uppercase">04 / ma</p>
    <div class="md:col-span-7 md:col-start-5 self-center">
      <h1 class="text-5xl md:text-6xl font-medium tracking-tight leading-[1.15] max-w-lg">El vacío también es material de diseño.</h1>
      <p class="mt-10 text-sm text-neutral-500 max-w-xs leading-7">Una línea, un número, un texto que no se apura. Sin sakura de stock.</p>
    </div>
  </main>
</body>
</html>
```

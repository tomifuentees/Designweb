# Bento grids

Grilla modular de mosaicos de distinto tamaño, como un bentō: el plato principal ocupa más caja, los acompañamientos menos. En 2026 es el patrón casi default para presentar features de producto. Toimi lo describe como pasado de curiosidad de keynotes de Apple (2022) a estándar de categoría (2024) y a casi universal en landings de software. Bubble lo marca como establecido y advierte lo obvio: si todos los paneles miden lo mismo, ya no es un bento, es una grilla común.

Ramp formalizó reglas internas con Bakken & Baeck (gutters uniformes, el tamaño como jerarquía). Linear, Notion, Attio, Vercel y las product pages de Apple lo usan de forma consistente. El riesgo, justo por eso, es aplicarlo en automático y que la landing se parezca a todas las demás.

## Cuándo usarlo y cuándo no

**Usalo** en una sección de producto, integraciones o “qué hace esto”, cuando hay entre 6 y 9 piezas de contenido heterogéneo (una demo grande, un dato, una cita, un recorte de UI) y una de ellas merece más peso. También sirve en e-commerce para destacar categorías.

**No lo uses** como layout de todo el sitio, ni cuando el contenido tiene alturas impredecibles, ni pasados los ~12 mosaicos: el ojo deja de leer una composición y empieza a ver una pared. En un dashboard denso suele estorbar. Y no lo combines con glass en cada celda ni con tres cards iguales adentro del bento: perdés la jerarquía.

## Reglas concretas

- **Grilla:** CSS Grid con `grid-template-areas` (es la mecánica que The Plus Addons asocia a que el patrón se haya vuelto fácil de mantener). En mobile, reescribí el mapa: una columna, el mosaico hero primero. Gutters uniformes (16–24 px en desktop, 12–16 en mobile).
- **Espaciado:** El aire va *entre* mosaicos, no como padding gigante dentro de cada uno. El tile grande puede tener más padding interno; los chicos, menos.
- **Radios:** Un solo radio para todos los tiles (8–16 px es lo habitual en SaaS; 0 px si el sistema es suizo o de catálogo). No mezcles `rounded-2xl` con `rounded-md` en la misma bandeja.
- **Bordes:** 1 px a bajo contraste (`color-mix` o blanco al 8–12% sobre oscuro; negro al 8–12% sobre claro). El borde, no la sombra, es lo que pone los tiles sobre el fondo.
- **Sombras:** Casi ninguna, o una sombra muy corta y poco opaca. La sombra suave e idéntica en cada tile es justamente el tic de IA.
- **Color:** El fondo de la bandeja y el de los tiles tienen que ser primos, no un arcoíris. Un acento para un solo tile o un solo dato. Fotos o recortes de UI reales adentro, no ilustraciones 3D de stock.
- **Tipografía:** Una grotesca o geométrica de producto para títulos de tile y un mono chico para labels / métricas.
  - Titular de tile: [Satoshi](../tipografias/sans-geometrica.md), [Switzer](../tipografias/sans-grotesk.md), [Mona Sans](../tipografias/sans-grotesk.md) o [Cabinet Grotesk](../tipografias/sans-grotesk.md).
  - Labels: [IBM Plex Mono](../tipografias/mono.md), [Commit Mono](../tipografias/mono.md) o [Geist Mono](../tipografias/mono.md) (este último, con la advertencia del catálogo: ya es default de devtools).
  - Evitá Inter o Geist como personalidad de toda la bandeja.

## Sitios reales

- [linear.app](https://linear.app/) — Toimi lo cita como referencia de bento de features sobre un sistema oscuro, junto a la demo viva del producto.
- [ramp.com](https://ramp.com/) — sistema de tiles formalizado con [Bakken & Baeck](https://bakkenbaeck.com/case/ramp) (GET 200).
- [attio.com](https://attio.com/) y [vercel.com](https://vercel.com/) — citados por Toimi en el mismo lote de producto que usa bento de forma consistente.
- [www.apple.com/iphone](https://www.apple.com/iphone/) — el origen “keynote” del patrón, todavía visible en páginas de producto.
- [drinkghia.com](https://drinkghia.com/) — Bubble cita una sección de reviews de Ghia armada como bento, fuera del mundo SaaS.

`notion.so` redirige a [notion.com](https://www.notion.com/); también aparece en ese lote.

## Errores comunes

- Hacer 3×N tiles del mismo tamaño y llamarlo bento.
- Poner un icono Lucide + un H3 + un párrafo en cada celda: es la grilla de tres features con otro nombre.
- Más de una “celda hero”. Si dos mosaicos pelean el primer lugar, no hay jerarquía.
- Contenido de altura libre (testimonios largos, blogs) que rompe la bandeja. El bento pide contenido recortado a un propósito.
- Reciclar el bento en el hero, en features, en pricing y en el footer.

## Snippet

Bandeja de 2×3 con un tile hero. Satoshi + IBM Plex Mono, fondo oscuro, un solo acento. Sin sombras.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=satoshi@500,700&display=swap">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
  <style>
    body { font-family: "Satoshi", sans-serif; }
    .mono { font-family: "IBM Plex Mono", ui-monospace, monospace; }
    .bento {
      display: grid;
      gap: 1rem;
      grid-template-columns: 1fr;
      grid-template-areas:
        "hero"
        "a"
        "b"
        "c";
    }
    .hero { grid-area: hero; }
    .a { grid-area: a; } .b { grid-area: b; } .c { grid-area: c; }
    @media (min-width: 768px) {
      .bento {
        grid-template-columns: 2fr 1fr;
        grid-template-rows: auto auto;
        grid-template-areas:
          "hero a"
          "hero b"
          "c    b";
      }
    }
  </style>
</head>
<body class="bg-[#0d0e10] text-zinc-100 min-h-screen p-6 md:p-10">
  <section class="max-w-5xl mx-auto">
    <p class="mono text-[11px] tracking-[0.16em] uppercase text-zinc-500 mb-6">Fig 02 — Producto</p>
    <div class="bento">
      <article class="hero rounded-xl border border-white/10 bg-[#16171b] p-6 md:p-8 flex flex-col justify-between min-h-[260px]">
        <p class="mono text-[11px] text-zinc-500">01 · Vista principal</p>
        <div>
          <h2 class="text-3xl md:text-4xl font-bold tracking-tight">El recorte grande lleva la feature que importa.</h2>
          <p class="mt-3 text-zinc-400 max-w-md">Acá va una captura real del producto, no un icono genérico ni una ilustración 3D de stock.</p>
        </div>
      </article>
      <article class="a rounded-xl border border-white/10 bg-[#16171b] p-5">
        <p class="mono text-[11px] text-amber-400">02 · Dato</p>
        <p class="mt-4 text-4xl font-bold tabular-nums">120ms</p>
        <p class="mt-1 text-sm text-zinc-400">Una métrica, no un párrafo.</p>
      </article>
      <article class="b rounded-xl border border-white/10 bg-[#16171b] p-5 flex flex-col justify-between">
        <p class="mono text-[11px] text-zinc-500">03 · Cita</p>
        <blockquote class="mt-4 text-lg leading-snug">“El tamaño del mosaico ya está diciendo qué leer primero.”</blockquote>
      </article>
      <article class="c rounded-xl border border-white/10 bg-[#16171b] p-5">
        <p class="mono text-[11px] text-zinc-500">04 · Atajo</p>
        <p class="mt-3 text-sm text-zinc-300"><kbd class="mono border border-white/15 rounded px-1.5 py-0.5 text-xs">⌘K</kbd> para buscar. Un gesto, no una lista de bullets.</p>
      </article>
    </div>
  </section>
</body>
</html>
```

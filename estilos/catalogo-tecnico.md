# Catálogo técnico

Toimi describe un contramovimiento de 2026, junto al editorial: un idioma heredado de la escuela suiza y del brutalismo web de los 90, ejecutado con valores actuales. Lo ve en Teenage Engineering (foto de producto tipo catálogo, fondo neutro), Resend (captions mono, dark de documentación), Mercury (monocromo de lujo) y, en su listado, Carta. Las marcas compartidas: grilla estricta, tipografía mono o técnica para metadatos, jerarquías mínimas, a veces lowercase, fotografía de objeto como ficha, filetes, arquitectura de información que trata el contenido como un manual.

Es primo del [suizo](./suizo-internacional.md) y vecino de la [UI casi invisible](./ui-casi-invisible.md), pero el acento está en *el objeto numerado*: SKU, FIG, peso, material, endpoint.

## Cuándo usarlo y cuándo no

**Usalo** en hardware, instrumentos, APIs, industrial, marcas “built, not decorated”, documentaciones que también son marketing.

**No lo uses** en beauty lúdica, en un restaurant, en una ONG que necesita calor, ni si no hay objeto o especificación que fichar. Sin ficha, queda un suizo vacío.

## Reglas concretas

- **Grilla:** Estricta, tipo catálogo o data sheet. Índices a la izquierda, el objeto al centro o a la derecha. Numeración visible (01, 02, SKU).
- **Espaciado:** Regular, predecible, más seco que el lujo monocromo. El aire existe, pero no es “poético”: es margen de ficha.
- **Radios:** 0, o 2–4 px en thumbnails de producto.
- **Bordes:** 1 px, casi negros o blanco al 12% en oscuro. Tablas y filetes antes que cards.
- **Sombras:** No. La foto del objeto puede tener su propia sombra de estudio, no una de CSS.
- **Color:** Neutro (gris de estudio, blanco, negro). Un acento funcional (un lima de stock, un rojo de alerta), no un degradé.
- **Tipografía:**
  - UI / títulos: [ABC Diatype](../tipografias/sans-grotesk.md), [Favorit](../tipografias/sans-grotesk.md), [Monument Grotesk](../tipografias/sans-grotesk.md), [IBM Plex Sans](../tipografias/sans-grotesk.md), [Söhne](../tipografias/sans-grotesk.md).
  - Captions, SKU, código: [IBM Plex Mono](../tipografias/mono.md), [Berkeley Mono](../tipografias/mono.md), [Geist Mono](../tipografias/mono.md) (con la advertencia de default devtools) o [Fragment Mono](../tipografias/mono.md).
  - Gratis de apoyo: [Switzer](../tipografias/sans-grotesk.md) + Plex Mono.

## Sitios reales

- [teenage.engineering](https://teenage.engineering/) — el ejemplo de catálogo que Toimi pone adelante: objeto, fondo neutro, ficha.
- [resend.com](https://resend.com/) — marketing de API con tono de documentación, captions técnicos.
- [mercury.com](https://mercury.com/) — citado en el mismo lote; monocromo, disciplina de sistema.
- [stripe.com](https://stripe.com/) — infraestructura con ficha, docs y marketing en un mismo clima técnico (más color que Teenage Engineering, misma idea de “especificación pública”).

Carta aparece en el listado de Toimi; no se verificó un URL unívoco en esta pasada y no se cita como link de ficha.

## Errores comunes

- Poner “SKU 004” en una landing que no tiene producto. Se lee como pose.
- Cards redondeadas con sombra alrededor de cada ficha: deshace el catálogo.
- Geist + un mockup de dashboard y llamarlo “technical catalog”.
- Olvidar la tabla / el spec real: este estilo *pide* datos, no copy de features.

## Snippet

Ficha de objeto, filetes, Switzer + IBM Plex Mono.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=switzer@400,500&display=swap">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400&display=swap" rel="stylesheet">
  <style>
    body { font-family: "Switzer", sans-serif; }
    .mono { font-family: "IBM Plex Mono", ui-monospace, monospace; }
  </style>
</head>
<body class="bg-[#efefed] text-neutral-900">
  <main class="max-w-5xl mx-auto px-6 py-12 grid md:grid-cols-12 gap-8">
    <p class="md:col-span-3 mono text-xs leading-6">
      TE-OP-1<br>field · portable<br>rev. 2026
    </p>
    <div class="md:col-span-6 aspect-square bg-[#d9d9d4]"></div>
    <dl class="md:col-span-3 mono text-xs leading-7 border-t border-neutral-900 pt-3">
      <div class="flex justify-between border-b border-neutral-900/20 py-2"><dt>peso</dt><dd>0.38 kg</dd></div>
      <div class="flex justify-between border-b border-neutral-900/20 py-2"><dt>material</dt><dd>ABS</dd></div>
      <div class="flex justify-between py-2"><dt>sku</dt><dd>004-A</dd></div>
    </dl>
  </main>
</body>
</html>
```

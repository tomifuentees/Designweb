# Features

Una sección de features existe para que se entienda *qué hace* el producto, en el orden que importa. No existe para llenar el espacio entre el hero y el pricing.

El default de 2024–2026 es una grilla de tres cards o un bento de 6–9 mosaicos. El bento puede estar bien si hay jerarquía de verdad: ver [`../estilos/bento-grids.md`](../estilos/bento-grids.md). Si no hay jerarquía, una lista tipográfica rinde más y se ve menos de plantilla.

## Cuándo usarlo y cuándo no

**Usalo** cuando hay 3–7 capacidades distintas que un humano puede verificar. **No lo uses** para repetir el slogan del hero en tres columnas, ni para un “AI-powered” que no se puede señalar en la interfaz.

## Qué se ve con terminación pro

- Alternativas al bento (usá una, no todas):
  - **Lista tipográfica** numerada o con una ceja mono, a dos columnas desiguales (título a la izquierda, texto a la derecha).
  - **Ritmo editorial:** un feature grande con captura real, después dos chicos, no una grilla isométrica.
  - **Catálogo técnico:** nombre, una línea, un identificador (`01 / 04`), fondo neutro. Ver [`../estilos/catalogo-tecnico.md`](../estilos/catalogo-tecnico.md).
  - **Bento con jerarquía:** un mosaico protagonista, no 9 tiles del mismo peso.
- Cada ítem tiene un verbo y un objeto (“Cruzá el conteo por sucursal”), no un sustantivo abstracto (“Insights”).
- Si hay captura, es del producto real o un esquema honesto, no un dashboard genérico de Dribbble.

## Qué hace mal el default de IA

- Tres columnas, `rounded-2xl`, ícono Lucide en un circulito índigo, título de dos palabras, párrafo de 15.
- Un bento de 9 con íconos y stats inventados (“99.9% uptime”, “10x faster”).
- Emojis como íconos de feature (r/web_design, 2026, lo marca como tic de IA).
- “Powerful”, “seamless”, “next-gen” en cada heading.
- La misma card copiada tres veces con el texto cambiado.

## Tipografía del kit

- Titular de ítem: [Bricolage Grotesque](../tipografias/sans-grotesk.md) o [Cabinet Grotesk](../tipografias/sans-grotesk.md).
- Cuerpo: [Satoshi](../tipografias/sans-geometrica.md).
- Índice: [IBM Plex Mono](../tipografias/mono.md).

## Snippet

Lista tipográfica a dos columnas, numerada, sin cards ni íconos.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=satoshi@400,500&display=swap">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500&family=IBM+Plex+Mono:wght@400&display=swap" rel="stylesheet">
  <style>
    body { font-family: "Satoshi", sans-serif; background: #f3f1ec; color: #1a1814; }
    h2, h3 { font-family: "Bricolage Grotesque", sans-serif; }
    .mono { font-family: "IBM Plex Mono", ui-monospace, monospace; }
  </style>
</head>
<body class="max-w-4xl mx-auto px-6 py-20">
  <p class="mono text-xs tracking-[0.16em] uppercase text-neutral-500">Qué hace, de verdad</p>
  <h2 class="mt-2 text-3xl tracking-tight">Cuatro cosas. Sin mosaico.</h2>
  <ol class="mt-12 divide-y divide-black/10">
    <li class="grid md:grid-cols-12 gap-4 py-8">
      <span class="mono text-xs text-neutral-500 md:col-span-2">01</span>
      <h3 class="text-xl md:col-span-4">Conteo por denominación</h3>
      <p class="md:col-span-6 text-neutral-600">Anotás 20.000, 10.000, 2.000 y el resto. El total y la diferencia salen solos.</p>
    </li>
    <li class="grid md:grid-cols-12 gap-4 py-8">
      <span class="mono text-xs text-neutral-500 md:col-span-2">02</span>
      <h3 class="text-xl md:col-span-4">Corte por sucursal</h3>
      <p class="md:col-span-6 text-neutral-600">Cruz del Sur, Naciones Unidas, Oro. Cada una con su encargado y su pendiente.</p>
    </li>
    <li class="grid md:grid-cols-12 gap-4 py-8">
      <span class="mono text-xs text-neutral-500 md:col-span-2">03</span>
      <h3 class="text-xl md:col-span-4">Calendario de depósitos</h3>
      <p class="md:col-span-6 text-neutral-600">Lunes, miércoles y viernes, con estado depositado o no. Sin una card de “scheduling”.</p>
    </li>
    <li class="grid md:grid-cols-12 gap-4 py-8">
      <span class="mono text-xs text-neutral-500 md:col-span-2">04</span>
      <h3 class="text-xl md:col-span-4">Diferencias anotadas</h3>
      <p class="md:col-span-6 text-neutral-600">Faltante o sobrante, con una observación. Queda en la semana, no en el chat.</p>
    </li>
  </ol>
</body>
</html>
```

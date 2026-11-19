# Pricing

Una tabla de precios es una decisión, no una galería de cards. La gente compara columnas, busca límites y quiere saber qué pasa si se pasa de plan. El oficio está en la comparación, no en el glow del plan “Pro”.

## Cuándo usarlo y cuándo no

**Usalo** cuando hay planes reales, con límites distintos. **No lo uses** si hay un solo precio (ahí basta una frase y un botón) o si todavía no sabés los números: no inventes tarifas.

## Qué se ve con terminación pro

- Una fila de features compartida (tabla o lista alineada), no tres cards con bullets que no coinciden.
- El plan recomendado se marca con un filete, una ceja o un fondo apenas distinto — no con un degradé, una corona ni “Most popular” en pill violeta.
- Precios en una cara mono o en un peso que no pelee con el titular. Periodicidad clara (por mes, por año, IVA).
- Footnotes para los asteriscos: overage, seats, “custom” que realmente tiene una conversación de ventas.
- Un camino para “no estoy seguro”: calculadora, “empezar gratis” o “hablar”. No tres CTAs gritones.

Referentes de tono, no para calcar: [Stripe](https://stripe.com/), [Cal.com](https://cal.com/), [Resend](https://resend.com/).

## Qué hace mal el default de IA

- Tres cards idénticas (`rounded-2xl shadow-xl`), la del medio escalada a `scale-105` con un badge índigo.
- Features que son slogans (“AI-powered insights”, “Priority support”) en vez de límites medibles.
- Precio en Inter ExtraBold a 72 px y un `/mo` diminuto ilegible.
- Toggle mensual/anual que no cambia de verdad los números, o un “Save 20%” sin hacer la cuenta.
- Un plan Enterprise que dice “Custom” y un botón “Get started” igual al del plan free.

## Tipografía del kit

- Titular de sección: [Cabinet Grotesk](../tipografias/sans-grotesk.md) o [Switzer](../tipografias/sans-grotesk.md).
- Precio: [IBM Plex Mono](../tipografias/mono.md).
- Cuerpo: [Satoshi](../tipografias/sans-geometrica.md).

## Snippet

Comparación en tabla, un plan marcado con un filete óxido, precios en mono. Sin cards gemelas.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=satoshi@400,500,600&f[]=cabinet-grotesk@500&display=swap">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500&display=swap" rel="stylesheet">
  <style>
    body { font-family: "Satoshi", sans-serif; background: #f7f5f0; color: #171513; }
    h2 { font-family: "Cabinet Grotesk", sans-serif; }
    .mono { font-family: "IBM Plex Mono", ui-monospace, monospace; }
  </style>
</head>
<body class="max-w-4xl mx-auto px-6 py-20">
  <h2 class="text-3xl tracking-tight">Planes, en una sola vista</h2>
  <p class="mt-2 text-neutral-600">Los números tienen que compararse en fila, no en tres afiches.</p>
  <div class="mt-10 overflow-x-auto">
    <table class="w-full text-sm text-left">
      <thead>
        <tr class="border-b border-black/15">
          <th class="py-3 font-medium"></th>
          <th class="py-3 font-medium">Solo</th>
          <th class="py-3 font-medium border-x border-[#9a4a2a]/40 bg-[#9a4a2a]/5 px-4">Taller <span class="block text-xs font-normal text-[#9a4a2a]">Recomendado</span></th>
          <th class="py-3 font-medium">Estudio</th>
        </tr>
      </thead>
      <tbody class="text-neutral-700">
        <tr class="border-b border-black/10">
          <td class="py-3">Precio / mes</td>
          <td class="mono">USD 0</td>
          <td class="mono border-x border-[#9a4a2a]/40 bg-[#9a4a2a]/5 px-4">USD 29</td>
          <td class="mono">USD 79</td>
        </tr>
        <tr class="border-b border-black/10">
          <td class="py-3">Sucursales</td>
          <td>1</td>
          <td class="border-x border-[#9a4a2a]/40 bg-[#9a4a2a]/5 px-4">Hasta 5</td>
          <td>Ilimitadas</td>
        </tr>
        <tr class="border-b border-black/10">
          <td class="py-3">Cierres guardados</td>
          <td>30 días</td>
          <td class="border-x border-[#9a4a2a]/40 bg-[#9a4a2a]/5 px-4">2 años</td>
          <td>Ilimitado</td>
        </tr>
        <tr>
          <td class="py-4"></td>
          <td><a href="#" class="border-b border-black/40 pb-0.5">Empezar</a></td>
          <td class="border-x border-[#9a4a2a]/40 bg-[#9a4a2a]/5 px-4 py-4"><a href="#" class="inline-block bg-[#171513] text-[#f7f5f0] px-3 py-2">Elegir Taller</a></td>
          <td><a href="#" class="border-b border-black/40 pb-0.5">Hablar</a></td>
        </tr>
      </tbody>
    </table>
  </div>
  <p class="mt-4 text-xs text-neutral-500">Precios de ejemplo para el snippet, no tarifas reales. En un sitio de verdad, no inventes números.</p>
</body>
</html>
```

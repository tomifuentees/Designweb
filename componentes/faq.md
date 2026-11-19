# FAQ

Un FAQ bueno responde las dudas que aparecen en ventas, en soporte o en la calle. Un FAQ malo es un bloque SEO con preguntas que nadie hizo (“What is [Product]?”).

## Cuándo usarlo y cuándo no

**Usalo** cerca de pricing o de un formulario, con 4–8 preguntas reales. **No lo uses** como índice del sitio, ni para esconder información que debería estar en la página (límites del plan, política de reembolso).

## Qué se ve con terminación pro

- Preguntas en el lenguaje del usuario (“¿Puedo depositar sin los de 100, 200 y 500?”), no en el de la marca (“How does our flexible banking module work?”).
- Acordeón nativo (`<details>`) o un componente con teclado bien resuelto (Radix/Base UI Accordion). El ícono es un plus/chevron que rota una vez, no un lottie.
- Una pregunta abierta a la vez, o todas legibles en mobile si son cortas. No un muro cerrado que obliga a cazar.
- Un escape: “¿No está tu pregunta? Escribinos”, con un link real.
- Respuestas concretas, con números y excepciones. Si la respuesta es “depende”, decí de qué.

## Qué hace mal el default de IA

- Diez preguntas genéricas (“Is there a free trial?”, “Is my data secure?”) con respuestas de lorem.
- Accordion shadcn default, `plus` lucide, bordes `rounded-xl`, abierto con un fade.
- Schema.org copiado y preguntas inventadas para “SEO”.
- FAQ que repite el copy del hero.
- Sin `:focus-visible` y sin poder abrir dos ítems si el usuario quiere comparar.

## Tipografía del kit

- Pregunta: [Satoshi](../tipografias/sans-geometrica.md) o [Switzer](../tipografias/sans-grotesk.md), peso medio.
- Respuesta: la misma familia, peso regular, un tono más bajo.

## Snippet

`<details>` nativo, filete, sin íconos de librería.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=satoshi@400,500,600&display=swap">
  <style>
    body { font-family: "Satoshi", sans-serif; background: #f7f5f0; color: #171513; }
    details + details { border-top: 1px solid rgba(23,21,19,.12); }
    summary { cursor: pointer; list-style: none; }
    summary::-webkit-details-marker { display: none; }
    summary::after { content: "+"; float: right; font-weight: 500; }
    details[open] summary::after { content: "–"; }
  </style>
</head>
<body class="max-w-2xl mx-auto px-6 py-20">
  <h2 class="text-2xl font-medium tracking-tight">Preguntas que aparecen de verdad</h2>
  <div class="mt-8 border-y border-black/10">
    <details class="py-4" open>
      <summary class="font-medium pr-8">¿Puedo dejar afuera los billetes de 100, 200 y 500?</summary>
      <p class="mt-3 text-neutral-600 text-sm leading-relaxed">Sí. El total del depósito es la suma de las denominaciones que llevás al banco. El cambio chico queda anotado aparte, para que no ensucie la boleta.</p>
    </details>
    <details class="py-4">
      <summary class="font-medium pr-8">¿Qué pasa si el banco cuenta menos?</summary>
      <p class="mt-3 text-neutral-600 text-sm leading-relaxed">Pedí el detalle por denominación y comparalo con tu conteo. Un faltante redondo (20.000) suele ser un billete o un fajo. Dejalo documentado en depósitos, con la observación “diferencia banco”.</p>
    </details>
    <details class="py-4">
      <summary class="font-medium pr-8">¿Puedo sumar el efectivo del fin de semana al lunes?</summary>
      <p class="mt-3 text-neutral-600 text-sm leading-relaxed">Podés, pero entonces el cierre del lunes no va a coincidir con el resumen de un solo día. Anotá el origen en observaciones, o pedí los resúmenes del sábado y del domingo para cruzarlos.</p>
    </details>
  </div>
  <p class="mt-6 text-sm text-neutral-600">¿Otra duda? <a href="#" class="border-b border-[#171513]">Escribir a soporte</a>.</p>
</body>
</html>
```

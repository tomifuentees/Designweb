# Hero

La primera pantalla no es un poster. Es una frase que alguien puede repetir, un objeto (producto, foto, cifra) y una sola acción. El resto es ruido.

Se lleva bien con [`../estilos/expresivo-minimo.md`](../estilos/expresivo-minimo.md), [`../estilos/editorial-revista.md`](../estilos/editorial-revista.md) o [`../estilos/catalogo-tecnico.md`](../estilos/catalogo-tecnico.md). Evitá arrancar por default con [`../estilos/estilo-linear.md`](../estilos/estilo-linear.md) o un glow de Aceternity si el producto no lo pide.

## Cuándo usarlo y cuándo no

**Usalo** en una landing, un estudio, un SaaS que tiene algo concreto para mostrar. **No lo uses** como bloque genérico en un dashboard, ni apilado con un segundo hero “de features”.

## Qué se ve con terminación pro

- Una promesa en una o dos líneas, con una sola rareza tipográfica (una itálica, un mono en la cifra, un filete).
- El producto o una imagen con recorte deliberado, no un mockup de dashboard genérico flotando en un degradé.
- Un CTA primario y, como mucho, uno secundario con menos peso (un texto subrayado, no un segundo pill).
- Prueba corta al lado: un logo, una cifra, una frase de un cliente con nombre real. No una fila de ocho logos grises.
- Mucho aire. El hero no tiene que llenar el viewport de objetos.

## Qué hace mal el default de IA

- Hero centrado, titular en Inter/Geist Black, subtítulo de marketing intercambiable (“La plataforma definitiva para…”) y un degradé violeta-índigo.
- Eyebrow en mayúsculas con un puntito o un badge “New” en cada sección.
- Dos botones pill (Get started + Learn more) y un mockup de Safari con un dashboard inventado.
- Fade-in de todo el bloque al cargar, y un `bg-gradient-to-r from-indigo-500 to-purple-500` en el título.
- Tres cards de features metidas *dentro* del hero.

En r/web_design (2026) esta receta es exactamente lo que llaman “vibecoded”. Ver [`fuentes-investigacion.md`](./fuentes-investigacion.md).

## Tipografía del kit

- Titular: [Cabinet Grotesk](../tipografias/sans-grotesk.md) o [Fraunces](../tipografias/serif-display.md) en una sola palabra itálica.
- Cuerpo: [Satoshi](../tipografias/sans-geometrica.md).
- Cifra o ceja: [IBM Plex Mono](../tipografias/mono.md).

## Snippet

Fondo crema, un acento óxido, Fraunces solo en una palabra, CTA como filete. No hay degradé ni tres cards.

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
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@1,9..144,500&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
  <style>
    body { font-family: "Satoshi", sans-serif; background: #f4efe6; color: #1c1915; }
    em { font-family: "Fraunces", serif; font-style: italic; font-weight: 500; }
    .mono { font-family: "IBM Plex Mono", ui-monospace, monospace; }
  </style>
</head>
<body>
  <section class="max-w-6xl mx-auto px-6 py-24 md:py-32 grid md:grid-cols-12 gap-10 items-end">
    <div class="md:col-span-7">
      <p class="mono text-xs tracking-[0.16em] uppercase text-[#9a4a2a]">Caja · diario</p>
      <h1 class="mt-4 text-5xl md:text-6xl font-medium tracking-tight leading-[1.05]">El cierre de caja, <em>sin</em> la planilla eterno.</h1>
      <p class="mt-6 text-lg text-neutral-600 max-w-xl">Contás los billetes, ves la diferencia por sucursal y dejás el depósito listo. Una sola pantalla, no un deck de features.</p>
      <div class="mt-10 flex flex-wrap items-baseline gap-8">
        <a href="#" class="bg-[#1c1915] text-[#f4efe6] px-5 py-3 text-sm font-medium">Empezar el conteo</a>
        <a href="#" class="border-b border-[#9a4a2a] text-[#9a4a2a] pb-0.5 text-sm">Ver un cierre de ejemplo</a>
      </div>
    </div>
    <aside class="md:col-span-5 border-t border-[#1c1915]/15 pt-6">
      <p class="mono text-xs text-neutral-500">Último cierre · 17.11</p>
      <p class="mt-2 text-4xl font-medium tracking-tight">$ 3.290.850</p>
      <p class="mt-2 text-sm text-neutral-600">Efectivo pasado a caja encargado, cruzado por sucursal. Sin mockup inventado.</p>
    </aside>
  </section>
</body>
</html>
```

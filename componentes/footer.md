# Footer

El footer es el mapa de lo que el header no pudo mostrar: legal, contacto, idiomas, un last-chance de orientación. No es un segundo hero ni un cementerio de doce columnas.

## Cuándo usarlo y cuándo no

**Usalo** en casi cualquier sitio de marketing o docs. **No lo uses** dentro de una app logueada como si fuera una landing (ahí suele bastar un subtítulo de versión y un link legal).

## Qué se ve con terminación pro

- Una estructura predecible: marca corta + una frase, 2–4 grupos de links, contacto o dirección si es un negocio local, legal al final en una línea.
- Tipografía más chica que el cuerpo, contraste todavía AA. Links con hover y focus claros.
- El legal no se esconde: razón social, jurisdicción, links a privacidad y términos.
- Si hay newsletter, un campo con etiqueta visible y un compromiso (“un mail por semana, sin secuencia de venta”). Si no lo vas a mandar, no lo pongas.
- Idioma y moneda, si aplican, no un selector decorativo.
- Un tono que coincide con el sitio: un footer “playful” con 40 íconos sociales en un estudio editorial se lee falso.

Referentes de contención: [Vitsœ](https://www.vitsoe.com/), [Cal.com](https://cal.com/), [The Gentlewoman](https://thegentlewoman.co.uk/).

## Qué hace mal el default de IA

- Cuatro o cinco columnas de links inventados (Company, Product, Resources, Legal, Social) con 15 ítems cada una.
- Fondo negro, logo grande, una fila de íconos de redes (incluida una que la marca no usa) y un CTA “Join our newsletter” con el botón índigo.
- Copyright `© 2024` desactualizado, o “Made with ❤️”.
- Duplicar la navbar completa.
- Contraste roto: gris 400 sobre gris 800 que no pasa AA.

## Tipografía del kit

- Nombre / marca: la sans del sitio, un peso medio.
- Links: [Satoshi](../tipografias/sans-geometrica.md) a 13–14 px.
- Legal: un punto más chico, no un gray desaparecido.

## Snippet

Tres grupos, una línea legal, sin redes de adorno.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=satoshi@400,500,600&display=swap">
  <style>
    body { font-family: "Satoshi", sans-serif; }
  </style>
</head>
<body>
  <footer class="border-t border-black/10 bg-[#f4f1ea] text-[#1b1915]">
    <div class="max-w-6xl mx-auto px-6 py-16 grid md:grid-cols-12 gap-10 text-sm">
      <div class="md:col-span-4">
        <p class="font-semibold tracking-tight">Caja</p>
        <p class="mt-2 text-neutral-600 max-w-xs">Herramienta de conteo y depósitos para un equipo chico de administración.</p>
      </div>
      <div class="md:col-span-3">
        <p class="text-xs uppercase tracking-[0.14em] text-neutral-500">Producto</p>
        <ul class="mt-3 space-y-2">
          <li><a href="#" class="hover:border-b border-current">Conteo</a></li>
          <li><a href="#" class="hover:border-b border-current">Depósitos</a></li>
          <li><a href="#" class="hover:border-b border-current">Precios</a></li>
        </ul>
      </div>
      <div class="md:col-span-3">
        <p class="text-xs uppercase tracking-[0.14em] text-neutral-500">Estudio</p>
        <ul class="mt-3 space-y-2">
          <li><a href="#" class="hover:border-b border-current">Oficio</a></li>
          <li><a href="#" class="hover:border-b border-current">Contacto</a></li>
        </ul>
      </div>
      <div class="md:col-span-2">
        <p class="text-xs uppercase tracking-[0.14em] text-neutral-500">Legal</p>
        <ul class="mt-3 space-y-2">
          <li><a href="#" class="hover:border-b border-current">Privacidad</a></li>
          <li><a href="#" class="hover:border-b border-current">Términos</a></li>
        </ul>
      </div>
    </div>
    <div class="max-w-6xl mx-auto px-6 py-4 border-t border-black/10 text-xs text-neutral-500 flex flex-wrap gap-4 justify-between">
      <p>© 2026 Nombre real de la empresa. Ciudad, país.</p>
      <p>Sin íconos de redes que no usamos.</p>
    </div>
  </footer>
</body>
</html>
```

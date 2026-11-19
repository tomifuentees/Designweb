# Testimonials

Una cita sirve si se puede atribuir y si dice algo que el marketing no puede decir solo (“pasamos el cierre de 40 minutos a 12”). Un slider de avatares inventados no suma confianza: la resta.

## Cuándo usarlo y cuándo no

**Usalo** cuando tenés clientes reales dispuestos a firmar nombre, rol y, si se puede, empresa o ciudad. **No lo uses** para rellenar la landing, ni con fotos de stock, ni con quotes que parecen salidas de un prompt (“¡Este producto cambió nuestro workflow!”).

## Qué se ve con terminación pro

- Una, tres o cinco citas, no un carrusel infinito de diez.
- Nombre real, rol, y una fuente verificable (link a LinkedIn o al caso). Si no hay permiso, no la publiques.
- Tipografía con voz: una serif de lectura para la cita, una sans chica para la atribución. Ver [`../estilos/editorial-revista.md`](../estilos/editorial-revista.md).
- Si hay retrato, que sea una foto verdadera, recortada con el mismo criterio que el resto del sitio — no un círculo con anillo degradé.
- El logo del cliente, si aparece, es un apoyo, no una fila de “as seen in” falsa.

## Qué hace mal el default de IA

- Slider infinito con 5 estrellas doradas, comillas gigantes y un avatar de thispersondoesnotexist.
- Tres cards gemelas, `shadow-lg`, el texto intercambiable.
- Nombres en inglés genéricos (Sarah J., CTO at TechCorp) en un producto que no tiene esos clientes.
- Autoplay del carrusel que no se puede pausar (malo también para accesibilidad).
- Testimonios arriba del fold, antes de explicar el producto.

## Tipografía del kit

- Cita: [Newsreader](../tipografias/serif-texto.md) o [Fraunces](../tipografias/serif-display.md) itálica, con optical size.
- Atribución: [Satoshi](../tipografias/sans-geometrica.md).

## Snippet

Una sola cita editorial, sin estrellas ni slider. El texto es un *placeholder de forma*: en producción, solo citas reales.

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
  <link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@1,6..72,400&display=swap" rel="stylesheet">
  <style>
    body { font-family: "Satoshi", sans-serif; background: #f6f1ea; color: #1c1915; }
    blockquote { font-family: "Newsreader", serif; font-style: italic; }
  </style>
</head>
<body class="max-w-3xl mx-auto px-6 py-24">
  <figure>
    <blockquote class="text-3xl md:text-4xl leading-snug tracking-tight">
      “Antes cerrábamos la caja en un cuaderno y un Excel suelto. Ahora el faltante queda anotado el mismo día, por sucursal.”
    </blockquote>
    <figcaption class="mt-8 text-sm text-neutral-600">
      <span class="font-medium text-[#1c1915]">Nombre, Apellido</span>
      <span class="mx-2 text-neutral-400">·</span>
      Rol, Empresa — reemplazar por una cita real, o no publicar la sección.
    </figcaption>
  </figure>
</body>
</html>
```

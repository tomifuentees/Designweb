# Empty states

La pantalla vacía es el primer producto que ve un usuario nuevo, y el más honesto cuando un filtro no devuelve nada. Diseñarla es tan parte del oficio como el dashboard lleno. El default de IA o la ignora, o la llena con una ilustración 3D genérica.

## Cuándo usarlo y cuándo no

**Usalo** en listas, búsquedas, bandejas, onboarding, permisos denegados, errores 404/500. **No lo uses** como una landing dentro de la app, ni como un chiste que no ayuda a dar el siguiente paso.

## Qué se ve con terminación pro

- Distinguí los casos: **aún no hay datos**, **el filtro no encontró**, **no tenés permiso**, **algo falló**. No es el mismo copy ni la misma acción.
- Un título concreto (“Todavía no hay depósitos esta semana”), un párrafo de una línea, una acción primaria (“Anotar el primero”).
- Si hay ilustración, que sea del sistema de la marca (un trazo, un ícono único). Preferible cero ilustración a un “empty state kit” de unibrow characters.
- En una tabla, el empty vive *dentro* de la tabla (una fila que ocupa el ancho), no en otra página.
- El 404 dice a dónde ir. El 500 no culpa al usuario y ofrece reintentar o un contacto.

## Qué hace mal el default de IA

- “Nothing here yet ✨” + una ilustración isometric de un astronauta o un cactus, botón índigo “Get started”.
- El mismo empty para “no hay resultados de búsqueda” y para “no tenés acceso”.
- Un lottie infinito que no se puede apagar con `prefers-reduced-motion`.
- Un empty que parece un error, o un error que parece un empty.
- Copy en inglés en una app en español.

## Tipografía del kit

- Título: la sans de UI, peso medio, no una display.
- Cuerpo: [Satoshi](../tipografias/sans-geometrica.md).

## Snippet

Vacío de lista, una acción, sin ilustración.

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
  </style>
</head>
<body class="min-h-screen flex items-center justify-center px-6">
  <div class="max-w-sm text-center">
    <h1 class="text-xl font-medium tracking-tight">Todavía no hay depósitos esta semana</h1>
    <p class="mt-2 text-sm text-neutral-600">Cuando anotes el de lunes, miércoles o viernes, va a aparecer acá con su monto y su estado.</p>
    <a href="#" class="inline-block mt-6 bg-[#171513] text-[#f7f5f0] px-4 py-2 text-sm">Anotar el primero</a>
  </div>
</body>
</html>
```

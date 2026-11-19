# Formularios

El formulario es de las piezas donde más se nota un diseño de IA: solo existe el happy path. Un form pro se diseña en cuatro estados — **vacío, carga, error y éxito** — y en los detalles (label visible, error al lado del campo, no borrar lo que el usuario ya escribió).

Las primitivas de [Base UI](https://base-ui.com/), [Radix](https://www.radix-ui.com/) o [React Aria](https://react-aria.adobe.com/) resuelven el teclado y el foco. coss ui y shadcn aportan patrones de campo. Esto no reemplaza esa base: muestra el criterio visual y de copy.

## Cuándo usarlo y cuándo no

**Usalo** en login, contacto, alta, cobro, cualquier cosa que pida datos. **No lo uses** como un “multi-step wizard” de seis pantallas si son cuatro campos.

## Qué se ve con terminación pro

- **Label visible siempre**, no un placeholder que desaparece y deja al usuario a ciegas. El placeholder, si existe, es un ejemplo (`201-650`), no la instrucción.
- Orden de tab lógico, `autocomplete` correcto, tipo de teclado en mobile (`inputmode`, `type="email"`).
- Errores: un resumen arriba *y* un mensaje bajo el campo, en texto (no solo color). `aria-invalid` y `aria-describedby`. El campo no se vacía.
- Carga: el botón entra en estado pending, no se puede reenviar, hay un texto “Enviando…”. No un spinner eterno sin aviso.
- Éxito: una confirmación concreta (“Te mandamos un mail a …”), no un toast verde que se va en 2 segundos si el resultado es irreversible.
- Vacío: la primera vez que se abre, un ejemplo o una ayuda corta, no un muro de validaciones anticipadas (no grites “requerido” antes de que interactúe).
- Contraseña: mostrar/ocultar, requisitos dichos *antes* de fallar, no después en una lista roja.
- Campos opcionales marcados como opcionales, no al revés.

## Qué hace mal el default de IA

- Labels flotando, un solo botón índigo, validación solo con `required` del browser.
- Error genérico “Something went wrong” sin el campo ni el motivo.
- Deshabilitar el botón hasta que el form esté “perfecto”, sin decir qué falta.
- Custom select inaccesible, date picker inventado, checkbox que no se puede tabinear.
- Mensajes en inglés en un form en español, o al revés.
- Éxito y error resueltos solo con color (rojo/verde), ilegibles para daltonismo.

## Tipografía del kit

- Labels y cuerpo: [Satoshi](../tipografias/sans-geometrica.md) o [Figtree](../tipografias/sans-grotesk.md).
- Códigos / IDs: [IBM Plex Mono](../tipografias/mono.md).

## Snippet

Un campo en error, uno opcional, botón en carga. Copy en español.

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
    label { display: block; font-size: 0.875rem; font-weight: 500; margin-bottom: 0.35rem; }
    input { width: 100%; border: 1px solid rgba(23,21,19,.25); background: #fff; padding: .6rem .7rem; font: inherit; }
    input:focus { outline: 2px solid #171513; outline-offset: 2px; }
    input[aria-invalid="true"] { border-color: #8b1e1e; }
  </style>
</head>
<body class="max-w-md mx-auto px-6 py-16">
  <h1 class="text-2xl font-medium tracking-tight">Anotar una diferencia</h1>
  <p class="mt-2 text-sm text-neutral-600" id="form-error" role="alert">Revisá el monto: hace falta un número, sin puntos de mil o con ellos, pero no letras.</p>
  <form class="mt-8 space-y-5" action="#" method="post">
    <div>
      <label for="monto">Monto de la diferencia</label>
      <input id="monto" name="monto" inputmode="decimal" autocomplete="off" value="veinte mil" aria-invalid="true" aria-describedby="monto-error form-error">
      <p id="monto-error" class="mt-1 text-sm text-[#8b1e1e]">Ingresá un número. Ejemplo: 20000.</p>
    </div>
    <div>
      <label for="nota">Observación <span class="font-normal text-neutral-500">(opcional)</span></label>
      <input id="nota" name="nota" maxlength="140" placeholder="Ej. diferencia banco, 16/11">
    </div>
    <button type="submit" disabled class="bg-[#171513] text-[#f7f5f0] px-4 py-2.5 text-sm disabled:opacity-60">
      Guardando…
    </button>
    <p class="text-xs text-neutral-500">El botón se bloquea mientras corre el envío, para no duplicar la nota.</p>
  </form>
</body>
</html>
```

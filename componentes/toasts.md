# Toasts

Un toast es un aviso transitorio de algo que ya pasó (“Depósito guardado”) o de algo que se puede deshacer. No es un diálogo, no es un banner de error de formulario, y no es el único lugar donde vive un resultado irreversible.

Radix y Base UI tienen Toast; shadcn lo envuelve. La terminación pro está en *cuándo* sale, cuánto dura y si se puede echar.

## Cuándo usarlo y cuándo no

**Usalo** para confirmaciones de baja gravedad, undo, “se copió al portapapeles”, sync en segundo plano. **No lo uses** para errores de un form (van al lado del campo), para permisos, para “¿estás seguro de borrar?”, ni para un mensaje que el usuario *tiene* que leer.

## Qué se ve con terminación pro

- Aparece cerca de la esquina (o debajo del header, según el sistema), con un solo renglón y, si hace falta, una acción (“Deshacer”).
- Duración: 4–6 s para un success; un error que no tiene pantalla propia dura más o se queda hasta que lo cierren.
- Pausa al hover y al foco. Botón de cerrar visible. No más de dos toasts a la vez; los nuevos reemplazan o se apilan con criterio, no en una torre de ocho.
- `role="status"` para un success, `role="alert"` para un error. Respetá `prefers-reduced-motion`: sin bounce, un fade corto o nada.
- El color no es el único canal: un verbo (“No se pudo guardar”) además de un fondo rojo.

## Qué hace mal el default de IA

- Toast que entra rebotando desde abajo, con un check verde gigante y un “Success!” en inglés.
- Cada clic dispara un toast (“Welcome!”, “Item added!”, “You’re doing great!”).
- Un error crítico que desaparece a los 2 segundos y no queda en ningún lado.
- Apilados en las cuatro esquinas, o un sistema de “sonner” default sin tokenizar.
- Toasts que no se pueden cerrar con teclado, o que roban el foco.

## Tipografía del kit

- La sans de UI a 13–14 px, un peso medio. Sin display, sin mono salvo un ID corto.

## Snippet

Aviso quieto, acción de deshacer, botón de cerrar. Animación mínima en CSS, apagada si hay reduced motion.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=satoshi@400,500&display=swap">
  <style>
    body { font-family: "Satoshi", sans-serif; background: #f3f1ec; color: #171513; }
    .toast { animation: in .25s ease-out; }
    @keyframes in { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: none; } }
    @media (prefers-reduced-motion: reduce) { .toast { animation: none; } }
  </style>
</head>
<body class="min-h-screen relative">
  <div class="fixed bottom-6 right-6 max-w-sm w-full border border-black/10 bg-[#faf8f4] shadow-[0_1px_2px_rgba(0,0,0,.06)] p-3 flex items-start gap-3 toast" role="status">
    <p class="text-sm flex-1">Depósito del viernes guardado como pendiente.</p>
    <button type="button" class="text-sm border-b border-current">Deshacer</button>
    <button type="button" class="text-sm text-neutral-500" aria-label="Cerrar">×</button>
  </div>
</body>
</html>
```

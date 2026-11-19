# Navbar

La barra no es un preview del brand book. Es un instrumento: dónde estoy, a dónde puedo ir, qué acción importa. Tiene que sobrevivir al scroll, al mobile y a un usuario que ya conoce el producto.

Encaja con casi cualquier estilo; se rompe cuando se disfraza de isla de glass o de menú experimental en un SaaS de trabajo. Ver [`../estilos/navegacion-experimental.md`](../estilos/navegacion-experimental.md) (alto riesgo) y [`../estilos/ui-casi-invisible.md`](../estilos/ui-casi-invisible.md).

## Cuándo usarlo y cuándo no

**Usalo** en sitios de varias secciones, apps y docs. **No lo uses** como un header gigante de 160 px con logo animado, o como única navegación si el producto pide un sidebar.

## Qué se ve con terminación pro

- Altura contenida (56–64 px), logo a la izquierda, links en un solo renglón, una acción a la derecha.
- El ítem activo se marca con un filete, un peso o un puntito — no con un pill de fondo índigo.
- Al hacer scroll, o bien se vuelve más densa (fondo sólido, borde inferior de 1 px), o bien se esconde y reaparece al subir. No “flota” con blur y sombra de plantilla si el resto del sitio es plano.
- Mobile: un botón claro, un panel o un sheet que no tape el CTA, y los mismos destinos que en desktop (no un menú distinto inventado).
- Estado de sesión visible (entrar / la inicial de la cuenta). El buscador, si existe, no es un ícono perdido: tiene un atajo (`/` o `⌘K`) anunciado en mono.

## Qué hace mal el default de IA

- Navbar `fixed` con `backdrop-blur`, borde blanco al 10%, logo Inter Bold y links `space-x-8` genéricos (Features, Pricing, Blog, Docs).
- CTA “Get started” en pill índigo *y* un “Sign in” también en botón.
- Menú mobile que es un overlay a pantalla completa con los links a 40 px y un degradé.
- Links que no tienen `:focus-visible`, ni estado actual, ni `aria-expanded` en el toggle.
- Un segundo renglón de anuncios (“New: AI copilot ✨”) que empuja el contenido.

## Tipografía del kit

- UI: [Satoshi](../tipografias/sans-geometrica.md) o [Switzer](../tipografias/sans-grotesk.md), un solo peso medio.
- Atajo o label técnico: [IBM Plex Mono](../tipografias/mono.md).

## Snippet

Barra baja, filete en el ítem activo, atajo en mono, toggle con `aria`. Sin blur.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=satoshi@500,600&display=swap">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
  <style>
    body { font-family: "Satoshi", sans-serif; background: #f7f5f0; color: #171513; }
    .mono { font-family: "IBM Plex Mono", ui-monospace, monospace; }
  </style>
</head>
<body>
  <header class="border-b border-black/10 bg-[#f7f5f0]">
    <div class="max-w-6xl mx-auto px-6 h-14 flex items-center gap-8">
      <a href="#" class="font-semibold tracking-tight">Caja</a>
      <nav class="hidden md:flex items-center gap-6 text-sm" aria-label="Principal">
        <a href="#" class="text-neutral-600 hover:text-[#171513]">Sucursales</a>
        <a href="#" class="border-b-2 border-[#171513] pb-0.5">Depósitos</a>
        <a href="#" class="text-neutral-600 hover:text-[#171513]">Diferencias</a>
      </nav>
      <div class="ml-auto flex items-center gap-3">
        <button type="button" class="hidden md:inline-flex items-center gap-2 text-xs text-neutral-500 border border-black/10 px-2 py-1">
          Buscar <kbd class="mono text-[10px]">/</kbd>
        </button>
        <a href="#" class="text-sm border-b border-[#171513] pb-0.5">Entrar</a>
        <button type="button" class="md:hidden text-sm" aria-expanded="false" aria-controls="nav-m">Menú</button>
      </div>
    </div>
  </header>
</body>
</html>
```

# Easing y duración

La IA improvisa `duration-500 ease-in-out` para todo, o un `spring` de Motion con bounce en un botón de “Guardar”. El oficio es más aburrido, y se siente más caro.

## Duraciones de UI (punto de partida)

| Gesto | Duración | Notas |
|---|---|---|
| Press / `:active` | 80–120 ms | Tiene que sentirse instantáneo |
| Hover de color o underline | 120–180 ms | Ease-out |
| Tooltip / toast entrada | 150–220 ms | Sin bounce |
| Popover, dialog, dropdown | 160–240 ms | `@starting-style` o Motion; exit un poco más corto |
| Reveal de un bloque | 400–600 ms | Una sola vez |
| Count-up de un número | 600–900 ms | Ease-out fuerte al final |
| Cambio de página (View Transition) | 200–350 ms | Morph de un elemento, no un fade de 1 s |
| Loop (marquee, spin de un loader) | 20–40 s el marquee; 700–1000 ms un spinner | Lineal en el loop |

Si algo tarda más de un segundo en *entrar*, casi seguro está atrasando la lectura. El scrollytelling es otra categoría: el tiempo lo marca el scroll, no el clock.

## Curvas

- **Entrada en escena (aparece, abre, entra desde abajo):** `ease-out` o `cubic-bezier(0.16, 1, 0.3, 1)` (un “ease-out expo” suave). Arranca con decisión, frena.
- **Salida (cierra, se va):** `ease-in` o un out más corto. El exit puede durar 70–80% del enter.
- **Movimiento de un lado a otro (un handle, un tab indicator):** `ease-in-out` suave, o un spring *muy* corto en Motion (`stiffness` alto, `damping` alto, sin bounce).
- **Loops:** `linear`. Un marquee con ease-in-out se siente borracho.
- **Springs con rebote:** solo si el objeto es físico y lúdico (un like, un ícono de juego). Nunca en un input, un toast de error, un precio o un modal de un banco.

En GSAP, `power2.out` y `power3.out` cubren el 90% de la UI. `elastic` y `bounce` son una decisión de marca, no un default. En Motion, `type: "tween"` con `ease: [0.16, 1, 0.3, 1]` es más predecible que el spring default para chrome de producto.

## Cuándo no animar

- El primer paint de un texto de lectura (párrafos, tablas densas).
- Un cambio de valor operativo en un dashboard, si el usuario está tratando de comparar (ahí, `tabular-nums` y punto).
- Cualquier cosa cuando `prefers-reduced-motion: reduce`.
- Un layout shift disfrazado de motion (`top`, `height`, `margin` animados en un documento que se lee). Preferí `transform` y `opacity`.
- Diez reveals en cadena. Uno, o un stagger corto, y el resto estático.

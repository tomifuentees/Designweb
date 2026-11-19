# Scrollytelling

Bubble lo da por establecido en 2026: el scroll no se secuestra, se *usa* para revelar una narrativa —animaciones y bloques que aparecen o se transforman según la posición—. Lo distingue del scroll-jacking, que marca como tendencia en retirada porque es lento y pelea con el dispositivo de todos los días. Las product pages de Apple son la referencia que más se menciona; Bubble cita además la landing de Recess. The Pudding lleva años en el long-form de datos. Envato habla de motion al servicio del relato, no de la demostración.

La regla de oro: cada sección tiene que tener sentido también si las animaciones están apagadas.

## Cuándo usarlo y cuándo no

**Usalo** en un lanzamiento de producto, un ensayo visual, un case, un relato de marca con principio y final.

**No lo uses** en un dashboard, en un pricing, en un blog post cotidiano o en una home que el usuario quiere *escanear*. No lo uses si no vas a construir un camino `prefers-reduced-motion` y un performance budget.

## Reglas concretas

- **Grilla:** Caps de “escena” a viewport (o a 80–120 vh), con un eje de lectura claro (típicamente de arriba abajo). En mobile, menos escenas, más stack.
- **Espaciado:** Cada escena necesita un ancla de lectura (un titular, un dato, una foto) que no dependa de estar a mitad de un tween.
- **Radios / bordes / sombras / color:** Los del estilo anfitrión (a menudo editorial o producto Apple-like). El scroll no es una paleta.
- **Motion:** `position: sticky` + cambios de opacidad / clip, o un canvas que reacciona al scroll *sin* bloquearlo. Nada de redefinir el wheel. Duraciones atadas al recorrido, no a un `setTimeout`.
- **Accesibilidad:** En `prefers-reduced-motion`, mostrá las escenas en un artículo estático, en el mismo orden. El contenido tiene que estar en el HTML, no solo pintado en un canvas.
- **Tipografía:** De lectura, porque hay un relato.
  - [Newsreader](../tipografias/serif-texto.md), [Fraunces](../tipografias/serif-display.md), [Source Serif 4](../tipografias/serif-texto.md), [Tiempos Text](../tipografias/serif-texto.md) / [Tiempos Headline](../tipografias/serif-display.md).
  - UI y cifras: [Switzer](../tipografias/sans-grotesk.md) o [IBM Plex Mono](../tipografias/mono.md).

## Sitios reales

- [www.apple.com/iphone](https://www.apple.com/iphone/) — la referencia de product page que Bubble menciona para scrollytelling (y, en general, las páginas de producto de [apple.com](https://www.apple.com/)).
- [takearecess.com](https://takearecess.com/) — Recess, el ejemplo de landing que cita Bubble.
- [pudding.cool](https://pudding.cool/) — ensayos visuales long-form, el scroll como herramienta de periodismo de datos.
- [locomotive.ca](https://locomotive.ca/) — estudio asociado a scroll y motion de alto oficio.

## Errores comunes

- Scroll-jacking (bloquear el wheel y “play” una timeline). Es justo lo que está en retirada.
- Escenas que, sin JS, son una página en blanco.
- Cinco librerías de motion en una landing de 4 MB de texturas.
- Animar cada heading al entrar al viewport (el fade-in universal de las landings de IA). El scrollytelling es una *secuencia*, no un on-scroll en todo.

## Snippet

Tres escenas con `sticky`. Sin JS. Con reduced-motion, se leen como un artículo.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500&family=Newsreader:opsz,wght@6..72,400&display=swap" rel="stylesheet">
  <style>
    body { font-family: "Newsreader", serif; background: #f6f3ee; color: #1c1916; }
    h2 { font-family: "Fraunces", serif; }
    .scene { min-height: 100vh; }
    @media (prefers-reduced-motion: reduce) {
      .scene { min-height: auto; padding: 3rem 0; }
      .sticky-title { position: static !important; }
    }
  </style>
</head>
<body>
  <article>
    <section class="scene max-w-3xl mx-auto px-6 flex items-center">
      <h2 class="text-5xl md:text-7xl leading-[1.05]">Primero, una afirmación.</h2>
    </section>
    <section class="scene relative max-w-3xl mx-auto px-6">
      <h2 class="sticky-title sticky top-8 text-4xl md:text-6xl bg-[#f6f3ee]/90 py-2">Después, el dato que la sostiene.</h2>
      <p class="mt-[40vh] pb-[40vh] text-xl leading-8">El bloque sigue scrolleando debajo. El titular se queda. Si el usuario pide menos motion, esto simplemente se lee, en el mismo orden.</p>
    </section>
    <section class="scene max-w-3xl mx-auto px-6 flex items-center">
      <h2 class="text-5xl md:text-6xl leading-[1.05]">Al final, una salida. No un loop.</h2>
    </section>
  </article>
</body>
</html>
```

# Tipografía cinética

Envato la pone primera entre las tendencias de 2026: el tipo que cambia de peso, se estira con el scroll, reacciona al hover o entra en el load. Las fuentes variables lo volvieron práctico (un archivo, interpolación en CSS). Figma habla de lettering cinético y pairings dinámicos en el hero (cita a Glossier y Samsung). Bubble la da por establecida, pone de ejemplo el sitio de Locomotive, y recoge una advertencia de StudioMeyer (retrospectiva 2026, citada por Bubble): “more polish than substance” si se abusa. La versión que aguanta es **un solo gesto fuerte** —casi siempre el titular del hero—, con fallback para `prefers-reduced-motion`.

Linear, en su ciclo 2025–2026, intercambia una palabra del headline: es cinética contenida, no un circus.

## Cuándo usarlo y cuándo no

**Usalo** en un hero, un lanzamiento, una opening de portfolio o una campaña. Un solo momento memorable.

**No lo uses** en navegación, en tablas, en precios, en body copy ni en cada heading de la página. No lo uses si no vas a testear teclado, screen reader (el texto tiene que seguir existiendo en el DOM) y reduced motion.

## Reglas concretas

- **Grilla:** El tipo *es* el layout del hero: puede ocupar el ancho, romperse en dos líneas, dejar que una palabra se mueva. El resto de la página vuelve a un ritmo quieto.
- **Espaciado:** Dejá margen para que el tipo se expanda sin recortarse ni tapar el CTA.
- **Radios / bordes / sombras / color:** Los del estilo anfitrión. La cinética no pide una paleta propia. Evitá animar además un degradé violeta: dos clichés a la vez.
- **Motion:** Preferí ejes de una variable (`font-weight`, `wdth`, `SOFT` / `opsz` en [Fraunces](../tipografias/serif-display.md) o [Bricolage Grotesque](../tipografias/sans-grotesk.md)) antes que un bounce de `translateY` en cada letra. Duración 400–800 ms, easing de verdad, no `linear`.
- **Accesibilidad:** `@media (prefers-reduced-motion: reduce) { * { animation: none; transition: none; } }` y un estado estático idéntico en contenido.
- **Tipografía:** Familias del catálogo con variable o con itálica memorable.
  - [Fraunces](../tipografias/serif-display.md), [Bricolage Grotesque](../tipografias/sans-grotesk.md), [Recursive](../tipografias/variable.md), [Roboto Flex](../tipografias/variable.md) (como *motor*, no como voz de marca), [Mona Sans](../tipografias/sans-grotesk.md), [Cabinet Grotesk](../tipografias/sans-grotesk.md), [Clash Display](../tipografias/display-experimental.md).
  - Una sola palabra en itálica ya es un gesto. No hace falta animar las diez.

## Sitios reales

- [linear.app](https://linear.app/) — Toimi describe un headline que intercambia “teams” y “agents”: cinética al servicio de un mensaje.
- [locomotive.ca](https://locomotive.ca/) — el ejemplo que cita Bubble (redirige a `/en`).
- [www.glossier.com](https://www.glossier.com/) — Figma la cita entre las marcas de tipografía expresiva / cinética en 2026.
- [www.samsung.com/us](https://www.samsung.com/us/) — citada por Figma en el mismo lote de tipo bold y motion. `samsung.com` redirige por región; esta ruta respondió 200.
- [basement.studio](https://basement.studio/) — tipo pesado y motion de estudio, útil como referencia de “un momento”, no de un sistema entero animado.

## Errores comunes

- Split de cada letra en un `<span>` que rompe el copiado, el SEO y el lector de pantalla.
- Scroll-jacking para “coreografiar” el tipo: Bubble lo da por tendencia en retirada, porque es lento.
- Animar peso *y* escala *y* color *y* blur a la vez.
- No probar el titular en mobile: una variable que enamora a 140 px puede romperse a 32.

## Snippet

Una palabra cuyo peso respira. Se apaga con reduced-motion.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400..800&display=swap" rel="stylesheet">
  <style>
    body { font-family: "Bricolage Grotesque", sans-serif; background: #f3f1ec; color: #161616; }
    .pulse { font-variation-settings: "wght" 500; animation: weight 2.8s ease-in-out infinite; }
    @keyframes weight {
      0%, 100% { font-variation-settings: "wght" 500; }
      50% { font-variation-settings: "wght" 800; }
    }
    @media (prefers-reduced-motion: reduce) {
      .pulse { animation: none; font-variation-settings: "wght" 700; }
    }
  </style>
</head>
<body class="min-h-screen flex items-center px-6">
  <h1 class="max-w-4xl text-5xl md:text-7xl leading-[1.02] font-medium">
    Una sola palabra <span class="pulse">respira</span>. El resto se queda quieto.
  </h1>
</body>
</html>
```

# Espacial / 3D

Figma abre sus tendencias 2026 con profundidad e inmersión: WebGL, modelos interactivos, animación atada al scroll, previews en AR. Cita a Nike e IKEA en el caso de “probar” un objeto o un espacio antes de comprar (el URL de Nike no se pudo confirmar de forma estable desde este entorno; IKEA sí). Envato también lo lista entre los cambios grandes del año. Sirve cuando explorar el objeto *es* el punto. No sirve como decoración de fondo de una landing que podría haber sido una foto.

Bruno Simon sigue siendo el portfolio-demostración del palo. Apple construye product pages donde el objeto tiene presencia espacial. teamLab trabaja la inmersión como contenido, no como adorno. Locomotive es un estudio asociado a ese nivel de motion.

## Cuándo usarlo y cuándo no

**Usalo** cuando hay un producto físico, una prenda, un espacio, un world-building o un portfolio de motion / 3D. Un modelo ligero que se pueda orbitar rinde más que un video autoplay.

**No lo uses** para “darle vida” a un SaaS que no tiene objeto, ni como background 3D detrás de un formulario (performance, mareo, accesibilidad). Si no hay budget de ingeniería y de QA en dispositivos bajos, no lo prometas.

## Reglas concretas

- **Grilla:** El canvas puede ir a sangre en el hero; la UI (precio, CTA, specs) se queda en una capa HTML predecible, no adentro del WebGL si se puede evitar.
- **Espaciado:** Dejá que el objeto respire. El tipo se apartá: acá el 3D es la voz, el tipo es el soporte.
- **Radios / bordes:** Chasis mínimo, o ninguno. Evitá enmarcar el canvas en una card con sombra suave: lo vuelve un “widget de plantilla”.
- **Sombras:** Las del mundo 3D, no un `shadow-2xl` de CSS debajo del canvas.
- **Color:** Una iluminación coherente (un key light, un fill). El fondo, un neutro o un entorno, no un degradé violeta de stock.
- **Performance y acceso:** Modelos livianos, `prefers-reduced-motion` (una toma estática o un turntable lento se apaga), un fallback imagen, nunca scroll-jacking pesado (Bubble lo da por tendencia en retirada).
- **Tipografía:** Quieta, para que no pelee con la escena.
  - [Satoshi](../tipografias/sans-geometrica.md), [Söhne](../tipografias/sans-grotesk.md), [ABC Diatype](../tipografias/sans-grotesk.md), [Switzer](../tipografias/sans-grotesk.md), [Neue Montreal](../tipografias/sans-grotesk.md).
  - Un mono chico para specs: [IBM Plex Mono](../tipografias/mono.md).

## Sitios reales

- [bruno-simon.com](https://bruno-simon.com/) — portfolio WebGL interactivo, referencia clásica todavía en línea (GET 200).
- [www.apple.com/iphone](https://www.apple.com/iphone/) — páginas de producto con presencia espacial / cinematográfica del objeto.
- [www.ikea.com](https://www.ikea.com/) — Figma lo cita por 3D / AR para visualizar un producto o un espacio.
- [www.teamlab.art](https://www.teamlab.art/) — inmersión como contenido.
- [locomotive.ca](https://locomotive.ca/) — estudio asociado a motion de alto nivel y experiencias espaciales.

Nike es citada por Figma para 3D/AR, pero `nike.com` no devolvió una respuesta estable acá (403 / 500 según la ruta). No se usa como link de ficha.

## Errores comunes

- Un spline / un header 3D de stock que no es el producto.
- Autoplay pesado sin fallback, 20 fps en un celular.
- Texto metido en el canvas, ilegible y no seleccionable.
- Usar Geist + un blob 3D violeta y llamarlo “spatial design”.

## Snippet

Este snippet no monta un motor WebGL (sería un demo falso). Muestra el chasis: objeto a sangre, tipo de soporte, fallback, y un recordatorio de reduced-motion.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=satoshi@500,700&display=swap">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400&display=swap" rel="stylesheet">
  <style>
    body { font-family: "Satoshi", sans-serif; background: #eceae6; color: #161616; }
    .mono { font-family: "IBM Plex Mono", ui-monospace, monospace; }
    .orb {
      width: min(52vw, 340px); aspect-ratio: 1; border-radius: 50%;
      background: radial-gradient(circle at 35% 30%, #fff 0%, #c8c2b8 32%, #6d675f 70%, #1a1917 100%);
    }
    @media (prefers-reduced-motion: no-preference) {
      .orb { animation: turn 14s linear infinite; }
    }
    @keyframes turn { to { filter: hue-rotate(12deg); } }
  </style>
</head>
<body class="min-h-screen grid md:grid-cols-2">
  <div class="flex items-center justify-center min-h-[50vh] md:min-h-screen">
    <div class="orb" role="img" aria-label="Sustituto del modelo 3D del producto"></div>
  </div>
  <div class="flex flex-col justify-center px-8 py-12">
    <p class="mono text-xs tracking-[0.16em] uppercase text-neutral-500">Modelo · fallback estático si hace falta</p>
    <h1 class="mt-4 text-5xl font-bold tracking-tight">El objeto es la voz. El tipo, el pie de foto.</h1>
    <p class="mt-4 text-neutral-600 max-w-sm">Orbitá el producto de verdad (WebGL / modelo liviano). Este orbe es solo el lugar del canvas, no un blob decorativo.</p>
  </div>
</body>
</html>
```

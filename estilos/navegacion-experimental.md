# Navegación experimental

Figma la lista como tendencia 2026: no todo el mundo sigue el camino “Home / About / Contact”. Habla de menús radiales, drawers escondidos, mapas interactivos, recorridos no lineales, y cita como inspiración a Locomotive, The Outline, Palmer dinnerware y Google Arts & Culture. Es de las tendencias de **más riesgo**: en un portfolio o en una campaña puede ser la firma del sitio; en un e-commerce o en un SaaS puede esconder la única acción que importa.

“Experimental” no es “escondé el menú y poné un cursor custom”. Es proponer *otro orden de lectura* y, al mismo tiempo, un escape claro (un índice, un skip, un search).

## Cuándo usarlo y cuándo no

**Usalo** en portfolios, estudios, cultura, microsites de campaña, archivos (Arts & Culture, Are.na, Cosmos).

**No lo uses** en checkout, en onboarding de un producto de productividad, en trámites ni en un sitio que la gente tiene que usar cada semana para *hacer* algo. Si lo usás, medií: si nadie encuentra el contacto, falló.

## Reglas concretas

- **Grilla:** Puede ser espacial (un mapa, un índice tipográfico, un radial). En mobile, caé a un patrón conocido (una lista, un drawer) aunque el desktop sea experimental.
- **Espaciado:** El hit area de cada destino tiene que ser generoso. Lo experimental no autoriza targets de 16 px.
- **Radios / bordes / sombras:** Al servicio de la idea (un radial, un dock). Evitá copiar un “orb menu” de Dribbble sobre un layout de SaaS.
- **Color:** Un acento para “estás acá”. El resto, contenido.
- **Accesibilidad:** Orden de foco real, `esc` cierra, un “saltar al contenido”, labels en cada control. Si la nav es un canvas, hace falta un `<nav>` equivalente en HTML.
- **Tipografía:** Display para el índice, grotesca para el escape.
  - [Syne](../tipografias/display-experimental.md), [Clash Display](../tipografias/display-experimental.md), [Cabinet Grotesk](../tipografias/sans-grotesk.md), [Monument Grotesk](../tipografias/sans-grotesk.md).
  - El índice puede ser casi todo tipo: [Fraunces](../tipografias/serif-display.md) o [Neue Montreal](../tipografias/sans-grotesk.md).

## Sitios reales

- [locomotive.ca](https://locomotive.ca/) — citada por Figma; agencia cuyo propio sitio es parte del argumento de exploración.
- [artsandculture.google.com](https://artsandculture.google.com/) — Figma la cita; archivo que se recorre como exploración, no como un menú de 6 ítems.
- [www.are.na](https://www.are.na/) — archivos y canales, una navegación de grafo más que de secciones fijas.
- [www.cosmos.so](https://www.cosmos.so/) — archivo visual, recorrer es el uso.
- The Outline, citada por Figma, fue un medio de la década anterior: no se pudo tratar como URL de ficha vigente en esta pasada, así que no se linkea.

## Errores comunes

- Esconder el menú detrás de un hover difícil, sin versión teclado.
- Un cursor custom que tapa el click o no tiene equivalente táctil.
- Cinco formas de entrar y ninguna de salir.
- Copiar un menú radial en el header de un SaaS de facturación.

## Snippet

Índice tipográfico a pantalla, con un escape “índice / contacto” siempre visible.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=cabinet-grotesk@500,700&display=swap">
  <style>body { font-family: "Cabinet Grotesk", sans-serif; }</style>
</head>
<body class="bg-[#111] text-[#f3f0ea] min-h-screen">
  <a href="#trabajo" class="sr-only focus:not-sr-only focus:absolute focus:top-3 focus:left-3 focus:bg-white focus:text-black focus:px-3 focus:py-2">Saltar al contenido</a>
  <header class="flex justify-between px-6 py-4 text-sm">
    <span>Estudio</span>
    <a href="#contacto" class="underline">Contacto</a>
  </header>
  <nav aria-label="Índice" class="px-6 py-12">
    <ol class="text-5xl md:text-7xl font-bold leading-[1.05] tracking-tight">
      <li><a href="#trabajo" class="hover:italic">01 Trabajo</a></li>
      <li><a href="#estudio" class="hover:italic">02 Estudio</a></li>
      <li><a href="#diario" class="hover:italic">03 Diario</a></li>
    </ol>
  </nav>
  <main id="trabajo" class="px-6 pb-20 text-neutral-400">El recorrido puede ser un índice, no un hamburger. El contacto, igual, se ve siempre.</main>
</body>
</html>
```

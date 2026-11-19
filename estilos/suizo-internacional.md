# Suizo / internacional

El Estilo Tipográfico Internacional (suizo) sigue siendo una de las bases más serias del diseño web: grilla visible o al menos sentida, sans grotesca o neo-grotesca, alineación al margen, jerarquía por escala y peso, fotografía o producto sin adorno, color contenido (a menudo un acento puntual sobre negro, blanco y un gris). filtercoffee.dev lo apunta a estudios, instituciones y sitios densos en información. Toimi registra, en 2026, un revival cercano —“Swiss-grid-inspired brutalism”— en marcas como Teenage Engineering, Resend o Mercury: la misma disciplina, con valores de producción actuales y a veces un dejo de catálogo o de manual.

No es “minimalismo genérico”. El suizo pide decisiones de retícula y de tipo; el default de IA pide aire y cards redondas.

## Cuándo usarlo y cuándo no

**Usalo** en estudios de arquitectura y diseño, universidades, cultura institucional, finanzas sobrias, documentación, portfolios profesionales y cualquier producto que quiera parecer objetivo.

**No lo uses** si la marca vive del calor, de lo artesanal o de lo infantil: va a leerse frío. Tampoco es el atajo para una landing de PyME que no tiene contenido denso: sin información que ordenar, la grilla se ve vacía.

## Reglas concretas

- **Grilla:** 12 columnas o un sistema de 8/12/16 columnas con márgenes generosos. Los bloques arrancan en líneas de la grilla; los textos largos a 60–72 caracteres. Alineación a la izquierda, no justificado de periódico.
- **Espaciado:** Escala dura (8 px). El aire es estructural, no “mucho padding porque queda moderno”.
- **Radios:** 0 px. Si hay radio, que sea mínimo y excepcional (un avatar, no un card).
- **Bordes:** Hairlines de 1 px, negros o al 15–20% de opacidad, usados como filetes editoriales. Nada de divisores decorativos con degradé.
- **Sombras:** No. La elevación se hace con filete, fondo o escala tipográfica.
- **Color:** Blanco, negro, un gris de texto y un acento (rojo, amarillo, o el color institucional). Fotografía a sangre o en un módulo de la grilla, no en un marco con sombra.
- **Tipografía:** Una sans de oficio, pocos pesos (regular + medium o bold), itálica si la familia la tiene bien. Evitá Inter / Poppins / Montserrat como voz.
  - [Söhne](../tipografias/sans-grotesk.md), [Neue Montreal](../tipografias/sans-grotesk.md), [Suisse Int'l](../tipografias/sans-grotesk.md), [Untitled Sans](../tipografias/sans-grotesk.md), [Monument Grotesk](../tipografias/sans-grotesk.md) o [Graphik](../tipografias/sans-grotesk.md) si hay presupuesto.
  - Gratis: [Switzer](../tipografias/sans-grotesk.md), [Mona Sans](../tipografias/sans-grotesk.md), [Public Sans](../tipografias/sans-grotesk.md).
  - Caps y números: un [IBM Plex Mono](../tipografias/mono.md) en 11–12 px para metadatos, no para el cuerpo.

## Sitios reales

- [ecal.ch](https://www.ecal.ch/) — filtercoffee.dev lo cita como sitio institucional de referencia para el estilo suizo (redirige a `/fr/`).
- [teenage.engineering](https://teenage.engineering/) — Toimi lo agrupa en el revival de catálogo: foto de producto sobre fondo neutro, jerarquía seca.
- [www.vitsoe.com](https://www.vitsoe.com/) — mobiliario y sistema, tipografía y aire usados como manual (redirige a `/us` según la región).
- [resend.com](https://resend.com/) — Toimi lo menciona en el mismo lote “developer-first” de grilla suiza contemporánea, en oscuro y con captions técnicos.
- [mercury.com](https://mercury.com/) — citado en ese grupo por una estética monocroma, casi de lujo, con disciplina de grilla.

## Errores comunes

- Confundirlo con “mucho blanco y un logo chico al centro”. El suizo es alineación y escala, no vacuidad.
- Meter cards con `rounded-2xl` y sombra suave “para que se sienta UI”. Rompe el idioma.
- Usar una geométrica amable (Poppins, Outfit) en lugar de una grotesca de trabajo.
- Justificar el texto o centrar todo el hero: son gestos ajenos a esta escuela.
- Aplicar un acento neón en cada fila. El acento es una excepción.

## Snippet

Cabecera de catálogo a dos columnas, filetes, radio 0, Switzer.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=switzer@400,500,600&display=swap">
  <style>
    body { font-family: "Switzer", sans-serif; }
  </style>
</head>
<body class="bg-white text-neutral-900">
  <header class="max-w-6xl mx-auto px-6 py-6 flex items-baseline justify-between border-b border-neutral-900">
    <p class="text-sm tracking-[0.18em] uppercase">Estudio 04</p>
    <nav class="text-sm flex gap-6">
      <a href="#" class="hover:underline">Proyectos</a>
      <a href="#" class="hover:underline">Estudio</a>
      <a href="#" class="hover:underline">Contacto</a>
    </nav>
  </header>
  <main class="max-w-6xl mx-auto px-6 py-16 grid md:grid-cols-12 gap-8">
    <p class="md:col-span-4 text-sm leading-relaxed">002 / 2026<br>Catálogo de obra. La grilla sostiene, el tipo habla, el color no interrumpe.</p>
    <h1 class="md:col-span-8 text-5xl md:text-7xl font-medium leading-[0.95] tracking-tight">Sistemas que se leen antes de decorarse.</h1>
  </main>
  <section class="max-w-6xl mx-auto px-6 pb-20 grid md:grid-cols-12 gap-8 border-t border-neutral-900 pt-8">
    <figure class="md:col-span-7 bg-neutral-200 aspect-[4/3]"></figure>
    <div class="md:col-span-5 text-sm leading-7">
      <p class="text-xs tracking-[0.16em] uppercase mb-3">Ficha</p>
      <p>Tipografía: una familia, dos pesos. Radio: cero. Sombra: ninguna. Un filete negro hace el trabajo que en otros sitios hace una card.</p>
    </div>
  </section>
</body>
</html>
```

# UI casi invisible

Bubble, en julio de 2026, la marca como tendencia emergente y pone de ejemplo la home de Linear: una sola familia de tipo haciendo la mayor parte del trabajo, bordes adelgazados a un pelo de línea de baja opacidad, y la estructura resuelta con espacio en blanco y jerarquía tipográfica más que con cajas. Lo llama *quiet*. Sirve a marcas que se apoyan en datos y en confianza (dashboards, plataformas, fintech). Es un mal encaje cuando la marca necesita personalidad ruidosa o storytelling visual.

No es “no diseñar”. Es sacar cromo hasta que lo que queda —tipo, alineación, estados— tenga que estar bien.

## Cuándo usarlo y cuándo no

**Usalo** en dashboards, herramientas internas, banca y productos donde el contenido (números, tablas, documentos) es el espectáculo. También como dirección de una marketing page de un producto muy sobrio.

**No lo uses** en cultura, moda, food o campañas que necesitan calor. Si lo aplicás sin una escala tipográfica clara, no queda “casi invisible”: queda inacabado.

## Reglas concretas

- **Grilla:** Estricta, de producto. Columnas predecibles. El marketing page puede ser casi un documento.
- **Espaciado:** Escala de 4/8 px. El aire entre bloques es la única “decoración”.
- **Radios:** 4–8 px, o 0. Nunca un radio espectacular.
- **Bordes:** 1 px al 6–12% de opacidad. Muchos contenedores, en realidad, no necesitan borde: con el espacio alcanza.
- **Sombras:** No. O una sombra de 1 px de aire para un popover, no para cada card.
- **Color:** Superficie casi igual al fondo. Color semántico (éxito, error, aviso) antes que acento de marca en cada botón. Un acento, usado poco.
- **Tipografía:** Una grotesca quieta de excelente lectura en tamaños chicos. Dos o tres pesos, no más.
  - [Untitled Sans](../tipografias/sans-grotesk.md), [Söhne](../tipografias/sans-grotesk.md), [Suisse Int'l](../tipografias/sans-grotesk.md), [Switzer](../tipografias/sans-grotesk.md), [Figtree](../tipografias/sans-grotesk.md) o [Public Sans](../tipografias/sans-grotesk.md).
  - Si hay requisito de accesibilidad: [Atkinson Hyperlegible](../tipografias/sans-grotesk.md).
  - Cifras y shortcuts: [IBM Plex Mono](../tipografias/mono.md).
  - Inter es legítima *como motor de UI* en este contexto, pero no la presentes como hallazgo de personalidad.

## Sitios reales

- [linear.app](https://linear.app/) — el ejemplo que cita Bubble para barely-there UI.
- [mercury.com](https://mercury.com/) — banca con muy poco cromo, monocromo, tipografía y aire.
- [resend.com](https://resend.com/) — interfaz y marketing de API con captions y filetes, poco adorno.
- [stripe.com](https://stripe.com/) — marketing de infraestructura con disciplina de tipo y de espacio (más color que Linear, misma idea de “el sistema se nota poco”).
- [cal.com](https://cal.com/) — producto de scheduling con UI contenida y tipografía de producto ([Cal Sans](../tipografias/sans-geometrica.md) está en el catálogo).

## Errores comunes

- Quitar tanto que el contraste cae por debajo de WCAG o que los botones no se reconocen como botones.
- Seguir usando una card con sombra suave “por las dudas” en cada widget: deshace el idioma.
- Elegir una display extravagante. Este estilo no es el lugar de Clash Display.
- Confundirlo con un wireframe gris: todavía hace falta un acento, un peso bold y estados hover / focus visibles (sobre todo el focus visible para teclado).

## Snippet

Una barra de datos y un título, filetes al 10%, sin sombras.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=switzer@400,500,600&display=swap">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400&display=swap" rel="stylesheet">
  <style>
    body { font-family: "Switzer", sans-serif; }
    .mono { font-family: "IBM Plex Mono", ui-monospace, monospace; }
  </style>
</head>
<body class="bg-[#f6f6f4] text-neutral-900 min-h-screen">
  <main class="max-w-3xl mx-auto px-6 py-16">
    <header class="flex items-baseline justify-between border-b border-neutral-900/10 pb-4">
      <h1 class="text-2xl font-medium tracking-tight">Cuentas</h1>
      <p class="mono text-xs text-neutral-500">Hoy · 19 nov</p>
    </header>
    <ul class="mt-0">
      <li class="flex items-baseline justify-between border-b border-neutral-900/10 py-4">
        <span>Operativo</span>
        <span class="mono text-sm tabular-nums">3.290.850</span>
      </li>
      <li class="flex items-baseline justify-between border-b border-neutral-900/10 py-4">
        <span>Reservas</span>
        <span class="mono text-sm tabular-nums">840.000</span>
      </li>
      <li class="flex items-baseline justify-between py-4">
        <span class="text-neutral-500">Pendiente de depósito</span>
        <span class="mono text-sm tabular-nums text-neutral-500">20.000</span>
      </li>
    </ul>
    <button class="mt-8 text-sm font-medium border-b border-neutral-900 pb-0.5 hover:opacity-60">Descargar extracto</button>
  </main>
</body>
</html>
```

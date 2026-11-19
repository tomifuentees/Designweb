# SaaS oscuro premium

En 2026, buena parte de los sitios de software “diseñados” arrancan en casi negro, con un solo acento y mucho aire. Toimi estima que alrededor de tres cuartos de las landings de SaaS de diseño liderado siguen esa disciplina, y aclara que lo difícil no es el dark mode: es **usar un solo acento con contención** (el púrpura de Linear, el rojo de Raycast, el lima de Mercury, el cian de Cursor, en sus palabras). El producto —un recorte de UI real, a menudo animado— ocupa el lugar que en otros años ocupaba una ilustración 3D.

Es un idioma creíble para devtools y B2B. También es, junto con el bento, el más imitado. Si lo usás, cambiale la voz (tipo, acento, ritmo) o vas a parecer un clon.

## Cuándo usarlo y cuándo no

**Usalo** en productos de software, infra, productividad, diseño, fintech técnica, donde el screenshot del producto es el argumento y el público ya vive en UIs oscuras.

**No lo uses** en una PyME local, un estudio jurídico, un e-commerce de comida o una marca que vende calidez. Tampoco lo uses “porque es premium”: sin un producto que mostrar, el fondo negro queda como un tema de plantilla. Cuidado con el contraste de los grises sobre negro (WCAG).

## Reglas concretas

- **Grilla:** Hero a ancho completo o partido (texto + recorte de producto). Debajo, una sección bento o un stack editorial, no tres cards iguales. Márgenes laterales generosos.
- **Espaciado:** Escala amplia (24–80 px entre bloques). El lujo está en el aire, no en el glow.
- **Radios:** 8–16 px en el recorte de producto; 6–10 px en controles. Consistentes. Evitá `rounded-3xl` en todo.
- **Bordes:** 1 px blanco al 8–12%. El borde define el “chasis” del producto mejor que una sombra luminosa.
- **Sombras:** Pocas. Si hay glow, es del acento y está localizado (un cursor, un botón, un estado activo), no un halo violeta detrás del hero.
- **Color:** Fondo `#0b0c0f`–`#111`, superficies un paso más claras, texto casi blanco y un *solo* acento. Nada de degradé índigo de esquina a esquina.
- **Tipografía:** Grotesca o geométrica de producto, un mono para atajos y cifras.
  - [Söhne](../tipografias/sans-grotesk.md), [Neue Montreal](../tipografias/sans-grotesk.md), [TWK Lausanne](../tipografias/sans-grotesk.md), [ABC Diatype](../tipografias/sans-grotesk.md), [Satoshi](../tipografias/sans-geometrica.md) o [Mona Sans](../tipografias/sans-grotesk.md).
  - Mono: [Berkeley Mono](../tipografias/mono.md), [IBM Plex Mono](../tipografias/mono.md) o [Commit Mono](../tipografias/mono.md).
  - Geist e Inter funcionan en este territorio, pero ya son el default; no las elijas como primera opción salvo que el brief lo pida. Ver [estilo Linear](./estilo-linear.md).

## Sitios reales

- [linear.app](https://linear.app/) — el gold standard que Toimi llama el sitio B2B más copiado del ciclo. Mejor mirarlo como referencia que clonarlo (ver ficha propia).
- [www.raycast.com](https://www.raycast.com/) — oscuro, acento rojo, el producto (la paleta de comandos) es el hero.
- [cursor.com](https://cursor.com/) — Toimi lo cita en la familia de “un acento sobre negro”.
- [vercel.com](https://vercel.com/) y [resend.com](https://resend.com/) — oscuro de producto, tipografía contenida, demos de UI.
- [mercury.com](https://mercury.com/) — misma disciplina, a menudo más monocroma / lima que púrpura.

## Errores comunes

- Degradé violeta-azul detrás del titular + Inter + tres cards de glass. Es el “AI look” más citado en r/web_design en 2026.
- Dos o tres acentos neón “para que no quede triste”.
- Mockups de Macbook genéricos en lugar del producto real.
- Grises que no contrastan (`#777` sobre `#111`): bonito en el monitor del diseñador, ilegible en el del usuario.
- Aplicar dark sí o sí, sin un toggle, en un producto usado de día en una oficina.

## Snippet

Hero oscuro, un acento lima, recorte de producto con borde, sin glow violeta.

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
    body { font-family: "Satoshi", sans-serif; }
    .mono { font-family: "IBM Plex Mono", ui-monospace, monospace; }
  </style>
</head>
<body class="bg-[#0c0d10] text-zinc-100 min-h-screen">
  <main class="max-w-6xl mx-auto px-6 py-20 grid md:grid-cols-2 gap-12 items-center">
    <div>
      <p class="mono text-[11px] tracking-[0.16em] uppercase text-lime-400">Producto · un acento</p>
      <h1 class="mt-4 text-5xl md:text-6xl font-bold tracking-tight leading-[1.02]">El software, en negro. El color, una sola vez.</h1>
      <p class="mt-5 text-zinc-400 text-lg max-w-md">Un recorte real de la UI hace más que un degradé. El acento marca el estado activo, no el fondo de la página.</p>
      <a href="#" class="inline-block mt-8 bg-lime-400 text-neutral-900 font-semibold px-4 py-2.5 rounded-md text-sm">Probar el producto</a>
    </div>
    <div class="rounded-xl border border-white/10 bg-[#16171c] p-4 min-h-[260px]">
      <p class="mono text-[11px] text-zinc-500 mb-3">app · dashboard</p>
      <div class="h-40 rounded-lg bg-[#0c0d10] border border-white/5 p-4">
        <p class="text-sm text-zinc-300">Acá va la captura o la demo, no un glow.</p>
        <p class="mt-6 mono text-lime-400 text-xs">status · ok</p>
      </div>
    </div>
  </main>
</body>
</html>
```

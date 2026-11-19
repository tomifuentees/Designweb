# Anti-diseño / brutalismo anti-grilla

Bubble llama “anti-grid brutalism” a una dirección establecida en 2026: layouts rotos, estética de HTML crudo, mono, radio cero, bordes de un píxel, a veces grano. Lo presenta como empujón contra el bento pulido y contra la UI blanda que la IA reproduce bien. Es primo del brutalismo clásico (estructura expuesta, “feísmo” deliberado) y primo lejano del [neo-brutalismo](./neo-brutalismo.md) de colores sticker: acá el ruido es más bien de sistema, de Times o de mono sobre fondo default, de ventanas superpuestas, no de una paleta de merch.

Are.na es un referente de producto que se permite lo crudo. Brutalist Websites sigue siendo la galería del palo. Byline aparece en Wix del lado “dial-up”, vecino de esta actitud.

## Cuándo usarlo y cuándo no

**Usalo** en estudios experimentales, editoriales independientes, arte, investigación, portfolios que quieren parecer un sistema, no una agencia de 2021.

**No lo uses** en e-commerce de masas, banca, salud, ni en un SaaS que todavía tiene que explicar qué hace. Si la navegación no se entiende, la actitud no justifica la pérdida. El contraste y el focus visible no son opcionales: “feo” no es “ilegal de leer”.

## Reglas concretas

- **Grilla:** Se puede romper (módulos que se pisan, anchos raros, un `<hr>` que atraviesa un título). Tiene que haber *algún* orden recuperable en mobile y para teclado.
- **Espaciado:** Irregular a propósito, no caótico al azar. Repetí dos o tres medidas, no quince.
- **Radios:** 0.
- **Bordes:** 1 px negro o un color de sistema. A veces el borde default del user-agent se deja a propósito en un botón.
- **Sombras:** No, o una sombra dura de 1–2 px. Nunca blur.
- **Color:** Default de documento (blanco, azul de link, gris de visits) o una paleta pobre (negro, un amarillo de highlight). Evitá el púrpura de plantilla y el “dark premium”.
- **Tipografía:** Sistema o mono, o una display rara usada como quien no quiere.
  - [Karrik](../tipografias/display-experimental.md), [Space Mono](../tipografias/mono.md), [Departure Mono](../tipografias/mono.md), [IBM Plex Mono](../tipografias/mono.md), [Fragment Mono](../tipografias/mono.md).
  - Cuerpo: [Public Sans](../tipografias/sans-grotesk.md) o, deliberadamente, una serif de sistema. Avisá si usás `ui-sans-serif` / Times: es una decisión, no un olvido.

## Sitios reales

- [www.are.na](https://www.are.na/) — producto cultural / de investigación, UI cruda, tipografía de trabajo, poco cosmética.
- [brutalistwebsites.com](https://brutalistwebsites.com/) — galería viva del estilo (es un índice, no un “producto”, pero es la referencia del palo).
- [www.bylinebyline.com](https://www.bylinebyline.com/) — Wix lo cita en el vecindario early-web / dial-up, actitud anti-template.
- [teenage.engineering](https://teenage.engineering/) — no es anti-diseño puro, pero Toimi lo acerca al “Swiss-grid brutalism”: crudeza de catálogo, no de plantilla suave.

## Errores comunes

- Hacerlo ilegible y llamarlo actitud. Si el contraste falla o el menú no tiene sentido con teclado, está mal resuelto.
- Un theme “brutalist” de CSS con radios 0 sobre una estructura de tres cards de SaaS: es un disfraz.
- Autoplay, cursores custom que no clickean, scroll roto.
- Mezclarlo con glassmorfismo o con un bento de 9 tiles pulidos.

## Snippet

Documento casi crudo, mono + Karrik (o un título en mono si Karrik no carga), radio 0.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&display=swap" rel="stylesheet">
  <style>
    body { font-family: "IBM Plex Mono", ui-monospace, monospace; background: #f2f2f2; color: #111; }
    a { text-decoration: underline; }
    button { border-radius: 0; border: 1px solid #111; background: #fff; padding: .4rem .7rem; }
    button:focus-visible { outline: 2px solid #111; outline-offset: 2px; }
  </style>
</head>
<body class="p-4 md:p-8">
  <p style="position:absolute;top:8px;right:8px;font-size:12px;">v0.1 / unstyled on purpose</p>
  <main class="max-w-xl mt-10">
    <p class="text-xs">index.html</p>
    <h1 class="mt-2 text-4xl md:text-5xl font-semibold leading-tight">El sitio se ve como un documento porque se niega a parecer una plantilla.</h1>
    <p class="mt-6 leading-7">Radio cero. Links azules si hace falta. Un botón de sistema. La grilla se puede romper; la lectura, no.</p>
    <p class="mt-6"><a href="#">entrar</a> · <button type="button">acción</button></p>
  </main>
</body>
</html>
```

# Glassmorfismo

Vidrio esmerilado: `backdrop-filter: blur()`, fondo semitransparente, un borde claro de 1 px, a veces un highlight superior. The Plus Addons lo ve al alza en 2026 por el halo de Apple Liquid Glass, pero lo acota a headers sticky y a cards de etiqueta corta. Falla en texto largo y cuando el contraste queda indeterminado. Envato habla de una toma “más madura”. Reddit, en cambio, lo nombra una y otra vez en 2026 como pieza del “AI look”, especialmente en combo con el degradé violeta.

La versión que todavía se puede usar: **un solo panel** (nav sticky, un modal, un control flotante) sobre una foto o un 3D reales, con texto que cumple WCAG *sin* confiar en el blur. La versión que hay que evitar: todo el sitio en paneles de vidrio sobre un mesh índigo.

## Cuándo usarlo y cuándo no

**Usalo** como acento, en un header, un popover o un dock, sobre una imagen rica, en un contexto oscuro o fotográfico.

**No lo uses** como tema de un landing completo, ni sobre tablas, ni sobre párrafos, ni sobre un fondo plano (el vidrio necesita algo que refractar). No lo uses si no hay fallback: `backdrop-filter` no es universal, y en esos casos el panel tiene que seguir siendo un sólido legible.

## Reglas concretas

- **Grilla:** La del estilo anfitrión. El vidrio no organiza la página.
- **Espaciado:** Interno contenido. Un panel de glass con mucho texto es un error de uso.
- **Radios:** 12–20 px en paneles flotantes; en un header puede ser 0.
- **Bordes:** `1px solid rgba(255,255,255,.25)` (o negro al 15% sobre claro). El borde es el que vende el “canto del vidrio”.
- **Sombras:** Muy suaves, o ninguna. Una sombra fuerte lo vuelve una card, no un vidrio.
- **Color / receta:**

```css
.glass {
  background: rgba(20, 20, 24, .45);
  backdrop-filter: blur(16px) saturate(1.2);
  -webkit-backdrop-filter: blur(16px) saturate(1.2);
  border: 1px solid rgba(255,255,255,.22);
}
@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .glass { background: rgba(20, 20, 24, .92); }
}
```

- El texto sobre el panel tiene que contrastar con el *fallback sólido*, no solo con la foto de fondo.
- **Tipografía:** Una grotesca clara, no una serif fina.
  - [Satoshi](../tipografias/sans-geometrica.md), [Switzer](../tipografias/sans-grotesk.md), [Mona Sans](../tipografias/sans-grotesk.md), [General Sans](../tipografias/sans-grotesk.md).
  - Evitá Inter + púrpura + glass: es la pila más citada como genérica.

## Sitios reales

El glass, como el grano, suele ser una capa, no “el sitio”. Referentes de uso contenido o de contexto (no de tema total):

- [www.apple.com](https://www.apple.com/) — el origen cultural del “liquid glass” en el ecosistema Apple; las product pages usan materiales translúcidos con más oficio que un blur de CSS suelto.
- [www.figma.com](https://www.figma.com/) — UI de producto y marketing con paneles / materiales, no un landing entero de vidrio.
- [linear.app](https://linear.app/) — cuando aparece translucidez, es de cromo de producto, no de un hero de mesh violeta.
- [resend.com](https://resend.com/) — write-ups de su sistema mencionan blur en puntos puntuales de UI; el conjunto sigue siendo oscuro y tipográfico, no “glass theme”.

No se cita ningún sitio *porque* sea un tutorial de glassmorphism: esos, en 2026, ya se leen como dated o como output de IA.

## Errores comunes

- Vidrio sobre degradé índigo, en cada sección, con texto a 14 px.
- Confiar en el blur para “salvar” un contraste que no está.
- Aplicarlo a un formulario largo o a una tabla.
- Olvidar el fallback para navegadores sin `backdrop-filter`.

## Snippet

Un nav de vidrio sobre una foto (acá, un fondo rico simulado). Fallback sólido.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=satoshi@500,600&display=swap">
  <style>
    body { font-family: "Satoshi", sans-serif; }
    .hero {
      min-height: 100vh;
      background:
        radial-gradient(circle at 20% 30%, #c4a574 0%, transparent 40%),
        radial-gradient(circle at 80% 70%, #2a4a4a 0%, transparent 42%),
        #1a1814;
    }
    .glass {
      background: rgba(20, 18, 16, .48);
      backdrop-filter: blur(16px) saturate(1.2);
      -webkit-backdrop-filter: blur(16px) saturate(1.2);
      border: 1px solid rgba(255,255,255,.22);
    }
    @supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
      .glass { background: rgba(20, 18, 16, .92); }
    }
  </style>
</head>
<body class="text-white">
  <div class="hero">
    <header class="glass sticky top-4 mx-4 md:mx-8 rounded-2xl px-5 py-3 flex items-center justify-between">
      <span class="font-semibold">Vidrio, una vez</span>
      <nav class="text-sm flex gap-5">
        <a href="#">Obra</a>
        <a href="#">Estudio</a>
      </nav>
    </header>
    <main class="px-8 pt-28 max-w-2xl">
      <h1 class="text-5xl md:text-6xl font-semibold leading-tight">Sobre una imagen real, no sobre un mesh violeta.</h1>
      <p class="mt-6 text-white/70">El panel es un header. El resto de la página no tiene que ser de vidrio.</p>
    </main>
  </div>
</body>
</html>
```

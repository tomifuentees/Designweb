# Estilo Linear

No es lo mismo que “SaaS oscuro”. El estilo Linear, tal como Toimi lo describe en 2026, es un sistema concreto: oscuro por default, acento púrpura, tipografía enorme que a veces intercambia una palabra (en su home, “teams” / “agents”), una demo *viva* del producto debajo del titular, etiquetas de documento técnico tipo “FIG 0.2”, bento de features, microinteracciones y mucho aire. Toimi lo llama el sitio B2B de software más copiado del ciclo. Bubble, por otro lado, usa esa misma home como ejemplo de [UI casi invisible](./ui-casi-invisible.md): pelo de línea, una familia de tipo haciendo casi todo el trabajo.

Copiar el púrpura + Inter Display + “FIG 0.1” es, a esta altura, otro default. La lección útil es otra: **el producto es la demo**, las etiquetas parecen una especificación, y no hay ornamentación de más.

## Cuándo usarlo y cuándo no

**Usalo** cuando el producto tiene una UI que se puede mostrar en movimiento (un issue, un inbox, un canvas) y el público entiende esa UI. Sirve en herramientas de desarrollo, productividad y collaboration.

**No lo uses** si no tenés esa demo —una captura estática genérica no es “estilo Linear”—. No lo uses en marcas que no son de software. Y no lo uses como disfraz de una landing sin producto: se nota.

## Reglas concretas

- **Grilla:** Hero tipográfico + demo a sangre o apenas metida en un chasis. Debajo, bento. Etiquetas `FIG` / `01` alineadas como en un plano, no como badges neón.
- **Espaciado:** Muy generoso. El hero puede ocupar una pantalla entera sin un grid de tres columnas.
- **Radios:** 8–12 px en el chasis del producto; controles más chicos y consistentes.
- **Bordes:** Hairlines blanco al ~10%. Casi no hay relleno decorativo.
- **Sombras:** Mínimas. La profundidad la da el recorte de UI, no un drop shadow.
- **Color:** Negro / grafito y un acento. Si vas a honrar el sistema, elegí *otro* acento que no sea el púrpura de Linear: es la forma más simple de no parecer un fork.
- **Tipografía:** Linear usa Inter Display (Toimi). En este kit, Inter está marcado como voz automática a evitar. Alternativas que conservan el clima técnico:
  - [ABC Diatype](../tipografias/sans-grotesk.md), [Mona Sans](../tipografias/sans-grotesk.md), [Switzer](../tipografias/sans-grotesk.md), [Söhne](../tipografias/sans-grotesk.md) o [Satoshi](../tipografias/sans-geometrica.md) para el titular.
  - [Berkeley Mono](../tipografias/mono.md) (es la pareja que se le atribuye a Linear en write-ups de su sistema), [Commit Mono](../tipografias/mono.md) o [IBM Plex Mono](../tipografias/mono.md) para las etiquetas FIG.
  - Si el brief pide “que se vea como Linear”, avisá que Inter Display + púrpura ya está muy visto y ofrecé esta variante.

## Sitios reales

- [linear.app](https://linear.app/) — la fuente. Mirala, no la calques.
- [attio.com](https://attio.com/) — mismo ecosistema de CRM / productividad, oscuro, producto al frente, bento.
- [ramp.com](https://ramp.com/) — disciplina de tiles y producto visible, en un registro cercano aunque no sea un clon.
- [cursor.com](https://cursor.com/) — demo de producto como argumento, un acento, aire de especificación.

## Errores comunes

- Púrpura + Inter + tres cards + un mockup de dashboard inventado. Eso no es Linear: es la plantilla que Linear dejó de usar.
- Poner “FIG 0.1” en una landing de una panadería o de un curso. La etiqueta técnica tiene que corresponder a un objeto real.
- Animar cada palabra del hero. Linear mueve *una* pieza; el resto queda quieto.
- Olvidar `prefers-reduced-motion` en la demo o en el tipo cinético.

## Snippet

Hero con etiqueta FIG, un acento que no es púrpura, y un chasis para la demo.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Mona+Sans:wght@500;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
  <style>
    body { font-family: "Mona Sans", sans-serif; }
    .mono { font-family: "IBM Plex Mono", ui-monospace, monospace; }
  </style>
</head>
<body class="bg-[#0a0a0b] text-zinc-100 min-h-screen">
  <main class="max-w-5xl mx-auto px-6 py-20">
    <p class="mono text-[11px] tracking-[0.14em] text-zinc-500">FIG 0.2 · Issue view</p>
    <h1 class="mt-4 text-5xl md:text-7xl font-bold tracking-tight leading-[0.98] max-w-4xl">
      El producto es la demo.
      <span class="text-teal-400">El resto, especificación.</span>
    </h1>
    <p class="mt-6 text-zinc-400 max-w-xl">Un acento (acá, teal — no el púrpura de Linear). Una etiqueta de plano. Abajo, la UI real en movimiento, no un mockup de stock.</p>
    <div class="mt-12 rounded-xl border border-white/10 overflow-hidden bg-[#111214] min-h-[240px] p-5">
      <div class="flex items-center gap-2 text-xs text-zinc-500 mono">
        <span class="text-teal-400">ENG-2703</span>
        <span>In progress</span>
      </div>
      <p class="mt-8 text-sm text-zinc-400">Acá iría la demo autonarrada del producto.</p>
    </div>
  </main>
</body>
</html>
```

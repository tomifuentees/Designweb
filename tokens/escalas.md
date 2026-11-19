# Escalas y por qué le ganan al default de IA

Cada escala es una decisión cerrada. El modelo, sin ella, elige el valor más común que vio en tutoriales: `p-4` / `p-8` alternados sin ritmo, `rounded-2xl` en todo, `shadow-xl`, `text-5xl font-bold` con `leading-tight` o al revés, `transition-all duration-500`, `z-50` hasta que alguien pone `z-[9999]`.

## Espacio

Base de **4 px (0.25rem)**. Pasos: 0, 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96, 128. El aire entre secciones es `--space-section` (96 px) o `section-sm` / `section-lg`, no un `py-28` improvisado.

En Tailwind v4 una sola variable `--spacing: 0.25rem` genera `p-4`, `gap-6`, etc. Eso está bien como *motor*. El ritmo lo marca usar pocos pasos, siempre los mismos. Un `gap-[18px]` o un `mt-[13px]` es la firma de un componente que nadie revisó.

Por qué le gana al default: un layout con un ritmo único se lee como un sistema. Uno con números sueltos se lee como un ensamble.

## Radio

`none` 0, `sm` 2, `md` 6, `lg` 10, `xl` 16, `full` 9999. Elegí **un default** (`md` en la mayoría de los productos; `none` en suizo, brutal o catálogo). `xl` es para un recorte de media, no para el botón, la card, el input y el badge.

El “todo `rounded-2xl` / `rounded-3xl` + sombra suave” es un tell citado en [Utsubo, junio de 2026](https://www.utsubo.com/blog/built-with-ai-trust-signals-2026) y en [Drop The Hassle, octubre de 2026](https://dropthehassle.com/guides/make-website-look-less-ai).

## Sombra / elevación

Cuatro niveles y un `none` que debería ser el más usado. En SaaS oscuro y en UI casi invisible, el borde de 1 px a bajo contraste (blanco u oscuro al 8–12 %) define el chasis mejor que un `shadow-xl`. El glow de acento no es un nivel de esta escala: si aparece, es un caso (un cursor, un estado activo), no un halo detrás del hero.

## Tipo (fluido)

Escala con `clamp()`, viewport **320–1240 px**, cuerpo de **16 a 18 px**. La receta es la de [Utopia](https://utopia.fyi/type/calculator/): un tamaño mínimo, uno máximo, y una pendiente en `vw`. Pasos: `caption`, `sm`, `body`, `lg`, `h4`, `h3`, `h2`, `h1`, `display`.

```css
--text-body: clamp(1.0000rem, 0.9565rem + 0.2174vw, 1.1250rem);
--text-h1:   clamp(2.5000rem, 2.1522rem + 1.7391vw, 3.5000rem);
```

Por qué le gana al default: la IA salta entre `text-4xl`, `text-5xl` y `text-7xl` según el prompt, y rara vez piensa en el móvil. Una escala fluida unifica las páginas y evita un titular que explota a 390 px o que queda tímido a 1440.

La familia tipográfica no se decide acá. Sale de [`../tipografias/`](../tipografias/README.md).

## Interlineado

Multiplicadores, no píxeles: `display` 1.05, `heading` 1.15, `tight` 1.25 (UI), `body` 1.5, `body-lg` 1.6, `mono` 1.4. El error clásico es `leading-none` en un párrafo o `leading-relaxed` en un display de seis palabras.

## Letter-spacing

`tighter` (−0.03 em) para display, `tight` (−0.02 em) para h1, `normal` para cuerpo, `wide` (0.04 em) y `widest` (0.16 em) para **un** kicker. El label en mayúsculas con tracking enorme arriba de cada heading es un tell ([Drop The Hassle](https://dropthehassle.com/guides/make-website-look-less-ai)).

## Motion

Duraciones: 0, 120, 180, 280, 400 ms. Curvas: `standard` `cubic-bezier(0.2, 0, 0, 1)`, `emphasized` `cubic-bezier(0.3, 0, 0, 1)` (las que Tailwind v4 muestra como `--ease-snappy` y `--ease-fluid` en su anuncio), más `enter` y `exit`. Sin bounce. Sin `ease-in-out` de medio segundo en todo.

`prefers-reduced-motion: reduce` pone las duraciones en 0. Es obligatorio. El fade-and-slide-up en cada sección, el badge con `animate-pulse` y el `transition-all duration-1000` son tells (Desai, Utsubo, Drop The Hassle).

## Breakpoints

Los de Tailwind v4, en rem: `sm` 40, `md` 48, `lg` 64, `xl` 80, `2xl` 96. Un `3xl` de 120 rem es opcional (aparece como ejemplo en las docs de v4) y no es default. No inventes un breakpoint por componente.

## z-index

Capas nombradas: `base` 0, `raised` 10, `dropdown` 20, `sticky` 30, `overlay` 40, `modal` 50, `toast` 60, `max` 70. Si hace falta un slot nuevo, se agrega acá. `z-[9999]` es la forma más rápida de declarar que el sistema no existe.

## Lo que esta carpeta no resuelve

Los tokens fijan *valores*. No arreglan un muro de tres cards iguales, un hero centrado genérico ni una copy de “Elevate your workflow”. Eso es layout y criterio, y está en [`../anti-patrones/`](../anti-patrones/README.md) y en [`../estilos/`](../estilos/README.md). Motif lo dice claro: una pared de cards en tu paleta sigue siendo una pared de cards.

# Microinteracciones

Recetas cortas, en CSS o JS mínimo. La regla de oro: **un gesto por interacción**, 150–300 ms en UI, curvas que arrancan rápido y frenan (ease-out) al entrar, ease-in-out en loops. El detalle de tiempos está en [easing-duracion.md](./easing-duracion.md); el de accesibilidad, en [accesibilidad-performance.md](./accesibilidad-performance.md).

Todas las recetas se apagan o se quedan en un estado estático con `prefers-reduced-motion: reduce`.

## Hover

**Pro:** el objeto responde en el pulso del cursor (color, un translate de 1–2 px, un underline que crece, un ojo del botón). El hit area no se mueve tanto como para que el usuario lo pierda.

**Default de IA:** `hover:-translate-y-2 hover:shadow-2xl hover:scale-105` en cada card, a veces con un glow índigo.

```css
.btn {
  background: #171513;
  color: #f7f5f0;
  transition: background-color 160ms ease-out, transform 160ms ease-out;
}
.btn:hover { background: #3a342e; }
.btn:active { transform: translateY(1px); }
@media (prefers-reduced-motion: reduce) {
  .btn { transition: background-color 120ms linear; }
  .btn:active { transform: none; }
}
```

## Press

**Pro:** un feedback inmediato (`:active`, `scale(0.98)` o `translateY(1px)`), y en un toggle un estado persistente. En React, Motion tiene `whileTap`. En un botón nativo, CSS alcanza.

**Default de IA:** solo hover, o un ripple Material incrustado en un sitio que no es Material.

```css
.icon-btn:active { transform: scale(0.97); }
.icon-btn { transition: transform 90ms ease-out; }
@media (prefers-reduced-motion: reduce) {
  .icon-btn:active { transform: none; }
}
```

## Reveal (entrada en viewport)

**Pro:** un solo eje (opacity + `translateY(8–16px)`), una vez, con `animation-fill-mode: both`. En CSS moderno, `animation-timeline: view()` evita IntersectionObserver. Fallback: el contenido visible de entrada, no `opacity: 0` eterno si la API no está.

**Default de IA:** fade-in de *toda* la página al cargar, o AOS con delays de 0.2, 0.4, 0.6, 0.8 s que retrasan la lectura.

```css
.reveal {
  animation: rise 500ms ease-out both;
  animation-timeline: view();
  animation-range: entry 0% entry 40%;
}
@keyframes rise {
  from { opacity: 0; transform: translateY(12px); }
  to   { opacity: 1; transform: none; }
}
@supports not (animation-timeline: view()) {
  .reveal { opacity: 1; transform: none; animation: none; }
}
@media (prefers-reduced-motion: reduce) {
  .reveal { animation: none; }
}
```

## Stagger

**Pro:** una lista de 4–8 ítems, delay de 40–70 ms entre ellos, el primero casi inmediato. En Motion, `stagger(0.05)`. En GSAP, `stagger: 0.05`. En CSS, `animation-delay` calculado o `animation-range` distinto, no 12 ítems que tardan 2 s en aparecer.

**Default de IA:** cada card espera 200 ms más que la anterior, y el usuario ya scrolleó.

```css
.list li { animation: rise 400ms ease-out both; }
.list li:nth-child(1) { animation-delay: 0ms; }
.list li:nth-child(2) { animation-delay: 50ms; }
.list li:nth-child(3) { animation-delay: 100ms; }
.list li:nth-child(4) { animation-delay: 150ms; }
@media (prefers-reduced-motion: reduce) {
  .list li { animation: none; }
}
```

## Contador de números

**Pro:** un KPI que cuenta hasta el valor *real* una vez, en 600–900 ms, con `tabular-nums`, y se queda. Respeta reduced motion (muestra el número final de entrada). No inventes el valor.

**Default de IA:** un odometer eterno, o un count-up cada vez que el componente se re-renderiza.

```html
<script>
  const el = document.querySelector("[data-count]");
  const end = Number(el.dataset.count);
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduce) { el.textContent = end.toLocaleString("es-AR"); }
  else {
    const t0 = performance.now();
    const dur = 800;
    const tick = (now) => {
      const p = Math.min(1, (now - t0) / dur);
      const eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(end * eased).toLocaleString("es-AR");
      if (p < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  }
</script>
<p class="mono" data-count="3290850">0</p>
```

En un proyecto GSAP, `gsap.to` con `innerText` o un proxy hace lo mismo, con cleanup al desmontar. Para un ticker de marketing, Magic UI tiene uno listo; no lo uses en un dashboard serio si el número es operativo.

## Marquee

**Pro:** una fila de logos o de una frase, pausa en hover y en foco, velocidad lenta, duplicás el contenido para el loop, y `aria-hidden` en el duplicado. Un `animation-play-state: paused` con reduced motion, o un wrap estático.

**Default de IA:** marquee rapidísimo de logos (incluido uno que no es cliente), imposible de leer, sin pausa, y es la tercera de la landing.

```css
.marquee { overflow: hidden; }
.track {
  display: flex;
  gap: 3rem;
  width: max-content;
  animation: slide 36s linear infinite;
}
.marquee:hover .track, .marquee:focus-within .track { animation-play-state: paused; }
@keyframes slide { to { transform: translateX(-50%); } }
@media (prefers-reduced-motion: reduce) {
  .track { animation: none; flex-wrap: wrap; width: auto; }
}
```

## Split de texto

**Pro:** un titular que entra por palabra o por línea, una sola vez, con sentido de lectura. En 2026 la herramienta correcta es **GSAP SplitText** (gratis, reescrito en 3.13, con `aria-label` en el original y `aria-hidden` en los spans). No reimplementes un split que rompe el lector de pantalla.

**Default de IA:** un split por letra en un párrafo de 40 palabras, o un wrapper `div` por caracter sin aria, o un efecto que se siente “más polish than substance” (la crítica que Bubble recogía en 2026 sobre la tipo cinética abusada). Ver [`../estilos/tipografia-kinetica.md`](../estilos/tipografia-kinetica.md).

```js
// Esquema (no es un bundle). Requiere gsap + SplitText desde npm.
import { gsap } from "gsap";
import { SplitText } from "gsap/SplitText";
gsap.registerPlugin(SplitText);

if (!window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
  const split = new SplitText(".hero-title", { type: "words", aria: "auto" });
  gsap.from(split.words, { y: 16, opacity: 0, stagger: 0.04, duration: 0.5, ease: "power2.out" });
}
```

Confirmá en la doc vigente de SplitText el flag exacto de accesibilidad (`aria: "auto"` u opciones equivalentes de 3.13+). Si no hay GSAP, animá la línea completa, no el caracter.

## Popover / dialog (entrada con `@starting-style`)

```css
dialog[open] {
  opacity: 1;
  transform: translateY(0);
  transition: opacity 180ms ease-out, transform 180ms ease-out, display 180ms allow-discrete;
}
@starting-style {
  dialog[open] {
    opacity: 0;
    transform: translateY(8px);
  }
}
@media (prefers-reduced-motion: reduce) {
  dialog[open] { transition: opacity 120ms linear, display 120ms allow-discrete; transform: none; }
}
```

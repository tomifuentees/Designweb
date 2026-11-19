# Rendimiento y velocidad percibida

Lento es inusable. Los Core Web Vitals son la medida pública de la experiencia de carga, respuesta y estabilidad.

## Umbrales (sin cambios al 19/11/2026)

Medidos en el **percentil 75** de visitas reales, por separado en mobile y desktop ([web.dev, Web Vitals](https://web.dev/articles/vitals); [INP](https://web.dev/articles/inp)).

| Métrica | Mide | Bueno | Mejorable | Malo |
|---|---|---|---|---|
| **LCP** (Largest Contentful Paint) | Carga del contenido principal | ≤ 2,5 s | ≤ 4 s | > 4 s |
| **INP** (Interaction to Next Paint) | Respuesta a interacciones (reemplazó a FID el 12/03/2024) | ≤ 200 ms | ≤ 500 ms | > 500 ms |
| **CLS** (Cumulative Layout Shift) | Estabilidad visual | ≤ 0,1 | ≤ 0,25 | > 0,25 |

Diagnóstico complementario: TTFB ≤ 0,8 s, FCP ≤ 1,8 s.

**Estado del ecosistema (CrUX, datos de octubre 2026, publicado 11/11/2026)**: 68,8 % de los orígenes tiene LCP bueno, 81,6 % CLS bueno, 85,2 % INP bueno y 56,3 % pasa los tres. En septiembre de 2026 CrUX agregó variantes **experimentales** que incluyen *soft navigations* de SPA y planea incorporarlas a partir de **mayo de 2027** ([CrUX release notes](https://developer.chrome.com/docs/crux/release-notes)). En agosto, el equipo marcó como preocupante la regresión continua de INP.

## Percepción (lo que sentís vs. lo que mide el cronómetro)

- Límites de 0,1 s / 1 s / 10 s ([`fundamentos.md`](fundamentos.md)).
- **Feedback en < 100 ms** a toda interacción (pressed state, pending), aunque el resultado tarde.
- **Contenido progresivo**: mostrar lo que ya está (streaming SSR, `Suspense`) mejor que esperar todo.
- **Skeleton** con la forma real en cargas de 300 ms – 10 s ([`estados.md`](estados.md)).
- **Optimistic UI** en acciones reversibles.
- **Prefetch/prerender** de la próxima página probable (Speculation Rules, solo Chromium; `quicklink`).
- **Esperas largas**: progreso determinado + estimación + permitir irse.
- Animaciones de transición cortas (150–300 ms) hacen que el cambio se entienda; largas lo hacen sentir lento.

## LCP: checklist

- [ ] El elemento LCP (hero/imagen principal) está en el HTML inicial, no inyectado por JS.
- [ ] `<img fetchpriority="high">` en la imagen LCP; **sin** `loading="lazy"` en ella.
- [ ] Imágenes en AVIF/WebP, con `srcset`/`sizes` y dimensiones.
- [ ] Fuentes: `font-display: swap` u `optional`, preload de la fuente del titular, subset ([`../tipografias/`](../tipografias/README.md)).
- [ ] TTFB bajo: caché/CDN, SSR o estático.
- [ ] Sin cadenas de requests bloqueantes (CSS crítico inline, JS `defer`).

```html
<link rel="preload" as="font" type="font/woff2" href="/fonts/titular.woff2" crossorigin>
<img src="/hero.avif" width="1200" height="800" alt="Panel de facturación con 3 alertas" fetchpriority="high"
     srcset="/hero-640.avif 640w, /hero-1200.avif 1200w" sizes="(max-width: 48rem) 100vw, 60vw">
```

## INP: checklist

- [ ] Ningún handler bloquea > 50 ms: dividí el trabajo y cedé el hilo (`scheduler.yield()` donde exista, fallback a `setTimeout`).
- [ ] Pintá el feedback **primero**, después hacé el trabajo pesado.
- [ ] Menos JS: code-splitting, islas, sacar librerías pesadas, terceros diferidos.
- [ ] Listas largas virtualizadas; evitá re-renders masivos (memo, estado local, `useTransition` para filtros).
- [ ] Inputs con debounce para búsquedas remotas (no para el valor del input).
- [ ] Evitá layout thrashing (leer y escribir estilos alternadamente).

```js
async function onFilterClick(btn) {
  btn.setAttribute('aria-pressed', 'true');           // 1. feedback inmediato
  await (globalThis.scheduler?.yield?.() ?? new Promise(r => setTimeout(r, 0))); // 2. ceder para pintar
  applyHeavyFilter();                                  // 3. trabajo pesado
}
```

```tsx
// React: mantener el input fluido mientras se filtra una lista grande
const [q, setQ] = useState(""); const [isPending, startTransition] = useTransition();
const [filter, setFilter] = useState("");
<input value={q} onChange={(e) => { setQ(e.target.value); startTransition(() => setFilter(e.target.value)); }} />
{isPending && <span role="status">Filtrando…</span>}
```

## CLS: checklist

- [ ] `width`/`height` (o `aspect-ratio`) en imágenes, videos, iframes y embeds.
- [ ] Espacio reservado para anuncios, banners de cookies y contenido que llega tarde (skeleton del mismo tamaño).
- [ ] Nada se inserta arriba del contenido existente salvo por acción de la persona.
- [ ] Fuentes con métricas ajustadas (`size-adjust`, `ascent-override`) para que el swap no mueva el layout.
- [ ] Animaciones con `transform`/`opacity`, no con `top`/`height`.
- [ ] `scrollbar-gutter: stable` para evitar saltos al abrir modales.

## Medir

- **Campo (usuarios reales)**: CrUX / PageSpeed Insights / Search Console; RUM con [`web-vitals`](https://github.com/GoogleChrome/web-vitals) (con atribución para saber qué elemento/interacción falla).
- **Laboratorio**: Lighthouse, DevTools Performance (con CPU 4× y red lenta), WebPageTest.
- Presupuestos de rendimiento en CI (Lighthouse CI, tamaño de bundle).

```js
import { onLCP, onINP, onCLS } from 'web-vitals/attribution';
const send = (m) => navigator.sendBeacon('/rum', JSON.stringify({ name: m.name, value: m.value, rating: m.rating, attribution: m.attribution }));
onLCP(send); onINP(send); onCLS(send);
```

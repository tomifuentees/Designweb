# Cómo evadir el degradé violeta de IA

El look más citado de un sitio “hecho por IA” en 2025–2026 es este: **fondo claro u oscuro, un degradé índigo-violeta, Inter, un hero centrado y tres cards**. No es un mito de Twitter. Está documentado en hilos de Reddit, en un tuit del autor de Tailwind, en artículos de oficio y en un post que llegó a la portada de Hacker News.

## De dónde sale

El 7 de agosto de 2025, Adam Wathan escribió: *“I'd like to formally apologize for making every button in Tailwind UI `bg-indigo-500` five years ago, leading to every AI generated UI on earth also being indigo.”* El post está en [x.com/adamwathan/status/1953510802159219096](https://x.com/adamwathan/status/1953510802159219096) (más de 1,5 millones de impresiones). La disculpa es en chiste, el mecanismo no: los modelos repiten lo que más vieron. Tailwind UI usó `bg-indigo-500` en demos; miles de tutoriales lo copiaron; el promedio estadístico de “UI moderna” quedó morado.

Ese fenómeno se discutió de frente en Reddit:

- r/web_design — [AI has a Purple Problem](https://www.reddit.com/r/web_design/comments/1nx0wus/ai_has_a_purple_problem/) (3 de octubre de 2025), con eco en r/webdev el mismo día.
- r/vibecoding — [Why is every vibe coded website purple?](https://www.reddit.com/r/vibecoding/comments/1nx14zc/why_is_every_vibe_coded_website_purple_i_went_to/) (octubre de 2025).
- r/webdesign — [Why is every AI website designed the same?](https://www.reddit.com/r/webdesign/comments/1m2om61/why_is_every_ai_website_designed_the_same/).
- r/vibecoding — [Why do all AI generated websites look the same](https://www.reddit.com/r/vibecoding/comments/1o18bb4/why_do_all_ai_generated_websites_look_the_same/) (8 de octubre de 2025).
- r/web_design — [Every Vibecoded websites looks the same](https://www.reddit.com/r/web_design/comments/1uzascg/every_vibecoded_websites_looks_the_same/) (17 de julio de 2026, 451 puntos).

Lo retomaron, entre otros, [prg.sh, 26 de octubre de 2025](https://prg.sh/ramblings/Why-Your-AI-Keeps-Building-the-Same-Purple-Gradient-Website), [Utsubo, 23 de junio de 2026](https://www.utsubo.com/blog/built-with-ai-trust-signals-2026) y [Drop The Hassle, 1 de octubre de 2026](https://dropthehassle.com/guides/make-website-look-less-ai). El 27 de septiembre de 2026, Pranav Desai publicó [10 tells of a slop ui](https://godobject.dev/blog/10-tells-of-slop/), que llegó a 386 puntos en [Hacker News](https://news.ycombinator.com/item?id=49867038). El primer tell: *“Gradients. Gradients Everywhere.”* Y: *“Slop Cannons LOVE purple for some reason.”*

## Cómo se ve el default (para reconocerlo)

En CSS, suele aparecer así:

```css
.hero {
  background: linear-gradient(135deg, #667eea, #764ba2);
}
.btn { background: #7c3aed; } /* violet-600 */
```

O, en Tailwind: `bg-gradient-to-br from-indigo-500 to-purple-600`, `text-transparent bg-clip-text` en el titular, `bg-indigo-500` en el CTA, a veces un halo `shadow-indigo-500/40` detrás del hero. En shadcn, el `primary` se queda en el azul-violeta de fábrica.

Cualquiera de esas cosas, sola, puede ser una decisión. Apiladas, son el promedio.

## Qué hacer en cambio

1. **Elegí un acento que salga del tema, no de la librería.** Corteza, óxido, lima, tinta, teja, café, cian de terminal. Está escrito con hex y roles en este catálogo.
2. **Un acento, no un degradé de identidad.** Un degradé pequeño como textura (un grano, un mesh muy suave en un recorte) no es el problema. El problema es el degradé como marca de la página.
3. **Prohibilo en el prompt y en `CLAUDE.md`.** Una línea sirve: “No uses índigo, violeta ni degradés `from-indigo-* to-purple-*` salvo que te lo pida el brief.” El bloque completo está en [`../anti-patrones/reglas-para-agentes.md`](../anti-patrones/reglas-para-agentes.md).
4. **Fijá los tokens.** Un modelo sin tokens inventa un acento por componente, o vuelve al índigo en la sesión siguiente. Ver [thanor.ai sobre tokens para sitios de IA](https://thanor.ai/blog/design-tokens-for-ai-websites) y [`../tokens/`](../tokens/README.md).
5. **Si el cliente ya es púrpura de verdad** (una marca que lleva violeta hace años), usalo como acento sólido, con roles y contraste, no como degradé de hero “porque sí”. El tell no es el matiz: es el promedio de cómo se aplica.

## Variantes que también delatan

- Un word del H1 en degradé (`bg-clip-text`).
- Glow violeta detrás del titular o del mockup.
- `primary` de shadcn sin tocar, o un preset de tweakcn violeta aplicado y listo.
- Sky-500 + indigo-500 + purple-400 en la misma pantalla (“rainbow vomit”).
- El “anti-slop” que se volvió default: cream + terracota pastel + una sola sans “con carácter”. Si lo usás, que no sea pastel de bajo contraste.

Cuando dudes, abrí [saas-producto.md](./saas-producto.md) o [organicas.md](./organicas.md) y elegí una paleta. Es más rápido que negociar con el modelo.

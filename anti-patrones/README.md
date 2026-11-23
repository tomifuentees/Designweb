# Anti-patrones

Catálogo de las señales que, en 2025–2026, delatan un UI “de IA” o vibe-coded sin dirección. El objetivo no es prohibir una técnica: es que un agente (o una pasada tuya) pueda **nombrar** lo que está viendo —el degradé violeta, las tres cards, el pulse, la copy que huele al prompt— y cortarlo con una regla concreta.

Esta carpeta se arma sobre hilos y artículos reales, no sobre una lista inventada. Las fuentes principales son [10 tells of a slop ui](https://godobject.dev/blog/10-tells-of-slop/) de Pranav Desai (27 de septiembre de 2026) y su discusión en [Hacker News](https://news.ycombinator.com/item?id=49867038) (386 puntos), la [disculpa de Adam Wathan](https://x.com/adamwathan/status/1953510802159219096) por el `bg-indigo-500` (7 de agosto de 2025), hilos de Reddit de 2025–2026, [Utsubo, 23 de junio de 2026](https://www.utsubo.com/blog/built-with-ai-trust-signals-2026) y [Drop The Hassle, 1 de octubre de 2026](https://dropthehassle.com/guides/make-website-look-less-ai).

Hay **60 anti-patrones**: los 30 originales, 29 minados en noviembre de 2026 de [impeccable](https://github.com/pbakaus/impeccable), la skill oficial de [Anthropic](https://github.com/anthropics/skills/tree/main/skills/frontend-design), [taste-skill](https://github.com/Leonxlnx/taste-skill) y [unslop](https://github.com/heydamir/unslop) (resumidos, con atribución; ver [`../recursos/minado-repos.md`](../recursos/minado-repos.md)) y 1 sumado el 23 de noviembre de 2026 a partir de [Slopstrap](https://slopstrap.mikelacher.com/) (ver [`../novedades/2026-11-23.md`](../novedades/2026-11-23.md)). Cada uno trae síntoma, por qué aparece, cómo arreglarlo, una regla pegable para un agente y links con fecha. Complementa [`../paletas/`](../paletas/README.md), [`../tokens/`](../tokens/README.md), [`../tipografias/`](../tipografias/README.md) y [`../estilos/`](../estilos/README.md): esas carpetas dan qué usar; esta, qué no dejar pasar.

## Qué hay acá

| Archivo | Contenido |
|---|---|
| [catalogo.md](./catalogo.md) | Las 60 fichas, completas |
| [checklist-revision.md](./checklist-revision.md) | Pasada rápida, para antes de shippear, con el orden y el método de revisión |
| [reglas-para-agentes.md](./reglas-para-agentes.md) | Bloque para pegar en `CLAUDE.md` / `AGENTS.md` |
| [anti-patrones.json](./anti-patrones.json) | El mismo catálogo, legible por máquinas |
| [fuentes-investigacion.md](./fuentes-investigacion.md) | Fuentes, con links y fechas |

## Cómo usarlo desde un agente

1. Leé este README y, si vas a diseñar, las [reglas](./reglas-para-agentes.md).
2. Antes de dar por cerrada una UI, pasá el [checklist](./checklist-revision.md).
3. Si aparece un tell, abrí la ficha en el [catálogo](./catalogo.md) y aplicá el arreglo (casi siempre: una paleta de este kit, unos tokens, una pareja tipográfica, prueba real).
4. No reemplaces este criterio por un “hacelo más único” vago: el modelo lo va a resolver con otro promedio (a veces cream + terracota, a veces un brutalismo de plantilla).

Un comentario del hilo de r/vibecoding de marzo de 2026 avisa, con razón, que si todo el mundo comparte el mismo “anti-slop prompt”, ese prompt se vuelve el próximo slop. Por eso este kit no es solo una lista de prohibiciones: es un criterio (estilo + paleta + tokens + tipografía) que cambia con el proyecto.

## Probar el detector con Slopstrap

[Slopstrap](https://slopstrap.mikelacher.com/) (Mike Lacher; [Hacker News](https://news.ycombinator.com/item?id=50576012), 20 de noviembre de 2026, 790 puntos y 148 comentarios) es una parodia: un "framework" que vuelve vibe-coded cualquier HTML con `Slopstrap.slopify('#id')` y lo revierte con `unslopify`. Reúne en una página casi todos los tells de este catálogo (dot que pulsa, raya a la izquierda, una palabra en serif itálica, eyebrow ✨, texto en degradé, cards dentro de cards, bento, cifras arbitrarias, marquee de logos, testimonios inventados). Sirve como **fixture**: si tu revisión o tu agente no marca esa página entera, el checklist no está funcionando. No es una librería para usar.

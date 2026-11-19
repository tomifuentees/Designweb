# Íconos

Un set por proyecto. Lucide es bueno y por eso es el default de las UIs AI-coded: no lo elijas primero. Phosphor (sobre todo duotone), Tabler, Iconoir, Heroicons o el pack free de Hugeicons alcanzan para casi cualquier producto. No mezcles familias.

Hay **12 recursos** en este grupo. El catálogo completo está en [`recursos.json`](./recursos.json).

## Phosphor Icons

`phosphor` — [https://phosphoricons.com/](https://phosphoricons.com/)

**Licencia:** MIT.  
**Repo:** https://github.com/phosphor-icons/core

**Cuándo usarlo.** Set principal de un producto que no quiere el look Lucide/shadcn. Seis pesos, incluido duotone: esa sola variante ya cambia la voz.

**Cuándo no.** Si el proyecto ya está lleno de Lucide y no vas a migrar todo el set (no mezcles familias).

El reemplazo más citado frente al default de IA. Regular, bold, fill, duotone, light, thin.

## Tabler Icons

`tabler` — [https://tabler.io/icons](https://tabler.io/icons)

**Licencia:** MIT.  
**Repo:** https://github.com/tabler/tabler-icons

**Cuándo usarlo.** Dashboards y admin: trazo consistente, muchos íconos de producto (tablas, filtros, settings).

**Cuándo no.** Como segundo set en el mismo UI que Phosphor o Lucide.

Muy usados en paneles. El sitio oficial es tabler.io/icons.

## Iconoir

`iconoir` — [https://iconoir.com/](https://iconoir.com/)

**Licencia:** MIT.  
**Repo:** https://github.com/iconoir-icons/iconoir

**Cuándo usarlo.** Querés un trazo más ‘diseñado’ que Lucide, sin irte a un pack comercial.

**Cuándo no.** Si necesitás una librería enorme tipo 10k íconos: no es esa.

Docs propias en iconoir.com. MIT, SVG.

## Heroicons

`heroicons` — [https://heroicons.com/](https://heroicons.com/)

**Licencia:** MIT.  
**Repo:** https://github.com/tailwindlabs/heroicons

**Cuándo usarlo.** Proyectos Tailwind que quieren el set del propio equipo (outline + solid). Más ‘oficial Tailwind’ que Lucide, y menos ubicuo en apps AI-coded.

**Cuándo no.** Si ya estás tratando de alejarte de todo el look Tailwind UI.

Hecho por Tailwind Labs. No confundir con heroicons.dev, que a veces es un mirror.

## Hugeicons (free)

`hugeicons-free` — [https://hugeicons.com/](https://hugeicons.com/)

**Licencia:** MIT (solo el pack free).  
**Repo:** https://github.com/hugeicons/hugeicons

**Cuándo usarlo.** Necesitás más detalle o más cobertura que Phosphor/Tabler, y te alcanza el set free.

**Cuándo no.** No redistribuyas los packs Pro. La licencia paga no es MIT. Confirmá en hugeicons.com/docs/faqs/license-questions qué ícono es free.

Free MIT; Pro es de pago por asiento y no se redistribuye como fuente. Citado seguido en listados de 2026.

## Lucide

`lucide` — [https://lucide.dev/](https://lucide.dev/)

**Licencia:** ISC.  
**Repo:** https://github.com/lucide-icons/lucide

**Cuándo usarlo.** Último recurso, o un proyecto que ya está en shadcn y no puede migrar ahora. Es limpio y consistente: por eso se volvió el default.

**Cuándo no.** Como primera elección de un kit que busca no parecer AI-coded. Ver anti-patrón lucide-por-default y el post de Om Patel (7 de marzo de 2026).

Fork de Feather. Es el set de shadcn/ui. Bueno, y por eso está en todas partes.

## Remix Icon

`remix-icon` — [https://remixicon.com/](https://remixicon.com/)

**Licencia:** Apache-2.0.  
**Repo:** https://github.com/Remix-Design/RemixIcon

**Cuándo usarlo.** Necesitás outline + fill de la misma forma, con una cobertura amplia (editor, media, Commerce).

**Cuándo no.** Mezclado con otro set de trazo distinto.

Muy completo. Apache-2.0, no MIT: compatible con uso comercial, distintas obligaciones de atribución que MIT.

## Radix Icons

`radix-icons` — [https://www.radix-ui.com/icons](https://www.radix-ui.com/icons)

**Licencia:** MIT.  
**Repo:** https://github.com/radix-ui/icons

**Cuándo usarlo.** UI de componentes (15–16 px) en un producto que ya usa Radix: flechas, checks, carets, alineados al sistema.

**Cuándo no.** Como librería general de features (es un set chico, de interfaz).

Pensado para chrome de UI, no para ilustrar ‘features’ de una landing.

## Simple Icons

`simple-icons` — [https://simpleicons.org/](https://simpleicons.org/)

**Licencia:** CC0-1.0 (las marcas siguen siendo de sus dueños).  
**Repo:** https://github.com/simple-icons/simple-icons

**Cuándo usarlo.** Logos de marcas (Stripe, GitHub, etc.) en un footer o un ‘integrates with’.

**Cuándo no.** Como set de UI. Respetá las brand guidelines de cada logo: CC0 cubre el SVG del repo, no el uso de la marca.

Solo marcas. El uso no está ‘libre de restricciones de trademark’.

## Bootstrap Icons

`bootstrap-icons` — [https://icons.getbootstrap.com/](https://icons.getbootstrap.com/)

**Licencia:** MIT.  
**Repo:** https://github.com/twbs/icons

**Cuándo usarlo.** Un proyecto que ya vive en Bootstrap y no quiere sumar otra familia.

**Cuándo no.** Si estás saliendo del look Bootstrap o si ya hay otro set.

Consistentes, reconocibles, y por eso también un poco ‘de plantilla’.

## Material Symbols

`material-symbols` — [https://fonts.google.com/icons](https://fonts.google.com/icons)

**Licencia:** Apache-2.0.  
**Repo:** https://github.com/google/material-design-icons

**Cuándo usarlo.** Producto que ya habla el idioma Material, o cuando necesitás una cobertura enorme con ejes variables (peso, fill, grade).

**Cuándo no.** Como voz de una marca que no es Google-like: se reconoce a metros.

Variable. No es un atajo para ‘verse serio’.

## Icônes

`icones` — [https://icones.js.org/](https://icones.js.org/)

**Licencia:** Varía por set (es un agregador).  
**Repo:** https://github.com/iconify/iconify

**Cuándo usarlo.** Explorar familias (Iconify) y comparar trazos antes de elegir un set único.

**Cuándo no.** Como excusa para mezclar cinco sets en un mismo UI. Elegí uno y quedate.

Iconify/Icônes no es una licencia: cada colección trae la suya. Leé la del set que uses.

# Designweb

Base de conocimiento de diseño visual para frontend. Sirve para lograr mejores terminaciones y escapar de los diseños genéricos que suele hacer la IA (Inter + gradiente violeta + cards iguales).

Está pensada para dos usos:
- **Referencia humana**: elegir tipografías, estilos, paletas, tokens, componentes y recursos con criterio.
- **Contexto para agentes** (Claude Code, Cursor, etc.): los `.json` son machine-readable para que una skill elija con datos reales. El bloque pegable para `CLAUDE.md` está en [`anti-patrones/reglas-para-agentes.md`](anti-patrones/reglas-para-agentes.md).

## Contenido

| Carpeta | Qué tiene | Estado |
|---|---|---|
| [`tipografias/`](tipografias/README.md) | 101 tipografías en tendencia, por categoría, con licencia, uso, pareja e import. 28 pairings. Reglas anti-IA genérica. | ✅ |
| [`estilos/`](estilos/README.md) | 27 estilos visuales 2025–2026 (bento, editorial, SaaS oscuro, anti-IA genérica, etc.), con reglas, sitios reales y `estilos.json`. | ✅ |
| [`paletas/`](paletas/README.md) | 35 paletas con tokens de rol (bg, surface, text, accent, estados) en claro y oscuro, OKLCH + hex, contraste WCAG/APCA, mapeadas a estilos. Cómo evadir el degradé violeta. | ✅ |
| [`tokens/`](tokens/README.md) | Escalas decididas: espacio, radio, sombra, tipo fluido, leading, tracking, motion, breakpoints, z-index. CSS, `@theme` de Tailwind v4 y `tokens.json` en formato DTCG 2025.10. | ✅ |
| [`anti-patrones/`](anti-patrones/README.md) | 30 tells de UI de IA documentados en 2025–2026, con arreglo, checklist y reglas para agentes. | ✅ |
| [`recursos/`](recursos/README.md) | 54 recursos de terminación: íconos (no Lucide por default), ilustración, grano, mesh, mockups, SVG, capturas, favicon y OG. | ✅ |
| [`componentes/`](componentes/README.md) | 16 librerías o registries y 12 patrones de página (hero, navbar, pricing, forms, etc.), con lo que hace mal el default de IA. | ✅ |
| [`librerias-visuales/`](librerias-visuales/README.md) | 40 sitios tipo Cult UI: componentes animados, bloques, fondos, texto, 3D y directorios de registries (8 ya estaban en componentes/, 32 nuevos). | ✅ |
| [`animaciones/`](animaciones/README.md) | Motion, GSAP, View Transitions, scroll-driven CSS, microinteracciones, easing y `prefers-reduced-motion`. | ✅ |
| [`inspiracion/`](inspiracion/README.md) | 22 galerías, 55 sitios de referencia, 32 cuentas de X y 8 newsletters, con un porqué. | ✅ |
| [`casos/`](casos/README.md) | Plantilla para documentar proyectos propios (antes / después). Todavía no hay casos cargados. | ⏳ |
| [`skills/`](skills/README.md) | Skill `frontend-design` para Claude Code: elige estilo, paleta, pareja y tokens antes de escribir UI, y se revisa contra el checklist. | ✅ |

## Cómo usarlo con Claude Code

1. Cloná este repo y copiá [`skills/frontend-design`](skills/frontend-design/SKILL.md) a `~/.claude/skills/` o a `.claude/skills/` del proyecto que vas a diseñar. El paso a paso está en [`skills/README.md`](skills/README.md).
2. Si no trabajás dentro de este clon, decile a Claude la ruta absoluta del clon. Las rutas de la skill salen de esta raíz.
3. Pegá el bloque de [`anti-patrones/reglas-para-agentes.md`](anti-patrones/reglas-para-agentes.md) en el `CLAUDE.md` del proyecto.

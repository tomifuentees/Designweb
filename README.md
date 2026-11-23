# Designweb

Base de conocimiento de diseño visual y experiencia de usuario para frontend. Sirve para lograr mejores terminaciones, escapar de los diseños genéricos que suele hacer la IA (Inter + gradiente violeta + cards iguales) y, sobre todo, que las interfaces funcionen: flujos, estados, formularios, accesibilidad y copy en [`ux/`](ux/README.md).

Está pensada para dos usos:
- **Referencia humana**: elegir tipografías, estilos, paletas, tokens, layout, componentes y recursos con criterio, y resolver problemas de UX con evidencia.
- **Contexto para agentes** (Claude Code, Cursor, etc.): los `.json` son machine-readable para que una skill elija con datos reales. El bloque pegable para `CLAUDE.md` está en [`anti-patrones/reglas-para-agentes.md`](anti-patrones/reglas-para-agentes.md).

## Contenido

| Carpeta | Qué tiene | Estado |
|---|---|---|
| [`tipografias/`](tipografias/README.md) | 122 tipografías en tendencia, por categoría, con licencia, uso, pareja e import. 42 pairings. Reglas anti-IA genérica. | ✅ |
| [`estilos/`](estilos/README.md) | 31 estilos visuales 2025–2026 (bento, editorial, SaaS oscuro, bauhaus, denso de datos, anti-IA genérica, etc.), con reglas, sitios reales y `estilos.json`. Dirección por rubro: 4 tipos de negocio y 22 rubros → estilo, paleta y pareja. | ✅ |
| [`paletas/`](paletas/README.md) | 41 paletas con tokens de rol (bg, surface, text, accent, estados) en claro y oscuro, OKLCH + hex, contraste WCAG/APCA, mapeadas a estilos. Cómo evadir el degradé violeta y el crema por reflejo. | ✅ |
| [`tokens/`](tokens/README.md) | Escalas decididas: espacio, radio, sombra, tipo fluido, leading, tracking, motion, breakpoints, z-index. Medidas de app y comparativa con Carbon, Primer, Polaris y GOV.UK. CSS, `@theme` de Tailwind v4 y `tokens.json` en formato DTCG 2025.10. | ✅ |
| [`layout/`](layout/README.md) | Disposición y composición: grillas (12/8/4, modular, baseline, subgrid, `grid-lanes`), proporciones con evidencia (áurea, escalas, medida, ratios), espaciado y ritmo, jerarquía y Gestalt, responsive intrínseco (primitivos de Every Layout, container queries), 19 patrones con wireframe y 18 tells de layout. `layout.json` para la skill. | ✅ |
| [`ux/`](ux/README.md) | Enciclopedia de UX actualizada a nov. 2026: fundamentos y leyes con calidad de evidencia, heurísticas de Nielsen, arquitectura y navegación, formularios (GOV.UK vs Baymard, passkeys), checkout y búsqueda (Baymard 2026), onboarding, estados, feedback, datos, mobile, accesibilidad WCAG 2.2 con estado legal 2026, microcopy ES/EN, Core Web Vitals, UX de IA y agentes, patrones oscuros y regulación, investigación y métricas. Checklist de 41 ítems con severidad, 35 anti-patrones de UX de IA, código accesible y `ux.json` para la skill. | ✅ |
| [`anti-patrones/`](anti-patrones/README.md) | 60 tells de UI de IA documentados en 2025–2026 (29 sumados del minado de repos de noviembre de 2026), con arreglo, checklist y reglas para agentes. | ✅ |
| [`recursos/`](recursos/README.md) | 54 recursos de terminación: íconos (no Lucide por default), ilustración, grano, mesh, mockups, SVG, capturas, favicon y OG. 41 repos de referencia y el [registro del minado](recursos/minado-repos.md) de los 8 principales. | ✅ |
| [`componentes/`](componentes/README.md) | 16 librerías o registries y 12 patrones de página (hero, navbar, pricing, forms, etc.), con lo que hace mal el default de IA. | ✅ |
| [`librerias-visuales/`](librerias-visuales/README.md) | 40 sitios tipo Cult UI: componentes animados, bloques, fondos, texto, 3D y directorios de registries (8 ya estaban en componentes/, 32 nuevos). | ✅ |
| [`animaciones/`](animaciones/README.md) | Motion, GSAP, View Transitions, scroll-driven CSS, microinteracciones, easing y `prefers-reduced-motion`. | ✅ |
| [`inspiracion/`](inspiracion/README.md) | 22 galerías, 55 sitios de referencia, 32 cuentas de X y 8 newsletters, con un porqué. | ✅ |
| [`casos/`](casos/README.md) | Plantilla para documentar proyectos propios (antes / después) y plantilla de `DESIGN.md` para la raíz de un proyecto. Todavía no hay casos cargados. | ⏳ |
| [`novedades/`](novedades/README.md) | Resumen semanal de lo nuevo que entró al kit, con fuente y fecha. Última: [23 de noviembre de 2026](novedades/2026-11-23.md). | ✅ |
| [`indice-rapido.json`](indice-rapido.json) | Índice compacto (~70 KB) de estilos, paletas (con hex de roles), fuentes y rubros, para elegir sin abrir los JSON grandes. Se regenera con [`recursos/generar-indice-rapido.py`](recursos/generar-indice-rapido.py). | ✅ |
| [`skills/`](skills/README.md) | Skill `frontend-design` para Claude Code con tres modos: **nuevo** (de cero), **restyling** (solo lo visual de un proyecto existente, con diffs chicos y sin pedir aprobación) y **auditoria** (solo reporte). En modo nuevo elige estilo, paleta, pareja, tokens y layout, define la UX (flujo, estados, formularios, accesibilidad, copy) antes de escribir UI, y se revisa contra los checklists visual, de layout y de UX. | ✅ |

## Cómo usarlo con Claude Code

1. Cloná este repo y copiá [`skills/frontend-design`](skills/frontend-design/SKILL.md) a `~/.claude/skills/` o a `.claude/skills/` del proyecto que vas a diseñar. El paso a paso está en [`skills/README.md`](skills/README.md).
2. Si no trabajás dentro de este clon, decile a Claude la ruta absoluta del clon. Las rutas de la skill salen de esta raíz.
3. Pegá el bloque de [`anti-patrones/reglas-para-agentes.md`](anti-patrones/reglas-para-agentes.md) en el `CLAUDE.md` del proyecto, y debajo el bloque de UX de [`ux/anti-patrones-ux.md`](ux/anti-patrones-ux.md#bloque-pegable-para-claudemd-ux).
4. Para rediseñar **solo lo visual** de un proyecto que ya existe, usá el modo restyling. El prompt pegable está en [`skills/README.md`](skills/README.md#los-tres-modos) y en la sección "Ejemplos de prompt" de la [skill](skills/frontend-design/SKILL.md#ejemplos-de-prompt).

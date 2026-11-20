# Minado de repos de referencia (20 de noviembre de 2026)

Registro de qué se tomó de cada uno de los 8 repos marcados como `mine_first` en [`repos-referencia.md`](./repos-referencia.md) y dónde quedó en el kit. Se clonó cada repo en modo lectura el 20 de noviembre de 2026 (hora de Salta, UTC-3) y se integró **solo lo que Designweb no tenía**, en castellano y con atribución.

## Reglas que se siguieron

- **No se copió texto de forma literal.** Todo está redactado de nuevo para el kit. De los repos MIT y Apache-2.0 se adaptaron ideas, estructuras y valores numéricos, citando la fuente.
- **CC BY 4.0 (unslop):** se resume y se atribuye a Damir Sokolovsky ([@heydamir](https://github.com/heydamir)) en cada lugar donde aparece, con link a la licencia.
- **Sin identidades de marca:** de awesome-design-md se tomó el *formato*, no los `DESIGN.md` de marcas reales. Las paletas de ui-ux-pro-max (colores por defecto de Tailwind) no se importaron.
- **Sin duplicados:** lo que ya existía con otro nombre (espaciado monótono, jerarquía plana y ritmo de títulos, que ya están en los tells `L-*` de [`../layout/`](../layout/README.md)) se descartó.

## Resumen

| # | Repo | Licencia | Commit leído | Qué se sumó | Dónde |
|---|---|---|---|---|---|
| 1 | [anthropics/skills](https://github.com/anthropics/skills) | Apache-2.0 (carpetas `frontend-design` y `theme-factory`) | `e4bb5d9` (16/11/2026) | 6 anti-patrones, 4 paletas, revisión del plan contra el brief | anti-patrones, paletas, skill |
| 2 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | MIT | `2de1134` (19/11/2026) | 4 estilos, 20 fuentes, 14 parejas, idea de mapeo por rubro | estilos, tipografias |
| 3 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | MIT | `fcc7028` (28/10/2026) | Plantilla de `DESIGN.md` | casos |
| 4 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | MIT | `f6b7657` (07/11/2026) | 6 anti-patrones de copy, 4 tipos de negocio | anti-patrones, estilos |
| 5 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | Apache-2.0 | `b49177d` (18/11/2026) | 18 anti-patrones, método de revisión, regla de restyling, detector CLI | anti-patrones, skill |
| 6 | [alexpate/awesome-design-systems](https://github.com/alexpate/awesome-design-systems) | Unlicense | `5f21c29` (13/11/2026) | Comparativa de escalas de 4 sistemas, verificadas en la fuente | tokens |
| 7 | [heydamir/unslop](https://github.com/heydamir/unslop) | CC BY 4.0 | `620163e` (15/11/2026) | 8 anti-patrones, orden de pasadas, triage, dirección en 5 líneas, valores de partida | anti-patrones, skill, estilos, tokens |
| 8 | [argyleink/open-props](https://github.com/argyleink/open-props) | MIT | `f39ab7c` (11/10/2026) | 3 easings y la técnica de sombras en capas | tokens |

Totales del kit después del minado: anti-patrones 30 → **59**, paletas 35 → **41**, estilos 27 → **31** (más [`direccion-por-rubro.md`](../estilos/direccion-por-rubro.md)), tipografías 101 → **121**, parejas 28 → **42**. Nuevo [`../indice-rapido.json`](../indice-rapido.json) en la raíz.

Los anti-patrones nuevos suman 29 fichas; varias tienen más de un origen, por eso la suma por repo (18 + 8 + 6 + 6) es mayor. Cada ficha de [`../anti-patrones/anti-patrones.json`](../anti-patrones/anti-patrones.json) lleva un campo `origen`.

## 1. anthropics/skills

- **Anti-patrones (6):** `crema-por-reflejo`, `negro-con-acento-acido`, `broadsheet-de-plantilla`, `metadatos-con-punto-medio`, `una-palabra-acentuada`, `tira-de-cifras`. Vienen de la lista de "clusters" que la skill oficial `frontend-design` marca como el nuevo default de los modelos (crema + serif + terracota; negro + un acento ácido; diario de plantilla). → [`../anti-patrones/catalogo.md`](../anti-patrones/catalogo.md#fichas-3159-minadas-de-repos-de-referencia-noviembre-de-2026).
- **Paletas (4):** `jardin-botanico`, `hora-dorada` ([`organicas.md`](../paletas/organicas.md)), `rosa-desierto` ([`culturales.md`](../paletas/culturales.md)) y `oceano-profundo` ([`saas-producto.md`](../paletas/saas-producto.md)). Adaptadas de los temas de `theme-factory`: se tomaron los colores base y se armaron los roles, el modo oscuro y la medición de contraste del kit. Todas pasan AA en cuerpo.
- **Skill:** el paso de "revisar el plan contra el brief antes de construir" del modo nuevo (`n4` en [`../skills/frontend-design/SKILL.md`](../skills/frontend-design/SKILL.md)).
- **Hallazgo:** al contrastar el cluster crema con el kit, 19 de las 35 paletas originales tienen fondo crema o beige en claro. Se dejó un aviso en [`../paletas/README.md`](../paletas/README.md); las 6 paletas nuevas no usan crema.

## 2. ui-ux-pro-max-skill

- **Estilos (4):** [`bauhaus`](../estilos/bauhaus.md), [`memphis`](../estilos/memphis.md), [`papel-e-ink`](../estilos/papel-e-ink.md) y [`denso-de-datos`](../estilos/denso-de-datos.md). El repo los lista; las fichas, los sitios de referencia y los snippets son del kit. Para bauhaus y memphis se armaron dos paletas propias: `bauhaus-primario` y `memphis-pastel` ([`expresivas.md`](../paletas/expresivas.md)).
- **Tipografías (20):** lexend, source-sans-3, bebas-neue, barlow-condensed, barlow, bodoni-moda, jost, libre-bodoni, crimson-pro, archivo, anton, epilogue, fira-sans, fira-code, fredoka, nunito, merriweather, abril-fatface, work-sans, syncopate. Todas de Google Fonts, con la URL de CSS verificada. Fichas redactadas para Designweb en los md de categoría de [`../tipografias/`](../tipografias/README.md).
- **Parejas (14):** 29 a 42 en [`../tipografias/pairings.md`](../tipografias/pairings.md), más 4 filas de atajos (salud o farmacia, deportes, gastronomía, kids). Índice en `parejas_extra` de `fonts.json`.
- **Idea de mapeo por rubro:** inspiró la tabla de 22 rubros de [`../estilos/direccion-por-rubro.md`](../estilos/direccion-por-rubro.md) y `por_rubro` en `estilos.json`. Los valores son del kit (slugs propios validados), no del CSV del repo.
- **No se tomó:** sus paletas, que son colores por defecto de Tailwind (`#15803D`, `#0891B2`…).

## 3. awesome-design-md

- **Plantilla:** [`../casos/plantilla-design-md.md`](../casos/plantilla-design-md.md), un `DESIGN.md` en castellano con *front matter* YAML de tokens y las secciones del formato (panorama, colores, tipografía, layout, elevación, formas, componentes, hacé y no hagas, responsive, guía para iterar, huecos conocidos). Linkeada desde [`../casos/plantilla.md`](../casos/plantilla.md) y [`../casos/README.md`](../casos/README.md).
- **No se tomó:** ninguno de los `DESIGN.md` de marcas.

## 4. taste-skill

- **Anti-patrones de copy (6):** `tira-de-cifras`, `titulos-en-dos-fragmentos`, `contrastes-fabricados`, `palabras-de-virtud`, `especificos-inventados`, `cierre-ingenioso-y-firma-de-footer`.
- **Tipos de negocio (4):** la división en tipos de negocio para elegir dirección, en [`../estilos/direccion-por-rubro.md`](../estilos/direccion-por-rubro.md) y `tipos_de_negocio` de `estilos.json`.
- Nota: el repo hoy tiene una sola skill (v2.5), no una por dirección como decía el listado anterior.

## 5. impeccable

- **Anti-patrones (18):** desde `serif-italica-de-hero` y `chip-eyebrow-en-hero` hasta `cards-cortadas-en-el-scroller` y `contrastes-fabricados` (lista completa en el campo `origen`). Se tomaron las señales que el kit no tenía de entre las 62 reglas del detector.
- **Método de revisión:** dos miradas separadas (primero el juicio de diseño, después la evidencia medible, idea del `critique` que las corre en subagentes aislados) y la clasificación de la deriva en el pulido, en [`../anti-patrones/checklist-revision.md`](../anti-patrones/checklist-revision.md).
- **Regla del modo restyling:** "pulir es refinar, nunca un rediseño encubierto", en [`../skills/frontend-design/restyling.md`](../skills/frontend-design/restyling.md).
- **Detector:** `npx impeccable detect src/` o contra `http://localhost:5173`, opcional en el paso 5 del restyling. Sus reglas contra `DESIGN.md` se mencionan en la plantilla de casos.

## 6. awesome-design-systems

- **Escalas (4 sistemas):** Carbon, Primer, Polaris y GOV.UK, en [`../tokens/escalas.md`](../tokens/escalas.md#cuatro-sistemas-grandes-una-misma-idea). Los valores se verificaron el 20/11/2026 en la documentación de Carbon y en el código de `primer/primitives`, `Shopify/polaris` y `govuk-frontend`. Se tomaron solo números y principios (la regla de Carbon de bajar un paso en móvil, los alias semánticos de Polaris, la escala responsive de GOV.UK).

## 7. unslop

Todo con atribución a Damir Sokolovsky, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

- **Anti-patrones (8):** `chip-eyebrow-en-hero`, `glow-de-color-en-sombras`, `easing-con-rebote`, `texto-diminuto-o-apretado`, `radios-anidados-que-no-suman`, `cifras-en-formatos-mezclados`, `exclamaciones-y-puntos-en-labels`, `especificos-inventados`.
- **Orden de las pasadas:** las 8 pasadas del restyling (tokens → tipo → color → espaciado → radio y sombra → componentes → layout → motion) en [`restyling.md`](../skills/frontend-design/restyling.md) y el orden por capas del checklist.
- **Triage:** según cuánto slop hay (mucho, poco o nada) se decide entre el flujo completo, arreglar solo lo marcado o proponer dos o tres ajustes. Está en el modo auditoria y en el checklist.
- **Dirección en 5 líneas:** producto, carácter, mundo, momento, firma. En el modo nuevo de la skill y con un ejemplo de farmacia en [`direccion-por-rubro.md`](../estilos/direccion-por-rubro.md). A diferencia de unslop, el kit **no espera aprobación** de la dirección en restyling.
- **Valores de partida:** guía de espaciado por relación, medidas de app (7 tokens `--size-*`), regla de radios anidados, rampas neutras graphite, warm e ink (claro y oscuro, medidas con el script del kit) y semánticos, en [`../tokens/escalas.md`](../tokens/escalas.md) y [`../tokens/tokens.json`](../tokens/tokens.json) (grupo `size`).

## 8. open-props

- **Easings (3):** `--ease-out-3`, `--ease-out-5` y `--ease-in-out-3`, en [`tokens.css`](../tokens/tokens.css), [`theme-tailwind-v4.css`](../tokens/theme-tailwind-v4.css) y `tokens.json`. Quedaron fuera los elastic, squish y spring.
- **Sombras:** la técnica de capas cortas y tenues (token `--shadow-layered`), el color de sombra con tinte más una fuerza que sube en oscuro y el brillo interior en botones oscuros, explicados en [`escalas.md`](../tokens/escalas.md#easings-y-sombras-de-open-props).

## Mantenimiento

- Cuando cambie `estilos.json`, `paletas.json` o `fonts.json`, regenerá el índice: `python3 recursos/generar-indice-rapido.py` desde la raíz del kit.
- Para un minado futuro, sumá una sección con fecha a este archivo y el campo `minado` en [`repos-referencia.json`](./repos-referencia.json).

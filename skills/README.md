# Skills

Hoy hay una skill: [`frontend-design`](frontend-design/SKILL.md), con tres modos (ver abajo). En modo `nuevo` obliga a elegir estilo, paleta, pareja tipográfica, tokens y layout (patrones, anchos, densidad, foco) de este kit, y a definir la UX (flujo, estados, formularios, accesibilidad, microcopy) con [`ux/`](../ux/README.md) antes de escribir UI. Cierra contra los checklists de anti-patrones, de layout y de UX ([`ux/checklist-ux.md`](../ux/checklist-ux.md)).

## Instalar

Claude Code lee skills de dos lugares. Copiá la carpeta, no el archivo suelto:

- Personal, en cualquier proyecto: `~/.claude/skills/frontend-design`
- Solo en un proyecto: `<proyecto>/.claude/skills/frontend-design`

Desde la raíz de este repo:

```bash
mkdir -p ~/.claude/skills
cp -R skills/frontend-design ~/.claude/skills/frontend-design
```

Para dejarla en el proyecto que vas a diseñar, cambiá el destino a `<proyecto>/.claude/skills/frontend-design`.

La skill se dispara al construir o rediseñar un sitio, una landing, una UI de SaaS, un dashboard o un componente. No hace falta invocarla por nombre.

## Los tres modos

La skill elige el modo sola por el pedido, pero conviene nombrarlo en el primer mensaje.

| Modo | Para qué | Cómo invocarlo | Qué hace distinto |
|---|---|---|---|
| `nuevo` | Construir una pantalla, página o componente desde cero, o rehacerlo entero | `Usá la skill frontend-design en modo nuevo…` | Flujo completo: clasificar, elegir estilo, paleta, tipo, tokens y layout, definir la UX, dirección y brief, construir y revisar. Un S4 de UX bloquea la entrega |
| `restyling` | Cambiar solo lo visual de algo que ya existe ("rediseño sin tocar interfaces") | `Usá la skill frontend-design en modo restyling…` | Lee como máximo 3 archivos del kit, detecta el stack, escribe un brief de 5 líneas **sin pedir aprobación** y edita enseguida tema, CSS y `className` en commits chicos. No cambia estructura, textos, props, lógica, rutas ni APIs. El checklist va al final como reporte, no bloquea. Nunca termina sin diffs. Detalle: [`frontend-design/restyling.md`](frontend-design/restyling.md) |
| `auditoria` | Saber qué le falla a una UI sin tocarla | `Usá la skill frontend-design en modo auditoria…` | No edita. Reporta cada tell con id, archivo, severidad y arreglo, y cierra con un triage (mucho, poco o nada de slop) |

Los prompts completos, listos para pegar, están al final de [`SKILL.md`](frontend-design/SKILL.md#ejemplos-de-prompt). El de restyling:

```
Usá la skill frontend-design en modo restyling. El kit Designweb está en <RUTA_AL_CLON>.
Rediseñá solo lo visual de <CARPETA_O_PANTALLA, p. ej. src/app>: tipografía, colores, espaciado,
radios, sombras, motion y pulido de layout. No cambies la estructura, los textos, las props,
la lógica, las rutas ni las APIs de los componentes.
Leé como máximo 3 archivos del kit (empezá por indice-rapido.json), detectá dónde viven los estilos,
escribí un brief de 5 líneas y aplicá los cambios enseguida en el tema, el CSS global y los className,
con un commit chico por pasada. No me pidas aprobación del brief y no termines sin diffs.
Al final corré el build, sacá capturas a 1440 y 390 px y pasame el checklist como reporte, con lo que
quede fuera de alcance como sugerencias.
```

Si Claude igual se queda planificando: verificá que no esté en modo plan (Shift+Tab en Claude Code) y que tenga permiso para editar archivos, y repetí "aplicá los cambios ahora, empezando por los tokens".

## Apuntarla al clon

Las rutas de la skill (`estilos/estilos.json`, `paletas/paletas.json`, etc.) son relativas a la raíz de **este** repo, no a la carpeta de la skill.

- Si trabajás dentro del clon, Claude ya está parado en la raíz y las rutas resuelven solas.
- Si la skill corre en otro proyecto, decile la ruta absoluta del clon en el primer mensaje o, mejor, en el `CLAUDE.md` de ese proyecto. Por ejemplo: `El kit Designweb está en /ruta/al/clon`. Sin esa ruta la skill tiene que pedirla. No adivina paletas ni fuentes.

Mantené el clon actualizado: la skill no copia el catálogo, lo lee. Si copiaste la skill antes de noviembre de 2026, volvé a copiar la carpeta entera: ahora trae `restyling.md` además de `SKILL.md`.

## Pegar las reglas en CLAUDE.md

El bloque listo está en [`anti-patrones/reglas-para-agentes.md`](../anti-patrones/reglas-para-agentes.md), dentro del fence `md`. Copiá ese bloque al `CLAUDE.md` (o `AGENTS.md`) del proyecto que se va a diseñar.

Para la UX hay un segundo bloque en [`ux/anti-patrones-ux.md`](../ux/anti-patrones-ux.md#bloque-pegable-para-claudemd-ux); pegalo debajo del primero.

Si el kit no vive en ese proyecto, ajustá las rutas del bloque a la ruta absoluta del clon. La skill elige; el bloque prohíbe los tells en cada sesión, aunque la skill no se dispare.

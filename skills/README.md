# Skills

Hoy hay una skill: [`frontend-design`](frontend-design/SKILL.md). Obliga a elegir estilo, paleta, pareja tipográfica, tokens y layout (patrones, anchos, densidad, foco) de este kit antes de escribir UI, y a cerrar contra los checklists de anti-patrones y de layout.

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

## Apuntarla al clon

Las rutas de la skill (`estilos/estilos.json`, `paletas/paletas.json`, etc.) son relativas a la raíz de **este** repo, no a la carpeta de la skill.

- Si trabajás dentro del clon, Claude ya está parado en la raíz y las rutas resuelven solas.
- Si la skill corre en otro proyecto, decile la ruta absoluta del clon en el primer mensaje o, mejor, en el `CLAUDE.md` de ese proyecto. Por ejemplo: `El kit Designweb está en /ruta/al/clon`. Sin esa ruta la skill tiene que pedirla. No adivina paletas ni fuentes.

Mantené el clon actualizado: la skill no copia el catálogo, lo lee.

## Pegar las reglas en CLAUDE.md

El bloque listo está en [`anti-patrones/reglas-para-agentes.md`](../anti-patrones/reglas-para-agentes.md), dentro del fence `md`. Copiá ese bloque al `CLAUDE.md` (o `AGENTS.md`) del proyecto que se va a diseñar.

Si el kit no vive en ese proyecto, ajustá las rutas del bloque a la ruta absoluta del clon. La skill elige; el bloque prohíbe los tells en cada sesión, aunque la skill no se dispare.

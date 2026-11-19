# Casos

Esta carpeta es el lugar donde Tomás documenta **sus** proyectos, no una galería inventada. El valor para un agente (Claude Code, Cursor) está en el antes / después y en las *decisiones*: por qué se eligió una tipografía del kit, un estilo, una paleta, y qué se descartó porque se veía a plantilla de IA.

Hoy **no hay casos cargados**. No se fabrican. Cuando haya uno real (con captura y una nota de oficio), se agrega un archivo por proyecto y se lo lista acá.

Proyectos que *podrían* entrar, cuando Tomás los documente — no son fichas, son recordatorios:

- trabajo de producto de MaatWork (por ejemplo gympro o el pilates de Oro)
- piezas propias de communication o de utilidad (un organigrama, una planilla, un experimento de landing)

Ninguno de esos nombres se toma como caso escrito hasta que exista el markdown, las capturas y las decisiones.

## Qué hay acá

| Archivo | Contenido |
|---|---|
| [plantilla.md](./plantilla.md) | Molde para un caso: contexto, antes, decisiones, después, qué no hacer la próxima |

## Cómo se documenta un caso

1. **Copiá** [plantilla.md](./plantilla.md) a un archivo `slug-del-proyecto.md` (minúsculas, sin acentos, guiones).
2. **Completá el antes** con una captura real (o un link a staging / un commit) y una descripción honesta de lo que estaba mal o de lo que la IA había propuesto. Si no hay “antes”, declaralo: es un trabajo de cero, y entonces el contraste es contra el *default* que se evitó (Inter + degradé violeta, tres cards, Geist).
3. **Anotá decisiones con puntero al kit**: tipografía de [`../tipografias/`](../tipografias/README.md), estilo de [`../estilos/`](../estilos/README.md), patrón de [`../componentes/`](../componentes/README.md), motion de [`../animaciones/`](../animaciones/README.md). Una línea de porqué alcanza; no un ensayo.
4. **El después** es una captura o un URL público. Sin retoque que mienta (no recortes que escondan un error).
5. **Cerrá** con lo que no funcionó y lo que no repetirías. Eso es lo que más le sirve a un agente la próxima vez.
6. **Listá el caso en esta tabla** (más abajo) y, si más adelante hay un `casos.json`, sumalo ahí.

Las capturas pueden vivir en esta carpeta (`casos/media/slug-antes.png`) o en un Drive, con el link en la ficha. No subas datos de clientes ni números de caja reales si el repo es o se vuelve público: anonimizá.

## Índice de casos

| Caso | Proyecto | Fecha | Estado |
|---|---|---|---|
| — | Todavía no hay | — | ⏳ Esperando el primero |

Cuando exista el primero, esta tabla deja de estar vacía y el README del repo puede apuntar a él.

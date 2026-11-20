# Plantilla de DESIGN.md para un proyecto

Un `DESIGN.md` en la raíz del proyecto es el archivo que un agente lee **antes** de tocar la UI: fija los tokens y las reglas de ese proyecto en particular, para que no tenga que adivinarlos ni volver a abrir el kit entero. Es especialmente útil para el modo restyling de [`../skills/frontend-design/`](../skills/frontend-design/SKILL.md): la primera sesión lo escribe y las siguientes lo respetan.

El formato está adaptado (no copiado) de dos fuentes con licencia permisiva, revisadas el 20 de noviembre de 2026:

- [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) (MIT): colección de `DESIGN.md` con *front matter* YAML de tokens y secciones fijas, en el formato que popularizó Google Stitch.
- [pbakaus/impeccable](https://github.com/pbakaus/impeccable) (Apache-2.0): su detector (`npx impeccable detect`) tiene reglas que comparan el código contra el `DESIGN.md` (fuentes, colores, radios y tamaños fuera del sistema).

La colección de awesome-design-md describe sitios de marcas reales. **No copies la identidad de una marca** a un proyecto propio: usá la estructura y completala con tokens del kit.

## Cómo usarla

1. Copiá el bloque de abajo a `DESIGN.md` en la raíz del proyecto (no en este kit).
2. Completá el YAML con los valores elegidos: la paleta de [`../paletas/`](../paletas/README.md), la pareja de [`../tipografias/pairings.md`](../tipografias/pairings.md) y la escala de [`../tokens/`](../tokens/README.md). Sin hex inventados: si no está decidido, dejá `TODO`.
3. Llená las secciones con una o dos líneas cada una. Si una sección no aplica, escribí "no aplica" en vez de borrarla, así el agente sabe que no es un olvido.
4. Agregá al `CLAUDE.md` o `AGENTS.md` del proyecto: "Antes de tocar la UI, leé `DESIGN.md` y no uses valores fuera de él."
5. Cada vez que cambie una decisión, se actualiza acá primero y en el código después.

## La plantilla

```markdown
---
version: 1
name: <Nombre del proyecto>
description: <Una línea: qué es y para quién>
kit:
  estilo: <slug de estilos.json, p. ej. suizo-neutro>
  paleta: <slug de paletas.json>
  pareja: <número o nombre en tipografias/pairings.md>
colors:
  light:
    background: "#......"
    surface: "#......"
    text: "#......"
    muted: "#......"
    border: "#......"
    accent: "#......"
    accent-foreground: "#......"
  dark:
    background: "#......"
    surface: "#......"
    text: "#......"
    muted: "#......"
    border: "#......"
    accent: "#......"
    accent-foreground: "#......"
typography:
  display: { family: "<familia>", weights: [500, 700] }
  body: { family: "<familia>", weights: [400, 500] }
  mono: { family: "<familia o ninguna>" }
  scale: [12, 14, 16, 18, 20, 24, 32, 40, 56]
rounded: { default: 6, card: 12, full: 9999 }
spacing: [4, 8, 12, 16, 24, 32, 48, 64, 96]
motion: { fast: 120ms, base: 180ms, ease: "cubic-bezier(0.2, 0, 0, 1)" }
components:
  button: { height: 36, padding-x: 16, radius: default }
  input: { height: 36, radius: default }
  card: { padding: 24, radius: card, shadow: none }
---

# <Nombre del proyecto>: sistema de diseño

## Panorama
Producto, carácter, mundo, momento y firma en cinco líneas (ver estilos/direccion-por-rubro.md del kit).

## Colores
Qué rol cumple cada color, dónde se usa el acento (unos pocos por ciento de la pantalla) y los pares medidos (WCAG y APCA).

## Tipografía
Para qué es cada familia, tamaño mínimo de cuerpo, interlineado y tracking del display.

## Layout
Grilla, ancho máximo, márgenes, ritmo entre secciones y qué pasa en móvil.

## Elevación y profundidad
Sombras (o su ausencia), bordes, cómo se separan las superficies en oscuro.

## Formas
Radio por defecto, radios anidados (interior = exterior − padding), íconos (set, tamaño, trazo).

## Componentes
Variantes permitidas de botón, input, card, tabla y nav. Estados: hover, focus visible, disabled, loading, vacío, error.

## Hacé y no hagas
- Hacé: <dos o tres reglas propias del proyecto>
- No hagas: <los anti-patrones del kit que este proyecto tiende a repetir, por slug>

## Comportamiento responsive
Breakpoints usados y qué cambia en cada uno.

## Guía para iterar
Qué se puede tocar sin preguntar (pulido visual) y qué necesita una decisión (estructura, copy, marca).

## Huecos conocidos
Lo que todavía no está decidido. Mejor declararlo que dejar que el agente lo invente.
```

## Por qué estas secciones

- **El YAML** es lo que un agente puede leer con `yq` o copiar a `tokens.css` sin interpretar prosa. Los detectores (impeccable) también lo usan para marcar valores fuera de sistema.
- **"Hacé y no hagas"** con slugs del kit evita repetir los tells de [`../anti-patrones/`](../anti-patrones/README.md) en cada sesión.
- **"Guía para iterar"** es la frontera del modo restyling: lo que se pule sin pedir permiso y lo que no.
- **"Huecos conocidos"** reemplaza la invención: si falta un dato, el agente lo ve declarado.

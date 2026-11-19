---
name: frontend-design
description: "Úsala al construir o rediseñar cualquier sitio web, landing, UI de SaaS, dashboard o componente. Use this skill before writing or restyling any website, landing page, SaaS UI, dashboard, or UI component. Elige un estilo, una paleta, una pareja tipográfica y tokens del kit Designweb, y revisa anti-patrones/checklist-revision.md antes de dar la UI por terminada."
---

# Diseño frontend

Antes de escribir o retocar UI, decidí con el kit. No arranques por un componente. Las rutas de abajo son relativas a la **raíz del clon de Designweb**, no a esta skill.

## Dónde está el kit

- Si el workspace es el clon, la raíz es ese repo.
- Si estás en otro proyecto, usá la ruta absoluta que el usuario indicó (o la de `CLAUDE.md`). Si no hay ruta, pedila. No inventes paletas, fuentes ni tokens.
- `casos/` está vacío. No fabriques casos.

## a) Clasificar

En una frase: tipo de proyecto (SaaS, landing, dashboard, editorial, devtool, comercio, marca) y mood (técnico, editorial, cálido, quieto, expresivo). Si el usuario ya eligió estilo, paleta o tipo, respetalo.

## b) Elegir

Leé los JSON. Una decisión por eje. El detalle vive en el markdown del slug, no lo copies acá.

1. **Estilo.** En `estilos/estilos.json`, un `slug` cuyo `mejor_para` encaje y cuyo `evitar_en` no contradiga el trabajo. Leé `estilos/<slug>.md` (reglas, “cuándo no”, ejemplos). Uno solo. Un acento de otro estilo solo si la ficha lo permite.
2. **Paleta compatible.** En `paletas/paletas.json`, una paleta cuyo array `estilos` incluya ese slug. Usá los roles de `modos.light.tokens` y `modos.dark.tokens` (`bg`, `surface`, `border`, `text`, `muted`, `accent`, `accent-foreground`, `accent-text`, estados). El color de marca existente se respeta: se arma la rampa alrededor, no se reemplaza. Si el acento duda, leé `paletas/evadir-degrade-violeta.md`.
3. **Pareja tipográfica.** Tomá los ids de `fuentes_recomendadas` del estilo y abrí esas fichas en `tipografias/fonts.json` (`nombre`, `licencia`, `snippet_import`, `pareja_recomendada`). Confirmá titular + cuerpo en `tipografias/pairings.md` según el tipo de proyecto. Dos familias; un mono solo si el producto lo pide. Mostrá licencia e import. En producción, autohospedá.
4. **Tokens.** Escalas en `tokens/tokens.json` y `tokens/escalas.md`. Pegá `tokens/tokens.css` o, si el stack es Tailwind v4, `tokens/theme-tailwind-v4.css`. El color sale de la paleta, no de este archivo. Un radio por proyecto. Una familia de sombra (o ninguna).
5. **Componentes.** En `componentes/componentes.json`, los `patrones` que vas a construir (`archivo`, `estilos_afines`, `error_ia`, `terminacion_pro`). Leé `componentes/<archivo>`. Una librería de `bibliotecas` solo si hace falta; el tema default de shadcn no es una estética.
6. **Motion.** En `animaciones/animaciones.json`, una herramienta y solo las `recetas` de la superficie (`archivo`, `duracion_ms`, `easing`). CSS primero. Leé `animaciones/accesibilidad-performance.md` si hay scroll o entrada. `prefers-reduced-motion` apaga la animación.

Íconos, imagen, grano y OG salen de `recursos/README.md`. No uses Lucide por default.

## c) Brief

Escribí esto, corto, **antes** del código:

```
Tipo y mood:
Estilo: <slug> — por qué, y qué evita
Paleta: <slug> — por qué combina con el estilo
Tipo: <titular> + <cuerpo> — licencia e import
Tokens: radio, sombra, duración base
Piezas: patrones y motion que sí entran
No entra: el tell más probable de este proyecto y cómo se corta
```

No reabras el menú en cada componente.

## d) Construir

Aplicá el brief. Nombres de token (`var(--space-6)`, radio y duración del sistema), no hex, `px` o `duration-1000` sueltos. Un acento sólido. Prueba real cerca del inicio (precio, nombre, horario, captura del producto). Meta, alt, favicon y OG no salen de la plantilla.

## e) Revisar

Pasá `anti-patrones/checklist-revision.md`. Cada “sí” es un tell. Con tres o más, arreglá antes de cerrar, usando `como_arreglar` en `anti-patrones/catalogo.md` o el slug en `anti-patrones/anti-patrones.json`. No respondas “hacelo más único”.

Salvo brief explícito, no uses Inter, Geist, Roboto, Poppins, Montserrat o Instrument Serif como voz principal, ni índigo, violeta o degradé `from-indigo-* to-purple-*` como identidad. El resto de las prohibiciones está en `anti-patrones/reglas-para-agentes.md`.

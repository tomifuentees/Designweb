# Papel / e-ink

Pantallas que se comportan como papel: escala de grises o un solo tinte, contraste alto, cero glow, cero motion decorativo, tipografía de lectura de verdad. Lo empujan los lectores e-ink, las "pantallas calmas" (Daylight, reMarkable) y la fatiga con las interfaces que brillan. [ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) (MIT) lo cataloga como "E-Ink / Paper"; esta ficha es propia.

## Cuándo usarlo y cuándo no

**Usalo** en lectura larga, documentación, newsletters, herramientas de escritura y notas, productos de "foco" o bienestar digital, archivos y bibliotecas.

**No lo uses** cuando el color codifica información crítica (estados de salud, mapas de calor, trading) ni en campañas que necesitan energía.

## Reglas concretas

- **Grilla:** una columna de lectura (`65ch`), márgenes amplios, notas al costado en pantallas anchas.
- **Espaciado:** ritmo vertical basado en el interlineado del cuerpo.
- **Radios:** 0–2 px.
- **Bordes:** filetes de 1 px en gris medio; separan secciones, no cajas.
- **Sombras:** ninguna. La profundidad no existe en el papel.
- **Color:** blanco papel **frío o neutro** (no crema por reflejo, ver `crema-por-reflejo` en ../anti-patrones/catalogo.md), negro tinta, dos grises. Un tinte opcional para links. Contraste de cuerpo ≥ 7:1.
- **Motion:** ninguno salvo el que responde a la persona; transiciones instantáneas o ≤ 100 ms.
- **Tipografía:** serif de texto de pantalla y una mono para metadatos solo si el producto es técnico.
  - Cuerpo: [Literata](../tipografias/serif-texto.md) (diseñada para lectura en pantalla) o [Source Serif 4](../tipografias/serif-texto.md).
  - UI: [Atkinson Hyperlegible](../tipografias/sans-grotesk.md) o [IBM Plex Sans](../tipografias/sans-grotesk.md).
  - Mono: [IBM Plex Mono](../tipografias/mono.md).

## Sitios reales

- [daylightcomputer.com](https://daylightcomputer.com/) — la tablet "live paper": la marca entera es calma.
- [remarkable.com](https://remarkable.com/) — tablet de papel; marketing sobrio, fotos de uso.
- [standardebooks.org](https://standardebooks.org/) — libros de dominio público con tipografía cuidada y casi sin cromo.
- [are.na](https://www.are.na/) — interfaz casi monocroma, centrada en el contenido.

## Errores comunes

- Grises claros para el cuerpo "porque es papel": el papel real tiene tinta negra.
- Fondo crema + serif + terracota: eso es el default de IA, no papel.
- Skeletons animados y fades: rompen la calma. Mostrá el texto cuando está.
- Tipografía display de moda en el cuerpo.

## Snippet

```css
:root {
  --bg: oklch(0.985 0 0);     /* papel neutro */
  --text: oklch(0.18 0 0);    /* tinta */
  --muted: oklch(0.42 0 0);
  --rule: oklch(0.80 0 0);
  --link: oklch(0.38 0.08 250);
}
body { background: var(--bg); color: var(--text); font: 400 1.125rem/1.65 "Literata", Georgia, serif; }
main { max-width: 65ch; margin-inline: auto; padding: 4rem 1.5rem; }
h1, h2 { font-weight: 600; line-height: 1.15; text-wrap: balance; }
p { text-wrap: pretty; }
hr { border: 0; border-top: 1px solid var(--rule); margin-block: 2.5rem; }
a { color: var(--link); text-underline-offset: 0.2em; }
```

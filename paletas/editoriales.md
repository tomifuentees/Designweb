# Paletas editoriales y de imprenta

Fondos de papel, tintas, un rojo o un azul de sello. Sirven para [`editorial-revista`](../estilos/editorial-revista.md), [`risografia-impreso`](../estilos/risografia-impreso.md), [`suizo-internacional`](../estilos/suizo-internacional.md) y buena parte de [`expresivo-minimo`](../estilos/expresivo-minimo.md). El fondo **no es blanco puro**: es crema, newsprint o pergamino. El acento aparece como un colofón, un kicker o un link, no como un hero degradé.


Hay **5 paletas** en este grupo. Los valores salen de [`paletas.json`](./paletas.json). Los links de estilo apuntan a las fichas de [`../estilos/`](../estilos/README.md).


---

## Papel y tinta

`papel-tinta` — Revista, crema, tinta, un rojo de imprenta

**Mejor para:** editoriales, estudios, blogs largos, marcas culturales.  
**Evitá en:** dashboards densos, devtools que necesitan dark por default.  
**Estilos:** [`editorial-revista`](../estilos/editorial-revista.md), [`risografia-impreso`](../estilos/risografia-impreso.md), [`expresivo-minimo`](../estilos/expresivo-minimo.md), [`scrollytelling`](../estilos/scrollytelling.md).

El fondo no es blanco puro (#fff). El rojo no es el danger: es tinta de acento (como un colofón). Danger se reserva más oscuro.

### Claro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#f4efe6` | `oklch(0.9535 0.01313 82.40)` |
| Superficie | `#ebe4d7` | `oklch(0.9208 0.01898 83.06)` |
| Borde | `#d4c9b6` | `oklch(0.8397 0.02861 81.46)` |
| Texto | `#1c1612` | `oklch(0.2061 0.01244 55.60)` |
| Muted | `#665c50` | `oklch(0.4807 0.02273 72.29)` |
| Acento (sólido) | `#a11c1c` | `oklch(0.4598 0.16823 27.00)` |
| Acento foreground | `#fff6f0` | `oklch(0.9785 0.01256 56.26)` |
| Acento texto/link | `#a11c1c` | `oklch(0.4598 0.16823 27.00)` |
| Success | `#1f6b3a` | `oklch(0.4689 0.10756 151.36)` |
| Warn | `#8a5a00` | `oklch(0.5078 0.10800 73.30)` |
| Danger | `#7a1212` | `oklch(0.3753 0.13802 27.09)` |

### Oscuro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#161310` | `oklch(0.1892 0.00770 67.33)` |
| Superficie | `#211c18` | `oklch(0.2308 0.01087 60.90)` |
| Borde | `#3a322a` | `oklch(0.3231 0.01791 67.12)` |
| Texto | `#f3ebde` | `oklch(0.9428 0.01935 80.12)` |
| Muted | `#b3a490` | `oklch(0.7261 0.03308 75.10)` |
| Acento (sólido) | `#c43e32` | `oklch(0.5563 0.17246 28.90)` |
| Acento foreground | `#ffffff` | `oklch(1.0000 0.00000 0.00)` |
| Acento texto/link | `#ff9f91` | `oklch(0.7965 0.11714 28.89)` |
| Success | `#7dda9a` | `oklch(0.8138 0.12756 152.72)` |
| Warn | `#e8b849` | `oklch(0.8060 0.13714 85.03)` |
| Danger | `#ff8a80` | `oklch(0.7594 0.14351 26.08)` |

### Contraste

**Claro:** texto sobre fondo WCAG 15.63:1, APCA Lc 95.4 (oscuro-sobre-claro); texto sobre superficie WCAG 14.16:1, APCA Lc 89.1 (oscuro-sobre-claro); accent-foreground sobre acento WCAG 7.3:1, APCA Lc -85.3 (claro-sobre-oscuro). Muted sobre fondo WCAG 5.71:1, APCA Lc 73.2 (oscuro-sobre-claro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 6.79:1, APCA Lc 76.1 (oscuro-sobre-claro)). `accent-text` está igualado o derivado para ese rol.

**Oscuro:** texto sobre fondo WCAG 15.64:1, APCA Lc -94.7 (claro-sobre-oscuro); texto sobre superficie WCAG 14.27:1, APCA Lc -93.7 (claro-sobre-oscuro); accent-foreground sobre acento WCAG 5.14:1, APCA Lc -79.8 (claro-sobre-oscuro). Muted sobre fondo WCAG 7.6:1, APCA Lc -53.4 (claro-sobre-oscuro): sirve para cuerpo secundario. El acento sólido no llega a 4.5:1 como texto sobre el fondo (3.6:1). Para botones usá `accent` + `accent-foreground`. Para links usá `accent-text` (9.36:1, Lc -63.8).

### Tokens CSS

```css
:root {
  /* Papel y tinta — claro */
  --bg: oklch(0.9535 0.01313 82.40); /* #f4efe6 */
  --surface: oklch(0.9208 0.01898 83.06); /* #ebe4d7 */
  --border: oklch(0.8397 0.02861 81.46); /* #d4c9b6 */
  --text: oklch(0.2061 0.01244 55.60); /* #1c1612 */
  --muted: oklch(0.4807 0.02273 72.29); /* #665c50 */
  --accent: oklch(0.4598 0.16823 27.00); /* #a11c1c */
  --accent-foreground: oklch(0.9785 0.01256 56.26); /* #fff6f0 */
  --accent-text: oklch(0.4598 0.16823 27.00); /* #a11c1c */
  --success: oklch(0.4689 0.10756 151.36); /* #1f6b3a */
  --warn: oklch(0.5078 0.10800 73.30); /* #8a5a00 */
  --danger: oklch(0.3753 0.13802 27.09); /* #7a1212 */
}

.dark {
  /* Papel y tinta — oscuro */
  --bg: oklch(0.1892 0.00770 67.33); /* #161310 */
  --surface: oklch(0.2308 0.01087 60.90); /* #211c18 */
  --border: oklch(0.3231 0.01791 67.12); /* #3a322a */
  --text: oklch(0.9428 0.01935 80.12); /* #f3ebde */
  --muted: oklch(0.7261 0.03308 75.10); /* #b3a490 */
  --accent: oklch(0.5563 0.17246 28.90); /* #c43e32 */
  --accent-foreground: oklch(1.0000 0.00000 0.00); /* #ffffff */
  --accent-text: oklch(0.7965 0.11714 28.89); /* #ff9f91 */
  --success: oklch(0.8138 0.12756 152.72); /* #7dda9a */
  --warn: oklch(0.8060 0.13714 85.03); /* #e8b849 */
  --danger: oklch(0.7594 0.14351 26.08); /* #ff8a80 */
}
```


---

## Crema y cobalto

`crema-cobalto` — Papel cálido con un azul de sello, no índigo de Tailwind

**Mejor para:** estudios, PyMEs con oficio, editoriales, arquitectura.  
**Evitá en:** si el cobalto se va hacia el violeta, dejalo.  
**Estilos:** [`editorial-revista`](../estilos/editorial-revista.md), [`expresivo-minimo`](../estilos/expresivo-minimo.md), [`suizo-internacional`](../estilos/suizo-internacional.md), [`ilustrado-humano`](../estilos/ilustrado-humano.md).

El cobalto de sello (~250–255°) no es bg-indigo-500 (~275°). Si al previsualizarlo ‘se siente plantilla’, bajale la croma o cambialo por óxido.

### Claro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#f6f1e8` | `oklch(0.9596 0.01311 82.40)` |
| Superficie | `#ede6da` | `oklch(0.9272 0.01775 81.33)` |
| Borde | `#d6ccbc` | `oklch(0.8489 0.02445 79.73)` |
| Texto | `#1a1713` | `oklch(0.2066 0.00906 75.12)` |
| Muted | `#5e574c` | `oklch(0.4601 0.01957 79.22)` |
| Acento (sólido) | `#1848a8` | `oklch(0.4323 0.16308 262.12)` |
| Acento foreground | `#f3f6ff` | `oklch(0.9735 0.01242 271.29)` |
| Acento texto/link | `#1848a8` | `oklch(0.4323 0.16308 262.12)` |
| Success | `#1f6b3a` | `oklch(0.4689 0.10756 151.36)` |
| Warn | `#8a5a00` | `oklch(0.5078 0.10800 73.30)` |
| Danger | `#b42318` | `oklch(0.5003 0.18205 29.51)` |

### Oscuro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#14120e` | `oklch(0.1831 0.00855 84.57)` |
| Superficie | `#1e1b16` | `oklch(0.2237 0.01050 80.58)` |
| Borde | `#3a342c` | `oklch(0.3287 0.01611 75.06)` |
| Texto | `#f2ebdf` | `oklch(0.9423 0.01768 81.33)` |
| Muted | `#afa496` | `oklch(0.7241 0.02359 74.01)` |
| Acento (sólido) | `#4271d6` | `oklch(0.5687 0.16359 263.36)` |
| Acento foreground | `#ffffff` | `oklch(1.0000 0.00000 0.00)` |
| Acento texto/link | `#8db3ff` | `oklch(0.7690 0.11727 263.52)` |
| Success | `#7dda9a` | `oklch(0.8138 0.12756 152.72)` |
| Warn | `#e8b849` | `oklch(0.8060 0.13714 85.03)` |
| Danger | `#ff8a80` | `oklch(0.7594 0.14351 26.08)` |

### Contraste

**Claro:** texto sobre fondo WCAG 15.87:1, APCA Lc 96.6 (oscuro-sobre-claro); texto sobre superficie WCAG 14.4:1, APCA Lc 90.3 (oscuro-sobre-claro); accent-foreground sobre acento WCAG 7.68:1, APCA Lc -86.8 (claro-sobre-oscuro). Muted sobre fondo WCAG 6.34:1, APCA Lc 76.7 (oscuro-sobre-claro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 7.37:1, APCA Lc 79.9 (oscuro-sobre-claro)). `accent-text` está igualado o derivado para ese rol.

**Oscuro:** texto sobre fondo WCAG 15.79:1, APCA Lc -94.7 (claro-sobre-oscuro); texto sobre superficie WCAG 14.49:1, APCA Lc -93.8 (claro-sobre-oscuro); accent-foreground sobre acento WCAG 4.6:1, APCA Lc -77.1 (claro-sobre-oscuro). Muted sobre fondo WCAG 7.64:1, APCA Lc -53.2 (claro-sobre-oscuro): sirve para cuerpo secundario. El acento sólido no llega a 4.5:1 como texto sobre el fondo (4.07:1). Para botones usá `accent` + `accent-foreground`. Para links usá `accent-text` (8.93:1, Lc -60.8).

### Tokens CSS

```css
:root {
  /* Crema y cobalto — claro */
  --bg: oklch(0.9596 0.01311 82.40); /* #f6f1e8 */
  --surface: oklch(0.9272 0.01775 81.33); /* #ede6da */
  --border: oklch(0.8489 0.02445 79.73); /* #d6ccbc */
  --text: oklch(0.2066 0.00906 75.12); /* #1a1713 */
  --muted: oklch(0.4601 0.01957 79.22); /* #5e574c */
  --accent: oklch(0.4323 0.16308 262.12); /* #1848a8 */
  --accent-foreground: oklch(0.9735 0.01242 271.29); /* #f3f6ff */
  --accent-text: oklch(0.4323 0.16308 262.12); /* #1848a8 */
  --success: oklch(0.4689 0.10756 151.36); /* #1f6b3a */
  --warn: oklch(0.5078 0.10800 73.30); /* #8a5a00 */
  --danger: oklch(0.5003 0.18205 29.51); /* #b42318 */
}

.dark {
  /* Crema y cobalto — oscuro */
  --bg: oklch(0.1831 0.00855 84.57); /* #14120e */
  --surface: oklch(0.2237 0.01050 80.58); /* #1e1b16 */
  --border: oklch(0.3287 0.01611 75.06); /* #3a342c */
  --text: oklch(0.9423 0.01768 81.33); /* #f2ebdf */
  --muted: oklch(0.7241 0.02359 74.01); /* #afa496 */
  --accent: oklch(0.5687 0.16359 263.36); /* #4271d6 */
  --accent-foreground: oklch(1.0000 0.00000 0.00); /* #ffffff */
  --accent-text: oklch(0.7690 0.11727 263.52); /* #8db3ff */
  --success: oklch(0.8138 0.12756 152.72); /* #7dda9a */
  --warn: oklch(0.8060 0.13714 85.03); /* #e8b849 */
  --danger: oklch(0.7594 0.14351 26.08); /* #ff8a80 */
}
```


---

## Diario y rojo

`diario-rojo` — Periódico, almost-swiss, spot red

**Mejor para:** noticias, estudios políticos, reportes, suizo con carácter.  
**Evitá en:** productos lúdicos, lujo cálido.  
**Estilos:** [`suizo-internacional`](../estilos/suizo-internacional.md), [`editorial-revista`](../estilos/editorial-revista.md), [`catalogo-tecnico`](../estilos/catalogo-tecnico.md), [`minimalismo-monocromo`](../estilos/minimalismo-monocromo.md).

Tipografía y grilla hacen el trabajo. El rojo aparece en un dato, un kicker o un link, no en un hero degradé.

### Claro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#f3f1ec` | `oklch(0.9583 0.00699 88.64)` |
| Superficie | `#e8e6e0` | `oklch(0.9248 0.00833 91.49)` |
| Borde | `#cfcbc3` | `oklch(0.8431 0.01183 84.58)` |
| Texto | `#111111` | `oklch(0.1776 0.00000 0.00)` |
| Muted | `#5a5854` | `oklch(0.4609 0.00688 84.58)` |
| Acento (sólido) | `#c3002f` | `oklch(0.5166 0.20769 20.73)` |
| Acento foreground | `#fff7f7` | `oklch(0.9823 0.00858 17.30)` |
| Acento texto/link | `#c3002f` | `oklch(0.5166 0.20769 20.73)` |
| Success | `#1f6b3a` | `oklch(0.4689 0.10756 151.36)` |
| Warn | `#8a5a00` | `oklch(0.5078 0.10800 73.30)` |
| Danger | `#8e1020` | `oklch(0.4158 0.15719 22.42)` |

### Oscuro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#121211` | `oklch(0.1818 0.00201 106.60)` |
| Superficie | `#1c1c1a` | `oklch(0.2257 0.00379 106.70)` |
| Borde | `#33322e` | `oklch(0.3167 0.00711 95.29)` |
| Texto | `#f1efea` | `oklch(0.9523 0.00700 88.64)` |
| Muted | `#a8a59e` | `oklch(0.7224 0.01055 87.49)` |
| Acento (sólido) | `#d52e4d` | `oklch(0.5753 0.20089 16.65)` |
| Acento foreground | `#ffffff` | `oklch(1.0000 0.00000 0.00)` |
| Acento texto/link | `#ff9ca1` | `oklch(0.7952 0.11848 16.83)` |
| Success | `#7dda9a` | `oklch(0.8138 0.12756 152.72)` |
| Warn | `#e8b849` | `oklch(0.8060 0.13714 85.03)` |
| Danger | `#ff8a80` | `oklch(0.7594 0.14351 26.08)` |

### Contraste

**Claro:** texto sobre fondo WCAG 16.73:1, APCA Lc 97.1 (oscuro-sobre-claro); texto sobre superficie WCAG 15.13:1, APCA Lc 90.6 (oscuro-sobre-claro); accent-foreground sobre acento WCAG 5.92:1, APCA Lc -79.5 (claro-sobre-oscuro). Muted sobre fondo WCAG 6.29:1, APCA Lc 76.4 (oscuro-sobre-claro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 5.53:1, APCA Lc 70.1 (oscuro-sobre-claro)). `accent-text` está igualado o derivado para ese rol.

**Oscuro:** texto sobre fondo WCAG 16.31:1, APCA Lc -96.9 (claro-sobre-oscuro); texto sobre superficie WCAG 14.85:1, APCA Lc -95.9 (claro-sobre-oscuro); accent-foreground sobre acento WCAG 4.85:1, APCA Lc -77.5 (claro-sobre-oscuro). Muted sobre fondo WCAG 7.62:1, APCA Lc -53.0 (claro-sobre-oscuro): sirve para cuerpo secundario. El acento sólido no llega a 4.5:1 como texto sobre el fondo (3.86:1). Para botones usá `accent` + `accent-foreground`. Para links usá `accent-text` (9.39:1, Lc -63.4).

### Tokens CSS

```css
:root {
  /* Diario y rojo — claro */
  --bg: oklch(0.9583 0.00699 88.64); /* #f3f1ec */
  --surface: oklch(0.9248 0.00833 91.49); /* #e8e6e0 */
  --border: oklch(0.8431 0.01183 84.58); /* #cfcbc3 */
  --text: oklch(0.1776 0.00000 0.00); /* #111111 */
  --muted: oklch(0.4609 0.00688 84.58); /* #5a5854 */
  --accent: oklch(0.5166 0.20769 20.73); /* #c3002f */
  --accent-foreground: oklch(0.9823 0.00858 17.30); /* #fff7f7 */
  --accent-text: oklch(0.5166 0.20769 20.73); /* #c3002f */
  --success: oklch(0.4689 0.10756 151.36); /* #1f6b3a */
  --warn: oklch(0.5078 0.10800 73.30); /* #8a5a00 */
  --danger: oklch(0.4158 0.15719 22.42); /* #8e1020 */
}

.dark {
  /* Diario y rojo — oscuro */
  --bg: oklch(0.1818 0.00201 106.60); /* #121211 */
  --surface: oklch(0.2257 0.00379 106.70); /* #1c1c1a */
  --border: oklch(0.3167 0.00711 95.29); /* #33322e */
  --text: oklch(0.9523 0.00700 88.64); /* #f1efea */
  --muted: oklch(0.7224 0.01055 87.49); /* #a8a59e */
  --accent: oklch(0.5753 0.20089 16.65); /* #d52e4d */
  --accent-foreground: oklch(1.0000 0.00000 0.00); /* #ffffff */
  --accent-text: oklch(0.7952 0.11848 16.83); /* #ff9ca1 */
  --success: oklch(0.8138 0.12756 152.72); /* #7dda9a */
  --warn: oklch(0.8060 0.13714 85.03); /* #e8b849 */
  --danger: oklch(0.7594 0.14351 26.08); /* #ff8a80 */
}
```


---

## Riso fucsia y menta

`riso-fucsia-menta` — Tinta limitada de risografía, dos tintas, granulado

**Mejor para:** zines, cultura, café, estudios independientes.  
**Evitá en:** SaaS B2B serio, banca, sistemas densos.  
**Estilos:** [`risografia-impreso`](../estilos/risografia-impreso.md), [`ilustrado-humano`](../estilos/ilustrado-humano.md), [`anti-diseno`](../estilos/anti-diseno.md), [`grano-ruido`](../estilos/grano-ruido.md).

Dos tintas, no un arcoíris. El fucsia y el menta no se mezclan en un degradé digital: se superponen como capas de tinta. Sumá grano.

### Claro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#f6f3ec` | `oklch(0.9645 0.00983 87.47)` |
| Superficie | `#efeae0` | `oklch(0.9382 0.01439 84.58)` |
| Borde | `#d8d0c2` | `oklch(0.8602 0.02098 81.78)` |
| Texto | `#1a1512` | `oklch(0.2007 0.01005 52.89)` |
| Muted | `#61584e` | `oklch(0.4659 0.01965 70.25)` |
| Acento (sólido) | `#c0176a` | `oklch(0.5318 0.20486 358.82)` |
| Acento foreground | `#fff0f6` | `oklch(0.9686 0.01792 351.14)` |
| Acento texto/link | `#c0176a` | `oklch(0.5318 0.20486 358.82)` |
| Success | `#0e6b4a` | `oklch(0.4688 0.09730 162.62)` |
| Warn | `#8a5a00` | `oklch(0.5078 0.10800 73.30)` |
| Danger | `#b42318` | `oklch(0.5003 0.18205 29.51)` |

### Oscuro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#161310` | `oklch(0.1892 0.00770 67.33)` |
| Superficie | `#221c18` | `oklch(0.2320 0.01207 55.72)` |
| Borde | `#3c322c` | `oklch(0.3260 0.01782 52.83)` |
| Texto | `#f3ebdf` | `oklch(0.9431 0.01818 78.24)` |
| Muted | `#b3a496` | `oklch(0.7276 0.02646 65.44)` |
| Acento (sólido) | `#cb3276` | `oklch(0.5718 0.19573 358.66)` |
| Acento foreground | `#ffffff` | `oklch(1.0000 0.00000 0.00)` |
| Acento texto/link | `#ff96ba` | `oklch(0.7924 0.13178 358.56)` |
| Success | `#6ee0b0` | `oklch(0.8268 0.12597 163.81)` |
| Warn | `#e8b849` | `oklch(0.8060 0.13714 85.03)` |
| Danger | `#ff8a80` | `oklch(0.7594 0.14351 26.08)` |

### Contraste

**Claro:** texto sobre fondo WCAG 16.34:1, APCA Lc 97.8 (oscuro-sobre-claro); texto sobre superficie WCAG 15.1:1, APCA Lc 92.6 (oscuro-sobre-claro); accent-foreground sobre acento WCAG 5.33:1, APCA Lc -75.4 (claro-sobre-oscuro). Muted sobre fondo WCAG 6.29:1, APCA Lc 77.1 (oscuro-sobre-claro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 5.3:1, APCA Lc 70.4 (oscuro-sobre-claro)). `accent-text` está igualado o derivado para ese rol.

**Oscuro:** texto sobre fondo WCAG 15.65:1, APCA Lc -94.7 (claro-sobre-oscuro); texto sobre superficie WCAG 14.24:1, APCA Lc -93.7 (claro-sobre-oscuro); accent-foreground sobre acento WCAG 4.93:1, APCA Lc -78.3 (claro-sobre-oscuro). Muted sobre fondo WCAG 7.64:1, APCA Lc -53.6 (claro-sobre-oscuro): sirve para cuerpo secundario. El acento sólido no llega a 4.5:1 como texto sobre el fondo (3.75:1). Para botones usá `accent` + `accent-foreground`. Para links usá `accent-text` (9.1:1, Lc -62.4).

### Tokens CSS

```css
:root {
  /* Riso fucsia y menta — claro */
  --bg: oklch(0.9645 0.00983 87.47); /* #f6f3ec */
  --surface: oklch(0.9382 0.01439 84.58); /* #efeae0 */
  --border: oklch(0.8602 0.02098 81.78); /* #d8d0c2 */
  --text: oklch(0.2007 0.01005 52.89); /* #1a1512 */
  --muted: oklch(0.4659 0.01965 70.25); /* #61584e */
  --accent: oklch(0.5318 0.20486 358.82); /* #c0176a */
  --accent-foreground: oklch(0.9686 0.01792 351.14); /* #fff0f6 */
  --accent-text: oklch(0.5318 0.20486 358.82); /* #c0176a */
  --success: oklch(0.4688 0.09730 162.62); /* #0e6b4a */
  --warn: oklch(0.5078 0.10800 73.30); /* #8a5a00 */
  --danger: oklch(0.5003 0.18205 29.51); /* #b42318 */
}

.dark {
  /* Riso fucsia y menta — oscuro */
  --bg: oklch(0.1892 0.00770 67.33); /* #161310 */
  --surface: oklch(0.2320 0.01207 55.72); /* #221c18 */
  --border: oklch(0.3260 0.01782 52.83); /* #3c322c */
  --text: oklch(0.9431 0.01818 78.24); /* #f3ebdf */
  --muted: oklch(0.7276 0.02646 65.44); /* #b3a496 */
  --accent: oklch(0.5718 0.19573 358.66); /* #cb3276 */
  --accent-foreground: oklch(1.0000 0.00000 0.00); /* #ffffff */
  --accent-text: oklch(0.7924 0.13178 358.56); /* #ff96ba */
  --success: oklch(0.8268 0.12597 163.81); /* #6ee0b0 */
  --warn: oklch(0.8060 0.13714 85.03); /* #e8b849 */
  --danger: oklch(0.7594 0.14351 26.08); /* #ff8a80 */
}
```


---

## Pergamino y sepia

`pergamino-sepia` — Papel envejecido, tinta sepia, un solo sello

**Mejor para:** literatura, museos, craft, marcas de historia.  
**Evitá en:** tech startups, dashboards, e-commerce de electrónica.  
**Estilos:** [`editorial-revista`](../estilos/editorial-revista.md), [`realismo-tactil`](../estilos/realismo-tactil.md), [`organico-terroso`](../estilos/organico-terroso.md), [`grano-ruido`](../estilos/grano-ruido.md).

Cuidado con el contraste del sepia claro: el texto tiene que ser casi negro, no marrón medio.

### Claro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#f3e6d0` | `oklch(0.9295 0.03242 80.99)` |
| Superficie | `#e9d8b8` | `oklch(0.8878 0.04639 83.27)` |
| Borde | `#d2ba93` | `oklch(0.7996 0.05901 79.74)` |
| Texto | `#2a2014` | `oklch(0.2517 0.02605 71.29)` |
| Muted | `#6a5840` | `oklch(0.4718 0.04324 74.42)` |
| Acento (sólido) | `#7a3e12` | `oklch(0.4326 0.09957 52.02)` |
| Acento foreground | `#fff3e0` | `oklch(0.9685 0.02816 79.48)` |
| Acento texto/link | `#7a3e12` | `oklch(0.4326 0.09957 52.02)` |
| Success | `#1f6b3a` | `oklch(0.4689 0.10756 151.36)` |
| Warn | `#8a5a00` | `oklch(0.5078 0.10800 73.30)` |
| Danger | `#9b1c1c` | `oklch(0.4484 0.16246 26.84)` |

### Oscuro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#1a140e` | `oklch(0.1966 0.01512 66.76)` |
| Superficie | `#251c14` | `oklch(0.2347 0.02036 63.21)` |
| Borde | `#3e3224` | `oklch(0.3261 0.02903 70.84)` |
| Texto | `#f3e4cc` | `oklch(0.9246 0.03577 79.68)` |
| Muted | `#b59a78` | `oklch(0.7018 0.05686 73.09)` |
| Acento (sólido) | `#a35f17` | `oklch(0.5516 0.11908 60.84)` |
| Acento foreground | `#ffffff` | `oklch(1.0000 0.00000 0.00)` |
| Acento texto/link | `#eca262` | `oklch(0.7716 0.11924 60.48)` |
| Success | `#7dda9a` | `oklch(0.8138 0.12756 152.72)` |
| Warn | `#e8b849` | `oklch(0.8060 0.13714 85.03)` |
| Danger | `#ff8a80` | `oklch(0.7594 0.14351 26.08)` |

### Contraste

**Claro:** texto sobre fondo WCAG 12.96:1, APCA Lc 88.9 (oscuro-sobre-claro); texto sobre superficie WCAG 11.39:1, APCA Lc 81.1 (oscuro-sobre-claro); accent-foreground sobre acento WCAG 7.58:1, APCA Lc -85.9 (claro-sobre-oscuro). Muted sobre fondo WCAG 5.53:1, APCA Lc 69.5 (oscuro-sobre-claro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 6.75:1, APCA Lc 74.3 (oscuro-sobre-claro)). `accent-text` está igualado o derivado para ese rol.

**Oscuro:** texto sobre fondo WCAG 14.59:1, APCA Lc -90.6 (claro-sobre-oscuro); texto sobre superficie WCAG 13.37:1, APCA Lc -89.7 (claro-sobre-oscuro); accent-foreground sobre acento WCAG 4.99:1, APCA Lc -79.6 (claro-sobre-oscuro). Muted sobre fondo WCAG 6.83:1, APCA Lc -49.1 (claro-sobre-oscuro): sirve para cuerpo secundario. El acento sólido no llega a 4.5:1 como texto sobre el fondo (3.66:1). Para botones usá `accent` + `accent-foreground`. Para links usá `accent-text` (8.62:1, Lc -60.1).

### Tokens CSS

```css
:root {
  /* Pergamino y sepia — claro */
  --bg: oklch(0.9295 0.03242 80.99); /* #f3e6d0 */
  --surface: oklch(0.8878 0.04639 83.27); /* #e9d8b8 */
  --border: oklch(0.7996 0.05901 79.74); /* #d2ba93 */
  --text: oklch(0.2517 0.02605 71.29); /* #2a2014 */
  --muted: oklch(0.4718 0.04324 74.42); /* #6a5840 */
  --accent: oklch(0.4326 0.09957 52.02); /* #7a3e12 */
  --accent-foreground: oklch(0.9685 0.02816 79.48); /* #fff3e0 */
  --accent-text: oklch(0.4326 0.09957 52.02); /* #7a3e12 */
  --success: oklch(0.4689 0.10756 151.36); /* #1f6b3a */
  --warn: oklch(0.5078 0.10800 73.30); /* #8a5a00 */
  --danger: oklch(0.4484 0.16246 26.84); /* #9b1c1c */
}

.dark {
  /* Pergamino y sepia — oscuro */
  --bg: oklch(0.1966 0.01512 66.76); /* #1a140e */
  --surface: oklch(0.2347 0.02036 63.21); /* #251c14 */
  --border: oklch(0.3261 0.02903 70.84); /* #3e3224 */
  --text: oklch(0.9246 0.03577 79.68); /* #f3e4cc */
  --muted: oklch(0.7018 0.05686 73.09); /* #b59a78 */
  --accent: oklch(0.5516 0.11908 60.84); /* #a35f17 */
  --accent-foreground: oklch(1.0000 0.00000 0.00); /* #ffffff */
  --accent-text: oklch(0.7716 0.11924 60.48); /* #eca262 */
  --success: oklch(0.8138 0.12756 152.72); /* #7dda9a */
  --warn: oklch(0.8060 0.13714 85.03); /* #e8b849 */
  --danger: oklch(0.7594 0.14351 26.08); /* #ff8a80 */
}
```

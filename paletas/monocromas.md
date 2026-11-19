# Paletas monocromas, suizas y de mínimo expresivo

Casi sin croma. La tipografía, la grilla y el aire hacen el trabajo. Sirven para [`suizo-internacional`](../estilos/suizo-internacional.md), [`minimalismo-monocromo`](../estilos/minimalismo-monocromo.md), [`ui-casi-invisible`](../estilos/ui-casi-invisible.md) y, cuando el ocre es la única rareza, [`expresivo-minimo`](../estilos/expresivo-minimo.md).

Ojo con el combo cream + terracota pastel: algunos detectores de “anti-slop” ya lo marcan como el nuevo default. Si lo usás, subí el contraste de la tinta y que el acento no sea un blush genérico.


Hay **4 paletas** en este grupo. Los valores salen de [`paletas.json`](./paletas.json). Los links de estilo apuntan a las fichas de [`../estilos/`](../estilos/README.md).


---

## Suizo neutro

`suizo-neutro` — Casi sin croma, la tipografía y la grilla mandan

**Mejor para:** estudios, arquitectura, institucional, sistemas de diseño.  
**Evitá en:** marcas que necesitan calor o juventud ruidosa.  
**Estilos:** [`suizo-internacional`](../estilos/suizo-internacional.md), [`minimalismo-monocromo`](../estilos/minimalismo-monocromo.md), [`ui-casi-invisible`](../estilos/ui-casi-invisible.md), [`catalogo-tecnico`](../estilos/catalogo-tecnico.md).

Sin acento de moda. El ‘acento’ es el negro mismo o un rojo muy puntual de señal (acá, un rojo de corrección, usado con extrema tacañería).

### Claro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#f2f2f0` | `oklch(0.9606 0.00265 106.45)` |
| Superficie | `#e8e8e6` | `oklch(0.9304 0.00267 106.45)` |
| Borde | `#ccccca` | `oklch(0.8446 0.00274 106.46)` |
| Texto | `#111111` | `oklch(0.1776 0.00000 0.00)` |
| Muted | `#585858` | `oklch(0.4604 0.00000 0.00)` |
| Acento (sólido) | `#111111` | `oklch(0.1776 0.00000 0.00)` |
| Acento foreground | `#f5f5f3` | `oklch(0.9696 0.00265 106.45)` |
| Acento texto/link | `#111111` | `oklch(0.1776 0.00000 0.00)` |
| Success | `#1f6b3a` | `oklch(0.4689 0.10756 151.36)` |
| Warn | `#8a5a00` | `oklch(0.5078 0.10800 73.30)` |
| Danger | `#b42318` | `oklch(0.5003 0.18205 29.51)` |

### Oscuro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#111111` | `oklch(0.1776 0.00000 0.00)` |
| Superficie | `#1a1a1a` | `oklch(0.2178 0.00000 0.00)` |
| Borde | `#333333` | `oklch(0.3211 0.00000 0.00)` |
| Texto | `#f3f3f1` | `oklch(0.9636 0.00265 106.45)` |
| Muted | `#a3a3a3` | `oklch(0.7155 0.00000 0.00)` |
| Acento (sólido) | `#f3f3f1` | `oklch(0.9636 0.00265 106.45)` |
| Acento foreground | `#111111` | `oklch(0.1776 0.00000 0.00)` |
| Acento texto/link | `#f3f3f1` | `oklch(0.9636 0.00265 106.45)` |
| Success | `#7dda9a` | `oklch(0.8138 0.12756 152.72)` |
| Warn | `#e8b849` | `oklch(0.8060 0.13714 85.03)` |
| Danger | `#ff8a80` | `oklch(0.7594 0.14351 26.08)` |

### Contraste

**Claro:** texto sobre fondo WCAG 16.85:1, APCA Lc 97.5 (oscuro-sobre-claro); texto sobre superficie WCAG 15.39:1, APCA Lc 91.7 (oscuro-sobre-claro); accent-foreground sobre acento WCAG 17.3:1, APCA Lc -100.7 (claro-sobre-oscuro). Muted sobre fondo WCAG 6.35:1, APCA Lc 76.9 (oscuro-sobre-claro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 16.85:1, APCA Lc 97.5 (oscuro-sobre-claro)). `accent-text` está igualado o derivado para ese rol.

**Oscuro:** texto sobre fondo WCAG 17.0:1, APCA Lc -99.4 (claro-sobre-oscuro); texto sobre superficie WCAG 15.67:1, APCA Lc -98.6 (claro-sobre-oscuro); accent-foreground sobre acento WCAG 17.0:1, APCA Lc 98.1 (oscuro-sobre-claro). Muted sobre fondo WCAG 7.49:1, APCA Lc -52.0 (claro-sobre-oscuro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 17.0:1, APCA Lc -99.4 (claro-sobre-oscuro)). `accent-text` está igualado o derivado para ese rol.

### Tokens CSS

```css
:root {
  /* Suizo neutro — claro */
  --bg: oklch(0.9606 0.00265 106.45); /* #f2f2f0 */
  --surface: oklch(0.9304 0.00267 106.45); /* #e8e8e6 */
  --border: oklch(0.8446 0.00274 106.46); /* #ccccca */
  --text: oklch(0.1776 0.00000 0.00); /* #111111 */
  --muted: oklch(0.4604 0.00000 0.00); /* #585858 */
  --accent: oklch(0.1776 0.00000 0.00); /* #111111 */
  --accent-foreground: oklch(0.9696 0.00265 106.45); /* #f5f5f3 */
  --accent-text: oklch(0.1776 0.00000 0.00); /* #111111 */
  --success: oklch(0.4689 0.10756 151.36); /* #1f6b3a */
  --warn: oklch(0.5078 0.10800 73.30); /* #8a5a00 */
  --danger: oklch(0.5003 0.18205 29.51); /* #b42318 */
}

.dark {
  /* Suizo neutro — oscuro */
  --bg: oklch(0.1776 0.00000 0.00); /* #111111 */
  --surface: oklch(0.2178 0.00000 0.00); /* #1a1a1a */
  --border: oklch(0.3211 0.00000 0.00); /* #333333 */
  --text: oklch(0.9636 0.00265 106.45); /* #f3f3f1 */
  --muted: oklch(0.7155 0.00000 0.00); /* #a3a3a3 */
  --accent: oklch(0.9636 0.00265 106.45); /* #f3f3f1 */
  --accent-foreground: oklch(0.1776 0.00000 0.00); /* #111111 */
  --accent-text: oklch(0.9636 0.00265 106.45); /* #f3f3f1 */
  --success: oklch(0.8138 0.12756 152.72); /* #7dda9a */
  --warn: oklch(0.8060 0.13714 85.03); /* #e8b849 */
  --danger: oklch(0.7594 0.14351 26.08); /* #ff8a80 */
}
```


---

## Monocromo cálido

`monocromo-calido` — Gris cálido, casi piel, un acento óxido mínimo

**Mejor para:** PyMEs, estudios, fotografía, productos serenos.  
**Evitá en:** si todo queda beige ‘IA tasteful’: subí el contraste o cambiale el acento.  
**Estilos:** [`minimalismo-monocromo`](../estilos/minimalismo-monocromo.md), [`expresivo-minimo`](../estilos/expresivo-minimo.md), [`editorial-revista`](../estilos/editorial-revista.md), [`realismo-tactil`](../estilos/realismo-tactil.md).

El combo cream+terracotta ya lo marcan algunos detectores como el ‘anti-slop’ que se volvió default. Esta paleta es más tinta y menos terracota pastel.

### Claro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#f3f0eb` | `oklch(0.9561 0.00741 80.72)` |
| Superficie | `#e9e5de` | `oklch(0.9231 0.01035 81.79)` |
| Borde | `#d0cbc3` | `oklch(0.8439 0.01230 79.78)` |
| Texto | `#1a1916` | `oklch(0.2134 0.00596 91.63)` |
| Muted | `#5c5852` | `oklch(0.4622 0.01085 78.22)` |
| Acento (sólido) | `#6e3b18` | `oklch(0.4095 0.08615 52.10)` |
| Acento foreground | `#fff4ea` | `oklch(0.9730 0.01781 64.94)` |
| Acento texto/link | `#6e3b18` | `oklch(0.4095 0.08615 52.10)` |
| Success | `#1f6b3a` | `oklch(0.4689 0.10756 151.36)` |
| Warn | `#8a5a00` | `oklch(0.5078 0.10800 73.30)` |
| Danger | `#b42318` | `oklch(0.5003 0.18205 29.51)` |

### Oscuro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#141311` | `oklch(0.1871 0.00430 84.59)` |
| Superficie | `#1e1c19` | `oklch(0.2276 0.00647 78.19)` |
| Borde | `#35322e` | `oklch(0.3188 0.00818 75.28)` |
| Texto | `#f0ebe4` | `oklch(0.9420 0.01081 76.60)` |
| Muted | `#a8a299` | `oklch(0.7147 0.01461 78.23)` |
| Acento (sólido) | `#e0a070` | `oklch(0.7567 0.09924 57.44)` |
| Acento foreground | `#0a0a0a` | `oklch(0.1448 0.00000 0.00)` |
| Acento texto/link | `#e7a676` | `oklch(0.7764 0.09967 57.09)` |
| Success | `#7dda9a` | `oklch(0.8138 0.12756 152.72)` |
| Warn | `#e8b849` | `oklch(0.8060 0.13714 85.03)` |
| Danger | `#ff8a80` | `oklch(0.7594 0.14351 26.08)` |

### Contraste

**Claro:** texto sobre fondo WCAG 15.47:1, APCA Lc 95.7 (oscuro-sobre-claro); texto sobre superficie WCAG 14.0:1, APCA Lc 89.3 (oscuro-sobre-claro); accent-foreground sobre acento WCAG 8.42:1, APCA Lc -88.9 (claro-sobre-oscuro). Muted sobre fondo WCAG 6.21:1, APCA Lc 75.8 (oscuro-sobre-claro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 8.03:1, APCA Lc 81.9 (oscuro-sobre-claro)). `accent-text` está igualado o derivado para ese rol.

**Oscuro:** texto sobre fondo WCAG 15.66:1, APCA Lc -94.5 (claro-sobre-oscuro); texto sobre superficie WCAG 14.34:1, APCA Lc -93.6 (claro-sobre-oscuro); accent-foreground sobre acento WCAG 8.89:1, APCA Lc 60.0 (oscuro-sobre-claro). Muted sobre fondo WCAG 7.33:1, APCA Lc -51.6 (claro-sobre-oscuro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 8.34:1, APCA Lc -57.8 (claro-sobre-oscuro)). `accent-text` está igualado o derivado para ese rol.

### Tokens CSS

```css
:root {
  /* Monocromo cálido — claro */
  --bg: oklch(0.9561 0.00741 80.72); /* #f3f0eb */
  --surface: oklch(0.9231 0.01035 81.79); /* #e9e5de */
  --border: oklch(0.8439 0.01230 79.78); /* #d0cbc3 */
  --text: oklch(0.2134 0.00596 91.63); /* #1a1916 */
  --muted: oklch(0.4622 0.01085 78.22); /* #5c5852 */
  --accent: oklch(0.4095 0.08615 52.10); /* #6e3b18 */
  --accent-foreground: oklch(0.9730 0.01781 64.94); /* #fff4ea */
  --accent-text: oklch(0.4095 0.08615 52.10); /* #6e3b18 */
  --success: oklch(0.4689 0.10756 151.36); /* #1f6b3a */
  --warn: oklch(0.5078 0.10800 73.30); /* #8a5a00 */
  --danger: oklch(0.5003 0.18205 29.51); /* #b42318 */
}

.dark {
  /* Monocromo cálido — oscuro */
  --bg: oklch(0.1871 0.00430 84.59); /* #141311 */
  --surface: oklch(0.2276 0.00647 78.19); /* #1e1c19 */
  --border: oklch(0.3188 0.00818 75.28); /* #35322e */
  --text: oklch(0.9420 0.01081 76.60); /* #f0ebe4 */
  --muted: oklch(0.7147 0.01461 78.23); /* #a8a299 */
  --accent: oklch(0.7567 0.09924 57.44); /* #e0a070 */
  --accent-foreground: oklch(0.1448 0.00000 0.00); /* #0a0a0a */
  --accent-text: oklch(0.7764 0.09967 57.09); /* #e7a676 */
  --success: oklch(0.8138 0.12756 152.72); /* #7dda9a */
  --warn: oklch(0.8060 0.13714 85.03); /* #e8b849 */
  --danger: oklch(0.7594 0.14351 26.08); /* #ff8a80 */
}
```


---

## Monocromo frío

`monocromo-frio` — Piedra fría, no el zinc-500 genérico de Tailwind

**Mejor para:** arquitectura, museos, docs, producto serio.  
**Evitá en:** hospitality cálida, comida.  
**Estilos:** [`suizo-internacional`](../estilos/suizo-internacional.md), [`catalogo-tecnico`](../estilos/catalogo-tecnico.md), [`ui-casi-invisible`](../estilos/ui-casi-invisible.md), [`minimalismo-monocromo`](../estilos/minimalismo-monocromo.md).

Un azul-gris de piedra, no slate-900 + sky-500. El acento es un azul de ingeniería, bajo en croma.

### Claro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#f2f3f4` | `oklch(0.9637 0.00172 247.84)` |
| Superficie | `#e6e8ea` | `oklch(0.9300 0.00346 247.86)` |
| Borde | `#cdd1d4` | `oklch(0.8585 0.00605 239.83)` |
| Texto | `#141618` | `oklch(0.1989 0.00509 248.08)` |
| Muted | `#555b60` | `oklch(0.4676 0.01110 243.02)` |
| Acento (sólido) | `#1e3a5f` | `oklch(0.3462 0.07355 256.04)` |
| Acento foreground | `#f0f5fa` | `oklch(0.9678 0.00857 247.91)` |
| Acento texto/link | `#1e3a5f` | `oklch(0.3462 0.07355 256.04)` |
| Success | `#1f6b3a` | `oklch(0.4689 0.10756 151.36)` |
| Warn | `#8a5a00` | `oklch(0.5078 0.10800 73.30)` |
| Danger | `#b42318` | `oklch(0.5003 0.18205 29.51)` |

### Oscuro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#101214` | `oklch(0.1809 0.00521 248.12)` |
| Superficie | `#181b1e` | `oklch(0.2202 0.00744 248.17)` |
| Borde | `#2e3338` | `oklch(0.3182 0.01131 248.18)` |
| Texto | `#e8ebee` | `oklch(0.9386 0.00518 247.88)` |
| Muted | `#9aa3aa` | `oklch(0.7105 0.01448 241.04)` |
| Acento (sólido) | `#49749d` | `oklch(0.5452 0.08034 248.38)` |
| Acento foreground | `#ffffff` | `oklch(1.0000 0.00000 0.00)` |
| Acento texto/link | `#8ab8e4` | `oklch(0.7659 0.08022 247.79)` |
| Success | `#7dda9a` | `oklch(0.8138 0.12756 152.72)` |
| Warn | `#e8b849` | `oklch(0.8060 0.13714 85.03)` |
| Danger | `#ff8a80` | `oklch(0.7594 0.14351 26.08)` |

### Contraste

**Claro:** texto sobre fondo WCAG 16.33:1, APCA Lc 97.6 (oscuro-sobre-claro); texto sobre superficie WCAG 14.77:1, APCA Lc 91.1 (oscuro-sobre-claro); accent-foreground sobre acento WCAG 10.49:1, APCA Lc -93.0 (claro-sobre-oscuro). Muted sobre fondo WCAG 6.19:1, APCA Lc 76.6 (oscuro-sobre-claro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 10.35:1, APCA Lc 89.1 (oscuro-sobre-claro)). `accent-text` está igualado o derivado para ese rol.

**Oscuro:** texto sobre fondo WCAG 15.69:1, APCA Lc -94.0 (claro-sobre-oscuro); texto sobre superficie WCAG 14.45:1, APCA Lc -93.2 (claro-sobre-oscuro); accent-foreground sobre acento WCAG 4.92:1, APCA Lc -79.4 (claro-sobre-oscuro). Muted sobre fondo WCAG 7.32:1, APCA Lc -51.2 (claro-sobre-oscuro): sirve para cuerpo secundario. El acento sólido no llega a 4.5:1 como texto sobre el fondo (3.82:1). Para botones usá `accent` + `accent-foreground`. Para links usá `accent-text` (8.99:1, Lc -60.9).

### Tokens CSS

```css
:root {
  /* Monocromo frío — claro */
  --bg: oklch(0.9637 0.00172 247.84); /* #f2f3f4 */
  --surface: oklch(0.9300 0.00346 247.86); /* #e6e8ea */
  --border: oklch(0.8585 0.00605 239.83); /* #cdd1d4 */
  --text: oklch(0.1989 0.00509 248.08); /* #141618 */
  --muted: oklch(0.4676 0.01110 243.02); /* #555b60 */
  --accent: oklch(0.3462 0.07355 256.04); /* #1e3a5f */
  --accent-foreground: oklch(0.9678 0.00857 247.91); /* #f0f5fa */
  --accent-text: oklch(0.3462 0.07355 256.04); /* #1e3a5f */
  --success: oklch(0.4689 0.10756 151.36); /* #1f6b3a */
  --warn: oklch(0.5078 0.10800 73.30); /* #8a5a00 */
  --danger: oklch(0.5003 0.18205 29.51); /* #b42318 */
}

.dark {
  /* Monocromo frío — oscuro */
  --bg: oklch(0.1809 0.00521 248.12); /* #101214 */
  --surface: oklch(0.2202 0.00744 248.17); /* #181b1e */
  --border: oklch(0.3182 0.01131 248.18); /* #2e3338 */
  --text: oklch(0.9386 0.00518 247.88); /* #e8ebee */
  --muted: oklch(0.7105 0.01448 241.04); /* #9aa3aa */
  --accent: oklch(0.5452 0.08034 248.38); /* #49749d */
  --accent-foreground: oklch(1.0000 0.00000 0.00); /* #ffffff */
  --accent-text: oklch(0.7659 0.08022 247.79); /* #8ab8e4 */
  --success: oklch(0.8138 0.12756 152.72); /* #7dda9a */
  --warn: oklch(0.8060 0.13714 85.03); /* #e8b849 */
  --danger: oklch(0.7594 0.14351 26.08); /* #ff8a80 */
}
```


---

## Hueso y ocre

`hueso-ocre` — Mínimo expresivo: fondo quieto, una rareza ocre

**Mejor para:** PyMEs, SaaS que no quieren parecer Linear, estudios, landings de oficio.  
**Evitá en:** si el ocre se usa en todos los botones y titulos, deja de ser rareza.  
**Estilos:** [`expresivo-minimo`](../estilos/expresivo-minimo.md), [`editorial-revista`](../estilos/editorial-revista.md), [`organico-terroso`](../estilos/organico-terroso.md), [`minimalismo-monocromo`](../estilos/minimalismo-monocromo.md).

La ficha de minimalismo expresivo: un diseño limpio con una sola rareza bien elegida. El ocre es esa rareza.

### Claro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#f5f2ea` | `oklch(0.9613 0.01109 89.72)` |
| Superficie | `#ebe6da` | `oklch(0.9256 0.01692 88.00)` |
| Borde | `#d5cebe` | `oklch(0.8527 0.02307 87.16)` |
| Texto | `#1a1812` | `oklch(0.2092 0.01180 91.78)` |
| Muted | `#5e594c` | `oklch(0.4647 0.02132 89.47)` |
| Acento (sólido) | `#9a6200` | `oklch(0.5444 0.11733 70.85)` |
| Acento foreground | `#fff8e8` | `oklch(0.9803 0.02232 87.15)` |
| Acento texto/link | `#9a6200` | `oklch(0.5444 0.11733 70.85)` |
| Success | `#1f6b3a` | `oklch(0.4689 0.10756 151.36)` |
| Warn | `#8a5a00` | `oklch(0.5078 0.10800 73.30)` |
| Danger | `#b42318` | `oklch(0.5003 0.18205 29.51)` |

### Oscuro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#13120e` | `oklch(0.1818 0.00808 95.49)` |
| Superficie | `#1d1b16` | `oklch(0.2226 0.00990 88.80)` |
| Borde | `#353126` | `oklch(0.3138 0.01961 90.43)` |
| Texto | `#f1ebdc` | `oklch(0.9407 0.02094 88.72)` |
| Muted | `#a8a090` | `oklch(0.7080 0.02452 84.59)` |
| Acento (sólido) | `#e0b15a` | `oklch(0.7859 0.11830 80.98)` |
| Acento foreground | `#1a1408` | `oklch(0.1950 0.02393 83.97)` |
| Acento texto/link | `#e0b15a` | `oklch(0.7859 0.11830 80.98)` |
| Success | `#7dda9a` | `oklch(0.8138 0.12756 152.72)` |
| Warn | `#e8b849` | `oklch(0.8060 0.13714 85.03)` |
| Danger | `#ff8a80` | `oklch(0.7594 0.14351 26.08)` |

### Contraste

**Claro:** texto sobre fondo WCAG 15.86:1, APCA Lc 96.9 (oscuro-sobre-claro); texto sobre superficie WCAG 14.25:1, APCA Lc 89.9 (oscuro-sobre-claro); accent-foreground sobre acento WCAG 4.82:1, APCA Lc -75.9 (claro-sobre-oscuro). Muted sobre fondo WCAG 6.24:1, APCA Lc 76.5 (oscuro-sobre-claro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 4.55:1, APCA Lc 67.1 (oscuro-sobre-claro)). `accent-text` está igualado o derivado para ese rol.

**Oscuro:** texto sobre fondo WCAG 15.76:1, APCA Lc -94.4 (claro-sobre-oscuro); texto sobre superficie WCAG 14.47:1, APCA Lc -93.5 (claro-sobre-oscuro); accent-foreground sobre acento WCAG 9.24:1, APCA Lc 64.7 (oscuro-sobre-claro). Muted sobre fondo WCAG 7.23:1, APCA Lc -50.6 (claro-sobre-oscuro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 9.47:1, APCA Lc -63.7 (claro-sobre-oscuro)). `accent-text` está igualado o derivado para ese rol.

### Tokens CSS

```css
:root {
  /* Hueso y ocre — claro */
  --bg: oklch(0.9613 0.01109 89.72); /* #f5f2ea */
  --surface: oklch(0.9256 0.01692 88.00); /* #ebe6da */
  --border: oklch(0.8527 0.02307 87.16); /* #d5cebe */
  --text: oklch(0.2092 0.01180 91.78); /* #1a1812 */
  --muted: oklch(0.4647 0.02132 89.47); /* #5e594c */
  --accent: oklch(0.5444 0.11733 70.85); /* #9a6200 */
  --accent-foreground: oklch(0.9803 0.02232 87.15); /* #fff8e8 */
  --accent-text: oklch(0.5444 0.11733 70.85); /* #9a6200 */
  --success: oklch(0.4689 0.10756 151.36); /* #1f6b3a */
  --warn: oklch(0.5078 0.10800 73.30); /* #8a5a00 */
  --danger: oklch(0.5003 0.18205 29.51); /* #b42318 */
}

.dark {
  /* Hueso y ocre — oscuro */
  --bg: oklch(0.1818 0.00808 95.49); /* #13120e */
  --surface: oklch(0.2226 0.00990 88.80); /* #1d1b16 */
  --border: oklch(0.3138 0.01961 90.43); /* #353126 */
  --text: oklch(0.9407 0.02094 88.72); /* #f1ebdc */
  --muted: oklch(0.7080 0.02452 84.59); /* #a8a090 */
  --accent: oklch(0.7859 0.11830 80.98); /* #e0b15a */
  --accent-foreground: oklch(0.1950 0.02393 83.97); /* #1a1408 */
  --accent-text: oklch(0.7859 0.11830 80.98); /* #e0b15a */
  --success: oklch(0.8138 0.12756 152.72); /* #7dda9a */
  --warn: oklch(0.8060 0.13714 85.03); /* #e8b849 */
  --danger: oklch(0.7594 0.14351 26.08); /* #ff8a80 */
}
```

# Paletas orgánicas y táctiles

Colores que parecen sacados de un material: barro, aceituna, café, cobre, matcha. Van con [`organico-terroso`](../estilos/organico-terroso.md), [`realismo-tactil`](../estilos/realismo-tactil.md), [`japones-inspirado`](../estilos/japones-inspirado.md) y marcas locales (comida, belleza, craft, hospitality). El truco es **no** tomar una rampa `orange-*` o `emerald-*` de Tailwind: tomá el color de una foto de la materia y construí los roles alrededor.


Hay **5 paletas** en este grupo. Los valores salen de [`paletas.json`](./paletas.json). Los links de estilo apuntan a las fichas de [`../estilos/`](../estilos/README.md).


---

## Terracota y arena

`terracota-arena` — Tierra, cerámica, calor de materia

**Mejor para:** comida, belleza, craft, PyMEs locales, arquitectura.  
**Evitá en:** devtools, crypto, look ‘Linear’.  
**Estilos:** [`organico-terroso`](../estilos/organico-terroso.md), [`realismo-tactil`](../estilos/realismo-tactil.md), [`expresivo-minimo`](../estilos/expresivo-minimo.md), [`ilustrado-humano`](../estilos/ilustrado-humano.md).

Sacá el color de un material real (barro, ladrillo, pan), no de una rampa de Tailwind orange. Un acento, el resto es arena.

### Claro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#f6efe6` | `oklch(0.9551 0.01417 74.42)` |
| Superficie | `#ede3d4` | `oklch(0.9197 0.02283 78.21)` |
| Borde | `#d7c7b0` | `oklch(0.8368 0.03599 77.04)` |
| Texto | `#1e1710` | `oklch(0.2108 0.01731 66.66)` |
| Muted | `#655849` | `oklch(0.4687 0.02886 71.02)` |
| Acento (sólido) | `#a33b16` | `oklch(0.4944 0.14562 38.26)` |
| Acento foreground | `#fff4ec` | `oklch(0.9736 0.01595 58.64)` |
| Acento texto/link | `#a33b16` | `oklch(0.4944 0.14562 38.26)` |
| Success | `#1f6b3a` | `oklch(0.4689 0.10756 151.36)` |
| Warn | `#8a5a00` | `oklch(0.5078 0.10800 73.30)` |
| Danger | `#b42318` | `oklch(0.5003 0.18205 29.51)` |

### Oscuro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#16110c` | `oklch(0.1821 0.01287 66.87)` |
| Superficie | `#221a13` | `oklch(0.2251 0.01817 62.88)` |
| Borde | `#3c2f22` | `oklch(0.3158 0.02896 66.46)` |
| Texto | `#f3e8d8` | `oklch(0.9354 0.02442 77.46)` |
| Muted | `#b3a08a` | `oklch(0.7164 0.03812 71.24)` |
| Acento (sólido) | `#b65326` | `oklch(0.5600 0.14091 42.83)` |
| Acento foreground | `#ffffff` | `oklch(1.0000 0.00000 0.00)` |
| Acento texto/link | `#ff996f` | `oklch(0.7802 0.13506 42.83)` |
| Success | `#7dda9a` | `oklch(0.8138 0.12756 152.72)` |
| Warn | `#e8b849` | `oklch(0.8060 0.13714 85.03)` |
| Danger | `#ff8a80` | `oklch(0.7594 0.14351 26.08)` |

### Contraste

**Claro:** texto sobre fondo WCAG 15.53:1, APCA Lc 95.5 (oscuro-sobre-claro); texto sobre superficie WCAG 13.95:1, APCA Lc 88.7 (oscuro-sobre-claro); accent-foreground sobre acento WCAG 6.07:1, APCA Lc -80.7 (claro-sobre-oscuro). Muted sobre fondo WCAG 6.04:1, APCA Lc 74.9 (oscuro-sobre-claro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 5.76:1, APCA Lc 72.7 (oscuro-sobre-claro)). `accent-text` está igualado o derivado para ese rol.

**Oscuro:** texto sobre fondo WCAG 15.49:1, APCA Lc -93.2 (claro-sobre-oscuro); texto sobre superficie WCAG 14.16:1, APCA Lc -92.2 (claro-sobre-oscuro); accent-foreground sobre acento WCAG 4.94:1, APCA Lc -79.0 (claro-sobre-oscuro). Muted sobre fondo WCAG 7.42:1, APCA Lc -51.8 (claro-sobre-oscuro): sirve para cuerpo secundario. El acento sólido no llega a 4.5:1 como texto sobre el fondo (3.8:1). Para botones usá `accent` + `accent-foreground`. Para links usá `accent-text` (8.97:1, Lc -61.1).

### Tokens CSS

```css
:root {
  /* Terracota y arena — claro */
  --bg: oklch(0.9551 0.01417 74.42); /* #f6efe6 */
  --surface: oklch(0.9197 0.02283 78.21); /* #ede3d4 */
  --border: oklch(0.8368 0.03599 77.04); /* #d7c7b0 */
  --text: oklch(0.2108 0.01731 66.66); /* #1e1710 */
  --muted: oklch(0.4687 0.02886 71.02); /* #655849 */
  --accent: oklch(0.4944 0.14562 38.26); /* #a33b16 */
  --accent-foreground: oklch(0.9736 0.01595 58.64); /* #fff4ec */
  --accent-text: oklch(0.4944 0.14562 38.26); /* #a33b16 */
  --success: oklch(0.4689 0.10756 151.36); /* #1f6b3a */
  --warn: oklch(0.5078 0.10800 73.30); /* #8a5a00 */
  --danger: oklch(0.5003 0.18205 29.51); /* #b42318 */
}

.dark {
  /* Terracota y arena — oscuro */
  --bg: oklch(0.1821 0.01287 66.87); /* #16110c */
  --surface: oklch(0.2251 0.01817 62.88); /* #221a13 */
  --border: oklch(0.3158 0.02896 66.46); /* #3c2f22 */
  --text: oklch(0.9354 0.02442 77.46); /* #f3e8d8 */
  --muted: oklch(0.7164 0.03812 71.24); /* #b3a08a */
  --accent: oklch(0.5600 0.14091 42.83); /* #b65326 */
  --accent-foreground: oklch(1.0000 0.00000 0.00); /* #ffffff */
  --accent-text: oklch(0.7802 0.13506 42.83); /* #ff996f */
  --success: oklch(0.8138 0.12756 152.72); /* #7dda9a */
  --warn: oklch(0.8060 0.13714 85.03); /* #e8b849 */
  --danger: oklch(0.7594 0.14351 26.08); /* #ff8a80 */
}
```


---

## Oliva y piedra

`oliva-piedra` — Aceituna, piedra, Mediterráneo contenido

**Mejor para:** comida, hospitality, bienestar, marcas lentas.  
**Evitá en:** neon / Y2K, fintech agresiva.  
**Estilos:** [`organico-terroso`](../estilos/organico-terroso.md), [`japones-inspirado`](../estilos/japones-inspirado.md), [`realismo-tactil`](../estilos/realismo-tactil.md), [`editorial-revista`](../estilos/editorial-revista.md).

El oliva de acento en claro tiene que ser lo bastante oscuro como para texto y botones (no un sage pastel ilegible).

### Claro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#f3f1ea` | `oklch(0.9578 0.00954 93.57)` |
| Superficie | `#e7e4d8` | `oklch(0.9179 0.01637 95.24)` |
| Borde | `#cfc9b6` | `oklch(0.8356 0.02669 92.43)` |
| Texto | `#1a1b14` | `oklch(0.2185 0.01326 114.11)` |
| Muted | `#5b5c4e` | `oklch(0.4696 0.02191 110.55)` |
| Acento (sólido) | `#4a5c1a` | `oklch(0.4452 0.09285 123.33)` |
| Acento foreground | `#f4f8e0` | `oklch(0.9698 0.03175 114.67)` |
| Acento texto/link | `#4a5c1a` | `oklch(0.4452 0.09285 123.33)` |
| Success | `#1f6b3a` | `oklch(0.4689 0.10756 151.36)` |
| Warn | `#8a5a00` | `oklch(0.5078 0.10800 73.30)` |
| Danger | `#b42318` | `oklch(0.5003 0.18205 29.51)` |

### Oscuro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#12130e` | `oklch(0.1837 0.01000 116.58)` |
| Superficie | `#1c1d16` | `oklch(0.2271 0.01315 114.06)` |
| Borde | `#333428` | `oklch(0.3201 0.02051 111.42)` |
| Texto | `#eeebd8` | `oklch(0.9373 0.02537 99.54)` |
| Muted | `#a4a48a` | `oklch(0.7116 0.03649 107.29)` |
| Acento (sólido) | `#c5d86a` | `oklch(0.8451 0.13733 117.55)` |
| Acento foreground | `#1a1c0c` | `oklch(0.2193 0.02875 114.63)` |
| Acento texto/link | `#c5d86a` | `oklch(0.8451 0.13733 117.55)` |
| Success | `#7dda9a` | `oklch(0.8138 0.12756 152.72)` |
| Warn | `#e8b849` | `oklch(0.8060 0.13714 85.03)` |
| Danger | `#ff8a80` | `oklch(0.7594 0.14351 26.08)` |

### Contraste

**Claro:** texto sobre fondo WCAG 15.35:1, APCA Lc 95.8 (oscuro-sobre-claro); texto sobre superficie WCAG 13.62:1, APCA Lc 88.2 (oscuro-sobre-claro); accent-foreground sobre acento WCAG 6.82:1, APCA Lc -84.2 (claro-sobre-oscuro). Muted sobre fondo WCAG 6.02:1, APCA Lc 75.1 (oscuro-sobre-claro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 6.55:1, APCA Lc 77.3 (oscuro-sobre-claro)). `accent-text` está igualado o derivado para ese rol.

**Oscuro:** texto sobre fondo WCAG 15.56:1, APCA Lc -93.8 (claro-sobre-oscuro); texto sobre superficie WCAG 14.16:1, APCA Lc -92.8 (claro-sobre-oscuro); accent-foreground sobre acento WCAG 11.03:1, APCA Lc 76.1 (oscuro-sobre-claro). Muted sobre fondo WCAG 7.34:1, APCA Lc -51.5 (claro-sobre-oscuro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 11.91:1, APCA Lc -76.6 (claro-sobre-oscuro)). `accent-text` está igualado o derivado para ese rol.

### Tokens CSS

```css
:root {
  /* Oliva y piedra — claro */
  --bg: oklch(0.9578 0.00954 93.57); /* #f3f1ea */
  --surface: oklch(0.9179 0.01637 95.24); /* #e7e4d8 */
  --border: oklch(0.8356 0.02669 92.43); /* #cfc9b6 */
  --text: oklch(0.2185 0.01326 114.11); /* #1a1b14 */
  --muted: oklch(0.4696 0.02191 110.55); /* #5b5c4e */
  --accent: oklch(0.4452 0.09285 123.33); /* #4a5c1a */
  --accent-foreground: oklch(0.9698 0.03175 114.67); /* #f4f8e0 */
  --accent-text: oklch(0.4452 0.09285 123.33); /* #4a5c1a */
  --success: oklch(0.4689 0.10756 151.36); /* #1f6b3a */
  --warn: oklch(0.5078 0.10800 73.30); /* #8a5a00 */
  --danger: oklch(0.5003 0.18205 29.51); /* #b42318 */
}

.dark {
  /* Oliva y piedra — oscuro */
  --bg: oklch(0.1837 0.01000 116.58); /* #12130e */
  --surface: oklch(0.2271 0.01315 114.06); /* #1c1d16 */
  --border: oklch(0.3201 0.02051 111.42); /* #333428 */
  --text: oklch(0.9373 0.02537 99.54); /* #eeebd8 */
  --muted: oklch(0.7116 0.03649 107.29); /* #a4a48a */
  --accent: oklch(0.8451 0.13733 117.55); /* #c5d86a */
  --accent-foreground: oklch(0.2193 0.02875 114.63); /* #1a1c0c */
  --accent-text: oklch(0.8451 0.13733 117.55); /* #c5d86a */
  --success: oklch(0.8138 0.12756 152.72); /* #7dda9a */
  --warn: oklch(0.8060 0.13714 85.03); /* #e8b849 */
  --danger: oklch(0.7594 0.14351 26.08); /* #ff8a80 */
}
```


---

## Café con leche

`cafe-leche` — Tostado, lácteo, interior de café

**Mejor para:** cafés, panaderías, hospitality, marcas locales.  
**Evitá en:** tech genérica, look clínico.  
**Estilos:** [`realismo-tactil`](../estilos/realismo-tactil.md), [`organico-terroso`](../estilos/organico-terroso.md), [`editorial-revista`](../estilos/editorial-revista.md), [`ilustrado-humano`](../estilos/ilustrado-humano.md).

Buena pareja para un ejemplo tipo ‘panadería’: acento de café, no un degradé violeta. Precios y horarios sobre esta paleta rinden más que tres cards.

### Claro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#f6f0e8` | `oklch(0.9576 0.01246 75.37)` |
| Superficie | `#ede4d6` | `oklch(0.9222 0.02113 79.09)` |
| Borde | `#d6c8b4` | `oklch(0.8389 0.03139 76.93)` |
| Texto | `#1c140e` | `oklch(0.1993 0.01748 58.41)` |
| Muted | `#645648` | `oklch(0.4628 0.02861 67.02)` |
| Acento (sólido) | `#5c3310` | `oklch(0.3661 0.07565 57.12)` |
| Acento foreground | `#fff4e8` | `oklch(0.9725 0.01983 70.00)` |
| Acento texto/link | `#5c3310` | `oklch(0.3661 0.07565 57.12)` |
| Success | `#1f6b3a` | `oklch(0.4689 0.10756 151.36)` |
| Warn | `#8a5a00` | `oklch(0.5078 0.10800 73.30)` |
| Danger | `#b42318` | `oklch(0.5003 0.18205 29.51)` |

### Oscuro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#14100c` | `oklch(0.1765 0.01041 67.07)` |
| Superficie | `#1f1913` | `oklch(0.2185 0.01477 66.92)` |
| Borde | `#3a2e24` | `oklch(0.3115 0.02457 61.53)` |
| Texto | `#f3e8d8` | `oklch(0.9354 0.02442 77.46)` |
| Muted | `#b3a090` | `oklch(0.7179 0.03186 62.40)` |
| Acento (sólido) | `#d4a574` | `oklch(0.7541 0.08528 67.10)` |
| Acento foreground | `#0a0a0a` | `oklch(0.1448 0.00000 0.00)` |
| Acento texto/link | `#dbab7a` | `oklch(0.7739 0.08566 66.58)` |
| Success | `#7dda9a` | `oklch(0.8138 0.12756 152.72)` |
| Warn | `#e8b849` | `oklch(0.8060 0.13714 85.03)` |
| Danger | `#ff8a80` | `oklch(0.7594 0.14351 26.08)` |

### Contraste

**Claro:** texto sobre fondo WCAG 16.05:1, APCA Lc 96.4 (oscuro-sobre-claro); texto sobre superficie WCAG 14.42:1, APCA Lc 89.5 (oscuro-sobre-claro); accent-foreground sobre acento WCAG 10.0:1, APCA Lc -92.5 (claro-sobre-oscuro). Muted sobre fondo WCAG 6.25:1, APCA Lc 76.1 (oscuro-sobre-claro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 9.58:1, APCA Lc 86.4 (oscuro-sobre-claro)). `accent-text` está igualado o derivado para ese rol.

**Oscuro:** texto sobre fondo WCAG 15.64:1, APCA Lc -93.3 (claro-sobre-oscuro); texto sobre superficie WCAG 14.37:1, APCA Lc -92.4 (claro-sobre-oscuro); accent-foreground sobre acento WCAG 8.89:1, APCA Lc 60.0 (oscuro-sobre-claro). Muted sobre fondo WCAG 7.53:1, APCA Lc -52.1 (claro-sobre-oscuro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 8.51:1, APCA Lc -57.9 (claro-sobre-oscuro)). `accent-text` está igualado o derivado para ese rol.

### Tokens CSS

```css
:root {
  /* Café con leche — claro */
  --bg: oklch(0.9576 0.01246 75.37); /* #f6f0e8 */
  --surface: oklch(0.9222 0.02113 79.09); /* #ede4d6 */
  --border: oklch(0.8389 0.03139 76.93); /* #d6c8b4 */
  --text: oklch(0.1993 0.01748 58.41); /* #1c140e */
  --muted: oklch(0.4628 0.02861 67.02); /* #645648 */
  --accent: oklch(0.3661 0.07565 57.12); /* #5c3310 */
  --accent-foreground: oklch(0.9725 0.01983 70.00); /* #fff4e8 */
  --accent-text: oklch(0.3661 0.07565 57.12); /* #5c3310 */
  --success: oklch(0.4689 0.10756 151.36); /* #1f6b3a */
  --warn: oklch(0.5078 0.10800 73.30); /* #8a5a00 */
  --danger: oklch(0.5003 0.18205 29.51); /* #b42318 */
}

.dark {
  /* Café con leche — oscuro */
  --bg: oklch(0.1765 0.01041 67.07); /* #14100c */
  --surface: oklch(0.2185 0.01477 66.92); /* #1f1913 */
  --border: oklch(0.3115 0.02457 61.53); /* #3a2e24 */
  --text: oklch(0.9354 0.02442 77.46); /* #f3e8d8 */
  --muted: oklch(0.7179 0.03186 62.40); /* #b3a090 */
  --accent: oklch(0.7541 0.08528 67.10); /* #d4a574 */
  --accent-foreground: oklch(0.1448 0.00000 0.00); /* #0a0a0a */
  --accent-text: oklch(0.7739 0.08566 66.58); /* #dbab7a */
  --success: oklch(0.8138 0.12756 152.72); /* #7dda9a */
  --warn: oklch(0.8060 0.13714 85.03); /* #e8b849 */
  --danger: oklch(0.7594 0.14351 26.08); /* #ff8a80 */
}
```


---

## Óxido y cobre

`oxido-cobre` — Metal envejecido, taller, materia

**Mejor para:** craft, hardware con alma, moda, interiorismo.  
**Evitá en:** salud, educación infantil, saas ‘clean’.  
**Estilos:** [`realismo-tactil`](../estilos/realismo-tactil.md), [`catalogo-tecnico`](../estilos/catalogo-tecnico.md), [`organico-terroso`](../estilos/organico-terroso.md), [`grano-ruido`](../estilos/grano-ruido.md).

Cobre no es un degradé naranja-rosa. En oscuro, el cobre ilumina como un metal, no como un neon.

### Claro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#f5f0ea` | `oklch(0.9574 0.00965 72.66)` |
| Superficie | `#ebe3d9` | `oklch(0.9194 0.01602 73.67)` |
| Borde | `#d4c6b8` | `oklch(0.8342 0.02484 67.48)` |
| Texto | `#1c1612` | `oklch(0.2061 0.01244 55.60)` |
| Muted | `#62564c` | `oklch(0.4618 0.02235 62.04)` |
| Acento (sólido) | `#8e3b16` | `oklch(0.4596 0.12271 41.92)` |
| Acento foreground | `#fff0e6` | `oklch(0.9643 0.02105 56.13)` |
| Acento texto/link | `#8e3b16` | `oklch(0.4596 0.12271 41.92)` |
| Success | `#1f6b3a` | `oklch(0.4689 0.10756 151.36)` |
| Warn | `#8a5a00` | `oklch(0.5078 0.10800 73.30)` |
| Danger | `#9b1c1c` | `oklch(0.4484 0.16246 26.84)` |

### Oscuro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#14110f` | `oklch(0.1805 0.00641 55.94)` |
| Superficie | `#1f1a17` | `oklch(0.2225 0.00979 52.96)` |
| Borde | `#3a302a` | `oklch(0.3181 0.01793 52.80)` |
| Texto | `#f0e6dc` | `oklch(0.9301 0.01729 67.61)` |
| Muted | `#b3a398` | `oklch(0.7261 0.02444 56.82)` |
| Acento (sólido) | `#ac5a29` | `oklch(0.5567 0.12368 48.70)` |
| Acento foreground | `#ffffff` | `oklch(1.0000 0.00000 0.00)` |
| Acento texto/link | `#f69d6d` | `oklch(0.7759 0.12397 48.58)` |
| Success | `#7dda9a` | `oklch(0.8138 0.12756 152.72)` |
| Warn | `#e8b849` | `oklch(0.8060 0.13714 85.03)` |
| Danger | `#ff8a80` | `oklch(0.7594 0.14351 26.08)` |

### Contraste

**Claro:** texto sobre fondo WCAG 15.8:1, APCA Lc 96.1 (oscuro-sobre-claro); texto sobre superficie WCAG 14.09:1, APCA Lc 88.8 (oscuro-sobre-claro); accent-foreground sobre acento WCAG 6.77:1, APCA Lc -82.2 (claro-sobre-oscuro). Muted sobre fondo WCAG 6.27:1, APCA Lc 76.1 (oscuro-sobre-claro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 6.65:1, APCA Lc 77.0 (oscuro-sobre-claro)). `accent-text` está igualado o derivado para ese rol.

**Oscuro:** texto sobre fondo WCAG 15.27:1, APCA Lc -92.1 (claro-sobre-oscuro); texto sobre superficie WCAG 14.0:1, APCA Lc -91.1 (claro-sobre-oscuro); accent-foreground sobre acento WCAG 4.94:1, APCA Lc -79.2 (claro-sobre-oscuro). Muted sobre fondo WCAG 7.71:1, APCA Lc -53.4 (claro-sobre-oscuro): sirve para cuerpo secundario. El acento sólido no llega a 4.5:1 como texto sobre el fondo (3.8:1). Para botones usá `accent` + `accent-foreground`. Para links usá `accent-text` (8.92:1, Lc -60.7).

### Tokens CSS

```css
:root {
  /* Óxido y cobre — claro */
  --bg: oklch(0.9574 0.00965 72.66); /* #f5f0ea */
  --surface: oklch(0.9194 0.01602 73.67); /* #ebe3d9 */
  --border: oklch(0.8342 0.02484 67.48); /* #d4c6b8 */
  --text: oklch(0.2061 0.01244 55.60); /* #1c1612 */
  --muted: oklch(0.4618 0.02235 62.04); /* #62564c */
  --accent: oklch(0.4596 0.12271 41.92); /* #8e3b16 */
  --accent-foreground: oklch(0.9643 0.02105 56.13); /* #fff0e6 */
  --accent-text: oklch(0.4596 0.12271 41.92); /* #8e3b16 */
  --success: oklch(0.4689 0.10756 151.36); /* #1f6b3a */
  --warn: oklch(0.5078 0.10800 73.30); /* #8a5a00 */
  --danger: oklch(0.4484 0.16246 26.84); /* #9b1c1c */
}

.dark {
  /* Óxido y cobre — oscuro */
  --bg: oklch(0.1805 0.00641 55.94); /* #14110f */
  --surface: oklch(0.2225 0.00979 52.96); /* #1f1a17 */
  --border: oklch(0.3181 0.01793 52.80); /* #3a302a */
  --text: oklch(0.9301 0.01729 67.61); /* #f0e6dc */
  --muted: oklch(0.7261 0.02444 56.82); /* #b3a398 */
  --accent: oklch(0.5567 0.12368 48.70); /* #ac5a29 */
  --accent-foreground: oklch(1.0000 0.00000 0.00); /* #ffffff */
  --accent-text: oklch(0.7759 0.12397 48.58); /* #f69d6d */
  --success: oklch(0.8138 0.12756 152.72); /* #7dda9a */
  --warn: oklch(0.8060 0.13714 85.03); /* #e8b849 */
  --danger: oklch(0.7594 0.14351 26.08); /* #ff8a80 */
}
```


---

## Matcha y carbón

`matcha-carbon` — Té, carbón, quietud, Japón contemporáneo

**Mejor para:** bienestar, comida, estudios, marcas contenidas.  
**Evitá en:** dopamina, Y2K, landings de crypto.  
**Estilos:** [`japones-inspirado`](../estilos/japones-inspirado.md), [`organico-terroso`](../estilos/organico-terroso.md), [`minimalismo-monocromo`](../estilos/minimalismo-monocromo.md), [`expresivo-minimo`](../estilos/expresivo-minimo.md).

El matcha no es el lime de SaaS: es más apagado, más tierra. Mucho aire (ma).

### Claro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#f3f2ec` | `oklch(0.9603 0.00803 98.88)` |
| Superficie | `#e6e6dc` | `oklch(0.9222 0.01336 106.66)` |
| Borde | `#cdd0c2` | `oklch(0.8514 0.01931 116.64)` |
| Texto | `#1a1b16` | `oklch(0.2192 0.00960 116.38)` |
| Muted | `#585a4e` | `oklch(0.4620 0.01906 114.83)` |
| Acento (sólido) | `#3c5a28` | `oklch(0.4311 0.08396 134.26)` |
| Acento foreground | `#f1f8e8` | `oklch(0.9695 0.02232 126.22)` |
| Acento texto/link | `#3c5a28` | `oklch(0.4311 0.08396 134.26)` |
| Success | `#1f6b3a` | `oklch(0.4689 0.10756 151.36)` |
| Warn | `#8a5a00` | `oklch(0.5078 0.10800 73.30)` |
| Danger | `#b42318` | `oklch(0.5003 0.18205 29.51)` |

### Oscuro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#10110e` | `oklch(0.1753 0.00625 122.07)` |
| Superficie | `#191b16` | `oklch(0.2181 0.00999 125.01)` |
| Borde | `#2f332a` | `oklch(0.3141 0.01659 126.90)` |
| Texto | `#ebecd8` | `oklch(0.9370 0.02650 109.23)` |
| Muted | `#a0a490` | `oklch(0.7098 0.02866 116.32)` |
| Acento (sólido) | `#a8c46a` | `oklch(0.7792 0.12080 123.37)` |
| Acento foreground | `#14180c` | `oklch(0.2007 0.02343 123.48)` |
| Acento texto/link | `#a8c46a` | `oklch(0.7792 0.12080 123.37)` |
| Success | `#7dda9a` | `oklch(0.8138 0.12756 152.72)` |
| Warn | `#e8b849` | `oklch(0.8060 0.13714 85.03)` |
| Danger | `#ff8a80` | `oklch(0.7594 0.14351 26.08)` |

### Contraste

**Claro:** texto sobre fondo WCAG 15.44:1, APCA Lc 96.3 (oscuro-sobre-claro); texto sobre superficie WCAG 13.79:1, APCA Lc 89.0 (oscuro-sobre-claro); accent-foreground sobre acento WCAG 7.2:1, APCA Lc -85.5 (claro-sobre-oscuro). Muted sobre fondo WCAG 6.27:1, APCA Lc 76.5 (oscuro-sobre-claro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 6.97:1, APCA Lc 79.2 (oscuro-sobre-claro)). `accent-text` está igualado o derivado para ese rol.

**Oscuro:** texto sobre fondo WCAG 15.81:1, APCA Lc -94.0 (claro-sobre-oscuro); texto sobre superficie WCAG 14.48:1, APCA Lc -93.1 (claro-sobre-oscuro); accent-foreground sobre acento WCAG 9.24:1, APCA Lc 65.2 (oscuro-sobre-claro). Muted sobre fondo WCAG 7.4:1, APCA Lc -51.4 (claro-sobre-oscuro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 9.71:1, APCA Lc -64.5 (claro-sobre-oscuro)). `accent-text` está igualado o derivado para ese rol.

### Tokens CSS

```css
:root {
  /* Matcha y carbón — claro */
  --bg: oklch(0.9603 0.00803 98.88); /* #f3f2ec */
  --surface: oklch(0.9222 0.01336 106.66); /* #e6e6dc */
  --border: oklch(0.8514 0.01931 116.64); /* #cdd0c2 */
  --text: oklch(0.2192 0.00960 116.38); /* #1a1b16 */
  --muted: oklch(0.4620 0.01906 114.83); /* #585a4e */
  --accent: oklch(0.4311 0.08396 134.26); /* #3c5a28 */
  --accent-foreground: oklch(0.9695 0.02232 126.22); /* #f1f8e8 */
  --accent-text: oklch(0.4311 0.08396 134.26); /* #3c5a28 */
  --success: oklch(0.4689 0.10756 151.36); /* #1f6b3a */
  --warn: oklch(0.5078 0.10800 73.30); /* #8a5a00 */
  --danger: oklch(0.5003 0.18205 29.51); /* #b42318 */
}

.dark {
  /* Matcha y carbón — oscuro */
  --bg: oklch(0.1753 0.00625 122.07); /* #10110e */
  --surface: oklch(0.2181 0.00999 125.01); /* #191b16 */
  --border: oklch(0.3141 0.01659 126.90); /* #2f332a */
  --text: oklch(0.9370 0.02650 109.23); /* #ebecd8 */
  --muted: oklch(0.7098 0.02866 116.32); /* #a0a490 */
  --accent: oklch(0.7792 0.12080 123.37); /* #a8c46a */
  --accent-foreground: oklch(0.2007 0.02343 123.48); /* #14180c */
  --accent-text: oklch(0.7792 0.12080 123.37); /* #a8c46a */
  --success: oklch(0.8138 0.12756 152.72); /* #7dda9a */
  --warn: oklch(0.8060 0.13714 85.03); /* #e8b849 */
  --danger: oklch(0.7594 0.14351 26.08); /* #ff8a80 */
}
```

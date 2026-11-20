# Paletas expresivas: brutal, dopamina, Y2K, póster

Alta saturación, pero **con regla 70-30-10**. Dopamina no es “rainbow vomit”: un coral (o un amarillo de señal, o un magenta Y2K deliberado) y el resto neutro. Van con [`neo-brutalismo`](../estilos/neo-brutalismo.md), [`dopamina-saturado`](../estilos/dopamina-saturado.md), [`retrofuturismo-y2k`](../estilos/retrofuturismo-y2k.md), [`maximalismo`](../estilos/maximalismo.md) y [`anti-diseno`](../estilos/anti-diseno.md).

El magenta de Y2K es una decisión de estilo, no el violeta de plantilla. No lo uses en un hero de “AI platform”.


Hay **6 paletas** (las dos últimas, bauhaus primario y memphis pastel, son propias para los estilos nuevos de noviembre de 2026) en este grupo. Los valores salen de [`paletas.json`](./paletas.json). Los links de estilo apuntan a las fichas de [`../estilos/`](../estilos/README.md).


---

## Brutal amarillo

`brutal-amarillo` — Borde negro, amarillo de señal, sombra dura

**Mejor para:** campañas, portfolios ruidosos, educación joven, anti-plantilla.  
**Evitá en:** banca, salud, lujo silencioso, como tema completo de un SaaS serio.  
**Estilos:** [`neo-brutalismo`](../estilos/neo-brutalismo.md), [`anti-diseno`](../estilos/anti-diseno.md), [`dopamina-saturado`](../estilos/dopamina-saturado.md), [`bauhaus`](../estilos/bauhaus.md), [`memphis`](../estilos/memphis.md).

Amarillo de señal + negro. El acento en claro es casi negro (botón sólido) o el amarillo con texto negro. Nada de sombra suave ni radios altos.

### Claro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#f5f5f0` | `oklch(0.9688 0.00661 106.52)` |
| Superficie | `#ffe94a` | `oklch(0.9253 0.17069 101.21)` |
| Borde | `#111111` | `oklch(0.1776 0.00000 0.00)` |
| Texto | `#111111` | `oklch(0.1776 0.00000 0.00)` |
| Muted | `#4a4a46` | `oklch(0.4078 0.00655 106.69)` |
| Acento (sólido) | `#111111` | `oklch(0.1776 0.00000 0.00)` |
| Acento foreground | `#ffe94a` | `oklch(0.9253 0.17069 101.21)` |
| Acento texto/link | `#111111` | `oklch(0.1776 0.00000 0.00)` |
| Success | `#146b30` | `oklch(0.4644 0.12138 148.98)` |
| Warn | `#8a5a00` | `oklch(0.5078 0.10800 73.30)` |
| Danger | `#d10000` | `oklch(0.5405 0.22179 29.23)` |

### Oscuro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#111111` | `oklch(0.1776 0.00000 0.00)` |
| Superficie | `#1a1a1a` | `oklch(0.2178 0.00000 0.00)` |
| Borde | `#f5e645` | `oklch(0.9102 0.17166 103.90)` |
| Texto | `#f5f5f0` | `oklch(0.9688 0.00661 106.52)` |
| Muted | `#b3b3a8` | `oklch(0.7636 0.01537 106.76)` |
| Acento (sólido) | `#f5e645` | `oklch(0.9102 0.17166 103.90)` |
| Acento foreground | `#111111` | `oklch(0.1776 0.00000 0.00)` |
| Acento texto/link | `#f5e645` | `oklch(0.9102 0.17166 103.90)` |
| Success | `#7dda9a` | `oklch(0.8138 0.12756 152.72)` |
| Warn | `#e8b849` | `oklch(0.8060 0.13714 85.03)` |
| Danger | `#ff6b6b` | `oklch(0.7116 0.18122 22.84)` |

### Contraste

**Claro:** texto sobre fondo WCAG 17.27:1, APCA Lc 99.2 (oscuro-sobre-claro); texto sobre superficie WCAG 15.29:1, APCA Lc 91.4 (oscuro-sobre-claro); accent-foreground sobre acento WCAG 15.29:1, APCA Lc -92.1 (claro-sobre-oscuro). Muted sobre fondo WCAG 8.14:1, APCA Lc 84.2 (oscuro-sobre-claro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 17.27:1, APCA Lc 99.2 (oscuro-sobre-claro)). `accent-text` está igualado o derivado para ese rol.

**Oscuro:** texto sobre fondo WCAG 17.27:1, APCA Lc -100.6 (claro-sobre-oscuro); texto sobre superficie WCAG 15.91:1, APCA Lc -99.7 (claro-sobre-oscuro); accent-foreground sobre acento WCAG 14.65:1, APCA Lc 88.7 (oscuro-sobre-claro). Muted sobre fondo WCAG 8.93:1, APCA Lc -60.3 (claro-sobre-oscuro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 14.65:1, APCA Lc -89.1 (claro-sobre-oscuro)). `accent-text` está igualado o derivado para ese rol.

### Tokens CSS

```css
:root {
  /* Brutal amarillo — claro */
  --bg: oklch(0.9688 0.00661 106.52); /* #f5f5f0 */
  --surface: oklch(0.9253 0.17069 101.21); /* #ffe94a */
  --border: oklch(0.1776 0.00000 0.00); /* #111111 */
  --text: oklch(0.1776 0.00000 0.00); /* #111111 */
  --muted: oklch(0.4078 0.00655 106.69); /* #4a4a46 */
  --accent: oklch(0.1776 0.00000 0.00); /* #111111 */
  --accent-foreground: oklch(0.9253 0.17069 101.21); /* #ffe94a */
  --accent-text: oklch(0.1776 0.00000 0.00); /* #111111 */
  --success: oklch(0.4644 0.12138 148.98); /* #146b30 */
  --warn: oklch(0.5078 0.10800 73.30); /* #8a5a00 */
  --danger: oklch(0.5405 0.22179 29.23); /* #d10000 */
}

.dark {
  /* Brutal amarillo — oscuro */
  --bg: oklch(0.1776 0.00000 0.00); /* #111111 */
  --surface: oklch(0.2178 0.00000 0.00); /* #1a1a1a */
  --border: oklch(0.9102 0.17166 103.90); /* #f5e645 */
  --text: oklch(0.9688 0.00661 106.52); /* #f5f5f0 */
  --muted: oklch(0.7636 0.01537 106.76); /* #b3b3a8 */
  --accent: oklch(0.9102 0.17166 103.90); /* #f5e645 */
  --accent-foreground: oklch(0.1776 0.00000 0.00); /* #111111 */
  --accent-text: oklch(0.9102 0.17166 103.90); /* #f5e645 */
  --success: oklch(0.8138 0.12756 152.72); /* #7dda9a */
  --warn: oklch(0.8060 0.13714 85.03); /* #e8b849 */
  --danger: oklch(0.7116 0.18122 22.84); /* #ff6b6b */
}
```


---

## Dopamina coral

`dopamina-coral` — Alto estímulo, un coral dominante, no un arcoíris

**Mejor para:** marcas jóvenes, consumo, campañas, eventos.  
**Evitá en:** sistemas densos, banca, gobierno.  
**Estilos:** [`dopamina-saturado`](../estilos/dopamina-saturado.md), [`maximalismo`](../estilos/maximalismo.md), [`retrofuturismo-y2k`](../estilos/retrofuturismo-y2k.md), [`memphis`](../estilos/memphis.md).

Dopamina no es rainbow vomit. Un coral (70) + un apoyo muy puntual, el resto neutro cálido. Si metés lima y violeta y cian juntos, volviste al slop.

### Claro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#fff6f1` | `oklch(0.9788 0.01177 51.32)` |
| Superficie | `#ffe4d8` | `oklch(0.9377 0.03393 45.49)` |
| Borde | `#f5c4b0` | `oklch(0.8584 0.06265 43.32)` |
| Texto | `#1a0e0a` | `oklch(0.1793 0.02229 39.19)` |
| Muted | `#6b4a40` | `oklch(0.4426 0.04826 37.56)` |
| Acento (sólido) | `#c83210` | `oklch(0.5485 0.19123 33.36)` |
| Acento foreground | `#ffffff` | `oklch(1.0000 0.00000 0.00)` |
| Acento texto/link | `#c83210` | `oklch(0.5485 0.19123 33.36)` |
| Success | `#1f6b3a` | `oklch(0.4689 0.10756 151.36)` |
| Warn | `#8a5a00` | `oklch(0.5078 0.10800 73.30)` |
| Danger | `#9b1008` | `oklch(0.4395 0.17125 29.50)` |

### Oscuro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#160e0c` | `oklch(0.1737 0.01442 34.45)` |
| Superficie | `#241612` | `oklch(0.2173 0.02434 36.60)` |
| Borde | `#4a2a22` | `oklch(0.3236 0.05018 34.83)` |
| Texto | `#ffede6` | `oklch(0.9585 0.02178 42.58)` |
| Muted | `#c4a098` | `oklch(0.7361 0.04445 32.66)` |
| Acento (sólido) | `#cb3917` | `oklch(0.5607 0.18799 33.86)` |
| Acento foreground | `#ffffff` | `oklch(1.0000 0.00000 0.00)` |
| Acento texto/link | `#ff9880` | `oklch(0.7815 0.12909 33.98)` |
| Success | `#7dda9a` | `oklch(0.8138 0.12756 152.72)` |
| Warn | `#e8b849` | `oklch(0.8060 0.13714 85.03)` |
| Danger | `#ff8a80` | `oklch(0.7594 0.14351 26.08)` |

### Contraste

**Claro:** texto sobre fondo WCAG 17.73:1, APCA Lc 100.9 (oscuro-sobre-claro); texto sobre superficie WCAG 15.61:1, APCA Lc 92.5 (oscuro-sobre-claro); accent-foreground sobre acento WCAG 5.36:1, APCA Lc -80.6 (claro-sobre-oscuro). Muted sobre fondo WCAG 7.36:1, APCA Lc 82.7 (oscuro-sobre-claro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 5.03:1, APCA Lc 70.8 (oscuro-sobre-claro)). `accent-text` está igualado o derivado para ese rol.

**Oscuro:** texto sobre fondo WCAG 16.79:1, APCA Lc -97.9 (claro-sobre-oscuro); texto sobre superficie WCAG 15.44:1, APCA Lc -97.1 (claro-sobre-oscuro); accent-foreground sobre acento WCAG 5.08:1, APCA Lc -79.1 (claro-sobre-oscuro). Muted sobre fondo WCAG 8.01:1, APCA Lc -54.7 (claro-sobre-oscuro): sirve para cuerpo secundario. El acento sólido no llega a 4.5:1 como texto sobre el fondo (3.75:1). Para botones usá `accent` + `accent-foreground`. Para links usá `accent-text` (9.12:1, Lc -61.3).

### Tokens CSS

```css
:root {
  /* Dopamina coral — claro */
  --bg: oklch(0.9788 0.01177 51.32); /* #fff6f1 */
  --surface: oklch(0.9377 0.03393 45.49); /* #ffe4d8 */
  --border: oklch(0.8584 0.06265 43.32); /* #f5c4b0 */
  --text: oklch(0.1793 0.02229 39.19); /* #1a0e0a */
  --muted: oklch(0.4426 0.04826 37.56); /* #6b4a40 */
  --accent: oklch(0.5485 0.19123 33.36); /* #c83210 */
  --accent-foreground: oklch(1.0000 0.00000 0.00); /* #ffffff */
  --accent-text: oklch(0.5485 0.19123 33.36); /* #c83210 */
  --success: oklch(0.4689 0.10756 151.36); /* #1f6b3a */
  --warn: oklch(0.5078 0.10800 73.30); /* #8a5a00 */
  --danger: oklch(0.4395 0.17125 29.50); /* #9b1008 */
}

.dark {
  /* Dopamina coral — oscuro */
  --bg: oklch(0.1737 0.01442 34.45); /* #160e0c */
  --surface: oklch(0.2173 0.02434 36.60); /* #241612 */
  --border: oklch(0.3236 0.05018 34.83); /* #4a2a22 */
  --text: oklch(0.9585 0.02178 42.58); /* #ffede6 */
  --muted: oklch(0.7361 0.04445 32.66); /* #c4a098 */
  --accent: oklch(0.5607 0.18799 33.86); /* #cb3917 */
  --accent-foreground: oklch(1.0000 0.00000 0.00); /* #ffffff */
  --accent-text: oklch(0.7815 0.12909 33.98); /* #ff9880 */
  --success: oklch(0.8138 0.12756 152.72); /* #7dda9a */
  --warn: oklch(0.8060 0.13714 85.03); /* #e8b849 */
  --danger: oklch(0.7594 0.14351 26.08); /* #ff8a80 */
}
```


---

## Y2K cromo

`y2k-cromo` — Cromo, magenta, una pizca de cian, nostalgia 2000

**Mejor para:** música, moda joven, campañas, portfolios.  
**Evitá en:** SaaS B2B, institucional, como default 2026.  
**Estilos:** [`retrofuturismo-y2k`](../estilos/retrofuturismo-y2k.md), [`maximalismo`](../estilos/maximalismo.md), [`dopamina-saturado`](../estilos/dopamina-saturado.md), [`espacial-3d`](../estilos/espacial-3d.md).

El magenta acá es deliberado (Y2K), no el violeta de plantilla. No lo uses en un hero de ‘AI platform’. El cromo es gris metálico, no un degradé índigo.

### Claro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#f3f4f7` | `oklch(0.9672 0.00414 271.37)` |
| Superficie | `#e4e7ee` | `oklch(0.9277 0.00999 267.36)` |
| Borde | `#c5cad6` | `oklch(0.8387 0.01756 267.77)` |
| Texto | `#12141a` | `oklch(0.1919 0.01257 270.68)` |
| Muted | `#555a68` | `oklch(0.4683 0.02352 269.90)` |
| Acento (sólido) | `#c4007a` | `oklch(0.5381 0.22255 352.58)` |
| Acento foreground | `#fff0f8` | `oklch(0.9692 0.01919 343.93)` |
| Acento texto/link | `#c4007a` | `oklch(0.5381 0.22255 352.58)` |
| Success | `#1f6b3a` | `oklch(0.4689 0.10756 151.36)` |
| Warn | `#8a5a00` | `oklch(0.5078 0.10800 73.30)` |
| Danger | `#b42318` | `oklch(0.5003 0.18205 29.51)` |

### Oscuro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#0c0d12` | `oklch(0.1604 0.01070 276.24)` |
| Superficie | `#161821` | `oklch(0.2112 0.01808 274.98)` |
| Borde | `#2e3344` | `oklch(0.3238 0.03110 271.84)` |
| Texto | `#eef0f6` | `oklch(0.9553 0.00831 271.33)` |
| Muted | `#9aa0b4` | `oklch(0.7075 0.02991 272.36)` |
| Acento (sólido) | `#d51a8d` | `oklch(0.5827 0.23103 350.36)` |
| Acento foreground | `#ffffff` | `oklch(1.0000 0.00000 0.00)` |
| Acento texto/link | `#ff8dc5` | `oklch(0.7822 0.15107 350.35)` |
| Success | `#7dda9a` | `oklch(0.8138 0.12756 152.72)` |
| Warn | `#e8b849` | `oklch(0.8060 0.13714 85.03)` |
| Danger | `#ff8a80` | `oklch(0.7594 0.14351 26.08)` |

### Contraste

**Claro:** texto sobre fondo WCAG 16.74:1, APCA Lc 98.5 (oscuro-sobre-claro); texto sobre superficie WCAG 14.87:1, APCA Lc 90.8 (oscuro-sobre-claro); accent-foreground sobre acento WCAG 5.26:1, APCA Lc -74.4 (claro-sobre-oscuro). Muted sobre fondo WCAG 6.26:1, APCA Lc 77.3 (oscuro-sobre-claro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 5.26:1, APCA Lc 69.8 (oscuro-sobre-claro)). `accent-text` está igualado o derivado para ese rol.

**Oscuro:** texto sobre fondo WCAG 17.03:1, APCA Lc -97.8 (claro-sobre-oscuro); texto sobre superficie WCAG 15.53:1, APCA Lc -96.9 (claro-sobre-oscuro); accent-foreground sobre acento WCAG 4.81:1, APCA Lc -76.9 (claro-sobre-oscuro). Muted sobre fondo WCAG 7.45:1, APCA Lc -50.8 (claro-sobre-oscuro): sirve para cuerpo secundario. El acento sólido no llega a 4.5:1 como texto sobre el fondo (4.03:1). Para botones usá `accent` + `accent-foreground`. Para links usá `accent-text` (9.12:1, Lc -60.6).

### Tokens CSS

```css
:root {
  /* Y2K cromo — claro */
  --bg: oklch(0.9672 0.00414 271.37); /* #f3f4f7 */
  --surface: oklch(0.9277 0.00999 267.36); /* #e4e7ee */
  --border: oklch(0.8387 0.01756 267.77); /* #c5cad6 */
  --text: oklch(0.1919 0.01257 270.68); /* #12141a */
  --muted: oklch(0.4683 0.02352 269.90); /* #555a68 */
  --accent: oklch(0.5381 0.22255 352.58); /* #c4007a */
  --accent-foreground: oklch(0.9692 0.01919 343.93); /* #fff0f8 */
  --accent-text: oklch(0.5381 0.22255 352.58); /* #c4007a */
  --success: oklch(0.4689 0.10756 151.36); /* #1f6b3a */
  --warn: oklch(0.5078 0.10800 73.30); /* #8a5a00 */
  --danger: oklch(0.5003 0.18205 29.51); /* #b42318 */
}

.dark {
  /* Y2K cromo — oscuro */
  --bg: oklch(0.1604 0.01070 276.24); /* #0c0d12 */
  --surface: oklch(0.2112 0.01808 274.98); /* #161821 */
  --border: oklch(0.3238 0.03110 271.84); /* #2e3344 */
  --text: oklch(0.9553 0.00831 271.33); /* #eef0f6 */
  --muted: oklch(0.7075 0.02991 272.36); /* #9aa0b4 */
  --accent: oklch(0.5827 0.23103 350.36); /* #d51a8d */
  --accent-foreground: oklch(1.0000 0.00000 0.00); /* #ffffff */
  --accent-text: oklch(0.7822 0.15107 350.35); /* #ff8dc5 */
  --success: oklch(0.8138 0.12756 152.72); /* #7dda9a */
  --warn: oklch(0.8060 0.13714 85.03); /* #e8b849 */
  --danger: oklch(0.7594 0.14351 26.08); /* #ff8a80 */
}
```


---

## Póster y tinta

`poster-tinta` — Maximalismo contenido: un póster, no un circo

**Mejor para:** cultura, eventos, editorial ruidosa, campañas.  
**Evitá en:** dashboards, onboarding de producto.  
**Estilos:** [`maximalismo`](../estilos/maximalismo.md), [`editorial-revista`](../estilos/editorial-revista.md), [`tipografia-kinetica`](../estilos/tipografia-kinetica.md), [`grilla-rota`](../estilos/grilla-rota.md), [`bauhaus`](../estilos/bauhaus.md).

70-30-10. El rojo póster es el 10. El fondo papel sucio es el 70. Si cada bloque pide atención, no es maximalismo: es ruido.

### Claro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#f2ebdd` | `oklch(0.9418 0.02009 84.59)` |
| Superficie | `#e8dcc8` | `oklch(0.8988 0.02983 80.65)` |
| Borde | `#1a1a1a` | `oklch(0.2178 0.00000 0.00)` |
| Texto | `#1a1a1a` | `oklch(0.2178 0.00000 0.00)` |
| Muted | `#5a5248` | `oklch(0.4432 0.01910 73.43)` |
| Acento (sólido) | `#d00020` | `oklch(0.5401 0.21912 25.26)` |
| Acento foreground | `#fff5f5` | `oklch(0.9779 0.01075 17.34)` |
| Acento texto/link | `#d00020` | `oklch(0.5401 0.21912 25.26)` |
| Success | `#1f6b3a` | `oklch(0.4689 0.10756 151.36)` |
| Warn | `#8a5a00` | `oklch(0.5078 0.10800 73.30)` |
| Danger | `#8e0010` | `oklch(0.4071 0.16542 25.88)` |

### Oscuro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#14110e` | `oklch(0.1801 0.00779 67.30)` |
| Superficie | `#1f1a16` | `oklch(0.2222 0.01097 60.87)` |
| Borde | `#f2ebdd` | `oklch(0.9418 0.02009 84.59)` |
| Texto | `#f2ebdd` | `oklch(0.9418 0.02009 84.59)` |
| Muted | `#b8afa0` | `oklch(0.7573 0.02337 80.66)` |
| Acento (sólido) | `#e02e2e` | `oklch(0.5903 0.21299 26.78)` |
| Acento foreground | `#ffffff` | `oklch(1.0000 0.00000 0.00)` |
| Acento texto/link | `#ff9b90` | `oklch(0.7897 0.12162 26.88)` |
| Success | `#7dda9a` | `oklch(0.8138 0.12756 152.72)` |
| Warn | `#e8b849` | `oklch(0.8060 0.13714 85.03)` |
| Danger | `#ff8a80` | `oklch(0.7594 0.14351 26.08)` |

### Contraste

**Claro:** texto sobre fondo WCAG 14.67:1, APCA Lc 92.7 (oscuro-sobre-claro); texto sobre superficie WCAG 12.85:1, APCA Lc 84.5 (oscuro-sobre-claro); accent-foreground sobre acento WCAG 5.3:1, APCA Lc -75.7 (claro-sobre-oscuro). Muted sobre fondo WCAG 6.47:1, APCA Lc 75.2 (oscuro-sobre-claro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 4.78:1, APCA Lc 64.0 (oscuro-sobre-claro)). `accent-text` está igualado o derivado para ese rol.

**Oscuro:** texto sobre fondo WCAG 15.86:1, APCA Lc -94.6 (claro-sobre-oscuro); texto sobre superficie WCAG 14.54:1, APCA Lc -93.7 (claro-sobre-oscuro); accent-foreground sobre acento WCAG 4.56:1, APCA Lc -75.4 (claro-sobre-oscuro). Muted sobre fondo WCAG 8.67:1, APCA Lc -59.0 (claro-sobre-oscuro): sirve para cuerpo secundario. El acento sólido no llega a 4.5:1 como texto sobre el fondo (4.12:1). Para botones usá `accent` + `accent-foreground`. Para links usá `accent-text` (9.27:1, Lc -62.6).

### Tokens CSS

```css
:root {
  /* Póster y tinta — claro */
  --bg: oklch(0.9418 0.02009 84.59); /* #f2ebdd */
  --surface: oklch(0.8988 0.02983 80.65); /* #e8dcc8 */
  --border: oklch(0.2178 0.00000 0.00); /* #1a1a1a */
  --text: oklch(0.2178 0.00000 0.00); /* #1a1a1a */
  --muted: oklch(0.4432 0.01910 73.43); /* #5a5248 */
  --accent: oklch(0.5401 0.21912 25.26); /* #d00020 */
  --accent-foreground: oklch(0.9779 0.01075 17.34); /* #fff5f5 */
  --accent-text: oklch(0.5401 0.21912 25.26); /* #d00020 */
  --success: oklch(0.4689 0.10756 151.36); /* #1f6b3a */
  --warn: oklch(0.5078 0.10800 73.30); /* #8a5a00 */
  --danger: oklch(0.4071 0.16542 25.88); /* #8e0010 */
}

.dark {
  /* Póster y tinta — oscuro */
  --bg: oklch(0.1801 0.00779 67.30); /* #14110e */
  --surface: oklch(0.2222 0.01097 60.87); /* #1f1a16 */
  --border: oklch(0.9418 0.02009 84.59); /* #f2ebdd */
  --text: oklch(0.9418 0.02009 84.59); /* #f2ebdd */
  --muted: oklch(0.7573 0.02337 80.66); /* #b8afa0 */
  --accent: oklch(0.5903 0.21299 26.78); /* #e02e2e */
  --accent-foreground: oklch(1.0000 0.00000 0.00); /* #ffffff */
  --accent-text: oklch(0.7897 0.12162 26.88); /* #ff9b90 */
  --success: oklch(0.8138 0.12756 152.72); /* #7dda9a */
  --warn: oklch(0.8060 0.13714 85.03); /* #e8b849 */
  --danger: oklch(0.7594 0.14351 26.08); /* #ff8a80 */
}
```

---

## Bauhaus primario

`bauhaus-primario` — Rojo, amarillo y azul ajustados, con negro y blanco

**Mejor para:** cultura y museos, escuelas de diseño, festivales, educación.  
**Evitá en:** salud, banca, dashboards densos.  
**Estilos:** [`bauhaus`](../estilos/bauhaus.md), [`suizo-internacional`](../estilos/suizo-internacional.md), [`expresivo-minimo`](../estilos/expresivo-minimo.md).

Paleta propia de Designweb para el estilo bauhaus. Secundarios para bloques de color (no para texto): azul #1f4fa3 y amarillo #f2c230. El amarillo nunca lleva texto blanco.

### Claro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#fafaf8` | `oklch(0.9845 0.00264 106.45)` |
| Superficie | `#efefec` | `oklch(0.9513 0.00399 106.48)` |
| Borde | `#d6d6d2` | `oklch(0.8750 0.00543 106.51)` |
| Texto | `#111111` | `oklch(0.1776 0.00000 0.00)` |
| Muted | `#4a4a48` | `oklch(0.4084 0.00328 106.54)` |
| Acento (sólido) | `#c8321e` | `oklch(0.5494 0.18963 31.05)` |
| Acento foreground | `#ffffff` | `oklch(1.0000 0.00000 0.00)` |
| Acento texto/link | `#b02a18` | `oklch(0.4987 0.17319 31.09)` |
| Success | `#1f6b3a` | `oklch(0.4689 0.10756 151.36)` |
| Warn | `#8a5a00` | `oklch(0.5078 0.10800 73.30)` |
| Danger | `#b42318` | `oklch(0.5003 0.18205 29.51)` |

### Oscuro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#111111` | `oklch(0.1776 0.00000 0.00)` |
| Superficie | `#1c1c1c` | `oklch(0.2264 0.00000 0.00)` |
| Borde | `#333333` | `oklch(0.3211 0.00000 0.00)` |
| Texto | `#f5f5f2` | `oklch(0.9693 0.00397 106.47)` |
| Muted | `#bababa` | `oklch(0.7889 0.00000 0.00)` |
| Acento (sólido) | `#f2c230` | `oklch(0.8340 0.15843 88.96)` |
| Acento foreground | `#111111` | `oklch(0.1776 0.00000 0.00)` |
| Acento texto/link | `#f2c230` | `oklch(0.8340 0.15843 88.96)` |
| Success | `#7dda9a` | `oklch(0.8138 0.12756 152.72)` |
| Warn | `#e8b849` | `oklch(0.8060 0.13714 85.03)` |
| Danger | `#ff8a80` | `oklch(0.7594 0.14351 26.08)` |

### Contraste

**Claro:** texto sobre fondo WCAG 18.07:1, APCA Lc 102.3 (oscuro-sobre-claro); texto sobre superficie WCAG 16.39:1, APCA Lc 95.7 (oscuro-sobre-claro); accent-foreground sobre acento WCAG 5.34:1, APCA Lc -80.5 (claro-sobre-oscuro). Muted sobre fondo WCAG 8.50:1, APCA Lc 87.3 (oscuro-sobre-claro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 5.11:1, APCA Lc 72.0 (oscuro-sobre-claro)). `accent-text` está igualado o derivado para ese rol.

**Oscuro:** texto sobre fondo WCAG 17.29:1, APCA Lc -100.7 (claro-sobre-oscuro); texto sobre superficie WCAG 15.60:1, APCA Lc -99.6 (claro-sobre-oscuro); accent-foreground sobre acento WCAG 11.27:1, APCA Lc 73.8 (oscuro-sobre-claro). Muted sobre fondo WCAG 9.73:1, APCA Lc -64.7 (claro-sobre-oscuro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 11.27:1, APCA Lc -72.9 (claro-sobre-oscuro)). `accent-text` está igualado o derivado para ese rol.

### Tokens CSS

```css
:root {
  /* Bauhaus primario — claro */
  --bg: oklch(0.9845 0.00264 106.45); /* #fafaf8 */
  --surface: oklch(0.9513 0.00399 106.48); /* #efefec */
  --border: oklch(0.8750 0.00543 106.51); /* #d6d6d2 */
  --text: oklch(0.1776 0.00000 0.00); /* #111111 */
  --muted: oklch(0.4084 0.00328 106.54); /* #4a4a48 */
  --accent: oklch(0.5494 0.18963 31.05); /* #c8321e */
  --accent-foreground: oklch(1.0000 0.00000 0.00); /* #ffffff */
  --accent-text: oklch(0.4987 0.17319 31.09); /* #b02a18 */
  --success: oklch(0.4689 0.10756 151.36); /* #1f6b3a */
  --warn: oklch(0.5078 0.10800 73.30); /* #8a5a00 */
  --danger: oklch(0.5003 0.18205 29.51); /* #b42318 */
}
.dark {
  /* Bauhaus primario — oscuro */
  --bg: oklch(0.1776 0.00000 0.00); /* #111111 */
  --surface: oklch(0.2264 0.00000 0.00); /* #1c1c1c */
  --border: oklch(0.3211 0.00000 0.00); /* #333333 */
  --text: oklch(0.9693 0.00397 106.47); /* #f5f5f2 */
  --muted: oklch(0.7889 0.00000 0.00); /* #bababa */
  --accent: oklch(0.8340 0.15843 88.96); /* #f2c230 */
  --accent-foreground: oklch(0.1776 0.00000 0.00); /* #111111 */
  --accent-text: oklch(0.8340 0.15843 88.96); /* #f2c230 */
  --success: oklch(0.8138 0.12756 152.72); /* #7dda9a */
  --warn: oklch(0.8060 0.13714 85.03); /* #e8b849 */
  --danger: oklch(0.7594 0.14351 26.08); /* #ff8a80 */
}
```

---

## Memphis pastel

`memphis-pastel` — Rosa chicle, menta y amarillo pollito, con negro de estructura

**Mejor para:** eventos y festivales, juguetes y kids, música, campañas de temporada.  
**Evitá en:** salud, finanzas, legal, B2B.  
**Estilos:** [`memphis`](../estilos/memphis.md), [`dopamina-saturado`](../estilos/dopamina-saturado.md), [`maximalismo`](../estilos/maximalismo.md).

Paleta propia de Designweb para el estilo memphis. Pasteles para formas y patrones (nunca bajo texto): rosa #ff8fb1, menta #7fe0c3, amarillo #ffe066, celeste #8ecbff.

### Claro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#ffffff` | `oklch(1.0000 0.00000 0.00)` |
| Superficie | `#f4f1ee` | `oklch(0.9596 0.00515 67.76)` |
| Borde | `#dcd7d2` | `oklch(0.8817 0.00876 67.71)` |
| Texto | `#141414` | `oklch(0.1913 0.00000 0.00)` |
| Muted | `#4d4a47` | `oklch(0.4110 0.00636 67.65)` |
| Acento (sólido) | `#c42a63` | `oklch(0.5479 0.19191 4.44)` |
| Acento foreground | `#ffffff` | `oklch(1.0000 0.00000 0.00)` |
| Acento texto/link | `#c42a63` | `oklch(0.5479 0.19191 4.44)` |
| Success | `#1f6b3a` | `oklch(0.4689 0.10756 151.36)` |
| Warn | `#8a5a00` | `oklch(0.5078 0.10800 73.30)` |
| Danger | `#b42318` | `oklch(0.5003 0.18205 29.51)` |

### Oscuro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#141414` | `oklch(0.1913 0.00000 0.00)` |
| Superficie | `#1f1d1c` | `oklch(0.2326 0.00364 48.56)` |
| Borde | `#3a3633` | `oklch(0.3359 0.00768 59.42)` |
| Texto | `#fbf6f0` | `oklch(0.9753 0.00961 72.66)` |
| Muted | `#c2bab2` | `oklch(0.7932 0.01439 67.62)` |
| Acento (sólido) | `#7fe0c3` | `oklch(0.8388 0.10168 172.37)` |
| Acento foreground | `#141414` | `oklch(0.1913 0.00000 0.00)` |
| Acento texto/link | `#7fe0c3` | `oklch(0.8388 0.10168 172.37)` |
| Success | `#7dda9a` | `oklch(0.8138 0.12756 152.72)` |
| Warn | `#e8b849` | `oklch(0.8060 0.13714 85.03)` |
| Danger | `#ff8a80` | `oklch(0.7594 0.14351 26.08)` |

### Contraste

**Claro:** texto sobre fondo WCAG 18.42:1, APCA Lc 105.1 (oscuro-sobre-claro); texto sobre superficie WCAG 16.37:1, APCA Lc 97.0 (oscuro-sobre-claro); accent-foreground sobre acento WCAG 5.44:1, APCA Lc -81.0 (claro-sobre-oscuro). Muted sobre fondo WCAG 8.80:1, APCA Lc 90.1 (oscuro-sobre-claro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 5.44:1, APCA Lc 75.7 (oscuro-sobre-claro)). `accent-text` está igualado o derivado para ese rol.

**Oscuro:** texto sobre fondo WCAG 17.14:1, APCA Lc -101.6 (claro-sobre-oscuro); texto sobre superficie WCAG 15.62:1, APCA Lc -100.6 (claro-sobre-oscuro); accent-foreground sobre acento WCAG 11.71:1, APCA Lc 76.8 (oscuro-sobre-claro). Muted sobre fondo WCAG 9.62:1, APCA Lc -65.1 (claro-sobre-oscuro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 11.71:1, APCA Lc -76.4 (claro-sobre-oscuro)). `accent-text` está igualado o derivado para ese rol.

### Tokens CSS

```css
:root {
  /* Memphis pastel — claro */
  --bg: oklch(1.0000 0.00000 0.00); /* #ffffff */
  --surface: oklch(0.9596 0.00515 67.76); /* #f4f1ee */
  --border: oklch(0.8817 0.00876 67.71); /* #dcd7d2 */
  --text: oklch(0.1913 0.00000 0.00); /* #141414 */
  --muted: oklch(0.4110 0.00636 67.65); /* #4d4a47 */
  --accent: oklch(0.5479 0.19191 4.44); /* #c42a63 */
  --accent-foreground: oklch(1.0000 0.00000 0.00); /* #ffffff */
  --accent-text: oklch(0.5479 0.19191 4.44); /* #c42a63 */
  --success: oklch(0.4689 0.10756 151.36); /* #1f6b3a */
  --warn: oklch(0.5078 0.10800 73.30); /* #8a5a00 */
  --danger: oklch(0.5003 0.18205 29.51); /* #b42318 */
}
.dark {
  /* Memphis pastel — oscuro */
  --bg: oklch(0.1913 0.00000 0.00); /* #141414 */
  --surface: oklch(0.2326 0.00364 48.56); /* #1f1d1c */
  --border: oklch(0.3359 0.00768 59.42); /* #3a3633 */
  --text: oklch(0.9753 0.00961 72.66); /* #fbf6f0 */
  --muted: oklch(0.7932 0.01439 67.62); /* #c2bab2 */
  --accent: oklch(0.8388 0.10168 172.37); /* #7fe0c3 */
  --accent-foreground: oklch(0.1913 0.00000 0.00); /* #141414 */
  --accent-text: oklch(0.8388 0.10168 172.37); /* #7fe0c3 */
  --success: oklch(0.8138 0.12756 152.72); /* #7dda9a */
  --warn: oklch(0.8060 0.13714 85.03); /* #e8b849 */
  --danger: oklch(0.7594 0.14351 26.08); /* #ff8a80 */
}
```

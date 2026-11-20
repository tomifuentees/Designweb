# Paletas de producto / SaaS

Estas paletas sirven cuando el producto (un recorte de UI, un dato, una consola) tiene que verse al frente, con **un solo acento** y mucho aire. Son el territorio de [`saas-oscuro-premium`](../estilos/saas-oscuro-premium.md), [`estilo-linear`](../estilos/estilo-linear.md), [`bento-grids`](../estilos/bento-grids.md), [`ui-casi-invisible`](../estilos/ui-casi-invisible.md) y [`catalogo-tecnico`](../estilos/catalogo-tecnico.md).

Ninguna usa índigo ni un degradé violeta-azul. El acento es lima, rojo de comando, cian de terminal, oro de baja croma, naranja de señal o menta. Si el brief pide “que se vea como Linear”, partí de acá y cambiale la voz: no copies el púrpura.


Hay **7 paletas** (la última, océano profundo, adaptada en noviembre de 2026 de la skill theme-factory de Anthropic) en este grupo. Los valores salen de [`paletas.json`](./paletas.json). Los links de estilo apuntan a las fichas de [`../estilos/`](../estilos/README.md).


---

## Lima mercurio

`lima-mercurio` — Oscuro o claro técnico, un acento lima, cero violeta

**Mejor para:** devtools, fintech técnica, SaaS B2B, dashboards.  
**Evitá en:** marca cálida, comida, estudio jurídico, salud infantil.  
**Estilos:** [`saas-oscuro-premium`](../estilos/saas-oscuro-premium.md), [`estilo-linear`](../estilos/estilo-linear.md), [`bento-grids`](../estilos/bento-grids.md), [`ui-casi-invisible`](../estilos/ui-casi-invisible.md), [`catalogo-tecnico`](../estilos/catalogo-tecnico.md), [`denso-de-datos`](../estilos/denso-de-datos.md).

Pariente de la disciplina ‘un acento sobre negro’ (Mercury/Linear), pero el lima no es el púrpura de Linear ni el índigo de Tailwind. Un solo acento.

### Claro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#f6f7f2` | `oklch(0.9740 0.00668 115.70)` |
| Superficie | `#eceee6` | `oklch(0.9454 0.01083 118.03)` |
| Borde | `#d3d7cb` | `oklch(0.8727 0.01679 121.80)` |
| Texto | `#141711` | `oklch(0.1991 0.01256 129.19)` |
| Muted | `#5a6154` | `oklch(0.4824 0.02214 130.45)` |
| Acento (sólido) | `#3f6b00` | `oklch(0.4770 0.13233 131.96)` |
| Acento foreground | `#f3ffd2` | `oklch(0.9797 0.05973 119.64)` |
| Acento texto/link | `#3f6b00` | `oklch(0.4770 0.13233 131.96)` |
| Success | `#1f6b3a` | `oklch(0.4689 0.10756 151.36)` |
| Warn | `#8a5a00` | `oklch(0.5078 0.10800 73.30)` |
| Danger | `#b42318` | `oklch(0.5003 0.18205 29.51)` |

### Oscuro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#0c0e0a` | `oklch(0.1598 0.00886 129.11)` |
| Superficie | `#161914` | `oklch(0.2083 0.01070 132.76)` |
| Borde | `#2c3228` | `oklch(0.3079 0.01936 132.85)` |
| Texto | `#f1f3eb` | `oklch(0.9604 0.01079 118.02)` |
| Muted | `#9aa392` | `oklch(0.7033 0.02631 130.02)` |
| Acento (sólido) | `#c6ec4a` | `oklch(0.8868 0.18683 121.81)` |
| Acento foreground | `#141711` | `oklch(0.1991 0.01256 129.19)` |
| Acento texto/link | `#c6ec4a` | `oklch(0.8868 0.18683 121.81)` |
| Success | `#7dda9a` | `oklch(0.8138 0.12756 152.72)` |
| Warn | `#e8b849` | `oklch(0.8060 0.13714 85.03)` |
| Danger | `#ff8a80` | `oklch(0.7594 0.14351 26.08)` |

### Contraste

**Claro:** texto sobre fondo WCAG 16.81:1, APCA Lc 99.7 (oscuro-sobre-claro); texto sobre superficie WCAG 15.46:1, APCA Lc 94.1 (oscuro-sobre-claro); accent-foreground sobre acento WCAG 6.05:1, APCA Lc -82.8 (claro-sobre-oscuro). Muted sobre fondo WCAG 5.96:1, APCA Lc 76.8 (oscuro-sobre-claro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 5.88:1, APCA Lc 76.1 (oscuro-sobre-claro)). `accent-text` está igualado o derivado para ese rol.

**Oscuro:** texto sobre fondo WCAG 17.32:1, APCA Lc -99.1 (claro-sobre-oscuro); texto sobre superficie WCAG 15.85:1, APCA Lc -98.2 (claro-sobre-oscuro); accent-foreground sobre acento WCAG 13.36:1, APCA Lc 85.2 (oscuro-sobre-claro). Muted sobre fondo WCAG 7.41:1, APCA Lc -50.6 (claro-sobre-oscuro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 14.31:1, APCA Lc -86.1 (claro-sobre-oscuro)). `accent-text` está igualado o derivado para ese rol.

### Tokens CSS

```css
:root {
  /* Lima mercurio — claro */
  --bg: oklch(0.9740 0.00668 115.70); /* #f6f7f2 */
  --surface: oklch(0.9454 0.01083 118.03); /* #eceee6 */
  --border: oklch(0.8727 0.01679 121.80); /* #d3d7cb */
  --text: oklch(0.1991 0.01256 129.19); /* #141711 */
  --muted: oklch(0.4824 0.02214 130.45); /* #5a6154 */
  --accent: oklch(0.4770 0.13233 131.96); /* #3f6b00 */
  --accent-foreground: oklch(0.9797 0.05973 119.64); /* #f3ffd2 */
  --accent-text: oklch(0.4770 0.13233 131.96); /* #3f6b00 */
  --success: oklch(0.4689 0.10756 151.36); /* #1f6b3a */
  --warn: oklch(0.5078 0.10800 73.30); /* #8a5a00 */
  --danger: oklch(0.5003 0.18205 29.51); /* #b42318 */
}

.dark {
  /* Lima mercurio — oscuro */
  --bg: oklch(0.1598 0.00886 129.11); /* #0c0e0a */
  --surface: oklch(0.2083 0.01070 132.76); /* #161914 */
  --border: oklch(0.3079 0.01936 132.85); /* #2c3228 */
  --text: oklch(0.9604 0.01079 118.02); /* #f1f3eb */
  --muted: oklch(0.7033 0.02631 130.02); /* #9aa392 */
  --accent: oklch(0.8868 0.18683 121.81); /* #c6ec4a */
  --accent-foreground: oklch(0.1991 0.01256 129.19); /* #141711 */
  --accent-text: oklch(0.8868 0.18683 121.81); /* #c6ec4a */
  --success: oklch(0.8138 0.12756 152.72); /* #7dda9a */
  --warn: oklch(0.8060 0.13714 85.03); /* #e8b849 */
  --danger: oklch(0.7594 0.14351 26.08); /* #ff8a80 */
}
```


---

## Rayo rojo

`rayo-rojo` — Producto oscuro con un rojo de comando, preciso

**Mejor para:** paletas de comandos, productividad, infra, herramientas de diseño.  
**Evitá en:** salud, ONG, marcas que no pueden usar rojo como acento.  
**Estilos:** [`saas-oscuro-premium`](../estilos/saas-oscuro-premium.md), [`estilo-linear`](../estilos/estilo-linear.md), [`bento-grids`](../estilos/bento-grids.md).

El rojo es de acción, no de error: el danger se baja un tono más oscuro/bordeado para no competir. Inspirado en la disciplina de un acento (tipo Raycast), no es un clon de su hex.

### Claro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#f7f5f4` | `oklch(0.9714 0.00253 48.72)` |
| Superficie | `#efecea` | `oklch(0.9448 0.00422 56.37)` |
| Borde | `#d9d3d0` | `oklch(0.8708 0.00782 48.64)` |
| Texto | `#1a1414` | `oklch(0.1987 0.00985 18.01)` |
| Muted | `#655c5a` | `oklch(0.4827 0.01212 32.54)` |
| Acento (sólido) | `#c0152e` | `oklch(0.5171 0.19862 22.16)` |
| Acento foreground | `#fff7f6` | `oklch(0.9820 0.00870 26.02)` |
| Acento texto/link | `#c0152e` | `oklch(0.5171 0.19862 22.16)` |
| Success | `#1f6b3a` | `oklch(0.4689 0.10756 151.36)` |
| Warn | `#9a5b00` | `oklch(0.5310 0.11903 65.12)` |
| Danger | `#8e1008` | `oklch(0.4135 0.15940 29.57)` |

### Oscuro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#100c0c` | `oklch(0.1595 0.00691 17.90)` |
| Superficie | `#1b1515` | `oklch(0.2031 0.00979 17.99)` |
| Borde | `#3a2c2c` | `oklch(0.3091 0.02075 18.34)` |
| Texto | `#f6edec` | `oklch(0.9529 0.00984 25.08)` |
| Muted | `#b3a3a1` | `oklch(0.7286 0.01897 26.16)` |
| Acento (sólido) | `#d63840` | `oklch(0.5830 0.19417 23.13)` |
| Acento foreground | `#ffffff` | `oklch(1.0000 0.00000 0.00)` |
| Acento texto/link | `#ff9792` | `oklch(0.7836 0.12577 23.27)` |
| Success | `#7dda9a` | `oklch(0.8138 0.12756 152.72)` |
| Warn | `#e8b849` | `oklch(0.8060 0.13714 85.03)` |
| Danger | `#ff9a90` | `oklch(0.7880 0.12271 26.25)` |

### Contraste

**Claro:** texto sobre fondo WCAG 16.74:1, APCA Lc 99.1 (oscuro-sobre-claro); texto sobre superficie WCAG 15.47:1, APCA Lc 93.9 (oscuro-sobre-claro); accent-foreground sobre acento WCAG 5.87:1, APCA Lc -79.9 (claro-sobre-oscuro). Muted sobre fondo WCAG 5.98:1, APCA Lc 76.5 (oscuro-sobre-claro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 5.7:1, APCA Lc 73.0 (oscuro-sobre-claro)). `accent-text` está igualado o derivado para ese rol.

**Oscuro:** texto sobre fondo WCAG 16.89:1, APCA Lc -97.1 (claro-sobre-oscuro); texto sobre superficie WCAG 15.66:1, APCA Lc -96.4 (claro-sobre-oscuro); accent-foreground sobre acento WCAG 4.67:1, APCA Lc -76.5 (claro-sobre-oscuro). Muted sobre fondo WCAG 8.03:1, APCA Lc -54.0 (claro-sobre-oscuro): sirve para cuerpo secundario. El acento sólido no llega a 4.5:1 como texto sobre el fondo (4.17:1). Para botones usá `accent` + `accent-foreground`. Para links usá `accent-text` (9.35:1, Lc -61.7).

### Tokens CSS

```css
:root {
  /* Rayo rojo — claro */
  --bg: oklch(0.9714 0.00253 48.72); /* #f7f5f4 */
  --surface: oklch(0.9448 0.00422 56.37); /* #efecea */
  --border: oklch(0.8708 0.00782 48.64); /* #d9d3d0 */
  --text: oklch(0.1987 0.00985 18.01); /* #1a1414 */
  --muted: oklch(0.4827 0.01212 32.54); /* #655c5a */
  --accent: oklch(0.5171 0.19862 22.16); /* #c0152e */
  --accent-foreground: oklch(0.9820 0.00870 26.02); /* #fff7f6 */
  --accent-text: oklch(0.5171 0.19862 22.16); /* #c0152e */
  --success: oklch(0.4689 0.10756 151.36); /* #1f6b3a */
  --warn: oklch(0.5310 0.11903 65.12); /* #9a5b00 */
  --danger: oklch(0.4135 0.15940 29.57); /* #8e1008 */
}

.dark {
  /* Rayo rojo — oscuro */
  --bg: oklch(0.1595 0.00691 17.90); /* #100c0c */
  --surface: oklch(0.2031 0.00979 17.99); /* #1b1515 */
  --border: oklch(0.3091 0.02075 18.34); /* #3a2c2c */
  --text: oklch(0.9529 0.00984 25.08); /* #f6edec */
  --muted: oklch(0.7286 0.01897 26.16); /* #b3a3a1 */
  --accent: oklch(0.5830 0.19417 23.13); /* #d63840 */
  --accent-foreground: oklch(1.0000 0.00000 0.00); /* #ffffff */
  --accent-text: oklch(0.7836 0.12577 23.27); /* #ff9792 */
  --success: oklch(0.8138 0.12756 152.72); /* #7dda9a */
  --warn: oklch(0.8060 0.13714 85.03); /* #e8b849 */
  --danger: oklch(0.7880 0.12271 26.25); /* #ff9a90 */
}
```


---

## Cian terminal

`cian-terminal` — Terminal, documentación de API, frío pero no índigo

**Mejor para:** devtools, docs de API, infra, CLI companions.  
**Evitá en:** marcas humanas o artesanales, e-commerce de moda.  
**Estilos:** [`saas-oscuro-premium`](../estilos/saas-oscuro-premium.md), [`catalogo-tecnico`](../estilos/catalogo-tecnico.md), [`ui-casi-invisible`](../estilos/ui-casi-invisible.md), [`bento-grids`](../estilos/bento-grids.md).

El cian vive en el matiz ~200, lejos del índigo 270–290 que dispara el look IA. No lo desaturés hasta que parezca el sky-500 de Tailwind.

### Claro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#f4f7f8` | `oklch(0.9741 0.00347 219.53)` |
| Superficie | `#e6eeef` | `oklch(0.9434 0.00866 205.89)` |
| Borde | `#c9d5d8` | `oklch(0.8648 0.01369 214.37)` |
| Texto | `#10181a` | `oklch(0.2019 0.01253 214.73)` |
| Muted | `#4f5e62` | `oklch(0.4707 0.01959 215.63)` |
| Acento (sólido) | `#0b6e7a` | `oklch(0.4935 0.08236 208.36)` |
| Acento foreground | `#e8fcff` | `oklch(0.9773 0.02132 207.59)` |
| Acento texto/link | `#0b6e7a` | `oklch(0.4935 0.08236 208.36)` |
| Success | `#1f6b3a` | `oklch(0.4689 0.10756 151.36)` |
| Warn | `#8a5a00` | `oklch(0.5078 0.10800 73.30)` |
| Danger | `#b42318` | `oklch(0.5003 0.18205 29.51)` |

### Oscuro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#0a1012` | `oklch(0.1677 0.01026 220.22)` |
| Superficie | `#121a1c` | `oklch(0.2107 0.01244 214.70)` |
| Borde | `#2a3a3e` | `oklch(0.3361 0.02196 214.78)` |
| Texto | `#e6f1f3` | `oklch(0.9505 0.01201 209.80)` |
| Muted | `#8aa0a6` | `oklch(0.6907 0.02626 216.00)` |
| Acento (sólido) | `#5ee1f0` | `oklch(0.8430 0.11551 205.67)` |
| Acento foreground | `#082022` | `oklch(0.2257 0.02984 202.74)` |
| Acento texto/link | `#5ee1f0` | `oklch(0.8430 0.11551 205.67)` |
| Success | `#7dda9a` | `oklch(0.8138 0.12756 152.72)` |
| Warn | `#e8b849` | `oklch(0.8060 0.13714 85.03)` |
| Danger | `#ff8a80` | `oklch(0.7594 0.14351 26.08)` |

### Contraste

**Claro:** texto sobre fondo WCAG 16.71:1, APCA Lc 99.6 (oscuro-sobre-claro); texto sobre superficie WCAG 15.28:1, APCA Lc 93.7 (oscuro-sobre-claro); accent-foreground sobre acento WCAG 5.62:1, APCA Lc -80.0 (claro-sobre-oscuro). Muted sobre fondo WCAG 6.27:1, APCA Lc 78.2 (oscuro-sobre-claro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 5.53:1, APCA Lc 74.2 (oscuro-sobre-claro)). `accent-text` está igualado o derivado para ese rol.

**Oscuro:** texto sobre fondo WCAG 16.65:1, APCA Lc -96.9 (claro-sobre-oscuro); texto sobre superficie WCAG 15.33:1, APCA Lc -96.1 (claro-sobre-oscuro); accent-foreground sobre acento WCAG 10.89:1, APCA Lc 76.3 (oscuro-sobre-claro). Muted sobre fondo WCAG 6.99:1, APCA Lc -48.4 (claro-sobre-oscuro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 12.32:1, APCA Lc -77.5 (claro-sobre-oscuro)). `accent-text` está igualado o derivado para ese rol.

### Tokens CSS

```css
:root {
  /* Cian terminal — claro */
  --bg: oklch(0.9741 0.00347 219.53); /* #f4f7f8 */
  --surface: oklch(0.9434 0.00866 205.89); /* #e6eeef */
  --border: oklch(0.8648 0.01369 214.37); /* #c9d5d8 */
  --text: oklch(0.2019 0.01253 214.73); /* #10181a */
  --muted: oklch(0.4707 0.01959 215.63); /* #4f5e62 */
  --accent: oklch(0.4935 0.08236 208.36); /* #0b6e7a */
  --accent-foreground: oklch(0.9773 0.02132 207.59); /* #e8fcff */
  --accent-text: oklch(0.4935 0.08236 208.36); /* #0b6e7a */
  --success: oklch(0.4689 0.10756 151.36); /* #1f6b3a */
  --warn: oklch(0.5078 0.10800 73.30); /* #8a5a00 */
  --danger: oklch(0.5003 0.18205 29.51); /* #b42318 */
}

.dark {
  /* Cian terminal — oscuro */
  --bg: oklch(0.1677 0.01026 220.22); /* #0a1012 */
  --surface: oklch(0.2107 0.01244 214.70); /* #121a1c */
  --border: oklch(0.3361 0.02196 214.78); /* #2a3a3e */
  --text: oklch(0.9505 0.01201 209.80); /* #e6f1f3 */
  --muted: oklch(0.6907 0.02626 216.00); /* #8aa0a6 */
  --accent: oklch(0.8430 0.11551 205.67); /* #5ee1f0 */
  --accent-foreground: oklch(0.2257 0.02984 202.74); /* #082022 */
  --accent-text: oklch(0.8430 0.11551 205.67); /* #5ee1f0 */
  --success: oklch(0.8138 0.12756 152.72); /* #7dda9a */
  --warn: oklch(0.8060 0.13714 85.03); /* #e8b849 */
  --danger: oklch(0.7594 0.14351 26.08); /* #ff8a80 */
}
```


---

## Grafito y oro

`grafito-oro` — Premium contenido, un metal, nada de neon

**Mejor para:** fintech, lujo discreto, consultoras, SaaS senior.  
**Evitá en:** productos infantiles, marcas de dopamina, devtool ‘hacker’.  
**Estilos:** [`saas-oscuro-premium`](../estilos/saas-oscuro-premium.md), [`expresivo-minimo`](../estilos/expresivo-minimo.md), [`minimalismo-monocromo`](../estilos/minimalismo-monocromo.md), [`ui-casi-invisible`](../estilos/ui-casi-invisible.md).

El oro es un acento de baja croma, no un degradé dorado. En claro se oscurece para contrastar.

### Claro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#f7f4ee` | `oklch(0.9678 0.00859 84.57)` |
| Superficie | `#efebe3` | `oklch(0.9410 0.01152 84.58)` |
| Borde | `#d8d1c4` | `oklch(0.8627 0.01928 83.06)` |
| Texto | `#161410` | `oklch(0.1921 0.00846 84.58)` |
| Muted | `#5e584c` | `oklch(0.4624 0.02036 84.58)` |
| Acento (sólido) | `#8a6914` | `oklch(0.5398 0.10377 85.15)` |
| Acento foreground | `#fff8e1` | `oklch(0.9785 0.03100 92.94)` |
| Acento texto/link | `#8a6914` | `oklch(0.5398 0.10377 85.15)` |
| Success | `#1f6b3a` | `oklch(0.4689 0.10756 151.36)` |
| Warn | `#8a5a00` | `oklch(0.5078 0.10800 73.30)` |
| Danger | `#b42318` | `oklch(0.5003 0.18205 29.51)` |

### Oscuro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#0e0d0b` | `oklch(0.1595 0.00446 84.59)` |
| Superficie | `#181714` | `oklch(0.2046 0.00602 91.64)` |
| Borde | `#322f28` | `oklch(0.3059 0.01292 87.57)` |
| Texto | `#f3eee4` | `oklch(0.9503 0.01435 84.58)` |
| Muted | `#a59c8c` | `oklch(0.6959 0.02509 82.09)` |
| Acento (sólido) | `#e4c572` | `oklch(0.8325 0.10851 89.50)` |
| Acento foreground | `#1a160c` | `oklch(0.2017 0.01955 88.67)` |
| Acento texto/link | `#e4c572` | `oklch(0.8325 0.10851 89.50)` |
| Success | `#7dda9a` | `oklch(0.8138 0.12756 152.72)` |
| Warn | `#e8b849` | `oklch(0.8060 0.13714 85.03)` |
| Danger | `#ff8a80` | `oklch(0.7594 0.14351 26.08)` |

### Contraste

**Claro:** texto sobre fondo WCAG 16.76:1, APCA Lc 98.6 (oscuro-sobre-claro); texto sobre superficie WCAG 15.47:1, APCA Lc 93.4 (oscuro-sobre-claro); accent-foreground sobre acento WCAG 4.81:1, APCA Lc -75.8 (claro-sobre-oscuro). Muted sobre fondo WCAG 6.43:1, APCA Lc 78.0 (oscuro-sobre-claro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 4.65:1, APCA Lc 68.6 (oscuro-sobre-claro)). `accent-text` está igualado o derivado para ese rol.

**Oscuro:** texto sobre fondo WCAG 16.8:1, APCA Lc -96.7 (claro-sobre-oscuro); texto sobre superficie WCAG 15.5:1, APCA Lc -96.0 (claro-sobre-oscuro); accent-foreground sobre acento WCAG 10.76:1, APCA Lc 73.0 (oscuro-sobre-claro). Muted sobre fondo WCAG 7.15:1, APCA Lc -49.0 (claro-sobre-oscuro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 11.59:1, APCA Lc -73.0 (claro-sobre-oscuro)). `accent-text` está igualado o derivado para ese rol.

### Tokens CSS

```css
:root {
  /* Grafito y oro — claro */
  --bg: oklch(0.9678 0.00859 84.57); /* #f7f4ee */
  --surface: oklch(0.9410 0.01152 84.58); /* #efebe3 */
  --border: oklch(0.8627 0.01928 83.06); /* #d8d1c4 */
  --text: oklch(0.1921 0.00846 84.58); /* #161410 */
  --muted: oklch(0.4624 0.02036 84.58); /* #5e584c */
  --accent: oklch(0.5398 0.10377 85.15); /* #8a6914 */
  --accent-foreground: oklch(0.9785 0.03100 92.94); /* #fff8e1 */
  --accent-text: oklch(0.5398 0.10377 85.15); /* #8a6914 */
  --success: oklch(0.4689 0.10756 151.36); /* #1f6b3a */
  --warn: oklch(0.5078 0.10800 73.30); /* #8a5a00 */
  --danger: oklch(0.5003 0.18205 29.51); /* #b42318 */
}

.dark {
  /* Grafito y oro — oscuro */
  --bg: oklch(0.1595 0.00446 84.59); /* #0e0d0b */
  --surface: oklch(0.2046 0.00602 91.64); /* #181714 */
  --border: oklch(0.3059 0.01292 87.57); /* #322f28 */
  --text: oklch(0.9503 0.01435 84.58); /* #f3eee4 */
  --muted: oklch(0.6959 0.02509 82.09); /* #a59c8c */
  --accent: oklch(0.8325 0.10851 89.50); /* #e4c572 */
  --accent-foreground: oklch(0.2017 0.01955 88.67); /* #1a160c */
  --accent-text: oklch(0.8325 0.10851 89.50); /* #e4c572 */
  --success: oklch(0.8138 0.12756 152.72); /* #7dda9a */
  --warn: oklch(0.8060 0.13714 85.03); /* #e8b849 */
  --danger: oklch(0.7594 0.14351 26.08); /* #ff8a80 */
}
```


---

## Pizarra y señal

`pizarra-senal` — Catálogo técnico, naranja de señal, acero

**Mejor para:** hardware, industria, logística, docs de producto físico.  
**Evitá en:** belleza, editorial romántica, fintech ‘soft’.  
**Estilos:** [`catalogo-tecnico`](../estilos/catalogo-tecnico.md), [`bento-grids`](../estilos/bento-grids.md), [`saas-oscuro-premium`](../estilos/saas-oscuro-premium.md), [`suizo-internacional`](../estilos/suizo-internacional.md).

El naranja es de señal (un dato, un CTA), no un fondo. El resto es acero.

### Claro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#f5f5f3` | `oklch(0.9696 0.00265 106.45)` |
| Superficie | `#ebebe8` | `oklch(0.9392 0.00400 106.48)` |
| Borde | `#d0d0cb` | `oklch(0.8562 0.00682 106.54)` |
| Texto | `#1a1a17` | `oklch(0.2166 0.00573 106.87)` |
| Muted | `#5b5b55` | `oklch(0.4693 0.00947 106.76)` |
| Acento (sólido) | `#c24e00` | `oklch(0.5695 0.16442 44.44)` |
| Acento foreground | `#ffffff` | `oklch(1.0000 0.00000 0.00)` |
| Acento texto/link | `#b94a00` | `oklch(0.5497 0.15872 44.43)` |
| Success | `#1f6b3a` | `oklch(0.4689 0.10756 151.36)` |
| Warn | `#8a5a00` | `oklch(0.5078 0.10800 73.30)` |
| Danger | `#b42318` | `oklch(0.5003 0.18205 29.51)` |

### Oscuro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#10110f` | `oklch(0.1757 0.00435 128.74)` |
| Superficie | `#1a1b18` | `oklch(0.2199 0.00592 121.93)` |
| Borde | `#33342f` | `oklch(0.3223 0.00876 116.08)` |
| Texto | `#eeede8` | `oklch(0.9455 0.00675 97.35)` |
| Muted | `#a3a39a` | `oklch(0.7128 0.01280 106.72)` |
| Acento (sólido) | `#ba5700` | `oklch(0.5702 0.14972 50.48)` |
| Acento foreground | `#ffffff` | `oklch(1.0000 0.00000 0.00)` |
| Acento texto/link | `#ffa067` | `oklch(0.7908 0.13460 50.76)` |
| Success | `#7dda9a` | `oklch(0.8138 0.12756 152.72)` |
| Warn | `#e8b849` | `oklch(0.8060 0.13714 85.03)` |
| Danger | `#ff8a80` | `oklch(0.7594 0.14351 26.08)` |

### Contraste

**Claro:** texto sobre fondo WCAG 15.98:1, APCA Lc 98.2 (oscuro-sobre-claro); texto sobre superficie WCAG 14.6:1, APCA Lc 92.3 (oscuro-sobre-claro); accent-foreground sobre acento WCAG 4.79:1, APCA Lc -77.8 (claro-sobre-oscuro). Muted sobre fondo WCAG 6.26:1, APCA Lc 77.6 (oscuro-sobre-claro): sirve para cuerpo secundario. El acento sólido no llega a 4.5:1 como texto sobre el fondo (4.39:1). Para botones usá `accent` + `accent-foreground`. Para links usá `accent-text` (4.76:1, Lc 68.8).

**Oscuro:** texto sobre fondo WCAG 16.15:1, APCA Lc -95.5 (claro-sobre-oscuro); texto sobre superficie WCAG 14.76:1, APCA Lc -94.6 (claro-sobre-oscuro); accent-foreground sobre acento WCAG 4.72:1, APCA Lc -77.5 (claro-sobre-oscuro). Muted sobre fondo WCAG 7.45:1, APCA Lc -51.6 (claro-sobre-oscuro): sirve para cuerpo secundario. El acento sólido no llega a 4.5:1 como texto sobre el fondo (4.01:1). Para botones usá `accent` + `accent-foreground`. Para links usá `accent-text` (9.45:1, Lc -63.3).

### Tokens CSS

```css
:root {
  /* Pizarra y señal — claro */
  --bg: oklch(0.9696 0.00265 106.45); /* #f5f5f3 */
  --surface: oklch(0.9392 0.00400 106.48); /* #ebebe8 */
  --border: oklch(0.8562 0.00682 106.54); /* #d0d0cb */
  --text: oklch(0.2166 0.00573 106.87); /* #1a1a17 */
  --muted: oklch(0.4693 0.00947 106.76); /* #5b5b55 */
  --accent: oklch(0.5695 0.16442 44.44); /* #c24e00 */
  --accent-foreground: oklch(1.0000 0.00000 0.00); /* #ffffff */
  --accent-text: oklch(0.5497 0.15872 44.43); /* #b94a00 */
  --success: oklch(0.4689 0.10756 151.36); /* #1f6b3a */
  --warn: oklch(0.5078 0.10800 73.30); /* #8a5a00 */
  --danger: oklch(0.5003 0.18205 29.51); /* #b42318 */
}

.dark {
  /* Pizarra y señal — oscuro */
  --bg: oklch(0.1757 0.00435 128.74); /* #10110f */
  --surface: oklch(0.2199 0.00592 121.93); /* #1a1b18 */
  --border: oklch(0.3223 0.00876 116.08); /* #33342f */
  --text: oklch(0.9455 0.00675 97.35); /* #eeede8 */
  --muted: oklch(0.7128 0.01280 106.72); /* #a3a39a */
  --accent: oklch(0.5702 0.14972 50.48); /* #ba5700 */
  --accent-foreground: oklch(1.0000 0.00000 0.00); /* #ffffff */
  --accent-text: oklch(0.7908 0.13460 50.76); /* #ffa067 */
  --success: oklch(0.8138 0.12756 152.72); /* #7dda9a */
  --warn: oklch(0.8060 0.13714 85.03); /* #e8b849 */
  --danger: oklch(0.7594 0.14351 26.08); /* #ff8a80 */
}
```


---

## Carbón y menta

`carbon-menta` — UI casi invisible, un menta para estados activos

**Mejor para:** editores, productos de escritura, herramientas quietas.  
**Evitá en:** landings que necesitan gritar, marcas de dopamina.  
**Estilos:** [`ui-casi-invisible`](../estilos/ui-casi-invisible.md), [`saas-oscuro-premium`](../estilos/saas-oscuro-premium.md), [`estilo-linear`](../estilos/estilo-linear.md), [`minimalismo-monocromo`](../estilos/minimalismo-monocromo.md), [`denso-de-datos`](../estilos/denso-de-datos.md).

Menta desaturada, no el emerald-400 de Tailwind en todo. El borde hace más trabajo que el color.

### Claro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#f4f6f5` | `oklch(0.9713 0.00250 165.08)` |
| Superficie | `#eaeeec` | `oklch(0.9455 0.00502 165.00)` |
| Borde | `#cdd5d2` | `oklch(0.8660 0.00959 171.76)` |
| Texto | `#141918` | `oklch(0.2078 0.00783 182.12)` |
| Muted | `#55605d` | `oklch(0.4786 0.01445 177.50)` |
| Acento (sólido) | `#0b6b5b` | `oklch(0.4734 0.08472 177.22)` |
| Acento foreground | `#e8fff8` | `oklch(0.9813 0.02565 175.60)` |
| Acento texto/link | `#0b6b5b` | `oklch(0.4734 0.08472 177.22)` |
| Success | `#1f6b3a` | `oklch(0.4689 0.10756 151.36)` |
| Warn | `#8a5a00` | `oklch(0.5078 0.10800 73.30)` |
| Danger | `#b42318` | `oklch(0.5003 0.18205 29.51)` |

### Oscuro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#0b0f0e` | `oklch(0.1636 0.00675 178.64)` |
| Superficie | `#141918` | `oklch(0.2078 0.00783 182.12)` |
| Borde | `#2a3331` | `oklch(0.3119 0.01279 180.51)` |
| Texto | `#e7efec` | `oklch(0.9452 0.00939 171.79)` |
| Muted | `#8fa09b` | `oklch(0.6908 0.02056 176.14)` |
| Acento (sólido) | `#5ee0c5` | `oklch(0.8268 0.12140 177.17)` |
| Acento foreground | `#06201a` | `oklch(0.2212 0.03424 175.34)` |
| Acento texto/link | `#5ee0c5` | `oklch(0.8268 0.12140 177.17)` |
| Success | `#7dda9a` | `oklch(0.8138 0.12756 152.72)` |
| Warn | `#e8b849` | `oklch(0.8060 0.13714 85.03)` |
| Danger | `#ff8a80` | `oklch(0.7594 0.14351 26.08)` |

### Contraste

**Claro:** texto sobre fondo WCAG 16.37:1, APCA Lc 98.9 (oscuro-sobre-claro); texto sobre superficie WCAG 15.18:1, APCA Lc 93.9 (oscuro-sobre-claro); accent-foreground sobre acento WCAG 6.15:1, APCA Lc -83.2 (claro-sobre-oscuro). Muted sobre fondo WCAG 6.01:1, APCA Lc 76.7 (oscuro-sobre-claro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 5.92:1, APCA Lc 75.8 (oscuro-sobre-claro)). `accent-text` está igualado o derivado para ese rol.

**Oscuro:** texto sobre fondo WCAG 16.49:1, APCA Lc -95.9 (claro-sobre-oscuro); texto sobre superficie WCAG 15.19:1, APCA Lc -95.1 (claro-sobre-oscuro); accent-foreground sobre acento WCAG 10.53:1, APCA Lc 74.1 (oscuro-sobre-claro). Muted sobre fondo WCAG 7.04:1, APCA Lc -48.5 (claro-sobre-oscuro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 11.89:1, APCA Lc -75.1 (claro-sobre-oscuro)). `accent-text` está igualado o derivado para ese rol.

### Tokens CSS

```css
:root {
  /* Carbón y menta — claro */
  --bg: oklch(0.9713 0.00250 165.08); /* #f4f6f5 */
  --surface: oklch(0.9455 0.00502 165.00); /* #eaeeec */
  --border: oklch(0.8660 0.00959 171.76); /* #cdd5d2 */
  --text: oklch(0.2078 0.00783 182.12); /* #141918 */
  --muted: oklch(0.4786 0.01445 177.50); /* #55605d */
  --accent: oklch(0.4734 0.08472 177.22); /* #0b6b5b */
  --accent-foreground: oklch(0.9813 0.02565 175.60); /* #e8fff8 */
  --accent-text: oklch(0.4734 0.08472 177.22); /* #0b6b5b */
  --success: oklch(0.4689 0.10756 151.36); /* #1f6b3a */
  --warn: oklch(0.5078 0.10800 73.30); /* #8a5a00 */
  --danger: oklch(0.5003 0.18205 29.51); /* #b42318 */
}

.dark {
  /* Carbón y menta — oscuro */
  --bg: oklch(0.1636 0.00675 178.64); /* #0b0f0e */
  --surface: oklch(0.2078 0.00783 182.12); /* #141918 */
  --border: oklch(0.3119 0.01279 180.51); /* #2a3331 */
  --text: oklch(0.9452 0.00939 171.79); /* #e7efec */
  --muted: oklch(0.6908 0.02056 176.14); /* #8fa09b */
  --accent: oklch(0.8268 0.12140 177.17); /* #5ee0c5 */
  --accent-foreground: oklch(0.2212 0.03424 175.34); /* #06201a */
  --accent-text: oklch(0.8268 0.12140 177.17); /* #5ee0c5 */
  --success: oklch(0.8138 0.12756 152.72); /* #7dda9a */
  --warn: oklch(0.8060 0.13714 85.03); /* #e8b849 */
  --danger: oklch(0.7594 0.14351 26.08); /* #ff8a80 */
}
```

---

## Océano profundo

`oceano-profundo` — Azul marino, verde azulado y espuma; frío y tranquilo

**Mejor para:** logística y puertos, salud digital, SaaS B2B, turismo de costa.  
**Evitá en:** comida, moda, marcas infantiles.  
**Estilos:** [`saas-oscuro-premium`](../estilos/saas-oscuro-premium.md), [`ui-casi-invisible`](../estilos/ui-casi-invisible.md), [`denso-de-datos`](../estilos/denso-de-datos.md), [`suizo-internacional`](../estilos/suizo-internacional.md).

Adaptada del tema 'Ocean Depths' de theme-factory (Anthropic, Apache 2.0): marino #1a2332, teal #2d8b8b, espuma #a8dadc. En claro el teal se oscurece para llegar a 4.5:1 con texto blanco; en oscuro el fondo es el marino del tema y el acento la espuma.

### Claro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#f3f7f8` | `oklch(0.9734 0.00447 214.33)` |
| Superficie | `#e6eef0` | `oklch(0.9437 0.00897 214.34)` |
| Borde | `#c8d6da` | `oklch(0.8667 0.01615 216.69)` |
| Texto | `#111a24` | `oklch(0.2140 0.02389 251.57)` |
| Muted | `#4b5b66` | `oklch(0.4618 0.02671 238.20)` |
| Acento (sólido) | `#1f6f70` | `oklch(0.4958 0.07437 196.25)` |
| Acento foreground | `#f1faf9` | `oklch(0.9781 0.00959 189.07)` |
| Acento texto/link | `#1f6f70` | `oklch(0.4958 0.07437 196.25)` |
| Success | `#1f6b3a` | `oklch(0.4689 0.10756 151.36)` |
| Warn | `#8a5a00` | `oklch(0.5078 0.10800 73.30)` |
| Danger | `#b42318` | `oklch(0.5003 0.18205 29.51)` |

### Oscuro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#1a2332` | `oklch(0.2549 0.03134 260.42)` |
| Superficie | `#222d3e` | `oklch(0.2950 0.03470 258.93)` |
| Borde | `#36445a` | `oklch(0.3840 0.04193 259.29)` |
| Texto | `#eef5f6` | `oklch(0.9652 0.00757 207.14)` |
| Muted | `#afbecb` | `oklch(0.7940 0.02480 244.21)` |
| Acento (sólido) | `#a8dadc` | `oklch(0.8542 0.05170 199.29)` |
| Acento foreground | `#1a2332` | `oklch(0.2549 0.03134 260.42)` |
| Acento texto/link | `#a8dadc` | `oklch(0.8542 0.05170 199.29)` |
| Success | `#7dda9a` | `oklch(0.8138 0.12756 152.72)` |
| Warn | `#e8b849` | `oklch(0.8060 0.13714 85.03)` |
| Danger | `#ff8a80` | `oklch(0.7594 0.14351 26.08)` |

### Contraste

**Claro:** texto sobre fondo WCAG 16.27:1, APCA Lc 99.1 (oscuro-sobre-claro); texto sobre superficie WCAG 14.91:1, APCA Lc 93.4 (oscuro-sobre-claro); accent-foreground sobre acento WCAG 5.55:1, APCA Lc -79.8 (claro-sobre-oscuro). Muted sobre fondo WCAG 6.52:1, APCA Lc 79.1 (oscuro-sobre-claro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 5.46:1, APCA Lc 73.9 (oscuro-sobre-claro)). `accent-text` está igualado o derivado para ese rol.

**Oscuro:** texto sobre fondo WCAG 14.30:1, APCA Lc -97.8 (claro-sobre-oscuro); texto sobre superficie WCAG 12.58:1, APCA Lc -96.0 (claro-sobre-oscuro); accent-foreground sobre acento WCAG 10.32:1, APCA Lc 75.9 (oscuro-sobre-claro). Muted sobre fondo WCAG 8.31:1, APCA Lc -63.7 (claro-sobre-oscuro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 10.32:1, APCA Lc -76.1 (claro-sobre-oscuro)). `accent-text` está igualado o derivado para ese rol.

### Tokens CSS

```css
:root {
  /* Océano profundo — claro */
  --bg: oklch(0.9734 0.00447 214.33); /* #f3f7f8 */
  --surface: oklch(0.9437 0.00897 214.34); /* #e6eef0 */
  --border: oklch(0.8667 0.01615 216.69); /* #c8d6da */
  --text: oklch(0.2140 0.02389 251.57); /* #111a24 */
  --muted: oklch(0.4618 0.02671 238.20); /* #4b5b66 */
  --accent: oklch(0.4958 0.07437 196.25); /* #1f6f70 */
  --accent-foreground: oklch(0.9781 0.00959 189.07); /* #f1faf9 */
  --accent-text: oklch(0.4958 0.07437 196.25); /* #1f6f70 */
  --success: oklch(0.4689 0.10756 151.36); /* #1f6b3a */
  --warn: oklch(0.5078 0.10800 73.30); /* #8a5a00 */
  --danger: oklch(0.5003 0.18205 29.51); /* #b42318 */
}
.dark {
  /* Océano profundo — oscuro */
  --bg: oklch(0.2549 0.03134 260.42); /* #1a2332 */
  --surface: oklch(0.2950 0.03470 258.93); /* #222d3e */
  --border: oklch(0.3840 0.04193 259.29); /* #36445a */
  --text: oklch(0.9652 0.00757 207.14); /* #eef5f6 */
  --muted: oklch(0.7940 0.02480 244.21); /* #afbecb */
  --accent: oklch(0.8542 0.05170 199.29); /* #a8dadc */
  --accent-foreground: oklch(0.2549 0.03134 260.42); /* #1a2332 */
  --accent-text: oklch(0.8542 0.05170 199.29); /* #a8dadc */
  --success: oklch(0.8138 0.12756 152.72); /* #7dda9a */
  --warn: oklch(0.8060 0.13714 85.03); /* #e8b849 */
  --danger: oklch(0.7594 0.14351 26.08); /* #ff8a80 */
}
```

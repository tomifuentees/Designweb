# Paletas culturales y de nicho

Voces más específicas: sumi y sello, hielo nórdico, vino de noche, bosque, arcilla, durazno, acero de seguridad, arena de PyME, teja y mar, niebla para un vidrio puntual, cera para claymorfismo. Cada una mapea a uno o dos estilos del [catálogo](../estilos/README.md). Varias son contrapesos: no las conviertas en el default de todos los proyectos.

`cera-suave` usa un violeta a propósito, porque el claymorfismo vive en pasteles. No es el degradé índigo de hero: es un relleno sólido con contraste chequeado, y está documentada como nicho, no como tendencia 2026. `niebla-vidrio` es para un panel sobre una foto, no para un sitio entero de glass.


Hay **12 paletas** (la última, rosa del desierto, adaptada en noviembre de 2026 de la skill theme-factory de Anthropic) en este grupo. Los valores salen de [`paletas.json`](./paletas.json). Los links de estilo apuntan a las fichas de [`../estilos/`](../estilos/README.md).


---

## Sumi y sello

`japon-sumi` — Tinta sumi, papel, un sello vermellón

**Mejor para:** cultura, comida, estudios, marcas contenidas.  
**Evitá en:** usar ‘zen’ como cliché, tipografía ‘orientalizante’ de costume.  
**Estilos:** [`japones-inspirado`](../estilos/japones-inspirado.md), [`minimalismo-monocromo`](../estilos/minimalismo-monocromo.md), [`editorial-revista`](../estilos/editorial-revista.md), [`expresivo-minimo`](../estilos/expresivo-minimo.md).

El vermellón es un sello, aparece una vez (un logotipo, un número, un CTA). El resto es tinta y papel. Mucho ma.

### Claro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#f4f1ea` | `oklch(0.9585 0.00984 87.47)` |
| Superficie | `#eae6dc` | `oklch(0.9253 0.01406 88.69)` |
| Borde | `#d0cbc0` | `oklch(0.8431 0.01603 86.43)` |
| Texto | `#161412` | `oklch(0.1928 0.00512 67.52)` |
| Muted | `#5a564e` | `oklch(0.4544 0.01372 84.59)` |
| Acento (sólido) | `#b31b1b` | `oklch(0.4934 0.18571 27.49)` |
| Acento foreground | `#fff6f2` | `oklch(0.9790 0.01107 45.72)` |
| Acento texto/link | `#b31b1b` | `oklch(0.4934 0.18571 27.49)` |
| Success | `#1f6b3a` | `oklch(0.4689 0.10756 151.36)` |
| Warn | `#8a5a00` | `oklch(0.5078 0.10800 73.30)` |
| Danger | `#8e1010` | `oklch(0.4141 0.15868 27.82)` |

### Oscuro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#12110f` | `oklch(0.1780 0.00435 84.59)` |
| Superficie | `#1c1a17` | `oklch(0.2189 0.00653 78.18)` |
| Borde | `#33302b` | `oklch(0.3106 0.00973 80.66)` |
| Texto | `#f0ebe2` | `oklch(0.9415 0.01317 82.40)` |
| Muted | `#a8a398` | `oklch(0.7165 0.01667 86.44)` |
| Acento (sólido) | `#d03a2c` | `oklch(0.5720 0.18911 29.48)` |
| Acento foreground | `#ffffff` | `oklch(1.0000 0.00000 0.00)` |
| Acento texto/link | `#ff9d8d` | `oklch(0.7923 0.12024 29.96)` |
| Success | `#7dda9a` | `oklch(0.8138 0.12756 152.72)` |
| Warn | `#e8b849` | `oklch(0.8060 0.13714 85.03)` |
| Danger | `#ff8a80` | `oklch(0.7594 0.14351 26.08)` |

### Contraste

**Claro:** texto sobre fondo WCAG 16.29:1, APCA Lc 96.8 (oscuro-sobre-claro); texto sobre superficie WCAG 14.74:1, APCA Lc 90.4 (oscuro-sobre-claro); accent-foreground sobre acento WCAG 6.38:1, APCA Lc -81.8 (claro-sobre-oscuro). Muted sobre fondo WCAG 6.47:1, APCA Lc 77.1 (oscuro-sobre-claro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 6.03:1, APCA Lc 73.3 (oscuro-sobre-claro)). `accent-text` está igualado o derivado para ese rol.

**Oscuro:** texto sobre fondo WCAG 15.89:1, APCA Lc -94.6 (claro-sobre-oscuro); texto sobre superficie WCAG 14.62:1, APCA Lc -93.8 (claro-sobre-oscuro); accent-foreground sobre acento WCAG 4.86:1, APCA Lc -77.8 (claro-sobre-oscuro). Muted sobre fondo WCAG 7.51:1, APCA Lc -52.1 (claro-sobre-oscuro): sirve para cuerpo secundario. El acento sólido no llega a 4.5:1 como texto sobre el fondo (3.89:1). Para botones usá `accent` + `accent-foreground`. Para links usá `accent-text` (9.4:1, Lc -63.2).

### Tokens CSS

```css
:root {
  /* Sumi y sello — claro */
  --bg: oklch(0.9585 0.00984 87.47); /* #f4f1ea */
  --surface: oklch(0.9253 0.01406 88.69); /* #eae6dc */
  --border: oklch(0.8431 0.01603 86.43); /* #d0cbc0 */
  --text: oklch(0.1928 0.00512 67.52); /* #161412 */
  --muted: oklch(0.4544 0.01372 84.59); /* #5a564e */
  --accent: oklch(0.4934 0.18571 27.49); /* #b31b1b */
  --accent-foreground: oklch(0.9790 0.01107 45.72); /* #fff6f2 */
  --accent-text: oklch(0.4934 0.18571 27.49); /* #b31b1b */
  --success: oklch(0.4689 0.10756 151.36); /* #1f6b3a */
  --warn: oklch(0.5078 0.10800 73.30); /* #8a5a00 */
  --danger: oklch(0.4141 0.15868 27.82); /* #8e1010 */
}

.dark {
  /* Sumi y sello — oscuro */
  --bg: oklch(0.1780 0.00435 84.59); /* #12110f */
  --surface: oklch(0.2189 0.00653 78.18); /* #1c1a17 */
  --border: oklch(0.3106 0.00973 80.66); /* #33302b */
  --text: oklch(0.9415 0.01317 82.40); /* #f0ebe2 */
  --muted: oklch(0.7165 0.01667 86.44); /* #a8a398 */
  --accent: oklch(0.5720 0.18911 29.48); /* #d03a2c */
  --accent-foreground: oklch(1.0000 0.00000 0.00); /* #ffffff */
  --accent-text: oklch(0.7923 0.12024 29.96); /* #ff9d8d */
  --success: oklch(0.8138 0.12756 152.72); /* #7dda9a */
  --warn: oklch(0.8060 0.13714 85.03); /* #e8b849 */
  --danger: oklch(0.7594 0.14351 26.08); /* #ff8a80 */
}
```


---

## Nórdico hielo

`nordico-hielo` — Frío claro, pino, un oro pálido, no sky-500

**Mejor para:** bienestar, arquitectura, producto sereno, marcas nórdicas.  
**Evitá en:** tropicales, dopamina, Y2K.  
**Estilos:** [`minimalismo-monocromo`](../estilos/minimalismo-monocromo.md), [`organico-terroso`](../estilos/organico-terroso.md), [`ui-casi-invisible`](../estilos/ui-casi-invisible.md), [`expresivo-minimo`](../estilos/expresivo-minimo.md).

El acento es un pino oscuro, no un azul de plantilla. El fondo tira a un blanco azulado muy leve.

### Claro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#f3f5f4` | `oklch(0.9684 0.00250 165.08)` |
| Superficie | `#e6ebe8` | `oklch(0.9354 0.00666 160.07)` |
| Borde | `#cdd5d1` | `oklch(0.8657 0.01024 164.83)` |
| Texto | `#14201c` | `oklch(0.2307 0.01865 171.95)` |
| Muted | `#4e5c58` | `oklch(0.4615 0.01851 176.35)` |
| Acento (sólido) | `#1b4f40` | `oklch(0.3880 0.06113 170.94)` |
| Acento foreground | `#eaf6f1` | `oklch(0.9628 0.01428 169.25)` |
| Acento texto/link | `#1b4f40` | `oklch(0.3880 0.06113 170.94)` |
| Success | `#1f6b3a` | `oklch(0.4689 0.10756 151.36)` |
| Warn | `#8a5a00` | `oklch(0.5078 0.10800 73.30)` |
| Danger | `#b42318` | `oklch(0.5003 0.18205 29.51)` |

### Oscuro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#0e1312` | `oklch(0.1810 0.00805 181.92)` |
| Superficie | `#161c1a` | `oklch(0.2195 0.00974 173.23)` |
| Borde | `#2c3633` | `oklch(0.3225 0.01450 175.28)` |
| Texto | `#e6eeea` | `oklch(0.9419 0.01003 164.86)` |
| Muted | `#8fa09a` | `oklch(0.6905 0.02111 172.48)` |
| Acento (sólido) | `#8fcbb3` | `oklch(0.7943 0.07071 167.75)` |
| Acento foreground | `#0c1814` | `oklch(0.1961 0.01909 171.30)` |
| Acento texto/link | `#8fcbb3` | `oklch(0.7943 0.07071 167.75)` |
| Success | `#7dda9a` | `oklch(0.8138 0.12756 152.72)` |
| Warn | `#e8b849` | `oklch(0.8060 0.13714 85.03)` |
| Danger | `#ff8a80` | `oklch(0.7594 0.14351 26.08)` |

### Contraste

**Claro:** texto sobre fondo WCAG 15.3:1, APCA Lc 97.4 (oscuro-sobre-claro); texto sobre superficie WCAG 13.9:1, APCA Lc 91.1 (oscuro-sobre-claro); accent-foreground sobre acento WCAG 8.46:1, APCA Lc -88.0 (claro-sobre-oscuro). Muted sobre fondo WCAG 6.4:1, APCA Lc 78.0 (oscuro-sobre-claro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 8.57:1, APCA Lc 85.2 (oscuro-sobre-claro)). `accent-text` está igualado o derivado para ese rol.

**Oscuro:** texto sobre fondo WCAG 15.87:1, APCA Lc -94.9 (claro-sobre-oscuro); texto sobre superficie WCAG 14.63:1, APCA Lc -94.1 (claro-sobre-oscuro); accent-foreground sobre acento WCAG 9.82:1, APCA Lc 68.0 (oscuro-sobre-claro). Muted sobre fondo WCAG 6.84:1, APCA Lc -48.3 (claro-sobre-oscuro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 10.14:1, APCA Lc -67.3 (claro-sobre-oscuro)). `accent-text` está igualado o derivado para ese rol.

### Tokens CSS

```css
:root {
  /* Nórdico hielo — claro */
  --bg: oklch(0.9684 0.00250 165.08); /* #f3f5f4 */
  --surface: oklch(0.9354 0.00666 160.07); /* #e6ebe8 */
  --border: oklch(0.8657 0.01024 164.83); /* #cdd5d1 */
  --text: oklch(0.2307 0.01865 171.95); /* #14201c */
  --muted: oklch(0.4615 0.01851 176.35); /* #4e5c58 */
  --accent: oklch(0.3880 0.06113 170.94); /* #1b4f40 */
  --accent-foreground: oklch(0.9628 0.01428 169.25); /* #eaf6f1 */
  --accent-text: oklch(0.3880 0.06113 170.94); /* #1b4f40 */
  --success: oklch(0.4689 0.10756 151.36); /* #1f6b3a */
  --warn: oklch(0.5078 0.10800 73.30); /* #8a5a00 */
  --danger: oklch(0.5003 0.18205 29.51); /* #b42318 */
}

.dark {
  /* Nórdico hielo — oscuro */
  --bg: oklch(0.1810 0.00805 181.92); /* #0e1312 */
  --surface: oklch(0.2195 0.00974 173.23); /* #161c1a */
  --border: oklch(0.3225 0.01450 175.28); /* #2c3633 */
  --text: oklch(0.9419 0.01003 164.86); /* #e6eeea */
  --muted: oklch(0.6905 0.02111 172.48); /* #8fa09a */
  --accent: oklch(0.7943 0.07071 167.75); /* #8fcbb3 */
  --accent-foreground: oklch(0.1961 0.01909 171.30); /* #0c1814 */
  --accent-text: oklch(0.7943 0.07071 167.75); /* #8fcbb3 */
  --success: oklch(0.8138 0.12756 152.72); /* #7dda9a */
  --warn: oklch(0.8060 0.13714 85.03); /* #e8b849 */
  --danger: oklch(0.7594 0.14351 26.08); /* #ff8a80 */
}
```


---

## Vino de noche

`vino-noche` — Editorial oscura, vino, crema, lujo de tinta

**Mejor para:** vino, moda, editorial de lujo, cultura nocturna.  
**Evitá en:** SaaS diurno, educación infantil, look clínico.  
**Estilos:** [`editorial-revista`](../estilos/editorial-revista.md), [`saas-oscuro-premium`](../estilos/saas-oscuro-premium.md), [`realismo-tactil`](../estilos/realismo-tactil.md), [`scrollytelling`](../estilos/scrollytelling.md).

No es el púrpura de plantilla: es un vino, más rojo que azul, baja luminosidad. El crema es el papel sobre la noche.

### Claro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#f6f0e8` | `oklch(0.9576 0.01246 75.37)` |
| Superficie | `#ede4d6` | `oklch(0.9222 0.02113 79.09)` |
| Borde | `#d6c8b4` | `oklch(0.8389 0.03139 76.93)` |
| Texto | `#1a1010` | `oklch(0.1865 0.01698 18.80)` |
| Muted | `#64544c` | `oklch(0.4594 0.02484 48.16)` |
| Acento (sólido) | `#6e1230` | `oklch(0.3572 0.12583 7.70)` |
| Acento foreground | `#fff0f2` | `oklch(0.9675 0.01640 8.16)` |
| Acento texto/link | `#6e1230` | `oklch(0.3572 0.12583 7.70)` |
| Success | `#1f6b3a` | `oklch(0.4689 0.10756 151.36)` |
| Warn | `#8a5a00` | `oklch(0.5078 0.10800 73.30)` |
| Danger | `#8e1020` | `oklch(0.4158 0.15719 22.42)` |

### Oscuro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#140c10` | `oklch(0.1670 0.01579 347.47)` |
| Superficie | `#1e1218` | `oklch(0.2008 0.02263 347.90)` |
| Borde | `#3a2230` | `oklch(0.2881 0.04296 344.24)` |
| Texto | `#f3e8dc` | `oklch(0.9364 0.02002 69.99)` |
| Muted | `#c0a8b0` | `oklch(0.7548 0.02989 355.70)` |
| Acento (sólido) | `#e8c9a8` | `oklch(0.8539 0.05629 68.71)` |
| Acento foreground | `#1a0c10` | `oklch(0.1765 0.02517 1.49)` |
| Acento texto/link | `#e8c9a8` | `oklch(0.8539 0.05629 68.71)` |
| Success | `#7dda9a` | `oklch(0.8138 0.12756 152.72)` |
| Warn | `#e8b849` | `oklch(0.8060 0.13714 85.03)` |
| Danger | `#ff8a80` | `oklch(0.7594 0.14351 26.08)` |

### Contraste

**Claro:** texto sobre fondo WCAG 16.48:1, APCA Lc 96.7 (oscuro-sobre-claro); texto sobre superficie WCAG 14.81:1, APCA Lc 89.8 (oscuro-sobre-claro); accent-foreground sobre acento WCAG 10.6:1, APCA Lc -91.8 (claro-sobre-oscuro). Muted sobre fondo WCAG 6.36:1, APCA Lc 76.5 (oscuro-sobre-claro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 10.35:1, APCA Lc 87.1 (oscuro-sobre-claro)). `accent-text` está igualado o derivado para ese rol.

**Oscuro:** texto sobre fondo WCAG 15.95:1, APCA Lc -93.6 (claro-sobre-oscuro); texto sobre superficie WCAG 15.05:1, APCA Lc -93.0 (claro-sobre-oscuro); accent-foreground sobre acento WCAG 12.09:1, APCA Lc 77.0 (oscuro-sobre-claro). Muted sobre fondo WCAG 8.69:1, APCA Lc -58.1 (claro-sobre-oscuro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 12.25:1, APCA Lc -76.6 (claro-sobre-oscuro)). `accent-text` está igualado o derivado para ese rol.

### Tokens CSS

```css
:root {
  /* Vino de noche — claro */
  --bg: oklch(0.9576 0.01246 75.37); /* #f6f0e8 */
  --surface: oklch(0.9222 0.02113 79.09); /* #ede4d6 */
  --border: oklch(0.8389 0.03139 76.93); /* #d6c8b4 */
  --text: oklch(0.1865 0.01698 18.80); /* #1a1010 */
  --muted: oklch(0.4594 0.02484 48.16); /* #64544c */
  --accent: oklch(0.3572 0.12583 7.70); /* #6e1230 */
  --accent-foreground: oklch(0.9675 0.01640 8.16); /* #fff0f2 */
  --accent-text: oklch(0.3572 0.12583 7.70); /* #6e1230 */
  --success: oklch(0.4689 0.10756 151.36); /* #1f6b3a */
  --warn: oklch(0.5078 0.10800 73.30); /* #8a5a00 */
  --danger: oklch(0.4158 0.15719 22.42); /* #8e1020 */
}

.dark {
  /* Vino de noche — oscuro */
  --bg: oklch(0.1670 0.01579 347.47); /* #140c10 */
  --surface: oklch(0.2008 0.02263 347.90); /* #1e1218 */
  --border: oklch(0.2881 0.04296 344.24); /* #3a2230 */
  --text: oklch(0.9364 0.02002 69.99); /* #f3e8dc */
  --muted: oklch(0.7548 0.02989 355.70); /* #c0a8b0 */
  --accent: oklch(0.8539 0.05629 68.71); /* #e8c9a8 */
  --accent-foreground: oklch(0.1765 0.02517 1.49); /* #1a0c10 */
  --accent-text: oklch(0.8539 0.05629 68.71); /* #e8c9a8 */
  --success: oklch(0.8138 0.12756 152.72); /* #7dda9a */
  --warn: oklch(0.8060 0.13714 85.03); /* #e8b849 */
  --danger: oklch(0.7594 0.14351 26.08); /* #ff8a80 */
}
```


---

## Bosque y musgo

`bosque-musgo` — Bosque de noche, un musgo que brilla poco

**Mejor para:** outdoor, sostenibilidad (sin cliché lima de ‘eco’), turismo, editorial de naturaleza.  
**Evitá en:** fintech, el cliché ‘green = eco’ chato de plantilla.  
**Estilos:** [`organico-terroso`](../estilos/organico-terroso.md), [`saas-oscuro-premium`](../estilos/saas-oscuro-premium.md), [`espacial-3d`](../estilos/espacial-3d.md), [`scrollytelling`](../estilos/scrollytelling.md).

Musgo apagado, no emerald-500 de ‘eco startup’. En claro, el acento es un verde de sotobosque, oscuro.

### Claro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#f1f3ec` | `oklch(0.9607 0.00949 119.58)` |
| Superficie | `#e3e8d8` | `oklch(0.9228 0.02197 120.98)` |
| Borde | `#c8d0b8` | `oklch(0.8449 0.03372 122.14)` |
| Texto | `#141810` | `oklch(0.2018 0.01661 129.42)` |
| Muted | `#545a48` | `oklch(0.4568 0.02929 122.54)` |
| Acento (sólido) | `#2c4a1c` | `oklch(0.3736 0.08037 136.01)` |
| Acento foreground | `#f0f8e4` | `oklch(0.9677 0.02764 124.76)` |
| Acento texto/link | `#2c4a1c` | `oklch(0.3736 0.08037 136.01)` |
| Success | `#1f6b3a` | `oklch(0.4689 0.10756 151.36)` |
| Warn | `#8a5a00` | `oklch(0.5078 0.10800 73.30)` |
| Danger | `#b42318` | `oklch(0.5003 0.18205 29.51)` |

### Oscuro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#0c100c` | `oklch(0.1670 0.01042 145.09)` |
| Superficie | `#151a14` | `oklch(0.2103 0.01386 140.43)` |
| Borde | `#2a3328` | `oklch(0.3088 0.02292 139.97)` |
| Texto | `#e6edd8` | `oklch(0.9351 0.02882 121.99)` |
| Muted | `#9aa490` | `oklch(0.7050 0.03064 128.95)` |
| Acento (sólido) | `#a4c86a` | `oklch(0.7855 0.12813 126.39)` |
| Acento foreground | `#10180c` | `oklch(0.1968 0.02607 135.59)` |
| Acento texto/link | `#a4c86a` | `oklch(0.7855 0.12813 126.39)` |
| Success | `#7dda9a` | `oklch(0.8138 0.12756 152.72)` |
| Warn | `#e8b849` | `oklch(0.8060 0.13714 85.03)` |
| Danger | `#ff8a80` | `oklch(0.7594 0.14351 26.08)` |

### Contraste

**Claro:** texto sobre fondo WCAG 16.07:1, APCA Lc 97.0 (oscuro-sobre-claro); texto sobre superficie WCAG 14.39:1, APCA Lc 89.9 (oscuro-sobre-claro); accent-foreground sobre acento WCAG 9.15:1, APCA Lc -90.6 (claro-sobre-oscuro). Muted sobre fondo WCAG 6.4:1, APCA Lc 77.2 (oscuro-sobre-claro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 8.92:1, APCA Lc 85.4 (oscuro-sobre-claro)). `accent-text` está igualado o derivado para ese rol.

**Oscuro:** texto sobre fondo WCAG 15.95:1, APCA Lc -93.9 (claro-sobre-oscuro); texto sobre superficie WCAG 14.68:1, APCA Lc -93.1 (claro-sobre-oscuro); accent-foreground sobre acento WCAG 9.54:1, APCA Lc 66.6 (oscuro-sobre-claro). Muted sobre fondo WCAG 7.38:1, APCA Lc -50.8 (claro-sobre-oscuro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 10.09:1, APCA Lc -66.0 (claro-sobre-oscuro)). `accent-text` está igualado o derivado para ese rol.

### Tokens CSS

```css
:root {
  /* Bosque y musgo — claro */
  --bg: oklch(0.9607 0.00949 119.58); /* #f1f3ec */
  --surface: oklch(0.9228 0.02197 120.98); /* #e3e8d8 */
  --border: oklch(0.8449 0.03372 122.14); /* #c8d0b8 */
  --text: oklch(0.2018 0.01661 129.42); /* #141810 */
  --muted: oklch(0.4568 0.02929 122.54); /* #545a48 */
  --accent: oklch(0.3736 0.08037 136.01); /* #2c4a1c */
  --accent-foreground: oklch(0.9677 0.02764 124.76); /* #f0f8e4 */
  --accent-text: oklch(0.3736 0.08037 136.01); /* #2c4a1c */
  --success: oklch(0.4689 0.10756 151.36); /* #1f6b3a */
  --warn: oklch(0.5078 0.10800 73.30); /* #8a5a00 */
  --danger: oklch(0.5003 0.18205 29.51); /* #b42318 */
}

.dark {
  /* Bosque y musgo — oscuro */
  --bg: oklch(0.1670 0.01042 145.09); /* #0c100c */
  --surface: oklch(0.2103 0.01386 140.43); /* #151a14 */
  --border: oklch(0.3088 0.02292 139.97); /* #2a3328 */
  --text: oklch(0.9351 0.02882 121.99); /* #e6edd8 */
  --muted: oklch(0.7050 0.03064 128.95); /* #9aa490 */
  --accent: oklch(0.7855 0.12813 126.39); /* #a4c86a */
  --accent-foreground: oklch(0.1968 0.02607 135.59); /* #10180c */
  --accent-text: oklch(0.7855 0.12813 126.39); /* #a4c86a */
  --success: oklch(0.8138 0.12756 152.72); /* #7dda9a */
  --warn: oklch(0.8060 0.13714 85.03); /* #e8b849 */
  --danger: oklch(0.7594 0.14351 26.08); /* #ff8a80 */
}
```


---

## Arcilla y sello

`arcilla-sello` — Cerámica, azul de sello, ilustrado

**Mejor para:** ilustración, artesanía, editoriales infantiles serias, café.  
**Evitá en:** SaaS genérico.  
**Estilos:** [`ilustrado-humano`](../estilos/ilustrado-humano.md), [`risografia-impreso`](../estilos/risografia-impreso.md), [`organico-terroso`](../estilos/organico-terroso.md), [`realismo-tactil`](../estilos/realismo-tactil.md).

El azul de sello es más tinta que UI. Combiná con ilustración humana, no con 3D de stock.

### Claro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#f6efe6` | `oklch(0.9551 0.01417 74.42)` |
| Superficie | `#ede2d2` | `oklch(0.9172 0.02454 77.45)` |
| Borde | `#d6c4ae` | `oklch(0.8294 0.03618 72.83)` |
| Texto | `#1c1610` | `oklch(0.2054 0.01498 66.83)` |
| Muted | `#645848` | `oklch(0.4674 0.02934 74.90)` |
| Acento (sólido) | `#1a4a8a` | `oklch(0.4136 0.11840 256.98)` |
| Acento foreground | `#f3f7ff` | `oklch(0.9754 0.01150 264.51)` |
| Acento texto/link | `#1a4a8a` | `oklch(0.4136 0.11840 256.98)` |
| Success | `#1f6b3a` | `oklch(0.4689 0.10756 151.36)` |
| Warn | `#8a5a00` | `oklch(0.5078 0.10800 73.30)` |
| Danger | `#b42318` | `oklch(0.5003 0.18205 29.51)` |

### Oscuro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#16110c` | `oklch(0.1821 0.01287 66.87)` |
| Superficie | `#221a14` | `oklch(0.2254 0.01698 58.63)` |
| Borde | `#3c2e22` | `oklch(0.3134 0.02892 62.07)` |
| Texto | `#f3e8d8` | `oklch(0.9354 0.02442 77.46)` |
| Muted | `#b3a090` | `oklch(0.7179 0.03186 62.40)` |
| Acento (sólido) | `#416fba` | `oklch(0.5458 0.12805 259.70)` |
| Acento foreground | `#ffffff` | `oklch(1.0000 0.00000 0.00)` |
| Acento texto/link | `#85b4ff` | `oklch(0.7665 0.11956 259.47)` |
| Success | `#7dda9a` | `oklch(0.8138 0.12756 152.72)` |
| Warn | `#e8b849` | `oklch(0.8060 0.13714 85.03)` |
| Danger | `#ff8a80` | `oklch(0.7594 0.14351 26.08)` |

### Contraste

**Claro:** texto sobre fondo WCAG 15.71:1, APCA Lc 95.7 (oscuro-sobre-claro); texto sobre superficie WCAG 14.01:1, APCA Lc 88.4 (oscuro-sobre-claro); accent-foreground sobre acento WCAG 8.18:1, APCA Lc -88.7 (claro-sobre-oscuro). Muted sobre fondo WCAG 6.07:1, APCA Lc 75.0 (oscuro-sobre-claro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 7.7:1, APCA Lc 80.7 (oscuro-sobre-claro)). `accent-text` está igualado o derivado para ese rol.

**Oscuro:** texto sobre fondo WCAG 15.49:1, APCA Lc -93.2 (claro-sobre-oscuro); texto sobre superficie WCAG 14.15:1, APCA Lc -92.2 (claro-sobre-oscuro); accent-foreground sobre acento WCAG 4.99:1, APCA Lc -79.7 (claro-sobre-oscuro). Muted sobre fondo WCAG 7.46:1, APCA Lc -52.0 (claro-sobre-oscuro): sirve para cuerpo secundario. El acento sólido no llega a 4.5:1 como texto sobre el fondo (3.76:1). Para botones usá `accent` + `accent-foreground`. Para links usá `accent-text` (8.9:1, Lc -60.5).

### Tokens CSS

```css
:root {
  /* Arcilla y sello — claro */
  --bg: oklch(0.9551 0.01417 74.42); /* #f6efe6 */
  --surface: oklch(0.9172 0.02454 77.45); /* #ede2d2 */
  --border: oklch(0.8294 0.03618 72.83); /* #d6c4ae */
  --text: oklch(0.2054 0.01498 66.83); /* #1c1610 */
  --muted: oklch(0.4674 0.02934 74.90); /* #645848 */
  --accent: oklch(0.4136 0.11840 256.98); /* #1a4a8a */
  --accent-foreground: oklch(0.9754 0.01150 264.51); /* #f3f7ff */
  --accent-text: oklch(0.4136 0.11840 256.98); /* #1a4a8a */
  --success: oklch(0.4689 0.10756 151.36); /* #1f6b3a */
  --warn: oklch(0.5078 0.10800 73.30); /* #8a5a00 */
  --danger: oklch(0.5003 0.18205 29.51); /* #b42318 */
}

.dark {
  /* Arcilla y sello — oscuro */
  --bg: oklch(0.1821 0.01287 66.87); /* #16110c */
  --surface: oklch(0.2254 0.01698 58.63); /* #221a14 */
  --border: oklch(0.3134 0.02892 62.07); /* #3c2e22 */
  --text: oklch(0.9354 0.02442 77.46); /* #f3e8d8 */
  --muted: oklch(0.7179 0.03186 62.40); /* #b3a090 */
  --accent: oklch(0.5458 0.12805 259.70); /* #416fba */
  --accent-foreground: oklch(1.0000 0.00000 0.00); /* #ffffff */
  --accent-text: oklch(0.7665 0.11956 259.47); /* #85b4ff */
  --success: oklch(0.8138 0.12756 152.72); /* #7dda9a */
  --warn: oklch(0.8060 0.13714 85.03); /* #e8b849 */
  --danger: oklch(0.7594 0.14351 26.08); /* #ff8a80 */
}
```


---

## Durazno y tinta

`durazno-tinta` — Piel, durazno, tinta negra: una rareza suave

**Mejor para:** belleza, estudios, PyMEs, ilustración, marcas personales.  
**Evitá en:** infra, look militar o industrial.  
**Estilos:** [`expresivo-minimo`](../estilos/expresivo-minimo.md), [`ilustrado-humano`](../estilos/ilustrado-humano.md), [`editorial-revista`](../estilos/editorial-revista.md), [`realismo-tactil`](../estilos/realismo-tactil.md).

El durazno es fondo o superficie, la tinta es el acento. Evitá volverlo un ‘blush gradient’ de plantilla.

### Claro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#fbefe6` | `oklch(0.9591 0.01771 59.48)` |
| Superficie | `#f4e0d2` | `oklch(0.9191 0.02901 57.36)` |
| Borde | `#e4c8b6` | `oklch(0.8516 0.04014 54.79)` |
| Texto | `#1a120e` | `oklch(0.1911 0.01555 47.89)` |
| Muted | `#6b5348` | `oklch(0.4638 0.03665 45.86)` |
| Acento (sólido) | `#1a1a1a` | `oklch(0.2178 0.00000 0.00)` |
| Acento foreground | `#ffede0` | `oklch(0.9569 0.02617 58.29)` |
| Acento texto/link | `#1a1a1a` | `oklch(0.2178 0.00000 0.00)` |
| Success | `#1f6b3a` | `oklch(0.4689 0.10756 151.36)` |
| Warn | `#8a5a00` | `oklch(0.5078 0.10800 73.30)` |
| Danger | `#b42318` | `oklch(0.5003 0.18205 29.51)` |

### Oscuro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#16100e` | `oklch(0.1800 0.01095 39.26)` |
| Superficie | `#221814` | `oklch(0.2202 0.01794 42.85)` |
| Borde | `#3c2c26` | `oklch(0.3097 0.02611 41.50)` |
| Texto | `#f8e8dc` | `oklch(0.9405 0.02375 59.39)` |
| Muted | `#c0a498` | `oklch(0.7401 0.03723 44.54)` |
| Acento (sólido) | `#f0b090` | `oklch(0.8093 0.08698 47.62)` |
| Acento foreground | `#1a0e0a` | `oklch(0.1793 0.02229 39.19)` |
| Acento texto/link | `#f0b090` | `oklch(0.8093 0.08698 47.62)` |
| Success | `#7dda9a` | `oklch(0.8138 0.12756 152.72)` |
| Warn | `#e8b849` | `oklch(0.8060 0.13714 85.03)` |
| Danger | `#ff8a80` | `oklch(0.7594 0.14351 26.08)` |

### Contraste

**Claro:** texto sobre fondo WCAG 16.35:1, APCA Lc 96.7 (oscuro-sobre-claro); texto sobre superficie WCAG 14.46:1, APCA Lc 88.9 (oscuro-sobre-claro); accent-foreground sobre acento WCAG 15.28:1, APCA Lc -96.8 (claro-sobre-oscuro). Muted sobre fondo WCAG 6.29:1, APCA Lc 76.3 (oscuro-sobre-claro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 15.41:1, APCA Lc 95.9 (oscuro-sobre-claro)). `accent-text` está igualado o derivado para ese rol.

**Oscuro:** texto sobre fondo WCAG 15.76:1, APCA Lc -94.1 (claro-sobre-oscuro); texto sobre superficie WCAG 14.53:1, APCA Lc -93.3 (claro-sobre-oscuro); accent-foreground sobre acento WCAG 10.19:1, APCA Lc 68.3 (oscuro-sobre-claro). Muted sobre fondo WCAG 8.08:1, APCA Lc -55.6 (claro-sobre-oscuro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 10.15:1, APCA Lc -67.1 (claro-sobre-oscuro)). `accent-text` está igualado o derivado para ese rol.

### Tokens CSS

```css
:root {
  /* Durazno y tinta — claro */
  --bg: oklch(0.9591 0.01771 59.48); /* #fbefe6 */
  --surface: oklch(0.9191 0.02901 57.36); /* #f4e0d2 */
  --border: oklch(0.8516 0.04014 54.79); /* #e4c8b6 */
  --text: oklch(0.1911 0.01555 47.89); /* #1a120e */
  --muted: oklch(0.4638 0.03665 45.86); /* #6b5348 */
  --accent: oklch(0.2178 0.00000 0.00); /* #1a1a1a */
  --accent-foreground: oklch(0.9569 0.02617 58.29); /* #ffede0 */
  --accent-text: oklch(0.2178 0.00000 0.00); /* #1a1a1a */
  --success: oklch(0.4689 0.10756 151.36); /* #1f6b3a */
  --warn: oklch(0.5078 0.10800 73.30); /* #8a5a00 */
  --danger: oklch(0.5003 0.18205 29.51); /* #b42318 */
}

.dark {
  /* Durazno y tinta — oscuro */
  --bg: oklch(0.1800 0.01095 39.26); /* #16100e */
  --surface: oklch(0.2202 0.01794 42.85); /* #221814 */
  --border: oklch(0.3097 0.02611 41.50); /* #3c2c26 */
  --text: oklch(0.9405 0.02375 59.39); /* #f8e8dc */
  --muted: oklch(0.7401 0.03723 44.54); /* #c0a498 */
  --accent: oklch(0.8093 0.08698 47.62); /* #f0b090 */
  --accent-foreground: oklch(0.1793 0.02229 39.19); /* #1a0e0a */
  --accent-text: oklch(0.8093 0.08698 47.62); /* #f0b090 */
  --success: oklch(0.8138 0.12756 152.72); /* #7dda9a */
  --warn: oklch(0.8060 0.13714 85.03); /* #e8b849 */
  --danger: oklch(0.7594 0.14351 26.08); /* #ff8a80 */
}
```


---

## Acero y seguridad

`acero-seguridad` — Industrial, amarillo de seguridad, ficha de producto

**Mejor para:** industria, hardware, autos, logística, catálogos.  
**Evitá en:** belleza, editorial romántica, infantil.  
**Estilos:** [`catalogo-tecnico`](../estilos/catalogo-tecnico.md), [`suizo-internacional`](../estilos/suizo-internacional.md), [`neo-brutalismo`](../estilos/neo-brutalismo.md), [`bento-grids`](../estilos/bento-grids.md).

El amarillo de seguridad no es el amarillo brutalista de poster: es un acento de norma, usado en etiquetas y avisos. El resto es acero.

### Claro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#f3f3f1` | `oklch(0.9636 0.00265 106.45)` |
| Superficie | `#e8e8e4` | `oklch(0.9299 0.00535 106.50)` |
| Borde | `#cecec8` | `oklch(0.8497 0.00819 106.57)` |
| Texto | `#161616` | `oklch(0.2002 0.00000 0.00)` |
| Muted | `#585858` | `oklch(0.4604 0.00000 0.00)` |
| Acento (sólido) | `#f0c430` | `oklch(0.8359 0.15895 90.87)` |
| Acento foreground | `#111111` | `oklch(0.1776 0.00000 0.00)` |
| Acento texto/link | `#856a00` | `oklch(0.5355 0.10948 91.12)` |
| Success | `#1f6b3a` | `oklch(0.4689 0.10756 151.36)` |
| Warn | `#8a5a00` | `oklch(0.5078 0.10800 73.30)` |
| Danger | `#b42318` | `oklch(0.5003 0.18205 29.51)` |

### Oscuro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#121212` | `oklch(0.1822 0.00000 0.00)` |
| Superficie | `#1b1b1b` | `oklch(0.2221 0.00000 0.00)` |
| Borde | `#333333` | `oklch(0.3211 0.00000 0.00)` |
| Texto | `#eeede8` | `oklch(0.9455 0.00675 97.35)` |
| Muted | `#a8a8a0` | `oklch(0.7293 0.01133 106.68)` |
| Acento (sólido) | `#f0c430` | `oklch(0.8359 0.15895 90.87)` |
| Acento foreground | `#1a1600` | `oklch(0.1988 0.04143 100.69)` |
| Acento texto/link | `#f0c430` | `oklch(0.8359 0.15895 90.87)` |
| Success | `#7dda9a` | `oklch(0.8138 0.12756 152.72)` |
| Warn | `#e8b849` | `oklch(0.8060 0.13714 85.03)` |
| Danger | `#ff8a80` | `oklch(0.7594 0.14351 26.08)` |

### Contraste

**Claro:** texto sobre fondo WCAG 16.29:1, APCA Lc 97.6 (oscuro-sobre-claro); texto sobre superficie WCAG 14.73:1, APCA Lc 91.1 (oscuro-sobre-claro); accent-foreground sobre acento WCAG 11.37:1, APCA Lc 74.2 (oscuro-sobre-claro). Muted sobre fondo WCAG 6.4:1, APCA Lc 77.5 (oscuro-sobre-claro): sirve para cuerpo secundario. El acento sólido no llega a 4.5:1 como texto sobre el fondo (1.49:1). Para botones usá `accent` + `accent-foreground`. Para links usá `accent-text` (4.66:1, Lc 68.2).

**Oscuro:** texto sobre fondo WCAG 15.98:1, APCA Lc -95.5 (claro-sobre-oscuro); texto sobre superficie WCAG 14.69:1, APCA Lc -94.6 (claro-sobre-oscuro); accent-foreground sobre acento WCAG 10.91:1, APCA Lc 73.6 (oscuro-sobre-claro). Muted sobre fondo WCAG 7.83:1, APCA Lc -54.3 (claro-sobre-oscuro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 11.28:1, APCA Lc -73.4 (claro-sobre-oscuro)). `accent-text` está igualado o derivado para ese rol.

### Tokens CSS

```css
:root {
  /* Acero y seguridad — claro */
  --bg: oklch(0.9636 0.00265 106.45); /* #f3f3f1 */
  --surface: oklch(0.9299 0.00535 106.50); /* #e8e8e4 */
  --border: oklch(0.8497 0.00819 106.57); /* #cecec8 */
  --text: oklch(0.2002 0.00000 0.00); /* #161616 */
  --muted: oklch(0.4604 0.00000 0.00); /* #585858 */
  --accent: oklch(0.8359 0.15895 90.87); /* #f0c430 */
  --accent-foreground: oklch(0.1776 0.00000 0.00); /* #111111 */
  --accent-text: oklch(0.5355 0.10948 91.12); /* #856a00 */
  --success: oklch(0.4689 0.10756 151.36); /* #1f6b3a */
  --warn: oklch(0.5078 0.10800 73.30); /* #8a5a00 */
  --danger: oklch(0.5003 0.18205 29.51); /* #b42318 */
}

.dark {
  /* Acero y seguridad — oscuro */
  --bg: oklch(0.1822 0.00000 0.00); /* #121212 */
  --surface: oklch(0.2221 0.00000 0.00); /* #1b1b1b */
  --border: oklch(0.3211 0.00000 0.00); /* #333333 */
  --text: oklch(0.9455 0.00675 97.35); /* #eeede8 */
  --muted: oklch(0.7293 0.01133 106.68); /* #a8a8a0 */
  --accent: oklch(0.8359 0.15895 90.87); /* #f0c430 */
  --accent-foreground: oklch(0.1988 0.04143 100.69); /* #1a1600 */
  --accent-text: oklch(0.8359 0.15895 90.87); /* #f0c430 */
  --success: oklch(0.8138 0.12756 152.72); /* #7dda9a */
  --warn: oklch(0.8060 0.13714 85.03); /* #e8b849 */
  --danger: oklch(0.7594 0.14351 26.08); /* #ff8a80 */
}
```


---

## Arena y verde seco

`arena-verde-seco` — Interior, planta seca, PyME con oficio

**Mejor para:** PyMEs, estudios de arquitectura de interiores, hospitality, bienestar.  
**Evitá en:** neon tech, crypto.  
**Estilos:** [`expresivo-minimo`](../estilos/expresivo-minimo.md), [`organico-terroso`](../estilos/organico-terroso.md), [`realismo-tactil`](../estilos/realismo-tactil.md), [`editorial-revista`](../estilos/editorial-revista.md).

Una paleta ‘de local’ (oficina, estudio, local a la calle), nada de índigo. El verde seco no es el lime de Mercury.

### Claro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#f5f1e8` | `oklch(0.9588 0.01270 86.83)` |
| Superficie | `#ebe5d8` | `oklch(0.9231 0.01855 86.15)` |
| Borde | `#d4ccb8` | `oklch(0.8463 0.02853 88.77)` |
| Texto | `#1a1810` | `oklch(0.2085 0.01532 95.70)` |
| Muted | `#5e5848` | `oklch(0.4613 0.02607 89.91)` |
| Acento (sólido) | `#4a5a28` | `oklch(0.4416 0.07619 124.16)` |
| Acento foreground | `#f4f8e0` | `oklch(0.9698 0.03175 114.67)` |
| Acento texto/link | `#4a5a28` | `oklch(0.4416 0.07619 124.16)` |
| Success | `#1f6b3a` | `oklch(0.4689 0.10756 151.36)` |
| Warn | `#8a5a00` | `oklch(0.5078 0.10800 73.30)` |
| Danger | `#b42318` | `oklch(0.5003 0.18205 29.51)` |

### Oscuro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#14120c` | `oklch(0.1824 0.01213 91.80)` |
| Superficie | `#1e1c14` | `oklch(0.2259 0.01509 95.66)` |
| Borde | `#363226` | `oklch(0.3175 0.02112 91.80)` |
| Texto | `#f0ebd8` | `oklch(0.9389 0.02573 94.74)` |
| Muted | `#a8a28c` | `oklch(0.7112 0.03171 94.46)` |
| Acento (sólido) | `#c0c878` | `oklch(0.8085 0.10359 113.39)` |
| Acento foreground | `#16180c` | `oklch(0.2028 0.02256 116.16)` |
| Acento texto/link | `#c0c878` | `oklch(0.8085 0.10359 113.39)` |
| Success | `#7dda9a` | `oklch(0.8138 0.12756 152.72)` |
| Warn | `#e8b849` | `oklch(0.8060 0.13714 85.03)` |
| Danger | `#ff8a80` | `oklch(0.7594 0.14351 26.08)` |

### Contraste

**Claro:** texto sobre fondo WCAG 15.76:1, APCA Lc 96.4 (oscuro-sobre-claro); texto sobre superficie WCAG 14.15:1, APCA Lc 89.4 (oscuro-sobre-claro); accent-foreground sobre acento WCAG 6.95:1, APCA Lc -84.7 (claro-sobre-oscuro). Muted sobre fondo WCAG 6.28:1, APCA Lc 76.4 (oscuro-sobre-claro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 6.69:1, APCA Lc 78.0 (oscuro-sobre-claro)). `accent-text` está igualado o derivado para ese rol.

**Oscuro:** texto sobre fondo WCAG 15.67:1, APCA Lc -94.1 (claro-sobre-oscuro); texto sobre superficie WCAG 14.28:1, APCA Lc -93.1 (claro-sobre-oscuro); accent-foreground sobre acento WCAG 10.06:1, APCA Lc 69.6 (oscuro-sobre-claro). Muted sobre fondo WCAG 7.32:1, APCA Lc -51.3 (claro-sobre-oscuro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 10.5:1, APCA Lc -69.2 (claro-sobre-oscuro)). `accent-text` está igualado o derivado para ese rol.

### Tokens CSS

```css
:root {
  /* Arena y verde seco — claro */
  --bg: oklch(0.9588 0.01270 86.83); /* #f5f1e8 */
  --surface: oklch(0.9231 0.01855 86.15); /* #ebe5d8 */
  --border: oklch(0.8463 0.02853 88.77); /* #d4ccb8 */
  --text: oklch(0.2085 0.01532 95.70); /* #1a1810 */
  --muted: oklch(0.4613 0.02607 89.91); /* #5e5848 */
  --accent: oklch(0.4416 0.07619 124.16); /* #4a5a28 */
  --accent-foreground: oklch(0.9698 0.03175 114.67); /* #f4f8e0 */
  --accent-text: oklch(0.4416 0.07619 124.16); /* #4a5a28 */
  --success: oklch(0.4689 0.10756 151.36); /* #1f6b3a */
  --warn: oklch(0.5078 0.10800 73.30); /* #8a5a00 */
  --danger: oklch(0.5003 0.18205 29.51); /* #b42318 */
}

.dark {
  /* Arena y verde seco — oscuro */
  --bg: oklch(0.1824 0.01213 91.80); /* #14120c */
  --surface: oklch(0.2259 0.01509 95.66); /* #1e1c14 */
  --border: oklch(0.3175 0.02112 91.80); /* #363226 */
  --text: oklch(0.9389 0.02573 94.74); /* #f0ebd8 */
  --muted: oklch(0.7112 0.03171 94.46); /* #a8a28c */
  --accent: oklch(0.8085 0.10359 113.39); /* #c0c878 */
  --accent-foreground: oklch(0.2028 0.02256 116.16); /* #16180c */
  --accent-text: oklch(0.8085 0.10359 113.39); /* #c0c878 */
  --success: oklch(0.8138 0.12756 152.72); /* #7dda9a */
  --warn: oklch(0.8060 0.13714 85.03); /* #e8b849 */
  --danger: oklch(0.7594 0.14351 26.08); /* #ff8a80 */
}
```


---

## Teja y mar

`teja-mar` — Teja, mediterráneo, un teal de agua, no navy-índigo

**Mejor para:** turismo, hospitality, comida de costa, marcas locales.  
**Evitá en:** SaaS genérico, si el teal se va a sky-500.  
**Estilos:** [`organico-terroso`](../estilos/organico-terroso.md), [`realismo-tactil`](../estilos/realismo-tactil.md), [`editorial-revista`](../estilos/editorial-revista.md), [`expresivo-minimo`](../estilos/expresivo-minimo.md).

La teja es el acento (material). El teal queda para links o datos de agua, no para un degradé hero.

### Claro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#f7f3ec` | `oklch(0.9653 0.01024 81.80)` |
| Superficie | `#eee7da` | `oklch(0.9299 0.01894 83.06)` |
| Borde | `#d8cdb8` | `oklch(0.8516 0.03093 83.63)` |
| Texto | `#1a1610` | `oklch(0.2028 0.01311 77.89)` |
| Muted | `#5e5648` | `oklch(0.4566 0.02427 81.66)` |
| Acento (sólido) | `#b33a1a` | `oklch(0.5206 0.16263 35.21)` |
| Acento foreground | `#fff4ee` | `oklch(0.9741 0.01433 50.81)` |
| Acento texto/link | `#b33a1a` | `oklch(0.5206 0.16263 35.21)` |
| Success | `#1f6b3a` | `oklch(0.4689 0.10756 151.36)` |
| Warn | `#8a5a00` | `oklch(0.5078 0.10800 73.30)` |
| Danger | `#8e1808` | `oklch(0.4187 0.15475 31.09)` |

### Oscuro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#14110c` | `oklch(0.1794 0.01101 80.47)` |
| Superficie | `#1f1a14` | `oklch(0.2215 0.01372 72.09)` |
| Borde | `#3a3226` | `oklch(0.3219 0.02326 77.80)` |
| Texto | `#f3ebdc` | `oklch(0.9423 0.02172 83.26)` |
| Muted | `#b3a890` | `oklch(0.7344 0.03575 86.30)` |
| Acento (sólido) | `#b65333` | `oklch(0.5614 0.13681 38.29)` |
| Acento foreground | `#ffffff` | `oklch(1.0000 0.00000 0.00)` |
| Acento texto/link | `#ff9978` | `oklch(0.7817 0.13117 38.67)` |
| Success | `#7dda9a` | `oklch(0.8138 0.12756 152.72)` |
| Warn | `#e8b849` | `oklch(0.8060 0.13714 85.03)` |
| Danger | `#ff8a80` | `oklch(0.7594 0.14351 26.08)` |

### Contraste

**Claro:** texto sobre fondo WCAG 16.28:1, APCA Lc 97.8 (oscuro-sobre-claro); texto sobre superficie WCAG 14.64:1, APCA Lc 90.9 (oscuro-sobre-claro); accent-foreground sobre acento WCAG 5.49:1, APCA Lc -77.9 (claro-sobre-oscuro). Muted sobre fondo WCAG 6.55:1, APCA Lc 78.2 (oscuro-sobre-claro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 5.37:1, APCA Lc 71.7 (oscuro-sobre-claro)). `accent-text` está igualado o derivado para ese rol.

**Oscuro:** texto sobre fondo WCAG 15.9:1, APCA Lc -94.8 (claro-sobre-oscuro); texto sobre superficie WCAG 14.58:1, APCA Lc -93.9 (claro-sobre-oscuro); accent-foreground sobre acento WCAG 4.91:1, APCA Lc -78.9 (claro-sobre-oscuro). Muted sobre fondo WCAG 8.0:1, APCA Lc -55.1 (claro-sobre-oscuro): sirve para cuerpo secundario. El acento sólido no llega a 4.5:1 como texto sobre el fondo (3.83:1). Para botones usá `accent` + `accent-foreground`. Para links usá `accent-text` (9.04:1, Lc -61.3).

### Tokens CSS

```css
:root {
  /* Teja y mar — claro */
  --bg: oklch(0.9653 0.01024 81.80); /* #f7f3ec */
  --surface: oklch(0.9299 0.01894 83.06); /* #eee7da */
  --border: oklch(0.8516 0.03093 83.63); /* #d8cdb8 */
  --text: oklch(0.2028 0.01311 77.89); /* #1a1610 */
  --muted: oklch(0.4566 0.02427 81.66); /* #5e5648 */
  --accent: oklch(0.5206 0.16263 35.21); /* #b33a1a */
  --accent-foreground: oklch(0.9741 0.01433 50.81); /* #fff4ee */
  --accent-text: oklch(0.5206 0.16263 35.21); /* #b33a1a */
  --success: oklch(0.4689 0.10756 151.36); /* #1f6b3a */
  --warn: oklch(0.5078 0.10800 73.30); /* #8a5a00 */
  --danger: oklch(0.4187 0.15475 31.09); /* #8e1808 */
}

.dark {
  /* Teja y mar — oscuro */
  --bg: oklch(0.1794 0.01101 80.47); /* #14110c */
  --surface: oklch(0.2215 0.01372 72.09); /* #1f1a14 */
  --border: oklch(0.3219 0.02326 77.80); /* #3a3226 */
  --text: oklch(0.9423 0.02172 83.26); /* #f3ebdc */
  --muted: oklch(0.7344 0.03575 86.30); /* #b3a890 */
  --accent: oklch(0.5614 0.13681 38.29); /* #b65333 */
  --accent-foreground: oklch(1.0000 0.00000 0.00); /* #ffffff */
  --accent-text: oklch(0.7817 0.13117 38.67); /* #ff9978 */
  --success: oklch(0.8138 0.12756 152.72); /* #7dda9a */
  --warn: oklch(0.8060 0.13714 85.03); /* #e8b849 */
  --danger: oklch(0.7594 0.14351 26.08); /* #ff8a80 */
}
```


---

## Niebla y vidrio

`niebla-vidrio` — Frío, translúcido, para usar el glass como acento no como tema

**Mejor para:** overlays, fotos con UI encima, un recorte, no una landing entera.  
**Evitá en:** tema completo de un sitio (es el tell del glassmorfismo de slop).  
**Estilos:** [`glassmorfismo`](../estilos/glassmorfismo.md), [`ui-casi-invisible`](../estilos/ui-casi-invisible.md), [`espacial-3d`](../estilos/espacial-3d.md), [`saas-oscuro-premium`](../estilos/saas-oscuro-premium.md).

Documentada para acentos de vidrio (un panel sobre una foto), no para pintar todo de blur + borde blanco. Contraste de texto sobre la superficie sólida, no sobre el blur.

### Claro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#eef2f6` | `oklch(0.9593 0.00687 247.90)` |
| Superficie | `#e2e8f0` | `oklch(0.9288 0.01262 255.51)` |
| Borde | `#c5d0dc` | `oklch(0.8528 0.02056 250.41)` |
| Texto | `#12181e` | `oklch(0.2057 0.01506 248.56)` |
| Muted | `#4e5a66` | `oklch(0.4617 0.02468 248.36)` |
| Acento (sólido) | `#1a4a6e` | `oklch(0.3950 0.07969 244.68)` |
| Acento foreground | `#f0f6fa` | `oklch(0.9698 0.00835 236.56)` |
| Acento texto/link | `#1a4a6e` | `oklch(0.3950 0.07969 244.68)` |
| Success | `#1f6b3a` | `oklch(0.4689 0.10756 151.36)` |
| Warn | `#8a5a00` | `oklch(0.5078 0.10800 73.30)` |
| Danger | `#b42318` | `oklch(0.5003 0.18205 29.51)` |

### Oscuro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#0c1014` | `oklch(0.1706 0.01054 248.44)` |
| Superficie | `#161c22` | `oklch(0.2231 0.01478 248.49)` |
| Borde | `#2c3640` | `oklch(0.3279 0.02236 248.51)` |
| Texto | `#e8eef3` | `oklch(0.9460 0.00932 242.84)` |
| Muted | `#8a98a6` | `oklch(0.6731 0.02624 248.22)` |
| Acento (sólido) | `#8ab4d4` | `oklch(0.7510 0.06463 241.52)` |
| Acento foreground | `#111111` | `oklch(0.1776 0.00000 0.00)` |
| Acento texto/link | `#90badb` | `oklch(0.7703 0.06534 242.33)` |
| Success | `#7dda9a` | `oklch(0.8138 0.12756 152.72)` |
| Warn | `#e8b849` | `oklch(0.8060 0.13714 85.03)` |
| Danger | `#ff8a80` | `oklch(0.7594 0.14351 26.08)` |

### Contraste

**Claro:** texto sobre fondo WCAG 15.89:1, APCA Lc 96.6 (oscuro-sobre-claro); texto sobre superficie WCAG 14.5:1, APCA Lc 90.6 (oscuro-sobre-claro); accent-foreground sobre acento WCAG 8.57:1, APCA Lc -89.1 (claro-sobre-oscuro). Muted sobre fondo WCAG 6.27:1, APCA Lc 76.4 (oscuro-sobre-claro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 8.3:1, APCA Lc 83.2 (oscuro-sobre-claro)). `accent-text` está igualado o derivado para ese rol.

**Oscuro:** texto sobre fondo WCAG 16.33:1, APCA Lc -95.8 (claro-sobre-oscuro); texto sobre superficie WCAG 14.68:1, APCA Lc -94.7 (claro-sobre-oscuro); accent-foreground sobre acento WCAG 8.6:1, APCA Lc 60.1 (oscuro-sobre-claro). Muted sobre fondo WCAG 6.48:1, APCA Lc -45.4 (claro-sobre-oscuro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 8.69:1, APCA Lc -58.6 (claro-sobre-oscuro)). `accent-text` está igualado o derivado para ese rol.

### Tokens CSS

```css
:root {
  /* Niebla y vidrio — claro */
  --bg: oklch(0.9593 0.00687 247.90); /* #eef2f6 */
  --surface: oklch(0.9288 0.01262 255.51); /* #e2e8f0 */
  --border: oklch(0.8528 0.02056 250.41); /* #c5d0dc */
  --text: oklch(0.2057 0.01506 248.56); /* #12181e */
  --muted: oklch(0.4617 0.02468 248.36); /* #4e5a66 */
  --accent: oklch(0.3950 0.07969 244.68); /* #1a4a6e */
  --accent-foreground: oklch(0.9698 0.00835 236.56); /* #f0f6fa */
  --accent-text: oklch(0.3950 0.07969 244.68); /* #1a4a6e */
  --success: oklch(0.4689 0.10756 151.36); /* #1f6b3a */
  --warn: oklch(0.5078 0.10800 73.30); /* #8a5a00 */
  --danger: oklch(0.5003 0.18205 29.51); /* #b42318 */
}

.dark {
  /* Niebla y vidrio — oscuro */
  --bg: oklch(0.1706 0.01054 248.44); /* #0c1014 */
  --surface: oklch(0.2231 0.01478 248.49); /* #161c22 */
  --border: oklch(0.3279 0.02236 248.51); /* #2c3640 */
  --text: oklch(0.9460 0.00932 242.84); /* #e8eef3 */
  --muted: oklch(0.6731 0.02624 248.22); /* #8a98a6 */
  --accent: oklch(0.7510 0.06463 241.52); /* #8ab4d4 */
  --accent-foreground: oklch(0.1776 0.00000 0.00); /* #111111 */
  --accent-text: oklch(0.7703 0.06534 242.33); /* #90badb */
  --success: oklch(0.8138 0.12756 152.72); /* #7dda9a */
  --warn: oklch(0.8060 0.13714 85.03); /* #e8b849 */
  --danger: oklch(0.7594 0.14351 26.08); /* #ff8a80 */
}
```


---

## Cera suave

`cera-suave` — Claymorfismo contenido: pasteles con contraste real

**Mejor para:** onboarding amable, kids (con contraste chequeado), fintech amable, educación.  
**Evitá en:** como default 2026 de un SaaS ‘serio’; nicho, no tendencia.  
**Estilos:** [`claymorfismo`](../estilos/claymorfismo.md), [`ilustrado-humano`](../estilos/ilustrado-humano.md), [`dopamina-saturado`](../estilos/dopamina-saturado.md).

Los pasteles de clay suelen fallar contraste. Acá el acento y el texto están forzados a AA. No uses sombra interna suave como único cromo.

### Claro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#f6f3ff` | `oklch(0.9699 0.01621 297.53)` |
| Superficie | `#ece6fa` | `oklch(0.9355 0.02750 299.54)` |
| Borde | `#d4cbe8` | `oklch(0.8584 0.04084 299.70)` |
| Texto | `#1a1528` | `oklch(0.2118 0.03729 295.13)` |
| Muted | `#5a5470` | `oklch(0.4626 0.04544 294.38)` |
| Acento (sólido) | `#5b3cc4` | `oklch(0.4761 0.19931 286.60)` |
| Acento foreground | `#f6f3ff` | `oklch(0.9699 0.01621 297.53)` |
| Acento texto/link | `#5b3cc4` | `oklch(0.4761 0.19931 286.60)` |
| Success | `#1f6b3a` | `oklch(0.4689 0.10756 151.36)` |
| Warn | `#8a5a00` | `oklch(0.5078 0.10800 73.30)` |
| Danger | `#b42318` | `oklch(0.5003 0.18205 29.51)` |

### Oscuro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#121018` | `oklch(0.1794 0.01651 296.16)` |
| Superficie | `#1c1826` | `oklch(0.2205 0.02749 297.21)` |
| Borde | `#342e48` | `oklch(0.3195 0.04615 294.23)` |
| Texto | `#eee8fa` | `oklch(0.9410 0.02485 301.07)` |
| Muted | `#a8a0c0` | `oklch(0.7231 0.04665 296.67)` |
| Acento (sólido) | `#b8a0ff` | `oklch(0.7634 0.13517 294.60)` |
| Acento foreground | `#0a0a0a` | `oklch(0.1448 0.00000 0.00)` |
| Acento texto/link | `#bea8ff` | `oklch(0.7830 0.12342 295.01)` |
| Success | `#7dda9a` | `oklch(0.8138 0.12756 152.72)` |
| Warn | `#e8b849` | `oklch(0.8060 0.13714 85.03)` |
| Danger | `#ff8a80` | `oklch(0.7594 0.14351 26.08)` |

### Contraste

**Claro:** texto sobre fondo WCAG 16.23:1, APCA Lc 98.3 (oscuro-sobre-claro); texto sobre superficie WCAG 14.61:1, APCA Lc 91.4 (oscuro-sobre-claro); accent-foreground sobre acento WCAG 6.64:1, APCA Lc -82.6 (claro-sobre-oscuro). Muted sobre fondo WCAG 6.53:1, APCA Lc 78.6 (oscuro-sobre-claro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 6.64:1, APCA Lc 78.3 (oscuro-sobre-claro)). `accent-text` está igualado o derivado para ese rol.

**Oscuro:** texto sobre fondo WCAG 15.78:1, APCA Lc -94.1 (claro-sobre-oscuro); texto sobre superficie WCAG 14.53:1, APCA Lc -93.2 (claro-sobre-oscuro); accent-foreground sobre acento WCAG 8.97:1, APCA Lc 60.4 (oscuro-sobre-claro). Muted sobre fondo WCAG 7.6:1, APCA Lc -52.6 (claro-sobre-oscuro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 8.54:1, APCA Lc -58.3 (claro-sobre-oscuro)). `accent-text` está igualado o derivado para ese rol.

### Tokens CSS

```css
:root {
  /* Cera suave — claro */
  --bg: oklch(0.9699 0.01621 297.53); /* #f6f3ff */
  --surface: oklch(0.9355 0.02750 299.54); /* #ece6fa */
  --border: oklch(0.8584 0.04084 299.70); /* #d4cbe8 */
  --text: oklch(0.2118 0.03729 295.13); /* #1a1528 */
  --muted: oklch(0.4626 0.04544 294.38); /* #5a5470 */
  --accent: oklch(0.4761 0.19931 286.60); /* #5b3cc4 */
  --accent-foreground: oklch(0.9699 0.01621 297.53); /* #f6f3ff */
  --accent-text: oklch(0.4761 0.19931 286.60); /* #5b3cc4 */
  --success: oklch(0.4689 0.10756 151.36); /* #1f6b3a */
  --warn: oklch(0.5078 0.10800 73.30); /* #8a5a00 */
  --danger: oklch(0.5003 0.18205 29.51); /* #b42318 */
}

.dark {
  /* Cera suave — oscuro */
  --bg: oklch(0.1794 0.01651 296.16); /* #121018 */
  --surface: oklch(0.2205 0.02749 297.21); /* #1c1826 */
  --border: oklch(0.3195 0.04615 294.23); /* #342e48 */
  --text: oklch(0.9410 0.02485 301.07); /* #eee8fa */
  --muted: oklch(0.7231 0.04665 296.67); /* #a8a0c0 */
  --accent: oklch(0.7634 0.13517 294.60); /* #b8a0ff */
  --accent-foreground: oklch(0.1448 0.00000 0.00); /* #0a0a0a */
  --accent-text: oklch(0.7830 0.12342 295.01); /* #bea8ff */
  --success: oklch(0.8138 0.12756 152.72); /* #7dda9a */
  --warn: oklch(0.8060 0.13714 85.03); /* #e8b849 */
  --danger: oklch(0.7594 0.14351 26.08); /* #ff8a80 */
}
```

---

## Rosa del desierto

`rosa-desierto` — Rosa viejo, arcilla y ciruela, cálido sin ser beige

**Mejor para:** cosmética y estética, bodas y eventos, moda, hospitality boutique.  
**Evitá en:** devtools, industria, salud clínica.  
**Estilos:** [`editorial-revista`](../estilos/editorial-revista.md), [`organico-terroso`](../estilos/organico-terroso.md), [`expresivo-minimo`](../estilos/expresivo-minimo.md), [`realismo-tactil`](../estilos/realismo-tactil.md).

Adaptada del tema 'Desert Rose' de theme-factory (Anthropic, Apache 2.0): rosa #d4a5a5, arcilla #b87d6d, arena #e8d5c4, ciruela #5d2e46. La ciruela es el acento sólido en claro; el rosa viejo, en oscuro. La arena queda para superficies de foto, no de fondo.

### Claro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#faf6f5` | `oklch(0.9759 0.00450 34.31)` |
| Superficie | `#f2e8e6` | `oklch(0.9383 0.01123 31.07)` |
| Borde | `#e0cdca` | `oklch(0.8631 0.02174 28.35)` |
| Texto | `#2a1620` | `oklch(0.2317 0.03629 348.94)` |
| Muted | `#6b5058` | `oklch(0.4622 0.03799 359.16)` |
| Acento (sólido) | `#5d2e46` | `oklch(0.3713 0.07548 349.48)` |
| Acento foreground | `#fbeff3` | `oklch(0.9626 0.01392 355.00)` |
| Acento texto/link | `#5d2e46` | `oklch(0.3713 0.07548 349.48)` |
| Success | `#1f6b3a` | `oklch(0.4689 0.10756 151.36)` |
| Warn | `#8a5a00` | `oklch(0.5078 0.10800 73.30)` |
| Danger | `#b42318` | `oklch(0.5003 0.18205 29.51)` |

### Oscuro

| Rol | Hex | OKLCH |
|---|---|---|
| Fondo | `#170d12` | `oklch(0.1751 0.01951 347.87)` |
| Superficie | `#22141b` | `oklch(0.2129 0.02601 348.12)` |
| Borde | `#3d2830` | `oklch(0.3052 0.03390 354.72)` |
| Texto | `#f5e9ec` | `oklch(0.9443 0.01357 0.27)` |
| Muted | `#ccb3ba` | `oklch(0.7902 0.03018 359.00)` |
| Acento (sólido) | `#dbb0b0` | `oklch(0.7956 0.05023 18.26)` |
| Acento foreground | `#1c0c14` | `oklch(0.1816 0.03080 349.26)` |
| Acento texto/link | `#e2b8b8` | `oklch(0.8196 0.04861 18.19)` |
| Success | `#7dda9a` | `oklch(0.8138 0.12756 152.72)` |
| Warn | `#e8b849` | `oklch(0.8060 0.13714 85.03)` |
| Danger | `#ff8a80` | `oklch(0.7594 0.14351 26.08)` |

### Contraste

**Claro:** texto sobre fondo WCAG 15.85:1, APCA Lc 98.9 (oscuro-sobre-claro); texto sobre superficie WCAG 14.15:1, APCA Lc 91.4 (oscuro-sobre-claro); accent-foreground sobre acento WCAG 9.64:1, APCA Lc -90.1 (claro-sobre-oscuro). Muted sobre fondo WCAG 6.72:1, APCA Lc 80.1 (oscuro-sobre-claro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 10.06:1, APCA Lc 89.8 (oscuro-sobre-claro)). `accent-text` está igualado o derivado para ese rol.

**Oscuro:** texto sobre fondo WCAG 16.10:1, APCA Lc -94.9 (claro-sobre-oscuro); texto sobre superficie WCAG 14.99:1, APCA Lc -94.2 (claro-sobre-oscuro); accent-foreground sobre acento WCAG 9.76:1, APCA Lc 66.1 (oscuro-sobre-claro). Muted sobre fondo WCAG 9.73:1, APCA Lc -64.3 (claro-sobre-oscuro): sirve para cuerpo secundario. El acento también funciona como texto/link sobre el fondo (WCAG 9.84:1, APCA Lc -64.9 (claro-sobre-oscuro)). `accent-text` está igualado o derivado para ese rol.

### Tokens CSS

```css
:root {
  /* Rosa del desierto — claro */
  --bg: oklch(0.9759 0.00450 34.31); /* #faf6f5 */
  --surface: oklch(0.9383 0.01123 31.07); /* #f2e8e6 */
  --border: oklch(0.8631 0.02174 28.35); /* #e0cdca */
  --text: oklch(0.2317 0.03629 348.94); /* #2a1620 */
  --muted: oklch(0.4622 0.03799 359.16); /* #6b5058 */
  --accent: oklch(0.3713 0.07548 349.48); /* #5d2e46 */
  --accent-foreground: oklch(0.9626 0.01392 355.00); /* #fbeff3 */
  --accent-text: oklch(0.3713 0.07548 349.48); /* #5d2e46 */
  --success: oklch(0.4689 0.10756 151.36); /* #1f6b3a */
  --warn: oklch(0.5078 0.10800 73.30); /* #8a5a00 */
  --danger: oklch(0.5003 0.18205 29.51); /* #b42318 */
}
.dark {
  /* Rosa del desierto — oscuro */
  --bg: oklch(0.1751 0.01951 347.87); /* #170d12 */
  --surface: oklch(0.2129 0.02601 348.12); /* #22141b */
  --border: oklch(0.3052 0.03390 354.72); /* #3d2830 */
  --text: oklch(0.9443 0.01357 0.27); /* #f5e9ec */
  --muted: oklch(0.7902 0.03018 359.00); /* #ccb3ba */
  --accent: oklch(0.7956 0.05023 18.26); /* #dbb0b0 */
  --accent-foreground: oklch(0.1816 0.03080 349.26); /* #1c0c14 */
  --accent-text: oklch(0.8196 0.04861 18.19); /* #e2b8b8 */
  --success: oklch(0.8138 0.12756 152.72); /* #7dda9a */
  --warn: oklch(0.8060 0.13714 85.03); /* #e8b849 */
  --danger: oklch(0.7594 0.14351 26.08); /* #ff8a80 */
}
```

# Mobile y touch

## Tamaños de objetivo

| Fuente | Mínimo | Nota |
|---|---|---|
| WCAG 2.2 · 2.5.8 *Target Size (Minimum)* (AA) | **24 × 24 CSS px** o espaciado equivalente | Excepciones: links en texto, controles nativos sin estilo, equivalentes en otra parte |
| WCAG 2.2 · 2.5.5 *Target Size (Enhanced)* (AAA) | 44 × 44 CSS px | |
| Apple HIG | 44 × 44 pt | [HIG, Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) |
| Material Design | 48 × 48 dp | [M3, Accessibility](https://m3.material.io/foundations/designing/structure) |

Regla del kit: **44 px para controles táctiles principales**, 24 px mínimo absoluto, 8 px entre objetivos adyacentes. Agrandá el área tocable sin agrandar lo visual:

```css
.icon-btn { position: relative; inline-size: 2rem; block-size: 2rem; }
.icon-btn::after { content: ""; position: absolute; inset: -0.375rem; } /* área ≈ 44 px */
@media (pointer: coarse) { .row-action { min-block-size: 2.75rem; } }
```

## Zonas del pulgar

Steven Hoober (2013, observación de ~1.300 personas en la calle) encontró que la mayoría sostiene el teléfono con una mano y usa el pulgar; estudios posteriores suyos muestran que la gente cambia de agarre a menudo y toca con más precisión en el centro de la pantalla que en los bordes. Implicancias:
- **Acción primaria abajo** (barra inferior, botón fijo al pie en flujos de checkout).
- **Destructivas lejos** de las frecuentes.
- **Arriba** lo que se usa poco o lo que se lee (título, buscar si es secundario).
- No asumas una mano diestra: centrado o ancho completo funciona para ambas.

## Gestos

- **Todo gesto tiene una alternativa visible** (botón). Swipe para borrar → también un botón "Eliminar".
- **WCAG 2.5.7 *Dragging Movements* (AA, nuevo en 2.2)**: todo lo que se hace arrastrando también se puede hacer con un solo puntero sin arrastrar (ej.: botones "Mover arriba/abajo", menú "Mover a…").
- **WCAG 2.5.1 *Pointer Gestures***: gestos multipunto o de trayectoria (pinch, swipe complejo) tienen alternativa de un toque.
- No secuestres gestos del sistema (swipe desde el borde = atrás en iOS/Android).
- Pull-to-refresh solo en listas que se actualizan.

## Teclado en pantalla

- `inputmode` y `type` correctos ([`formularios-inputs.md`](formularios-inputs.md)); `enterkeyhint="search|next|send|done"`.
- El campo enfocado no debe quedar tapado por el teclado (WCAG 2.4.11 *Focus Not Obscured*): usá `scroll-margin` y evitá barras fijas que lo cubran. Con `interactive-widget=resizes-content` en el meta viewport, el layout se ajusta al teclado (soporte desigual: probá).
- No hagas zoom automático: inputs ≥ 16 px de fuente evitan el zoom de iOS Safari. **Nunca** `maximum-scale=1` ni `user-scalable=no` (rompe 1.4.4 *Resize Text*).

```html
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
```

## Layout mobile

- Una columna; contenido > chrome. Header que se oculta al hacer scroll hacia abajo y vuelve al subir (si es largo).
- `env(safe-area-inset-*)` para notch y barra de gestos en elementos fijos.
- Unidades `dvh`/`svh` en vez de `100vh` para pantallas completas.
- Bottom sheets con handle, altura máxima y botón cerrar; el contenido detrás `inert`.
- Respetá orientación (WCAG 1.3.4: no bloquear vertical/horizontal salvo que sea esencial).
- Reflow a 320 CSS px sin scroll horizontal (WCAG 1.4.10).

```css
.sticky-cta { position: sticky; bottom: 0; padding: .75rem 1rem calc(.75rem + env(safe-area-inset-bottom)); background: var(--bg); }
.fullscreen { min-block-size: 100dvh; }
```

## Plataformas 2025–2026

- **iOS 26 / Liquid Glass** (WWDC, junio 2025): NN/g criticó que la translucidez esconde contenido y reemplaza convenciones ([NN/g, 10/10/2025](https://www.nngroup.com/articles/liquid-glass/)). En web no lo imites como tema: contraste primero; respetá `prefers-reduced-transparency` donde exista y `prefers-contrast`.
- **Material 3 Expressive** (mayo 2025): Google reporta, en 46 estudios con 18.000+ participantes, que los diseños expresivos ayudaron a ubicar elementos clave más rápido ([Google Design](https://design.google/library/expressive-material-design-google-research); estudio controlado con 48 participantes en [CHI 2026](https://dl.acm.org/doi/10.1145/3772318.3790373)). Lección: jerarquía fuerte, tamaños y formas distintos para la acción principal; no "todo igual de suave".

## Rendimiento en mobile

Los teléfonos de gama media son el caso real: INP y LCP se miden en el p75 de usuarios reales ([`rendimiento-percibido.md`](rendimiento-percibido.md)). Probá con CPU throttling 4× y red "Fast 4G".

## Checklist mobile

- [ ] Objetivos ≥ 24 px (principales ≥ 44 px) y separados.
- [ ] Acción primaria al alcance del pulgar.
- [ ] Gestos con alternativa; arrastre con alternativa de un toque.
- [ ] Teclado correcto por campo; foco no tapado.
- [ ] Sin `user-scalable=no`; texto escalable al 200 %.
- [ ] 320 px sin scroll horizontal; safe areas respetadas.
- [ ] Nada solo al hover.

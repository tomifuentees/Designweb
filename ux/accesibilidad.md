# Accesibilidad (WCAG 2.2 AA y más)

Accesibilidad es UX para todo el espectro de personas (y, desde 2026, también para agentes de IA que leen el árbol de accesibilidad: [NN/g, 10/04/2026](https://www.nngroup.com/articles/ai-agents-as-users/)). No es una fase final: se decide en el HTML.

## Estado normativo (19/11/2026)

| Norma | Estado | Qué exige |
|---|---|---|
| **WCAG 2.2** | Recomendación W3C (oct. 2023); publicada como **ISO/IEC 40500:2025** ([ISO](https://www.iso.org/standard/91029.html)) | Referencia actual. Apuntá a AA |
| **WCAG 3.0** | **Working Draft** (último: 10/09/2026). El grupo apunta a Candidate Recommendation a fines de 2027 y publicación a inicios de 2028; el charter estima Q4 2027 ([W3C TR](https://www.w3.org/TR/wcag-3.0/); [minuta AGWG 13/10/2026](https://www.w3.org/2026/10/13-ag-minutes.html); [minuta 30/10/2026](https://www.w3.org/2026/10/30-apa-minutes.html)) | **No usar para cumplimiento.** El propio borrador dice que no reemplaza WCAG 2 |
| **ADA Title II** (EE.UU., gobiernos estatales y locales) | Regla del DOJ de 2024 → **WCAG 2.1 AA**. El 20/04/2026 una regla interina **extendió los plazos**: 26/04/2027 (población ≥ 50.000) y 26/04/2028 (menor y distritos especiales) ([Federal Register](https://www.federalregister.gov/documents/2026/04/20/2026-07663/extension-of-compliance-dates-for-nondiscrimination-on-the-basis-of-disability-accessibility-of-web); [ADA.gov](https://www.ada.gov/resources/2024-03-08-web-rule/)) | Web y apps de entes públicos |
| **ADA Title III** (EE.UU., negocios privados) | Sin regla técnica del DOJ; miles de demandas por año, en general con WCAG 2.1 AA como vara | Riesgo legal real en e-commerce |
| **Section 508** (EE.UU., gobierno federal) | Referencia WCAG 2.0 AA | |
| **European Accessibility Act** | Aplicable desde el **28/06/2025** a productos y servicios nuevos (e-commerce, banca, transporte, e-books, etc.) ([Comisión Europea](https://commission.europa.eu/strategy-and-policy/policies/justice-and-fundamental-rights/disability/union-equality-strategy-rights-persons-disabilities-2021-2030/european-accessibility-act_en)) | Norma armonizada EN 301 549 |
| **EN 301 549 V4.1.1** | Publicada en septiembre de 2026, alinea con WCAG 2.2; **todavía no citada** en el Diario Oficial, así que V3.2.1 (WCAG 2.1) sigue siendo la referencia de presunción de conformidad ([AccessibleEU, 07/09/2026](https://accessible-eu-centre.ec.europa.eu/content-corner/news/european-accessibility-standard-en-301-549-has-been-updated-2026-09-07_en)) | |

No es asesoramiento legal.

## Lo nuevo de WCAG 2.2 (lo que la IA casi nunca hace)

| Criterio | Nivel | Qué pide | Cómo cumplir |
|---|---|---|---|
| 2.4.11 Focus Not Obscured (Minimum) | AA | El elemento con foco no queda totalmente tapado por headers fijos, banners de cookies, chats | `scroll-padding-top` = alto del header fijo; banners que no tapen |
| 2.4.12 Focus Not Obscured (Enhanced) | AAA | Ni parcialmente tapado | |
| 2.4.13 Focus Appearance | AAA | Indicador de foco ≥ 2 px de perímetro y 3:1 de contraste de cambio | `outline: 2px solid; outline-offset: 2px` |
| 2.5.7 Dragging Movements | AA | Alternativa sin arrastrar | Botones mover / menú "Mover a…" |
| 2.5.8 Target Size (Minimum) | AA | 24 × 24 CSS px o espaciado | Ver [`mobile-touch.md`](mobile-touch.md) |
| 3.2.6 Consistent Help | A | Ayuda (contacto, chat, FAQ) en el mismo orden relativo en todas las páginas | Footer/header consistente |
| 3.3.7 Redundant Entry | A | No pedir dos veces lo mismo en un proceso | Autocompletar, "igual que envío" |
| 3.3.8 Accessible Authentication (Minimum) | AA | Sin prueba cognitiva para loguearse sin alternativa | Permitir pegar y gestores; passkeys; magic link; no CAPTCHA de memoria/transcripción sin alternativa |
| 3.3.9 Accessible Authentication (Enhanced) | AAA | Ni siquiera reconocer objetos/contenido propio | |
| 4.1.1 Parsing | — | **Eliminado** en 2.2 | |

## Checklist WCAG 2.2 AA para frontend (ids `A-*` en `ux.json`)

**Perceptible**
- [ ] `A-01` Imágenes con `alt` útil; decorativas `alt=""`; íconos de botón con nombre accesible (1.1.1).
- [ ] `A-02` Video con subtítulos; audio con transcripción (1.2.x).
- [ ] `A-03` Estructura semántica: landmarks (`header`, `nav`, `main`, `footer`), un `h1`, headings en orden, listas reales, tablas con `th`/`scope` (1.3.1).
- [ ] `A-04` Orden del DOM = orden visual/lectura (1.3.2).
- [ ] `A-05` Instrucciones que no dependen solo de forma, color o posición (1.3.3).
- [ ] `A-06` `autocomplete` en datos personales (1.3.5).
- [ ] `A-07` Color no es el único medio (errores, estados, gráficos) (1.4.1).
- [ ] `A-08` Contraste texto 4,5:1 (3:1 para ≥ 24 px o ≥ 18,66 px bold) (1.4.3).
- [ ] `A-09` Texto al 200 % sin pérdida (1.4.4); reflow a 320 px (1.4.10).
- [ ] `A-10` Contraste no textual 3:1: bordes de inputs, íconos, foco, estados (1.4.11).
- [ ] `A-11` Text spacing ajustable sin cortes (1.4.12): nada de alturas fijas en contenedores de texto.
- [ ] `A-12` Contenido en hover/foco: descartable (Esc), recorrible, persistente (1.4.13).

**Operable**
- [ ] `A-13` Todo funciona con teclado (2.1.1), sin trampas de foco (2.1.2).
- [ ] `A-14` Tiempos ajustables o avisados (2.2.1); pausar carruseles y animaciones automáticas > 5 s (2.2.2).
- [ ] `A-15` Nada parpadea más de 3 veces por segundo (2.3.1).
- [ ] `A-16` Skip link (2.4.1); `<title>` descriptivo por página/ruta (2.4.2).
- [ ] `A-17` Orden de foco lógico (2.4.3); propósito del link claro en contexto (2.4.4).
- [ ] `A-18` Foco **visible** (2.4.7) y **no tapado** (2.4.11).
- [ ] `A-19` Gestos y arrastres con alternativa (2.5.1, 2.5.7); objetivos ≥ 24 px (2.5.8).
- [ ] `A-20` El nombre accesible contiene el texto visible (2.5.3).

**Comprensible**
- [ ] `A-21` `lang` en `<html>` y en fragmentos de otro idioma (3.1.1, 3.1.2).
- [ ] `A-22` Nada cambia de contexto al enfocar o cambiar un valor sin aviso (3.2.1, 3.2.2).
- [ ] `A-23` Navegación e identificación consistentes (3.2.3, 3.2.4); ayuda consistente (3.2.6).
- [ ] `A-24` Errores identificados en texto, con sugerencia (3.3.1, 3.3.3); labels/instrucciones (3.3.2).
- [ ] `A-25` Prevención de errores en transacciones legales/financieras: revisar, confirmar o revertir (3.3.4).
- [ ] `A-26` Sin entradas redundantes (3.3.7); autenticación accesible (3.3.8).

**Robusto**
- [ ] `A-27` Nombre, rol y valor correctos en componentes custom (4.1.2): primero HTML nativo.
- [ ] `A-28` Mensajes de estado anunciados sin mover el foco (`role="status"`, `aria-live`) (4.1.3).

## Reglas de ARIA

1. **Primera regla de ARIA: no uses ARIA** si hay un elemento HTML nativo (`<button>`, `<a href>`, `<dialog>`, `<details>`, `<select>`, `<input type="checkbox">`).
2. Nunca `div` o `span` clickeables. Un `<button>` trae foco, Enter/Espacio y rol.
3. Link = navega (cambia URL). Botón = hace algo.
4. No cambies semántica nativa (`<h2 role="button">` no).
5. Todo elemento interactivo con rol ARIA tiene que ser operable con teclado.
6. No pongas `aria-hidden="true"` en elementos enfocables.
7. Todo control tiene nombre accesible.

### Patrones del APG que más se usan (y el atajo nativo)

| Componente | Nativo / moderno | Patrón APG |
|---|---|---|
| Modal | `<dialog>` + `showModal()` | [Dialog (Modal)](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/) |
| Acordeón | `<details name="grupo">` (exclusivo, Baseline 2024) | [Accordion](https://www.w3.org/WAI/ARIA/apg/patterns/accordion/) |
| Menú desplegable no modal | `popover` (Baseline 2025) + `<button popovertarget>` | [Disclosure](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/) |
| Tabs | — | [Tabs](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/) (flechas mueven, Tab sale) |
| Combobox / autocompletar | `<input list>` + `<datalist>` (limitado) | [Combobox](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/) |
| Menú de acciones (tipo app) | — | [Menu Button](https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/) |
| Switch | `<input type="checkbox" role="switch">` | [Switch](https://www.w3.org/WAI/ARIA/apg/patterns/switch/) |
| Tooltip | `popover="hint"` (solo Chromium) | [Tooltip](https://www.w3.org/WAI/ARIA/apg/patterns/tooltip/) |
| Carrusel | Evitalo si podés | [Carousel](https://www.w3.org/WAI/ARIA/apg/patterns/carousel/) (botón pausa obligatorio si rota) |

Para React, preferí primitivas probadas (React Aria, Radix, Base UI, Ariakit) antes que escribir el teclado a mano ([`../componentes/bibliotecas.md`](../componentes/bibliotecas.md)).

## Snippet: tabs accesibles (vanilla)

```html
<div class="tabs">
  <div role="tablist" aria-label="Plan">
    <button role="tab" id="t-m" aria-selected="true"  aria-controls="p-m">Mensual</button>
    <button role="tab" id="t-a" aria-selected="false" aria-controls="p-a" tabindex="-1">Anual</button>
  </div>
  <div role="tabpanel" id="p-m" aria-labelledby="t-m" tabindex="0">…</div>
  <div role="tabpanel" id="p-a" aria-labelledby="t-a" tabindex="0" hidden>…</div>
</div>
<script>
document.querySelectorAll('[role="tablist"]').forEach((list) => {
  const tabs = [...list.querySelectorAll('[role="tab"]')];
  const select = (t) => tabs.forEach((x) => {
    const on = x === t; x.setAttribute('aria-selected', on); x.tabIndex = on ? 0 : -1;
    document.getElementById(x.getAttribute('aria-controls')).hidden = !on; if (on) x.focus();
  });
  list.addEventListener('click', (e) => e.target.closest('[role="tab"]') && select(e.target.closest('[role="tab"]')));
  list.addEventListener('keydown', (e) => {
    const i = tabs.indexOf(document.activeElement);
    const map = { ArrowRight: i + 1, ArrowLeft: i - 1, Home: 0, End: tabs.length - 1 };
    if (e.key in map) { e.preventDefault(); select(tabs[(map[e.key] + tabs.length) % tabs.length]); }
  });
});
</script>
```

## Gestión del foco

- **Indicador visible siempre** con `:focus-visible`; nunca `outline: none` sin reemplazo.
- Al abrir modal: foco al primer elemento útil o al título; al cerrar: vuelve al disparador.
- Al cambiar de ruta (SPA): foco al `h1` (con `tabindex="-1"`) o anuncio del título.
- Al borrar un ítem de una lista: foco al siguiente ítem o al contenedor, no al `body`.
- Tras enviar un form con errores: foco al resumen de errores.
- `inert` en el contenido de fondo de overlays custom.
- `scroll-padding-top` para headers fijos (2.4.11).

```css
:root { --focus: oklch(0.72 0.17 70); }
:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; border-radius: 2px; }
html { scroll-padding-top: calc(var(--header-h, 4rem) + 1rem); }
.sr-only { position:absolute; width:1px; height:1px; padding:0; margin:-1px; overflow:hidden; clip:rect(0 0 0 0); white-space:nowrap; border:0; }
```

## Preferencias del sistema

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: .01ms !important; animation-iteration-count: 1 !important;
    transition-duration: .01ms !important; scroll-behavior: auto !important; }
}
@media (prefers-contrast: more) { :root { --border: var(--text); --muted: var(--text); } }
@media (forced-colors: active) { .btn { border: 1px solid ButtonText; } }
```
Además: modo oscuro con `prefers-color-scheme` y `color-scheme: light dark`; no dependas de imágenes de fondo para transmitir información.

## Accesibilidad cognitiva (COGA)

De la guía del W3C [*Making Content Usable for People with Cognitive and Learning Disabilities*](https://www.w3.org/TR/coga-usable/), que alimenta WCAG 3:
- Lenguaje claro, frases cortas, una idea por párrafo.
- Pasos claros, sin límites de tiempo, guardar progreso.
- Evitar distracciones (autoplay, popups) y no depender de la memoria.
- Ayuda fácil de encontrar; errores fáciles de evitar y corregir.

## Testing

1. **Automático** (encuentra una parte de los problemas, no todos): [axe-core](https://github.com/dequelabs/axe-core) (en Playwright/Jest: `@axe-core/playwright`), Lighthouse, WAVE, pa11y en CI.
2. **Teclado**: recorré todo el flujo solo con Tab, Shift+Tab, Enter, Espacio, flechas, Esc.
3. **Zoom 200 % y 400 %** (reflow a 320 px).
4. **Lector de pantalla**: VoiceOver (macOS/iOS), NVDA (Windows, gratis), TalkBack (Android).
5. **Contraste**: con las herramientas de `../paletas/`; revisá estados hover/disabled/focus.
6. **Personas con discapacidad** en tests de usabilidad: nada lo reemplaza.

```ts
// Playwright + axe
import { test, expect } from "@playwright/test";
import AxeBuilder from "@axe-core/playwright";
test("checkout sin violaciones WCAG A/AA", async ({ page }) => {
  await page.goto("/checkout");
  const r = await new AxeBuilder({ page }).withTags(["wcag2a", "wcag2aa", "wcag21aa", "wcag22aa"]).analyze();
  expect(r.violations).toEqual([]);
});
```

## Overlays de accesibilidad

Los widgets "un script y listo" no hacen accesible un sitio. En EE.UU. la FTC aprobó en abril de 2025 una orden final que obliga a accessiBe a pagar US$1 M por afirmaciones engañosas sobre cumplimiento WCAG ([National Law Review](https://natlawreview.com/article/ftc-settles-accessibe-misleading-statements-about-wcag-compliance)). Arreglá el código.

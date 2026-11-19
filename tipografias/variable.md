# Variables (fichas específicas)

2 familias en esta categoría. Catálogo armado en noviembre 2026 para el repo de diseño frontend. Solo se incluyen datos verificados (links oficiales que resolvieron, o —en el caso de Sharp Type— la URL canónica de la foundry, que respondió 429 por un challenge de bot, no 404).

Casi todas las familias modernas de este catálogo tienen corte variable; estas dos fichas son *variable-first*: el valor está en los ejes, no en un único estilo estático. El resto de las variables importantes (Fraunces, Bricolage, Mona Sans, Instrument Sans, Satoshi, Geist, Newsreader, Source Serif 4, Obviously, Roboto Flex) están documentadas en su categoría principal y se retoman al final de este archivo.

Regla de performance: si vas a usar tres o más pesos, una variable bien subseteada (OFL) suele pesar menos que varios archivos estáticos. Las Fontshare FFL **no permiten subsetear**; autohospedá el archivo oficial completo o usá solo los pesos que devuelve su CSS.

---

## 1. Recursive

- **Foundry:** Arrow Type / Google Fonts
- **Diseño:** Stephen Nixon (Arrow Type)
- **Licencia:** Gratis. SIL Open Font License, Google Fonts. Una sola familia variable cubre sans lineal y mono, con ejes de 'casual' y cursiva.
- **Link oficial:** https://fonts.google.com/specimen/Recursive
- **Estilo / personalidad:** Superfamilia variable: puede ser una sans de UI, una mono de código y una display informal moviendo ejes (MONO, CASL, CRSV, slnt, wght). Ideal para un design system económico con mucha voz.
- **Mejor uso:** Tech / devtools, SaaS, Dashboard / UI, Landing
- **Pesos / ejes:** Variable: wght, slnt, MONO, CRSV, CASL.
- **Variable:** Sí
- **Pareja recomendada:** Se puede usar sola como sistema. Si se busca contraste, Fraunces en el héroe.

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Recursive:slnt,wght@-15..0,300..1000&display=swap" rel="stylesheet">
/* font-family: "Recursive", sans-serif; */
```

## 2. Roboto Flex

- **Foundry:** Google / Font Bureau
- **Licencia:** Gratis. SIL Open Font License, Google Fonts. Versión variable 'paramétrica' de Roboto, con muchos ejes (peso, ancho, grado, tamaño óptico, etc.).
- **Link oficial:** https://fonts.google.com/specimen/Roboto+Flex
- **Estilo / personalidad:** No es una voz de marca por sí sola (Roboto ya está muy visto), pero como motor tipográfico variable es de lo más potente y gratis que hay: se puede afinar grado, ancho y optical size para UI densa o marketing.
- **Mejor uso:** Dashboard / UI, SaaS, Tech / devtools
- **Pesos / ejes:** Variable con muchos ejes (wght, wdth, opsz, GRAD y ejes paramétricos adicionales).
- **Variable:** Sí
- **Pareja recomendada:** Una display con carácter (Fraunces, Clash Display, Syne) para que el sistema no se sienta 'Material default'
- **Nota:** Las guías de pairing 2025 la combinan con Work Sans como stack variable de producto.

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto+Flex:opsz,wght@8..144,100..1000&display=swap" rel="stylesheet">
/* font-family: "Roboto Flex", sans-serif; */
```

---

## Otras variables del catálogo

Estas familias también son variables y tienen ficha en su categoría:

- **ABC Diatype** (`sans-grotesk`): https://abcdinamo.com/typefaces/diatype — Familia amplia, con variable en el ecosistema Dinamo.
- **Bricolage Grotesque** (`sans-grotesk`): https://fonts.google.com/specimen/Bricolage+Grotesque — Variable: ejes wght, opsz, wdth y GRAD. Hay un acompañante condensado.
- **Cabinet Grotesk** (`sans-grotesk`): https://www.fontshare.com/fonts/cabinet-grotesk — Nueve pesos, de Thin a ExtraBold; hay variable.
- **DM Sans** (`sans-grotesk`): https://fonts.google.com/specimen/DM+Sans — Variable, con cursivas. Forma sistema con DM Serif Display, DM Serif Text y DM Mono.
- **Figtree** (`sans-grotesk`): https://fonts.google.com/specimen/Figtree — Variable, con cursivas, varios pesos.
- **Geist** (`sans-grotesk`): https://fonts.google.com/specimen/Geist — Variable, Thin 100 a Black 900, con cursivas.
- **General Sans** (`sans-grotesk`): https://www.fontshare.com/fonts/general-sans — De Extralight a Extrabold, con cursivas; hay variable.
- **Instrument Sans** (`sans-grotesk`): https://fonts.google.com/specimen/Instrument+Sans — Variable: peso 400–700, ancho 75–100, cursivas.
- **Inter** (`sans-grotesk`): https://rsms.me/inter/ — Variable 100–900, con cursivas y ejes de display en las versiones recientes. También está en Google Fonts: https://fonts.google.com/specimen/Inter
- **Manrope** (`sans-grotesk`): https://fonts.google.com/specimen/Manrope — Variable, de ExtraLight a ExtraBold.
- **Mona Sans** (`sans-grotesk`): https://fonts.google.com/specimen/Mona+Sans — Variable: weight, width y slant.
- **Plus Jakarta Sans** (`sans-grotesk`): https://fonts.google.com/specimen/Plus+Jakarta+Sans — Variable, con cursivas; varios pesos de ExtraLight a ExtraBold.
- **Public Sans** (`sans-grotesk`): https://fonts.google.com/specimen/Public+Sans — Variable, de Thin a Black, con cursivas.
- **Roobert** (`sans-grotesk`): https://displaay.net/typeface/roobert/ — Colección proporcional + semimono + mono; hay variable.
- **Switzer** (`sans-grotesk`): https://www.fontshare.com/fonts/switzer — Familia amplia, con variable en Fontshare.
- **Aspekta** (`sans-geometrica`): https://github.com/ivodolenc/aspekta — Variable, 100–1000, con stylistic sets.
- **Cal Sans** (`sans-geometrica`): https://cal.com/font — Variable; consultar cortes en el repo oficial.
- **Clash Grotesk** (`sans-geometrica`): https://www.fontshare.com/fonts/clash-grotesk — Varios pesos; hay variable en Fontshare.
- **Degular** (`sans-geometrica`): https://ohnotype.co/fonts/degular — Familia Oh no, con anchos y pesos típicos de la foundry (consultar ficha).
- **Hubot Sans** (`sans-geometrica`): https://fonts.google.com/specimen/Hubot+Sans — Variable: weight, width, slant.
- **Onest** (`sans-geometrica`): https://fonts.google.com/specimen/Onest — Varios pesos; hay variable.
- **Outfit** (`sans-geometrica`): https://fonts.google.com/specimen/Outfit — Variable, Thin a Black.
- **Satoshi** (`sans-geometrica`): https://www.fontshare.com/fonts/satoshi — Variable, de Light a Black, con obliques.
- **Sora** (`sans-geometrica`): https://fonts.google.com/specimen/Sora — Varios pesos, de ExtraLight a ExtraBold; hay variable.
- **Space Grotesk** (`sans-geometrica`): https://fonts.google.com/specimen/Space+Grotesk — Cinco pesos; hay variable.
- **Boska** (`serif-display`): https://www.fontshare.com/fonts/boska — Varios pesos en Fontshare; consultar variable en la ficha.
- **Fraunces** (`serif-display`): https://fonts.google.com/specimen/Fraunces — Variable 100–900, opsz 9–144, más ejes SOFT y WONK.
- **Reckless** (`serif-display`): https://displaay.net/typeface/reckless/ — Familia (y ahora colección) con muchos estilos; incluye variable.
- **Zodiak** (`serif-display`): https://www.fontshare.com/fonts/zodiak — Familia Fontshare con varios pesos y cursivas; hay variable.
- **EB Garamond** (`serif-texto`): https://fonts.google.com/specimen/EB+Garamond — Varios pesos con cursivas (el eje llega a ExtraBold en la ficha actual).
- **Literata** (`serif-texto`): https://fonts.google.com/specimen/Literata — Variable, con opsz, cursivas y un rango amplio de pesos.
- **Lora** (`serif-texto`): https://fonts.google.com/specimen/Lora — Variable, con cursivas (Regular a Bold en la práctica, con eje de peso más amplio en variable).
- **Newsreader** (`serif-texto`): https://fonts.google.com/specimen/Newsreader — Variable, con opsz, pesos de ExtraLight a ExtraBold y cursivas.
- **Sentient** (`serif-texto`): https://www.fontshare.com/fonts/sentient — Familia Fontshare con varios pesos y cursivas.
- **Source Serif 4** (`serif-texto`): https://fonts.google.com/specimen/Source+Serif+4 — Variable, con opsz y cursivas; de ExtraLight a Black.
- **Berkeley Mono** (`mono`): https://usgraphics.com/products/berkeley-mono — Familia comercial, con variable y ligaduras como add-ons.
- **Geist Mono** (`mono`): https://fonts.google.com/specimen/Geist+Mono — Variable, Thin a Black.
- **JetBrains Mono** (`mono`): https://fonts.google.com/specimen/JetBrains+Mono — De Thin a ExtraBold, con cursivas; hay variable.
- **ABC Arizona Flare** (`display-experimental`): https://abcdinamo.com/typefaces/arizona — Colección Arizona (varios cortes; Flare es uno de ellos).
- **Clash Display** (`display-experimental`): https://www.fontshare.com/fonts/clash-display — Varios pesos (de Extralight a Bold en la ficha de Fontshare).
- **Melodrama** (`display-experimental`): https://www.fontshare.com/fonts/melodrama — Familia Fontshare de display; consultar pesos en la ficha.
- **Obviously** (`display-experimental`): https://ohnotype.co/fonts/obviously — Variable de peso y ancho (familia extensa de Oh no).
- **Panchang** (`display-experimental`): https://www.fontshare.com/fonts/panchang — Familia Fontshare, varios pesos; hay variable.
- **Shantell Sans** (`display-experimental`): https://fonts.google.com/specimen/Shantell+Sans — Variable, con cursivas y ejes de informalidad (consultar ficha: wght y ejes adicionales).
- **Syne** (`display-experimental`): https://fonts.google.com/specimen/Syne — Regular a ExtraBold; hay variable. Existe Syne Mono y Syne Tactile en el ecosistema.
- **Unbounded** (`display-experimental`): https://fonts.google.com/specimen/Unbounded — Variable, de Light a Black.

## Cómo pedir ejes en CSS

```css
/* Peso continuo */
h1 { font-family: "Fraunces", serif; font-weight: 600; font-optical-sizing: auto; }

/* Ejes no estándar (Fraunces: WONK y SOFT) */
h1 { font-variation-settings: "WONK" 1, "SOFT" 50; }

/* Ancho (Mona Sans, Instrument Sans, Obviously, Bricolage) */
.tight { font-stretch: 85%; }
```

Fraunces admite `WONK` (0 o 1, irregularidad de la itálica y de algunas letras) y `SOFT` (redondeo). Bricolage Grotesque mueve `wght`, `opsz`, `wdth` y `GRAD`. Recursive mueve `MONO`, `CASL`, `CRSV` y `slnt`. Roboto Flex expone un set paramétrico amplio (grado, ancho, optical size). Siempre confirmá los ejes en la ficha oficial antes de copiar valores.

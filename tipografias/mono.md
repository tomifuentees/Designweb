# Monoespaciadas

10 familias en esta categoría. Catálogo armado en noviembre 2026 para el repo de diseño frontend. Solo se incluyen datos verificados (links oficiales que resolvieron, o —en el caso de Sharp Type— la URL canónica de la foundry, que respondió 429 por un challenge de bot, no 404).

En 2026 la mono dejó de ser solo para código: es voz de marca en devtools, IA, data y labels. Geist Mono y JetBrains Mono son excelentes y, por eso mismo, empiezan a saturar el rubro. IBM Plex Mono, Commit Mono, Berkeley Mono (de pago, con licencia exigente) o una indie como Necto / Departure dan más carácter.

Usá la mono como acento (precio, eyebrow, snippet, numeración) o como sistema completo en un producto dev. Evitá ponerla en un párrafo de 400 palabras.

---

## 1. Berkeley Mono

- **Foundry:** U.S. Graphics Company
- **Licencia:** Comercial. Licencia comercial estricta: el plan Developer es personal; las licencias de empresa se cotizan por tamaño. El uso en apps open source, terminales o software embebido suele requerir un acuerdo custom. Leer la licencia antes de usarla en un producto.
- **Precio aproximado:** Developer 75 USD (uso personal en dispositivos de la empresa, sin uso comercial del producto). Comercial desde 225 USD (monotributista/sole proprietor), 495 USD (2–7 empleados), 845 USD (8–50). Add-ons: master fonts 50, webfonts 45, ligaduras 20, variable 25 USD.
- **Link oficial:** https://usgraphics.com/products/berkeley-mono
- **Estilo / personalidad:** Mono 'herramienta de ingeniero', de mucho prestigio en círculos de diseño y dev de EE. UU. Se siente cara y precisa. No es un lujo barato: la licencia es exigente.
- **Mejor uso:** Tech / devtools, SaaS, Dashboard / UI
- **Pesos / ejes:** Familia comercial, con variable y ligaduras como add-ons.
- **Variable:** Sí
- **Pareja recomendada:** Söhne o Untitled Sans

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "Berkeley Mono";
  src: url("/fonts/berkeley-mono-regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 2. Commit Mono

- **Foundry:** Commit Mono
- **Licencia:** Gratis. SIL Open Font License. Sitio oficial commitmono.com, se presenta como tipografía de programación neutra.
- **Link oficial:** https://commitmono.com/
- **Estilo / personalidad:** Mono de código, neutra y configurable. Alternativa menos 'marca Vercel/JetBrains' para docs y productos dev.
- **Mejor uso:** Tech / devtools, Dashboard / UI, SaaS
- **Pesos / ejes:** Familia de programación con varios pesos; consultar el configurador oficial.
- **Variable:** No
- **Pareja recomendada:** IBM Plex Sans o Mona Sans

Snippet de import:

```html
/* Descargá el WOFF2 oficial (OFL) y autohospedalo. Subsetear está permitido. */
@font-face {
  font-family: "Commit Mono";
  src: url("/fonts/commit-mono.woff2") format("woff2");
  font-weight: 100 900;
  font-style: normal;
  font-display: swap;
}
```

## 3. Departure Mono

- **Foundry:** Helena Zhang
- **Diseño:** Helena Zhang
- **Licencia:** Gratis. SIL Open Font License. Sitio oficial departuremono.com.
- **Link oficial:** https://departuremono.com/
- **Estilo / personalidad:** Mono pixel / lo-fi, de carácter fuerte. Las guías de pairing 2026 la combinan con Inter o con Instrument Serif para un contraste 'máquina / humano'. No es para cuerpo largo.
- **Mejor uso:** Tech / devtools, Landing, Editorial
- **Pesos / ejes:** Familia pixel mono (consultar estilos en el sitio).
- **Variable:** No
- **Pareja recomendada:** Inter o Instrument Serif

Snippet de import:

```html
/* Descargá el WOFF2 oficial (OFL) y autohospedalo. Subsetear está permitido. */
@font-face {
  font-family: "Departure Mono";
  src: url("/fonts/departure-mono.woff2") format("woff2");
  font-weight: 100 900;
  font-style: normal;
  font-display: swap;
}
```

## 4. DM Mono

- **Foundry:** Colophon Foundry / Google Fonts
- **Licencia:** Gratis. SIL Open Font License, Google Fonts. Forma sistema con DM Sans y DM Serif.
- **Link oficial:** https://fonts.google.com/specimen/DM+Mono
- **En uso real:** https://modal.com/ — Detectada en Modal, Cap, Dagster, Prefect, Tuple y ustwo (emblematic.dev/fonts).
- **Estilo / personalidad:** Mono geométrica, de pocas variantes, muy usable como acento de un sistema DM o como label de producto.
- **Mejor uso:** Tech / devtools, SaaS, Dashboard / UI
- **Pesos / ejes:** Light, Regular y Medium.
- **Variable:** No
- **Pareja recomendada:** DM Sans

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Mono:ital,wght@0,300;0,400;0,500;1,300;1,400;1,500&display=swap" rel="stylesheet">
/* font-family: "DM Mono", sans-serif; */
```

## 5. Fragment Mono

- **Foundry:** Google Fonts
- **Licencia:** Gratis. SIL Open Font License, Google Fonts.
- **Link oficial:** https://fonts.google.com/specimen/Fragment+Mono
- **Estilo / personalidad:** Mono menos transitada que JetBrains o Plex. Útil cuando se quiere un acento mono que no grite 'IA 2025'.
- **Mejor uso:** Tech / devtools, SaaS, Landing
- **Pesos / ejes:** Regular e Italic.
- **Variable:** No
- **Pareja recomendada:** Figtree o Onest

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fragment+Mono:ital@0;1&display=swap" rel="stylesheet">
/* font-family: "Fragment Mono", sans-serif; */
```

## 6. Geist Mono

- **Foundry:** Vercel / Basement Studio
- **Licencia:** Gratis. SIL Open Font License. Compañera de Geist, en Google Fonts y en el repo de Vercel.
- **Link oficial:** https://fonts.google.com/specimen/Geist+Mono
- **En uso real:** https://raycast.com/ — Detectada en Raycast, Spline, Neon, Coolify, ElevenLabs, Statsig y otros productos dev (emblematic.dev/fonts).
- **Estilo / personalidad:** Mono de producto, nítida y contemporánea. Muy usada en 2025-2026 como voz de marcas de IA y devtools. Buena; en riesgo de volverse default del rubro.
- **Mejor uso:** Tech / devtools, SaaS, Dashboard / UI
- **Pesos / ejes:** Variable, Thin a Black.
- **Variable:** Sí
- **Pareja recomendada:** Geist

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geist+Mono:wght@100..900&display=swap" rel="stylesheet">
/* font-family: "Geist Mono", sans-serif; */
```

## 7. IBM Plex Mono

- **Foundry:** IBM / Bold Monday
- **Licencia:** Gratis. SIL Open Font License. Parte de IBM Plex.
- **Link oficial:** https://fonts.google.com/specimen/IBM+Plex+Mono
- **En uso real:** https://huggingface.co/ — Detectada en Hugging Face, Sanity, WorkOS, Eight Sleep, Hex, dbt y LlamaIndex (emblematic.dev/fonts).
- **Estilo / personalidad:** Mono corporativa-técnica, un poco más 'IBM' y menos 'startup AI' que Geist Mono. Muy creíble en data, infra y enterprise.
- **Mejor uso:** Tech / devtools, SaaS, Dashboard / UI
- **Pesos / ejes:** De Thin a Bold, con cursivas.
- **Variable:** No
- **Pareja recomendada:** IBM Plex Sans

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,400;1,700&display=swap" rel="stylesheet">
/* font-family: "IBM Plex Mono", sans-serif; */
```

## 8. JetBrains Mono

- **Foundry:** JetBrains / Google Fonts
- **Licencia:** Gratis. SIL Open Font License. Diseñada por JetBrains para código; ligaduras opcionales.
- **Link oficial:** https://fonts.google.com/specimen/JetBrains+Mono
- **En uso real:** https://www.jetbrains.com/ — Tipografía de JetBrains. Emblematic también la detectó en Expo, Ghostty, Railway, Replicate, Attio y Upstash.
- **Estilo / personalidad:** Mono de programación, con altura de x alta y un dibujo amable. Excelente para docs, landings de devtools y para etiquetas de un design system.
- **Mejor uso:** Tech / devtools, SaaS, Dashboard / UI
- **Pesos / ejes:** De Thin a ExtraBold, con cursivas; hay variable.
- **Variable:** Sí
- **Pareja recomendada:** Mona Sans, General Sans o Cabinet Grotesk

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,100..800;1,100..800&display=swap" rel="stylesheet">
/* font-family: "JetBrains Mono", sans-serif; */
```

## 9. Necto Mono

- **Foundry:** Collletttivo
- **Diseño:** Marco Condello
- **Licencia:** Gratis. SIL Open Font License, con atribución. Catálogo Collletttivo.
- **Link oficial:** https://www.collletttivo.it/typefaces/necto-mono
- **Estilo / personalidad:** Mono indie italiana, más identitaria que una mono de código estándar. Buena para branding, no necesariamente para un IDE.
- **Mejor uso:** Tech / devtools, Landing, Editorial
- **Pesos / ejes:** Familia OFL de Collletttivo (consultar ficha).
- **Variable:** No
- **Pareja recomendada:** Apfel Grotezk

Snippet de import:

```html
/* Descargá el WOFF2 oficial (OFL) y autohospedalo. Subsetear está permitido. */
@font-face {
  font-family: "Necto Mono";
  src: url("/fonts/necto-mono-regular.woff2") format("woff2");
  font-weight: 100 900;
  font-style: normal;
  font-display: swap;
}
```

## 10. Space Mono

- **Foundry:** Colophon Foundry / Google Fonts
- **Licencia:** Gratis. SIL Open Font License, Google Fonts. Diseñada por Colophon. Tiene hermana proporcional: Space Grotesk.
- **Link oficial:** https://fonts.google.com/specimen/Space+Mono
- **Estilo / personalidad:** Mono display, más rara y 'poster' que una mono de código. Ideal para labels, precios, hero y sistemas de identidad tech-retro, no para un editor de 12px.
- **Mejor uso:** Tech / devtools, Landing, Editorial
- **Pesos / ejes:** Regular y Bold, con cursivas.
- **Variable:** No
- **Pareja recomendada:** Space Grotesk

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Mono:ital,wght@0,400;0,700;1,400;1,700&display=swap" rel="stylesheet">
/* font-family: "Space Mono", sans-serif; */
```

---

## Sumadas el 20 de noviembre de 2026

Fuentes de Google Fonts (SIL OFL) que entraron para las parejas 29–42 de [`pairings.md`](./pairings.md). El diseñador, los ejes y el ranking de popularidad salen del dataset de [ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) (MIT); la descripción es propia.

## 11. Fira Code

- **Diseño:** The Mozilla Foundation, Telefonica S.A., Nikita Prokopov
- **Licencia:** Gratis. SIL Open Font License, Google Fonts.
- **Link oficial:** https://fonts.google.com/specimen/Fira+Code
- **Estilo / personalidad:** Mono derivada de Fira Mono con ligaduras de programación (Nikita Prokopov).
- **Mejor uso:** Código, Dashboard, Devtools
- **Pesos / ejes:** Variable (wght: 300..700)
- **Variable:** Sí
- **Pareja recomendada:** Fira Sans
- **Nota:** Ranking de popularidad en Google Fonts: 60 (dataset de ui-ux-pro-max-skill, nov. 2026).

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@300..700&display=swap" rel="stylesheet">
/* font-family: "Fira Code", monospace; */
```


# Sans geométrica

16 familias en esta categoría. Catálogo armado en noviembre 2026 para el repo de diseño frontend. Solo se incluyen datos verificados (links oficiales que resolvieron, o —en el caso de Sharp Type— la URL canónica de la foundry, que respondió 429 por un challenge de bot, no 404).

Las geométricas construyen un look más 'diseñado' que una grotesca pura: círculos, terminales limpios, un poco de pretensión moderna. Satoshi, Clash Grotesk, Space Grotesk y las PP (Mori, Agrandir, Neue Montreal está en grotesk pero convive acá) son el vocabulario de muchas landings buenas de 2025-2026.

Cuidado con dos trampas: Circular ya está muy asociada a Spotify, y Outfit/Poppins/Montserrat se leen como default de template. Si usás una geométrica de Google Fonts, contrastala con una serif o un mono que tenga carácter.

---

## 1. Aeonik

- **Foundry:** CoType Foundry
- **Licencia:** Comercial. Licencias desktop, web, app y trial en CoType Foundry.
- **Precio aproximado:** Aeonik Full Family, licencia desktop hasta 2 workstations, 336 GBP (shop de CoType, consultado 2026).
- **Link oficial:** https://cotypefoundry.com/our-fonts/aeonik
- **Estilo / personalidad:** Geométrica distintiva, de las más mencionadas en r/webdesign como 'rising star' de producto digital. Formas muy reconocibles; hay que usarla con oficio para que no se vea de moda pasajera.
- **Mejor uso:** Landing, SaaS, Tech / devtools
- **Pesos / ejes:** Familia completa (hay Soft Pro y recortes adicionales en el catálogo CoType).
- **Variable:** No
- **Pareja recomendada:** Newsreader o General Sans

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "Aeonik";
  src: url("/fonts/aeonik-regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 2. Agrandir

- **Foundry:** Pangram Pangram Foundry
- **Licencia:** Comercial. Comercial, free-to-try. Pangram la presenta como familia muy extensa (la ficha oficial habla de 74 estilos).
- **Precio aproximado:** Licencias comerciales Pangram desde 40 USD; confirmar el paquete de Agrandir en la ficha.
- **Link oficial:** https://pangrampangram.com/products/agrandir
- **Estilo / personalidad:** Sans display-geométrica de muchísimos recortes (tight, regular, wide, etc.). Ideal para sistemas de marca expresivos, no para un cuerpo largo.
- **Mejor uso:** Landing, Lujo, Editorial
- **Pesos / ejes:** Hasta 74 estilos según la ficha oficial de Pangram.
- **Variable:** No
- **Pareja recomendada:** Neue Montreal o Editorial New

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "PP Agrandir";
  src: url("/fonts/pp-agrandir-regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 3. Apfel Grotezk

- **Foundry:** Collletttivo
- **Diseño:** Luigi Gorlero
- **Licencia:** Gratis. SIL Open Font License, con atribución. Catálogo y licencia en collletttivo.it.
- **Link oficial:** https://www.collletttivo.it/typefaces/apfel-grotezk
- **Estilo / personalidad:** Sans geométrica-grotesca indie, de dibujo más raro y europeo que las de Google Fonts. Muy útil para salirse del look 'IA' sin pagar foundry.
- **Mejor uso:** Landing, Editorial, Tech / devtools
- **Pesos / ejes:** Familia OFL de Collletttivo (consultar pesos en la ficha oficial).
- **Variable:** No
- **Pareja recomendada:** Sprat o Necto Mono (misma foundry)

Snippet de import:

```html
/* Descargá el WOFF2 oficial (OFL) y autohospedalo. Subsetear está permitido. */
@font-face {
  font-family: "Apfel Grotezk";
  src: url("/fonts/apfel-grotezk-regular.woff2") format("woff2");
  font-weight: 100 900;
  font-style: normal;
  font-display: swap;
}
```

## 4. Aspekta

- **Foundry:** Ivo Dolenc
- **Diseño:** Ivo Dolenc
- **Licencia:** Gratis. SIL Open Font License 1.1. Repo oficial: github.com/ivodolenc/aspekta (estáticos y variable, pesos 100–1000).
- **Link oficial:** https://github.com/ivodolenc/aspekta
- **Estilo / personalidad:** Geométrica variable de dibujo fresco, citada en r/webdesign 2025. Buena opción cuando se quiere algo menos transitado que las de Google Fonts de siempre.
- **Mejor uso:** SaaS, Landing, Tech / devtools
- **Pesos / ejes:** Variable, 100–1000, con stylistic sets.
- **Variable:** Sí
- **Pareja recomendada:** Newsreader o IBM Plex Mono

Snippet de import:

```html
/* Descargá el WOFF2 oficial (OFL) y autohospedalo. Subsetear está permitido. */
@font-face {
  font-family: "Aspekta";
  src: url("/fonts/aspekta-variable.woff2") format("woff2");
  font-weight: 100 900;
  font-style: normal;
  font-display: swap;
}
```

## 5. Cal Sans

- **Foundry:** Cal.com / WORDMARK
- **Diseño:** Mark Davis (WORDMARK)
- **Licencia:** Gratis. SIL Open Font License. Repositorio oficial github.com/calcom/sans y página cal.com/font.
- **Link oficial:** https://cal.com/font
- **En uso real:** https://cal.com/ — Es la tipografía de Cal.com, presentada en cal.com/font.
- **Estilo / personalidad:** Sans geométrica minimalista, pensada para producto. En r/webdesign 2025 la citaron como rising star de estética 'linear / minimal'.
- **Mejor uso:** SaaS, Tech / devtools, Dashboard / UI, Landing
- **Pesos / ejes:** Variable; consultar cortes en el repo oficial.
- **Variable:** Sí
- **Pareja recomendada:** Inter o Geist como cuerpo de UI, o un mono para el stack dev

Snippet de import:

```html
/* Descargá el WOFF2 oficial (OFL) y autohospedalo. Subsetear está permitido. */
@font-face {
  font-family: "Cal Sans";
  src: url("/fonts/cal-sans-variable.woff2") format("woff2");
  font-weight: 100 900;
  font-style: normal;
  font-display: swap;
}
```

## 6. Circular

- **Foundry:** Lineto
- **Licencia:** Comercial. Licencia comercial Lineto, en CHF. No es una fuente 'tipo Spotify para copiar': si se usa, hay que licenciarla.
- **Precio aproximado:** La familia de 16 cortes empieza en 840 CHF (página de pricing de Lineto, consultada 2026).
- **Link oficial:** https://lineto.com/typefaces/circular
- **Estilo / personalidad:** Geométrica redondeada, muy asociada al branding de producto de la década pasada (en particular a Spotify). Sigue siendo excelente, pero ya tiene connotaciones de marca ajenas.
- **Mejor uso:** SaaS, Landing, Lujo
- **Pesos / ejes:** 16 cortes en la familia principal.
- **Variable:** No
- **Pareja recomendada:** Una serif editorial como Canela, o un mono discreto
- **Nota:** Incluida por su peso histórico y por Typewolf. No es un atajo 'anti-IA' si el cliente la lee como 'la de Spotify'.

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "Circular";
  src: url("/fonts/circular-book.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 7. Clash Grotesk

- **Foundry:** Indian Type Foundry / Fontshare
- **Licencia:** Gratis. ITF Free Font License (FFL) 2.0: uso comercial gratis, sin modificar ni redistribuir el archivo.
- **Link oficial:** https://www.fontshare.com/fonts/clash-grotesk
- **Estilo / personalidad:** La hermana de texto/título de Clash Display: geométrica, un poco squarish, con actitud tech. Más usable en UI que el Display, menos gritona.
- **Mejor uso:** SaaS, Landing, Tech / devtools
- **Pesos / ejes:** Varios pesos; hay variable en Fontshare.
- **Variable:** Sí
- **Pareja recomendada:** Zodiak o Satoshi

Snippet de import:

```html
<link href="https://api.fontshare.com/v2/css?f[]=clash-grotesk@300,400,500,600,700&display=swap" rel="stylesheet">
/* font-family: "Clash Grotesk", sans-serif; */
/* Preferí autohospedar los archivos oficiales. La API de Fontshare no garantiza uptime.
   La licencia FFL no permite subsetear ni convertir el archivo. */
```

## 8. Degular

- **Foundry:** Oh no Type Co.
- **Licencia:** Comercial. Licencia comercial de Oh no Type (James Edmondson).
- **Precio aproximado:** Comercial; consultar en ohnotype.co.
- **Link oficial:** https://ohnotype.co/fonts/degular
- **Estilo / personalidad:** Sans suave, un poco redonda y muy de marca contemporánea estadounidense. Menos agresiva que Obviously; excelente para producto de consumo y D2C.
- **Mejor uso:** Landing, SaaS, Lujo
- **Pesos / ejes:** Familia Oh no, con anchos y pesos típicos de la foundry (consultar ficha).
- **Variable:** Sí
- **Pareja recomendada:** Fraunces o una serif suave como Reckless

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "Degular";
  src: url("/fonts/degular-regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 9. GT Walsheim

- **Foundry:** Grilli Type
- **Licencia:** Comercial. Licencia comercial Grilli Type.
- **Precio aproximado:** 75 USD por estilo; familia (32 estilos) 720 USD; subfamilias desde 480 USD (shop Grilli, 2026).
- **Link oficial:** https://www.grillitype.com/font/gt-walsheim
- **Estilo / personalidad:** Geométrica de raigambre europea, amable y redonda, muy reconocible. Sirve para marcas cercanas que no quieren parecer 'startup Inter'.
- **Mejor uso:** Landing, SaaS, Editorial
- **Pesos / ejes:** 32 estilos en la familia completa.
- **Variable:** No
- **Pareja recomendada:** GT Super o GT Alpina

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "GT Walsheim";
  src: url("/fonts/gt-walsheim-regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 10. Hubot Sans

- **Foundry:** GitHub / Google Fonts
- **Licencia:** Gratis. SIL Open Font License 1.1. Variable de peso, ancho y slant. Presentada junto a Mona Sans.
- **Link oficial:** https://fonts.google.com/specimen/Hubot+Sans
- **En uso real:** https://github.com/ — Compañera de Mona Sans en la identidad de GitHub (github.blog, 2022, y Google Fonts).
- **Estilo / personalidad:** Más geométrica y 'robot' que Mona, con eje de ancho. Excelente para títulos, números y un look dev sin caer en la mono por default.
- **Mejor uso:** Tech / devtools, SaaS, Landing
- **Pesos / ejes:** Variable: weight, width, slant.
- **Variable:** Sí
- **Pareja recomendada:** Mona Sans

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Hubot+Sans:wdth,wght@75..125,200..900&display=swap" rel="stylesheet">
/* font-family: "Hubot Sans", sans-serif; */
```

## 11. Onest

- **Foundry:** Google Fonts
- **Licencia:** Gratis. SIL Open Font License, Google Fonts.
- **Link oficial:** https://fonts.google.com/specimen/Onest
- **Estilo / personalidad:** Geométrica discreta, de las 'quiet sans' que las guías de 2026 recomiendan para UI cuando Inter se siente clínica. Buena como cuerpo de un sistema con un display más raro.
- **Mejor uso:** SaaS, Dashboard / UI, Landing
- **Pesos / ejes:** Varios pesos; hay variable.
- **Variable:** Sí
- **Pareja recomendada:** Fraunces o Bricolage Grotesque

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Onest:wght@100..900&display=swap" rel="stylesheet">
/* font-family: "Onest", sans-serif; */
```

## 12. Outfit

- **Foundry:** Google Fonts
- **Licencia:** Gratis. SIL Open Font License, Google Fonts.
- **Link oficial:** https://fonts.google.com/specimen/Outfit
- **Estilo / personalidad:** Geométrica simple y redondeada, muy usable. En r/webdesign 2025 la mencionaron como un go-to de muchos diseñadores. Ojo: ya camina hacia territorio 'default'; usarla con una serif o un mono la salva.
- **Mejor uso:** SaaS, Landing, Dashboard / UI
- **Pesos / ejes:** Variable, Thin a Black.
- **Variable:** Sí
- **Pareja recomendada:** Young Serif / Newsreader o JetBrains Mono

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap" rel="stylesheet">
/* font-family: "Outfit", sans-serif; */
```

## 13. PP Mori

- **Foundry:** Pangram Pangram Foundry
- **Licencia:** Comercial. Comercial, free-to-try. Licencias Pangram desde 40 USD en el catálogo general.
- **Precio aproximado:** Una ficha de tienda la listaba a 60 USD; las licencias Pangram parten de 40 USD. Confirmar en la ficha de Mori.
- **Link oficial:** https://pangrampangram.com/products/mori
- **Estilo / personalidad:** Sans geométrica premium, de las rising stars citadas en r/webdesign 2025. Se siente de marca cara, con un dibujo más particular que Neue Montreal.
- **Mejor uso:** Landing, Lujo, SaaS
- **Pesos / ejes:** Familia comercial Pangram (varios estilos).
- **Variable:** No
- **Pareja recomendada:** Editorial New o Agrandir (misma foundry, con cuidado de no saturar de PP)

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "PP Mori";
  src: url("/fonts/pp-mori-regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 14. Satoshi

- **Foundry:** Indian Type Foundry / Fontshare
- **Diseño:** Deni Anggara
- **Licencia:** Gratis. ITF Free Font License (FFL) 2.0: uso personal y comercial gratis. Prohibido modificar, subsetear, convertir o redistribuir el archivo. Autohospedaje permitido. La API no garantiza uptime.
- **Link oficial:** https://www.fontshare.com/fonts/satoshi
- **En uso real:** https://www.beehiiv.com/ — Detectada en beehiiv, Dub, Plane, Shortcut, Trigger.dev y el propio Fontshare (emblematic.dev/fonts).
- **Estilo / personalidad:** Sans modernista, geométrica con detalles más amables que una grotesca fría. Funciona en título y en cuerpo. Es la alternativa gratis más citada a Inter en diseño de producto 2024-2026.
- **Mejor uso:** SaaS, Landing, Dashboard / UI
- **Pesos / ejes:** Variable, de Light a Black, con obliques.
- **Variable:** Sí
- **Pareja recomendada:** Clash Display
- **Nota:** Familia más vista del catálogo Fontshare en un snapshot de agosto 2026 (más de 100 mil vistas, por encima de Clash Display y General Sans).

Snippet de import:

```html
<link href="https://api.fontshare.com/v2/css?f[]=satoshi@300,400,500,700,900&display=swap" rel="stylesheet">
/* font-family: "Satoshi", sans-serif; */
/* Preferí autohospedar los archivos oficiales. La API de Fontshare no garantiza uptime.
   La licencia FFL no permite subsetear ni convertir el archivo. */
```

## 15. Sora

- **Foundry:** Google Fonts
- **Licencia:** Gratis. SIL Open Font License, Google Fonts.
- **Link oficial:** https://fonts.google.com/specimen/Sora
- **Estilo / personalidad:** Geométrica contemporánea, citada en r/webdesign 2025 como cada vez más presente en branding de startups. Un poco más rara que Outfit, buena para títulos de producto.
- **Mejor uso:** Landing, SaaS, Tech / devtools
- **Pesos / ejes:** Varios pesos, de ExtraLight a ExtraBold; hay variable.
- **Variable:** Sí
- **Pareja recomendada:** Newsreader o IBM Plex Sans

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@100..800&display=swap" rel="stylesheet">
/* font-family: "Sora", sans-serif; */
```

## 16. Space Grotesk

- **Foundry:** Florian Karsten / Google Fonts
- **Diseño:** Florian Karsten
- **Licencia:** Gratis. SIL Open Font License, Google Fonts.
- **Link oficial:** https://fonts.google.com/specimen/Space+Grotesk
- **Estilo / personalidad:** Hermana proporcional de Space Mono: curvas un poco cuadradas, sabor técnico y retro-futurista. Sigue fuerte en marcas tech que quieren verse 'construidas'.
- **Mejor uso:** Tech / devtools, SaaS, Landing
- **Pesos / ejes:** Cinco pesos; hay variable.
- **Variable:** Sí
- **Pareja recomendada:** Space Mono o Newsreader
- **Nota:** Aparece en las tendencias 2026 junto a Bricolage y Syne como grotesca con trampas de tinta / carácter.

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300..700&display=swap" rel="stylesheet">
/* font-family: "Space Grotesk", sans-serif; */
```

---

## Sumadas el 20 de noviembre de 2026

Fuentes de Google Fonts (SIL OFL) que entraron para las parejas 29–42 de [`pairings.md`](./pairings.md). El diseñador, los ejes y el ranking de popularidad salen del dataset de [ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) (MIT); la descripción es propia.

## 17. Lexend

- **Diseño:** Bonnie Shaver-Troup, Thomas Jockin, Santiago Orozco, Héctor Gómez, Superunion
- **Licencia:** Gratis. SIL Open Font License, Google Fonts.
- **Link oficial:** https://fonts.google.com/specimen/Lexend
- **Estilo / personalidad:** Geométrica ancha, diseñada a partir de investigación sobre fluidez de lectura (Bonnie Shaver-Troup). Clara en tamaños chicos, con un aire amable y serio a la vez.
- **Mejor uso:** Salud, Gobierno, Educación, Dashboard
- **Pesos / ejes:** Variable (wght: 100..900)
- **Variable:** Sí
- **Pareja recomendada:** Source Sans 3 o Source Serif 4
- **Nota:** Ranking de popularidad en Google Fonts: 98 (dataset de ui-ux-pro-max-skill, nov. 2026).

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lexend:wght@100..900&display=swap" rel="stylesheet">
/* font-family: "Lexend", sans-serif; */
```

## 18. Jost

- **Diseño:** Owen Earl
- **Licencia:** Gratis. SIL Open Font License, Google Fonts.
- **Link oficial:** https://fonts.google.com/specimen/Jost
- **Estilo / personalidad:** Geométrica de inspiración Futura (Owen Earl), variable. Clásica y limpia; el par natural de una didona.
- **Mejor uso:** Lujo, Marca, Landing
- **Pesos / ejes:** Variable (wght: 100..900)
- **Variable:** Sí
- **Pareja recomendada:** Bodoni Moda
- **Nota:** Ranking de popularidad en Google Fonts: 16 (dataset de ui-ux-pro-max-skill, nov. 2026). Muy usada: tratala como cuerpo, no como voz de marca.

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Jost:wght@100..900&display=swap" rel="stylesheet">
/* font-family: "Jost", sans-serif; */
```

## 19. Nunito

- **Diseño:** Vernon Adams, Cyreal, Jacques Le Bailly
- **Licencia:** Gratis. SIL Open Font License, Google Fonts.
- **Link oficial:** https://fonts.google.com/specimen/Nunito
- **Estilo / personalidad:** Sans redondeada muy popular (Vernon Adams y otros). Amable; por su popularidad, usala como cuerpo, no como voz.
- **Mejor uso:** Kids, Bienestar, Apps
- **Pesos / ejes:** Variable (wght: 200..1000)
- **Variable:** Sí
- **Pareja recomendada:** Fredoka
- **Nota:** Ranking de popularidad en Google Fonts: 15 (dataset de ui-ux-pro-max-skill, nov. 2026). Muy usada: tratala como cuerpo, no como voz de marca.

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@200..1000&display=swap" rel="stylesheet">
/* font-family: "Nunito", sans-serif; */
```


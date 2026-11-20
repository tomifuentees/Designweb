# Sans grotesk / neo-grotesk

31 familias en esta categoría. Catálogo armado en noviembre 2026 para el repo de diseño frontend. Solo se incluyen datos verificados (links oficiales que resolvieron, o —en el caso de Sharp Type— la URL canónica de la foundry, que respondió 429 por un challenge de bot, no 404).

Las grotescas (y neo-grotescas) son el caballo de batalla del producto digital: neutras, legibles, fáciles de sistematizar. El riesgo, en 2026, es que *neutra* se lea como *genérica*. Inter, y cada vez más Geist, cumplen muy bien en UI, pero no pueden ser la voz de todas las marcas.

Esta lista mezcla foundries de pago que hoy dominan Typewolf (Klim, Dinamo, Pangram, Grilli, Swiss Typefaces, Commercial Type) con alternativas gratis de oficio (Fontshare, Google Fonts, GitHub, IBM, USWDS). La regla práctica: si el presupuesto alcanza, licenciá una grotesca de foundry para la marca y dejá una OFL para la UI densa. Si no alcanza, elegí Cabinet Grotesk, Switzer, Mona Sans o Bricolage antes que Inter por default.

---

## 1. ABC Diatype

- **Foundry:** Dinamo Typefaces
- **Licencia:** Comercial. Licenciamiento Dinamo por tamaño de empresa.
- **Precio aproximado:** Pack de estudiante listaba la familia a 504 EUR (50% off), o sea alrededor de 1.008 EUR la familia completa a precio estándar. Confirmar en Dinamo.
- **Link oficial:** https://abcdinamo.com/typefaces/diatype
- **En uso real:** https://modal.com/ — Detectada en Modal, Speakeasy, ustwo y Creative Boom (emblematic.dev/fonts).
- **Estilo / personalidad:** Sans técnica y un poco rectangular, con sabor a señalética y a producto. Muy creíble en herramientas para developers y en marcas 'built, not decorated'.
- **Mejor uso:** Tech / devtools, SaaS, Dashboard / UI, Landing
- **Pesos / ejes:** Familia amplia, con variable en el ecosistema Dinamo.
- **Variable:** Sí
- **Pareja recomendada:** IBM Plex Mono o Geist Mono

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "ABC Diatype";
  src: url("/fonts/abc-diatype-regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 2. ABC Oracle

- **Foundry:** Dinamo Typefaces
- **Licencia:** Comercial. Licenciamiento Dinamo por tamaño de empresa.
- **Precio aproximado:** Comercial; consultar precio según tamaño de empresa en Dinamo.
- **Link oficial:** https://abcdinamo.com/typefaces/oracle
- **En uso real:** https://arc.net/ — Emblematic la asocia a Arc (arc.net), Dia y al propio sitio de Dinamo. Documentación no oficial de sistemas de diseño también la menciona en Arc.
- **Estilo / personalidad:** Sans de contornos suaves y contraste sutil, pensada para texto editorial y producto a la vez. Menos 'UI default' que Inter, más humana.
- **Mejor uso:** SaaS, Editorial, Tech / devtools, Landing
- **Pesos / ejes:** Varios pesos, cursivas y alternates.
- **Variable:** No
- **Pareja recomendada:** Feature o Newsreader

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "ABC Oracle";
  src: url("/fonts/abc-oracle-regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 3. Aperçu

- **Foundry:** Colophon Foundry
- **Licencia:** Comercial. Hoy se licencia sobre todo a través de MyFonts / Monotype. La ficha de tipo en colophon-foundry.org/typefaces/apercu devolvió 404; el sitio de la foundry sigue en línea.
- **Precio aproximado:** Alrededor de 60 USD por estilo, o 768 USD la familia completa de 16 estilos en MyFonts (consultado en reseñas de 2026). Confirmar al comprar.
- **Link oficial:** https://www.myfonts.com/collections/apercu-font-colophon-foundry
- **En uso real:** https://www.wired.com/ — Typewolf la ubica como la sans más popular de su ranking 2026. Emblematic la detectó en WIRED, Glossier y GRAZA. También se ha citado su uso en MoMA y Zeit.
- **Estilo / personalidad:** Humanista-grotesca de trazo uniforme y aire casual. Queda especialmente bien con ilustración geométrica y composiciones minimalistas.
- **Mejor uso:** Editorial, Landing, Lujo
- **Pesos / ejes:** Familia de 16 estilos.
- **Variable:** No
- **Pareja recomendada:** Editorial New o Feature
- **Nota:** En 2026 Typewolf la sitúa por encima de Futura en su top de sans. El nombre oficial se escribe Aperçu / Apercu según la ficha.

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "Apercu";
  src: url("/fonts/apercu-regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 4. Atkinson Hyperlegible

- **Foundry:** Braille Institute / Google Fonts
- **Licencia:** Gratis. SIL Open Font License. Diseñada con el Braille Institute para maximizar la distinción entre caracteres. También existe Atkinson Hyperlegible Next en Google Fonts.
- **Link oficial:** https://fonts.google.com/specimen/Atkinson+Hyperlegible
- **Estilo / personalidad:** Sans de accesibilidad: letras muy diferenciadas (I, l, 1, O, 0). No es 'fea'; es clara. Imprescindible en salud, educación, sector público y cualquier producto que no pueda permitirse ambigüedad.
- **Mejor uso:** Dashboard / UI, SaaS
- **Pesos / ejes:** La familia original trae pocos estilos (Regular, Bold y cursivas). Next amplía el rango: https://fonts.google.com/specimen/Atkinson+Hyperlegible+Next
- **Variable:** No
- **Pareja recomendada:** Source Serif 4 o Lexend (si todo el sistema es de baja visión)
- **Nota:** Las guías de tipografía 2026 la agrupan con Inclusive Sans y Lexend como tipografías 'accessibility-first'.

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&display=swap" rel="stylesheet">
/* font-family: "Atkinson Hyperlegible", sans-serif; */
```

## 5. Atlas Grotesk

- **Foundry:** Commercial Type
- **Diseño:** Kai Bernau, Susana Carvalho y Christian Schwartz
- **Licencia:** Comercial. Licencia comercial de Commercial Type.
- **Precio aproximado:** Comercial; consultar en Commercial Type.
- **Link oficial:** https://commercialtype.com/catalog/atlas
- **En uso real:** https://www.dropbox.com/ — Detectada en Dropbox, The Pudding, Aeon, Asterisk y Reclaim (emblematic.dev/fonts).
- **Estilo / personalidad:** Grotesca de trabajo, un poco más cálida y con más 'aire de revista' que Graphik. Muy creíble en producto y en editorial digital.
- **Mejor uso:** SaaS, Editorial, Dashboard / UI
- **Pesos / ejes:** Seis pesos con cursivas en Atlas Grotesk; la colección Atlas incluye Typewriter y otros cortes.
- **Variable:** No
- **Pareja recomendada:** Newsreader o Canela

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "Atlas Grotesk";
  src: url("/fonts/atlas-grotesk-regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 6. Bricolage Grotesque

- **Foundry:** Mathieu Triay / Google Fonts
- **Diseño:** Mathieu Triay
- **Licencia:** Gratis. SIL Open Font License, Google Fonts. Se puede subsetear y autohospedar.
- **Link oficial:** https://fonts.google.com/specimen/Bricolage+Grotesque
- **Estilo / personalidad:** Grotesca con trampas de tinta y mucha flexibilidad: peso, tamaño óptico, ancho y grade. Los pesos display son expresivos; los de texto, serviciales. Es una de las mejores gratis 'anti-IA' de 2025-2026.
- **Mejor uso:** Landing, Editorial, SaaS
- **Pesos / ejes:** Variable: ejes wght, opsz, wdth y GRAD. Hay un acompañante condensado.
- **Variable:** Sí
- **Pareja recomendada:** Fraunces o Newsreader
- **Nota:** Listados de tendencias 2026 la agrupan con Space Grotesk y Syne como grotescas con carácter.

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,200..800&display=swap" rel="stylesheet">
/* font-family: "Bricolage Grotesque", sans-serif; */
```

## 7. Cabinet Grotesk

- **Foundry:** Indian Type Foundry / Fontshare
- **Licencia:** Gratis. ITF Free Font License (FFL) 2.0: uso comercial gratis, sin modificar ni redistribuir el archivo. Autohospedaje permitido.
- **Link oficial:** https://www.fontshare.com/fonts/cabinet-grotesk
- **Estilo / personalidad:** Grotesca con rarezas controladas (la g, la R, la a). En display tiene carácter; en cuerpo se bankea. Es de las mejores alternativas gratis a Inter cuando se busca que alguien pregunte 'qué fuente es'.
- **Mejor uso:** SaaS, Landing, Editorial
- **Pesos / ejes:** Nueve pesos, de Thin a ExtraBold; hay variable.
- **Variable:** Sí
- **Pareja recomendada:** DM Sans o Source Serif 4
- **Nota:** Muy citada en listados de UI 2025-2026 y cuarta más vista en Fontshare (snapshot agosto 2026).

Snippet de import:

```html
<link href="https://api.fontshare.com/v2/css?f[]=cabinet-grotesk@100,300,400,500,700,800&display=swap" rel="stylesheet">
/* font-family: "Cabinet Grotesk", sans-serif; */
/* Preferí autohospedar los archivos oficiales. La API de Fontshare no garantiza uptime.
   La licencia FFL no permite subsetear ni convertir el archivo. */
```

## 8. DM Sans

- **Foundry:** Colophon Foundry / Google Fonts
- **Licencia:** Gratis. SIL Open Font License, Google Fonts.
- **Link oficial:** https://fonts.google.com/specimen/DM+Sans
- **Estilo / personalidad:** Sans geométrica-grotesca de bajo contraste, diseñada por Colophon. Muy legible, un poco más 'branded' que Inter, aunque ya está bastante vista.
- **Mejor uso:** SaaS, Dashboard / UI, Landing
- **Pesos / ejes:** Variable, con cursivas. Forma sistema con DM Serif Display, DM Serif Text y DM Mono.
- **Variable:** Sí
- **Pareja recomendada:** DM Serif Display o Cabinet Grotesk

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,100..1000;1,9..40,100..1000&display=swap" rel="stylesheet">
/* font-family: "DM Sans", sans-serif; */
```

## 9. Favorit

- **Foundry:** Dinamo Typefaces
- **Licencia:** Comercial. Licenciamiento Dinamo por tamaño de empresa.
- **Precio aproximado:** Pack de estudiante 50% off listaba la familia completa a 405 EUR, lo que implica un precio estándar de familia en torno a 810 EUR. Confirmar en Dinamo.
- **Link oficial:** https://abcdinamo.com/typefaces/favorit
- **Estilo / personalidad:** Grotesca redondeada con un aire funcional y un poco naíf. Menos seria que Monument, muy reconocible en branding cultural y tech amable.
- **Mejor uso:** Landing, SaaS, Editorial
- **Pesos / ejes:** Familia completa; hay cortes mono y otras extensiones en el catálogo ABC Favorit.
- **Variable:** No
- **Pareja recomendada:** Editorial New o Fraunces

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "ABC Favorit";
  src: url("/fonts/abc-favorit-regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 10. Figtree

- **Foundry:** Erik Kennedy / Google Fonts
- **Licencia:** Gratis. SIL Open Font License, Google Fonts.
- **Link oficial:** https://fonts.google.com/specimen/Figtree
- **Estilo / personalidad:** Sans geométrica-grotesca amable, con aberturas abiertas y buen rendimiento en tamaños chicos. Una de las workhorses 'tranquilas' que listan las guías de 2026 cuando Inter se siente clínica.
- **Mejor uso:** SaaS, Dashboard / UI, Landing
- **Pesos / ejes:** Variable, con cursivas, varios pesos.
- **Variable:** Sí
- **Pareja recomendada:** Unbounded o Fraunces

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Figtree:ital,wght@0,300..900;1,300..900&display=swap" rel="stylesheet">
/* font-family: "Figtree", sans-serif; */
```

## 11. Founders Grotesk

- **Foundry:** Klim Type Foundry
- **Diseño:** Kris Sowersby
- **Licencia:** Comercial. Licencia perpetua Klim, pago único, desde el primer estilo.
- **Precio aproximado:** Desde 60 USD el primer estilo (mismo esquema de Klim).
- **Link oficial:** https://klim.co.nz/fonts/founders-grotesk/
- **Estilo / personalidad:** Grotesca de texto con un poco más de carácter que Söhne: compacta, editorial, muy legible en UI y en títulos medianos.
- **Mejor uso:** SaaS, Editorial, Landing, Dashboard / UI
- **Pesos / ejes:** Familia amplia, con cortes de texto y condensados.
- **Variable:** No
- **Pareja recomendada:** Tiempos Text o Reckless
- **Nota:** Aparece de forma constante en los top anuales de Typewolf (incluso en 2025).

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "Founders Grotesk";
  src: url("/fonts/founders-grotesk-regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 12. Geist

- **Foundry:** Vercel / Basement Studio
- **Diseño:** Andrés Briganti, Mateo Zaragoza, Basement Studio y Vercel
- **Licencia:** Gratis. SIL Open Font License. Disponible en Google Fonts y en github.com/vercel/geist-font.
- **Link oficial:** https://fonts.google.com/specimen/Geist
- **En uso real:** https://vercel.com/ — Es la tipografía de Vercel, v0, Next.js y Turborepo. Emblematic también la detectó en Calendly, Spline, Statsig, Tinybird, Xata y Trigger.dev.
- **Estilo / personalidad:** Sans de producto, más nítida y 'devtools' que Inter. Proporciones modernas, muy legible en UI. La pareja mono es parte del sistema.
- **Mejor uso:** SaaS, Tech / devtools, Dashboard / UI, Landing
- **Pesos / ejes:** Variable, Thin 100 a Black 900, con cursivas.
- **Variable:** Sí
- **Pareja recomendada:** Geist Mono (sistema propio) o Fraunces si hace falta contraste editorial
- **Nota:** En 2026 ya es la sans de moda en productos de IA. Buena, pero si todos los SaaS de AI la usan, deja de diferenciar. Considerala el nuevo Inter.

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geist:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
/* font-family: "Geist", sans-serif; */
```

## 13. General Sans

- **Foundry:** Indian Type Foundry / Fontshare
- **Licencia:** Gratis. ITF Free Font License (FFL) 2.0: uso comercial gratis, sin modificar ni redistribuir el archivo. Autohospedaje permitido.
- **Link oficial:** https://www.fontshare.com/fonts/general-sans
- **Estilo / personalidad:** Sans neutra y profesional, pensada para funcionar en cuerpo y en títulos. Es de las mejores 'workhorses' gratis cuando no se quiere Inter ni Geist.
- **Mejor uso:** SaaS, Dashboard / UI, Landing
- **Pesos / ejes:** De Extralight a Extrabold, con cursivas; hay variable.
- **Variable:** Sí
- **Pareja recomendada:** JetBrains Mono o Clash Display
- **Nota:** Tercera familia más vista en Fontshare en un snapshot de agosto 2026.

Snippet de import:

```html
<link href="https://api.fontshare.com/v2/css?f[]=general-sans@200,300,400,500,600,700&display=swap" rel="stylesheet">
/* font-family: "General Sans", sans-serif; */
/* Preferí autohospedar los archivos oficiales. La API de Fontshare no garantiza uptime.
   La licencia FFL no permite subsetear ni convertir el archivo. */
```

## 14. Graphik

- **Foundry:** Commercial Type
- **Licencia:** Comercial. Licencia comercial de Commercial Type (desktop, web, app).
- **Precio aproximado:** Alrededor de 60 USD por estilo en type.today; familias en Commercial Type cerca de 400 USD (licencias más amplias, más caras). Confirmar al comprar.
- **Link oficial:** https://commercialtype.com/catalog/graphik
- **En uso real:** https://basecamp.com/ — Detectada en Basecamp, The New Yorker, Todoist, Luma y Away (emblematic.dev/fonts).
- **Estilo / personalidad:** Grotesca geométrica-neutral, muy de 'marca de producto de los 2010-2020', todavía sólida si no se usa como atajo perezoso. Excelente en sistemas de diseño.
- **Mejor uso:** SaaS, Editorial, Dashboard / UI, Landing
- **Pesos / ejes:** Colección amplia, con condensados y otros cortes en Graphik Collection.
- **Variable:** No
- **Pareja recomendada:** Canela o Feature

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "Graphik";
  src: url("/fonts/graphik-regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 15. GT America

- **Foundry:** Grilli Type
- **Licencia:** Comercial. Licencia comercial Grilli Type. Estilos sueltos o familia completa.
- **Precio aproximado:** 75 USD por estilo; subfamilias desde 630 USD; familia completa (84 estilos) 945 USD (shop Grilli, consultado 2026).
- **Link oficial:** https://www.grillitype.com/font/gt-america
- **Estilo / personalidad:** Superfamilia norteamericana: cruza grotesca, geométrica y gótica comprimida. Sirve para resolver una identidad entera sin salir de la familia.
- **Mejor uso:** SaaS, Landing, Editorial, Tech / devtools
- **Pesos / ejes:** 84 estilos en la familia completa (varios anchos y construcciones).
- **Variable:** No
- **Pareja recomendada:** GT Alpina o GT Super
- **Nota:** Fue durante años la tipografía más vista en Typewolf (2017-2019).

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "GT America";
  src: url("/fonts/gt-america-regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 16. IBM Plex Sans

- **Foundry:** IBM / Bold Monday
- **Licencia:** Gratis. SIL Open Font License. Superfamilia abierta de IBM.
- **Link oficial:** https://fonts.google.com/specimen/IBM+Plex+Sans
- **En uso real:** https://www.ibm.com/ — Es la tipografía corporativa de IBM, visible en ibm.com. La superfamilia (Sans, Serif, Mono) se usa también en producto enterprise.
- **Estilo / personalidad:** Sans humanista-técnica, con un poco de sabor corporativo y mucho oficio. Ideal cuando un producto PyME quiere verse sólido, no 'startup genérica'.
- **Mejor uso:** SaaS, Dashboard / UI, Tech / devtools
- **Pesos / ejes:** Varios pesos con cursivas; hay condensados. Forma sistema con Plex Serif y Plex Mono.
- **Variable:** No
- **Pareja recomendada:** IBM Plex Serif e IBM Plex Mono

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,400;1,700&display=swap" rel="stylesheet">
/* font-family: "IBM Plex Sans", sans-serif; */
```

## 17. Instrument Sans

- **Foundry:** Instrument / Google Fonts
- **Diseño:** Rodrigo Fuenzalida, dirección de Jordan Egstad
- **Licencia:** Gratis. SIL Open Font License. También en github.com/Instrument/instrument-sans.
- **Link oficial:** https://fonts.google.com/specimen/Instrument+Sans
- **En uso real:** https://www.netlify.com/ — Detectada en Netlify, Instrument, Riverside, Cap y Heptabase (emblematic.dev/fonts).
- **Estilo / personalidad:** Sans contemporánea con eje de ancho (75–100) y un aire editorial-tech. Es la pareja natural de Instrument Serif, aunque el serif ya está muy visto en landings de startups.
- **Mejor uso:** SaaS, Landing, Dashboard / UI
- **Pesos / ejes:** Variable: peso 400–700, ancho 75–100, cursivas.
- **Variable:** Sí
- **Pareja recomendada:** Instrument Serif (con moderación) o Newsreader

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wdth,wght@0,75..100,400..700;1,75..100,400..700&display=swap" rel="stylesheet">
/* font-family: "Instrument Sans", sans-serif; */
```

## 18. Inter

- **Foundry:** Rasmus Andersson / Google Fonts
- **Diseño:** Rasmus Andersson
- **Licencia:** Gratis. SIL Open Font License. Gratis, uso comercial, se puede subsetear y autohospedar.
- **Link oficial:** https://rsms.me/inter/
- **En uso real:** https://tailwindcss.com/ — Emblematic la detectó en decenas de sitios (Tailwind CSS, Framer, Raycast, Deno, Linear aparece en listados similares, etc.). Es la sans más usada en producto tech.
- **Estilo / personalidad:** Sans diseñada para pantallas: gran altura de x, métricas de UI, variable. Excelente herramienta; pésima voz de marca si es lo único que se ve.
- **Mejor uso:** Dashboard / UI, SaaS, Tech / devtools
- **Pesos / ejes:** Variable 100–900, con cursivas y ejes de display en las versiones recientes. También está en Google Fonts: https://fonts.google.com/specimen/Inter
- **Variable:** Sí
- **Pareja recomendada:** Fraunces, Clash Display o cualquier display con carácter (Inter como cuerpo, no como héroe)
- **Nota:** Fue la más vista en Typewolf en 2023. En 2026 es el default de muchos agentes de IA. Usala de apoyo, no como personalidad.

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap" rel="stylesheet">
/* font-family: "Inter", sans-serif; */
```

## 19. Maison Neue

- **Foundry:** Milieu Grotesque (distribución actual en MyFonts / Monotype)
- **Diseño:** Timo Gaessner
- **Licencia:** Comercial. Comercial. El sitio milieugrotesque.com redirige a la colección de la foundry en MyFonts.
- **Precio aproximado:** Comercial; consultar en MyFonts la superfamilia (alrededor de 40 estilos, con condensados, extendidos y mono).
- **Link oficial:** https://www.myfonts.com/collections/maison-neue-font-milieu-grotesque/
- **Estilo / personalidad:** Grotesca contemporánea de muy amplio espectro: sirve de sistema completo (texto, display, condensed, mono). Aire europeo, funcional, un poco arquitectónico.
- **Mejor uso:** SaaS, Landing, Editorial, Tech / devtools
- **Pesos / ejes:** Superfamilia de unos 40 estilos, con anchos y un corte mono.
- **Variable:** No
- **Pareja recomendada:** Editorial Old o Reckless
- **Nota:** Typewolf la destacó en su portada de tendencias y fue top 10 en 2021.

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "Maison Neue";
  src: url("/fonts/maison-neue-book.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 20. Manrope

- **Foundry:** Mikhail Sharanda / Google Fonts
- **Licencia:** Gratis. SIL Open Font License, Google Fonts.
- **Link oficial:** https://fonts.google.com/specimen/Manrope
- **En uso real:** https://supabase.com/ — Detectada en Supabase, StackBlitz, Phosphor Icons y Lindy (emblematic.dev/fonts).
- **Estilo / personalidad:** Sans geométrica-grotesca de formas abiertas y trazo bastante uniforme. Cálida, moderna, muy usada en producto y en landings tech.
- **Mejor uso:** SaaS, Landing, Dashboard / UI
- **Pesos / ejes:** Variable, de ExtraLight a ExtraBold.
- **Variable:** Sí
- **Pareja recomendada:** Syne o Fraunces

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@200..800&display=swap" rel="stylesheet">
/* font-family: "Manrope", sans-serif; */
```

## 21. Mona Sans

- **Foundry:** GitHub / Google Fonts
- **Licencia:** Gratis. SIL Open Font License 1.1. Variable de peso, ancho y slant. Repositorio y anuncio oficial en GitHub.
- **Link oficial:** https://fonts.google.com/specimen/Mona+Sans
- **En uso real:** https://github.com/ — Es la sans de GitHub, presentada junto a Hubot Sans en el blog oficial de GitHub.
- **Estilo / personalidad:** Sans variable de producto, con eje de ancho que permite títulos compactos y UI cómoda sin cambiar de familia. Mucho más interesante que usar Inter por default en un producto dev.
- **Mejor uso:** Tech / devtools, SaaS, Dashboard / UI, Landing
- **Pesos / ejes:** Variable: weight, width y slant.
- **Variable:** Sí
- **Pareja recomendada:** Hubot Sans o JetBrains Mono

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Mona+Sans:ital,wdth,wght@0,75..125,200..900;1,75..125,200..900&display=swap" rel="stylesheet">
/* font-family: "Mona Sans", sans-serif; */
```

## 22. Monument Grotesk

- **Foundry:** Dinamo Typefaces
- **Licencia:** Comercial. Dinamo cobra según el tamaño de la empresa, no por usuario. Licencias de escritorio, web, etc.
- **Precio aproximado:** Alrededor de 90 EUR por estilo para un estudio de 3 personas (tabla de Dinamo). El precio sube con el tamaño de la compañía.
- **Link oficial:** https://abcdinamo.com/typefaces/monument-grotesk
- **En uso real:** https://abcdinamo.com/typefaces/monument-grotesk — El sitio de Dinamo la usa; emblematic también la detectó en Wolff Olins y Lithic.
- **Estilo / personalidad:** Grotesca con personalidad de estudio suizo contemporáneo: geométrica en algunos detalles, cruda en otros. Muy usada en identidades de diseño.
- **Mejor uso:** Landing, Editorial, Tech / devtools
- **Pesos / ejes:** Familia amplia, con variantes (entre ellas Mono en el ecosistema Monument).
- **Variable:** No
- **Pareja recomendada:** Reckless o GT Alpina
- **Nota:** Sigue apareciendo en los tops de Typewolf (2024 y 2025).

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "ABC Monument Grotesk";
  src: url("/fonts/abc-monument-grotesk-regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 23. Neue Montreal

- **Foundry:** Pangram Pangram Foundry
- **Licencia:** Comercial. Comercial, free-to-try. Pangram publica que las licencias comerciales empiezan en 40 USD.
- **Precio aproximado:** Licencias comerciales desde 40 USD (catálogo Pangram, 2026). Confirmar en la ficha al comprar.
- **Link oficial:** https://pangrampangram.com/products/neue-montreal
- **En uso real:** https://suno.com/ — Detectada en Suno, Eight Sleep, Cap y el sitio de Pangram Pangram (emblematic.dev/fonts).
- **Estilo / personalidad:** Grotesca geometrizante al estilo Montreal/Helvetica, un poco más ancha y contemporánea. Se siente de agencia premium sin ser tan fría como Helvetica.
- **Mejor uso:** Landing, SaaS, Lujo, Tech / devtools
- **Pesos / ejes:** Familia completa con cursivas; hay cortes relacionados en el ecosistema PP.
- **Variable:** No
- **Pareja recomendada:** Editorial New
- **Nota:** Tercera tipografía más vista en Typewolf en 2025. En r/typography se la menciona como grotesca de moda, relativamente ancha.

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "PP Neue Montreal";
  src: url("/fonts/pp-neue-montreal-regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 24. Plus Jakarta Sans

- **Foundry:** Tokotype / Google Fonts
- **Licencia:** Gratis. SIL Open Font License, Google Fonts.
- **Link oficial:** https://fonts.google.com/specimen/Plus+Jakarta+Sans
- **Estilo / personalidad:** Sans de producto un poco más cálida y 'startup del Sudeste Asiático' que Inter. Muy usada en landings B2B y design systems accesibles.
- **Mejor uso:** SaaS, Dashboard / UI, Landing
- **Pesos / ejes:** Variable, con cursivas; varios pesos de ExtraLight a ExtraBold.
- **Variable:** Sí
- **Pareja recomendada:** DM Sans o Newsreader

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,200..800;1,200..800&display=swap" rel="stylesheet">
/* font-family: "Plus Jakarta Sans", sans-serif; */
```

## 25. Public Sans

- **Foundry:** U.S. Web Design System (USWDS) / Google Fonts
- **Licencia:** Gratis. SIL Open Font License. Mantenida por el sistema de diseño del gobierno de EE. UU., a partir de Libre Franklin.
- **Link oficial:** https://fonts.google.com/specimen/Public+Sans
- **En uso real:** https://designsystem.digital.gov/ — Es la sans del U.S. Web Design System, documentada en designsystem.digital.gov.
- **Estilo / personalidad:** Sans cívica, neutra y muy legible. Perfecta para trámites, salud, educación y productos que tienen que inspirar confianza institucional.
- **Mejor uso:** Dashboard / UI, SaaS
- **Pesos / ejes:** Variable, de Thin a Black, con cursivas.
- **Variable:** Sí
- **Pareja recomendada:** Source Serif 4 o Merriweather (si se busca un tono más editorial clásico)

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Public+Sans:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
/* font-family: "Public Sans", sans-serif; */
```

## 26. Roobert

- **Foundry:** Displaay Type Foundry
- **Diseño:** Martin Vácha
- **Licencia:** Comercial. Licencia comercial Displaay. La colección actual incluye cortes proporcional, semimono y mono, con variable.
- **Precio aproximado:** Comercial; consultar en Displaay.
- **Link oficial:** https://displaay.net/typeface/roobert/
- **En uso real:** https://ngrok.com/ — Detectada en ngrok, Clay, Playdate y Creative Boom (emblematic.dev/fonts).
- **Estilo / personalidad:** Sans contemporánea, un poco geométrica y muy de producto digital. El semimono y el mono permiten un sistema tech completo.
- **Mejor uso:** Tech / devtools, SaaS, Dashboard / UI, Landing
- **Pesos / ejes:** Colección proporcional + semimono + mono; hay variable.
- **Variable:** Sí
- **Pareja recomendada:** Reckless (misma foundry) o Geist Mono

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "Roobert";
  src: url("/fonts/roobert-regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 27. Suisse Int'l

- **Foundry:** Swiss Typefaces
- **Licencia:** Comercial. Licencia perpetua, sin suscripción. Swiss Typefaces vende por estilo y por subfamilia, en CHF.
- **Precio aproximado:** Desde 50 CHF por estilo; subfamilia completa desde unos 300 CHF (referencias de typecase.dev y la foundry). Confirmar en el shop.
- **Link oficial:** https://www.swisstypefaces.com/fonts/suisse/
- **En uso real:** https://clerk.com/ — Detectada en Clerk, AREA 17, Column, DuckDB, Liveblocks, Krea y el sitio de Swiss Typefaces (emblematic.dev/fonts).
- **Estilo / personalidad:** La grotesca suiza contemporánea de cabecera: limpia, internacional, muy versátil en producto y en marca.
- **Mejor uso:** SaaS, Tech / devtools, Dashboard / UI, Landing
- **Pesos / ejes:** 18 estilos en Suisse Int'l, más la colección Suisse (Neue, Works, etc.).
- **Variable:** No
- **Pareja recomendada:** GT Alpina o Tiempos Headline
- **Nota:** Sigue en los tops de Typewolf (2024 y 2025).

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "Suisse Int'l";
  src: url("/fonts/suisse-intl-regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 28. Switzer

- **Foundry:** Indian Type Foundry / Fontshare
- **Licencia:** Gratis. ITF Free Font License (FFL) 2.0: uso personal y comercial gratis. Prohibido modificar, subsetear, convertir o redistribuir el archivo. Autohospedaje permitido. La API es opcional y no tiene garantía de uptime.
- **Link oficial:** https://www.fontshare.com/fonts/switzer
- **Estilo / personalidad:** Grotesca limpia, de líneas muy pulidas, a medio camino entre una neo-grotesk suiza y una sans de producto. En r/webdesign 2025 la listaron entre las rising stars.
- **Mejor uso:** SaaS, Landing, Dashboard / UI
- **Pesos / ejes:** Familia amplia, con variable en Fontshare.
- **Variable:** Sí
- **Pareja recomendada:** Zodiak o Editorial New
- **Nota:** Typewolf la destacó en su portada de tendencias (2025). En un snapshot de Fontshare de agosto 2026 figuraba entre las más vistas del catálogo.

Snippet de import:

```html
<link href="https://api.fontshare.com/v2/css?f[]=switzer@300,400,500,600,700&display=swap" rel="stylesheet">
/* font-family: "Switzer", sans-serif; */
/* Preferí autohospedar los archivos oficiales. La API de Fontshare no garantiza uptime.
   La licencia FFL no permite subsetear ni convertir el archivo. */
```

## 29. Söhne

- **Foundry:** Klim Type Foundry
- **Diseño:** Kris Sowersby
- **Licencia:** Comercial. Licencia perpetua (desktop, web, app, etc.), pago único. Sin vencimiento ni suscripción. Hay que ampliar la licencia si crece el uso.
- **Precio aproximado:** Desde 60 USD el primer estilo; estilos siguientes con descuento. Familias más baratas en bloque.
- **Link oficial:** https://klim.co.nz/fonts/soehne/
- **En uso real:** https://stripe.com/ — Detectada en Stripe, LaunchDarkly, Fellow y en el propio sitio de Klim (emblematic.dev/fonts y klim.co.nz/in-use).
- **Estilo / personalidad:** Neo-grotesca contemporánea, heredera de Akzidenz-Grotesk. Neutra, precisa y con mucho oficio: no grita, pero se siente cara. Hay anchos y un corte mono.
- **Mejor uso:** SaaS, Tech / devtools, Dashboard / UI, Landing
- **Pesos / ejes:** Colección amplia (Söhne, Schmal, Breit, Mono) con varios pesos y cursivas.
- **Variable:** No
- **Pareja recomendada:** Tiempos Headline o Signifier
- **Nota:** Fue la tipografía más registrada en Typewolf durante 2025. Excelente default premium cuando Inter ya se ve genérica.

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "Söhne";
  src: url("/fonts/soehne-buch.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 30. TWK Lausanne

- **Foundry:** WELTKERN
- **Diseño:** Nizar Kazan
- **Licencia:** Comercial. Comercial, publicada por WELTKERN. El crédito recomendado por la foundry es: © TWK Lausanne designed by Nizar Kazan, published by WELTKERN®.
- **Precio aproximado:** Comercial; consultar en weltkern.com.
- **Link oficial:** https://weltkern.com/typefaces/twk-lausanne
- **En uso real:** https://asana.com/ — Detectada en Asana, Typeform, Jitter y LangChain (emblematic.dev/fonts).
- **Estilo / personalidad:** Sans suiza elegante, un poco más fashion que una grotesca pura. Queda muy bien en marketing sites y en productos que quieren verse internacionales.
- **Mejor uso:** SaaS, Landing, Lujo
- **Pesos / ejes:** Familia amplia (varios pesos).
- **Variable:** No
- **Pareja recomendada:** Editorial New o Canela
- **Nota:** Fue la tipografía más registrada en Typewolf en 2024.

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "TWK Lausanne";
  src: url("/fonts/twk-lausanne-regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 31. Untitled Sans

- **Foundry:** Klim Type Foundry
- **Diseño:** Kris Sowersby
- **Licencia:** Comercial. Licencia perpetua Klim, pago único.
- **Precio aproximado:** Desde 60 USD el primer estilo (Klim).
- **Link oficial:** https://klim.co.nz/fonts/untitled-sans/
- **En uso real:** https://www.radix-ui.com/ — Detectada en Radix UI, Craft y WorkOS (emblematic.dev/fonts).
- **Estilo / personalidad:** Sans anónima a propósito: menos 'diseñada' que Söhne, muy útil cuando la interfaz tiene que desaparecer detrás del producto.
- **Mejor uso:** Dashboard / UI, SaaS, Tech / devtools
- **Pesos / ejes:** Familia de texto con cursivas, varios pesos.
- **Variable:** No
- **Pareja recomendada:** Signifier o Untitled Serif (si se licencia la pareja de Klim)

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "Untitled Sans";
  src: url("/fonts/untitled-sans-regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

---

## Sumadas el 20 de noviembre de 2026

Fuentes de Google Fonts (SIL OFL) que entraron para las parejas 29–42 de [`pairings.md`](./pairings.md). El diseñador, los ejes y el ranking de popularidad salen del dataset de [ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) (MIT); la descripción es propia.

## 32. Source Sans 3

- **Diseño:** Paul D. Hunt
- **Licencia:** Gratis. SIL Open Font License, Google Fonts.
- **Link oficial:** https://fonts.google.com/specimen/Source+Sans+3
- **Estilo / personalidad:** Humanista de Adobe, sobria y muy legible. No tiene personalidad propia: es cuerpo, no voz.
- **Mejor uso:** Cuerpo, Dashboard, Gobierno, Docs
- **Pesos / ejes:** Variable (wght: 200..900)
- **Variable:** Sí
- **Pareja recomendada:** Lexend, Bebas Neue o Source Serif 4
- **Nota:** Ranking de popularidad en Google Fonts: 15 (dataset de ui-ux-pro-max-skill, nov. 2026). Muy usada: tratala como cuerpo, no como voz de marca.

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@200..900&display=swap" rel="stylesheet">
/* font-family: "Source Sans 3", sans-serif; */
```

## 33. Barlow

- **Diseño:** Jeremy Tribby
- **Licencia:** Gratis. SIL Open Font License, Google Fonts.
- **Link oficial:** https://fonts.google.com/specimen/Barlow
- **Estilo / personalidad:** Grotesca un poco redondeada, de la misma superfamilia que Barlow Condensed. Muy usada: necesita una display con carácter al lado.
- **Mejor uso:** Cuerpo, Deportes, Industria
- **Pesos / ejes:** Estáticos: 100, 100i, 200, 200i, 300, 300i, 400, 400i, 500, 500i, 600, 600i, 700, 700i, 800, 800i, 900, 900i
- **Variable:** No
- **Pareja recomendada:** Barlow Condensed
- **Nota:** Ranking de popularidad en Google Fonts: 14 (dataset de ui-ux-pro-max-skill, nov. 2026). Muy usada: tratala como cuerpo, no como voz de marca.

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@100;200;300;400;500;600;700;800;900&display=swap" rel="stylesheet">
/* font-family: "Barlow", sans-serif; */
```

## 34. Archivo

- **Diseño:** Omnibus-Type
- **Licencia:** Gratis. SIL Open Font License, Google Fonts.
- **Link oficial:** https://fonts.google.com/specimen/Archivo
- **Estilo / personalidad:** Grotesca de Omnibus-Type con eje de ancho (62–125) y peso: de muy condensada a expandida en una sola familia.
- **Mejor uso:** Portfolio, Marca, Editorial, Dashboard
- **Pesos / ejes:** Variable (wdth: 62..125 | wght: 100..900)
- **Variable:** Sí
- **Pareja recomendada:** Space Grotesk o una serif de texto
- **Nota:** Ranking de popularidad en Google Fonts: 58 (dataset de ui-ux-pro-max-skill, nov. 2026).

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@100..900&display=swap" rel="stylesheet">
/* font-family: "Archivo", sans-serif; */
```

## 35. Epilogue

- **Diseño:** Tyler Finck, ETC
- **Licencia:** Gratis. SIL Open Font License, Google Fonts.
- **Link oficial:** https://fonts.google.com/specimen/Epilogue
- **Estilo / personalidad:** Grotesca de Etcetera Type Co., variable, con un aire editorial y un poco excéntrico en pesos altos.
- **Mejor uso:** Marca, Editorial, Campañas
- **Pesos / ejes:** Variable (wght: 100..900)
- **Variable:** Sí
- **Pareja recomendada:** Anton
- **Nota:** Ranking de popularidad en Google Fonts: 72 (dataset de ui-ux-pro-max-skill, nov. 2026).

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Epilogue:wght@100..900&display=swap" rel="stylesheet">
/* font-family: "Epilogue", sans-serif; */
```

## 36. Fira Sans

- **Diseño:** Carrois Apostrophe
- **Licencia:** Gratis. SIL Open Font License, Google Fonts.
- **Link oficial:** https://fonts.google.com/specimen/Fira+Sans
- **Estilo / personalidad:** Humanista de Erik Spiekermann y Carrois para Mozilla. Legible en pantallas chicas y tablas.
- **Mejor uso:** Dashboard, Docs, Producto
- **Pesos / ejes:** Estáticos: 100, 100i, 200, 200i, 300, 300i, 400, 400i, 500, 500i, 600, 600i, 700, 700i, 800, 800i, 900, 900i
- **Variable:** No
- **Pareja recomendada:** Fira Code
- **Nota:** Ranking de popularidad en Google Fonts: 19 (dataset de ui-ux-pro-max-skill, nov. 2026). Muy usada: tratala como cuerpo, no como voz de marca.

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fira+Sans:wght@100;200;300;400;500;600;700;800;900&display=swap" rel="stylesheet">
/* font-family: "Fira Sans", sans-serif; */
```

## 37. Work Sans

- **Diseño:** Wei Huang
- **Licencia:** Gratis. SIL Open Font License, Google Fonts.
- **Link oficial:** https://fonts.google.com/specimen/Work+Sans
- **Estilo / personalidad:** Grotesca de Wei Huang, optimizada para pantalla en pesos medios. Muy popular: buena como cuerpo, no como voz.
- **Mejor uso:** Cuerpo, Agencias, Landing
- **Pesos / ejes:** Variable (wght: 100..900)
- **Variable:** Sí
- **Pareja recomendada:** Outfit
- **Nota:** Ranking de popularidad en Google Fonts: 10 (dataset de ui-ux-pro-max-skill, nov. 2026). Muy usada: tratala como cuerpo, no como voz de marca.

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Work+Sans:wght@100..900&display=swap" rel="stylesheet">
/* font-family: "Work Sans", sans-serif; */
```


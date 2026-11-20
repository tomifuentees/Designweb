# Serif display

19 familias en esta categoría. Catálogo armado en noviembre 2026 para el repo de diseño frontend. Solo se incluyen datos verificados (links oficiales que resolvieron, o —en el caso de Sharp Type— la URL canónica de la foundry, que respondió 429 por un challenge de bot, no 404).

El rasgo tipográfico más claro de 2025-2026 es el regreso de la serif expresiva en el titular, apoyada por una sans quieta en el cuerpo. Pantallas de alta densidad por fin dibujan los terminales finos sin que se rompan.

Fraunces (gratis, con eje WONK) y las comerciales de Pangram, Klim, Grilli, Displaay, Sharp Type y Commercial Type son el estante premium. Instrument Serif sigue siendo bella, pero en comunidades de diseño ya se la señala como el nuevo cliché de landing 'IA editorial'. Playfair Display no está en esta lista a propósito: está en las reglas anti-genéricas del README.

---

## 1. Boska

- **Foundry:** Indian Type Foundry / Fontshare
- **Licencia:** Gratis. ITF Free Font License (FFL) 2.0: uso comercial gratis, sin modificar ni redistribuir el archivo.
- **Link oficial:** https://www.fontshare.com/fonts/boska
- **Estilo / personalidad:** Serif display de alto contraste, de las mejores opciones gratis para un look de revista de lujo sin caer en Playfair.
- **Mejor uso:** Lujo, Editorial, Landing
- **Pesos / ejes:** Varios pesos en Fontshare; consultar variable en la ficha.
- **Variable:** Sí
- **Pareja recomendada:** Switzer o General Sans

Snippet de import:

```html
<link href="https://api.fontshare.com/v2/css?f[]=boska@400,500,700&display=swap" rel="stylesheet">
/* font-family: "Boska", sans-serif; */
/* Preferí autohospedar los archivos oficiales. La API de Fontshare no garantiza uptime.
   La licencia FFL no permite subsetear ni convertir el archivo. */
```

## 2. Canela

- **Foundry:** Commercial Type
- **Licencia:** Comercial. Licencia comercial de Commercial Type.
- **Precio aproximado:** En type.today se la vio desde 72 USD por estilo; familias en Commercial Type en el rango 325–350 USD, paquetes más amplios alrededor de 800 USD. Confirmar al comprar.
- **Link oficial:** https://commercialtype.com/catalog/canela
- **Estilo / personalidad:** Serif de lujo, de terminales florales y mucho contraste. Es la voz de muchas marcas de belleza, moda y lifestyle. Hay que usarla grande y con espacio.
- **Mejor uso:** Lujo, Editorial, Landing
- **Pesos / ejes:** Colección Canela (display y text, varios pesos).
- **Variable:** No
- **Pareja recomendada:** Graphik o Suisse Int'l
- **Nota:** Dominó Typewolf a fines de los 2010 (top 2017-2020) y sigue siendo una referencia de lujo.

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "Canela";
  src: url("/fonts/canela-regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 3. Cardinal

- **Foundry:** Production Type
- **Diseño:** Jean-Baptiste Levée, Yoann Minet y Quentin Schmerber
- **Licencia:** Comercial. Licencia comercial de Production Type. Publicada en 2018.
- **Precio aproximado:** Comercial; consultar en Production Type.
- **Link oficial:** https://productiontype.com/font/cardinal
- **Estilo / personalidad:** Familia serif con varias alturas de x (Classic Short, Mid, Long) y un corte Fruit condensado, evocado a Apple Garamond. Muy versátil entre display y texto.
- **Mejor uso:** Editorial, Lujo, Landing
- **Pesos / ejes:** Cuatro versiones; cada una en cuatro pesos con cursivas (Typewolf).
- **Variable:** No
- **Pareja recomendada:** Suisse Int'l o General Sans
- **Nota:** Top 10 Typewolf 2025.

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "Cardinal";
  src: url("/fonts/cardinal-classic-regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 4. DM Serif Display

- **Foundry:** Colophon Foundry / Google Fonts
- **Licencia:** Gratis. SIL Open Font License, Google Fonts. Forma sistema con DM Sans y DM Serif Text.
- **Link oficial:** https://fonts.google.com/specimen/DM+Serif+Display
- **Estilo / personalidad:** Serif display de alto contraste, fácil de cargar y muy usada. Ya está un poco vista (junto a Playfair) como atajo de 'elegancia barata'; sigue funcionando si el resto del sistema no es genérico.
- **Mejor uso:** Landing, Editorial, Lujo
- **Pesos / ejes:** Regular e Italic.
- **Variable:** No
- **Pareja recomendada:** DM Sans o Lato (si se busca un cuerpo más cálido)

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet">
/* font-family: "DM Serif Display", sans-serif; */
```

## 5. Editorial New

- **Foundry:** Pangram Pangram Foundry
- **Licencia:** Comercial. Comercial, free-to-try. Licencias Pangram desde 40 USD en el catálogo.
- **Precio aproximado:** Licencias comerciales Pangram desde 40 USD; confirmar paquete en la ficha.
- **Link oficial:** https://pangrampangram.com/products/editorial-new
- **Estilo / personalidad:** Serif de moda editorial: alto contraste, itálicas muy expresivas, aire de revista de lujo. Fue durante años una de las serifs más vistas en Typewolf (número 1 en 2021).
- **Mejor uso:** Editorial, Lujo, Landing
- **Pesos / ejes:** Familia amplia con cursivas.
- **Variable:** No
- **Pareja recomendada:** Neue Montreal o Suisse Int'l

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "PP Editorial New";
  src: url("/fonts/pp-editorial-new-regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 6. Editorial Old

- **Foundry:** Pangram Pangram Foundry
- **Licencia:** Comercial. Comercial, free-to-try. Pangram la describe como una versión 'melting, eroded' de Editorial New (Typewolf).
- **Precio aproximado:** Licencias comerciales Pangram desde 40 USD; confirmar en la ficha.
- **Link oficial:** https://pangrampangram.com/products/editorial-old
- **Estilo / personalidad:** La hermana erosionada de Editorial New: mismos huesos, terminales derretidos. Mucho más 'anti-perfecto' y útil cuando Editorial New ya se siente de template.
- **Mejor uso:** Editorial, Lujo, Landing
- **Pesos / ejes:** Nueve pesos con cursivas (Typewolf).
- **Variable:** No
- **Pareja recomendada:** Maison Neue o Switzer
- **Nota:** Tercera serif más vista en Typewolf en 2025, empatada en menciones con Founders Grotesk y Cardinal.

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "PP Editorial Old";
  src: url("/fonts/pp-editorial-old-regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 7. Feature

- **Foundry:** Commercial Type
- **Diseño:** Christian Schwartz y Berton Hasebe; ampliación de Hrvoje Živčić
- **Licencia:** Comercial. Licencia comercial de Commercial Type. Originalmente encargada para T: The New York Times Style Magazine (2018); retail posterior con itálicas y más pesos.
- **Precio aproximado:** Comercial; consultar en Commercial Type.
- **Link oficial:** https://commercialtype.com/catalog/feature
- **Estilo / personalidad:** Serif de revista de moda, con tamaños ópticos Display, Deck y Text, más condensados. Mucha distinción entre el titular y el cuerpo.
- **Mejor uso:** Editorial, Lujo, Landing
- **Pesos / ejes:** Cinco subfamilias: Feature Display, Display Condensed, Deck, Deck Condensed y Text.
- **Variable:** No
- **Pareja recomendada:** Druk (sugerencia de Typewolf) o Graphik
- **Nota:** Fue la segunda tipografía más vista en Typewolf en 2025, empatada con Söhne.

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "Feature";
  src: url("/fonts/feature-display-regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 8. Fraunces

- **Foundry:** Undercase Type / Google Fonts
- **Diseño:** CJ Dunn / Undercase Type
- **Licencia:** Gratis. SIL Open Font License, Google Fonts.
- **Link oficial:** https://fonts.google.com/specimen/Fraunces
- **Estilo / personalidad:** Serif 'soft-wonky' con ejes de peso, tamaño óptico, SOFT (redondeo) y WONK (irregularidad). Puede ir de editorial refinada a display casi naíf. Es la mejor serif gratis con personalidad de este ciclo.
- **Mejor uso:** Landing, Editorial, Lujo
- **Pesos / ejes:** Variable 100–900, opsz 9–144, más ejes SOFT y WONK.
- **Variable:** Sí
- **Pareja recomendada:** Geist, Hanken Grotesk, Manrope o Bricolage Grotesque
- **Nota:** Las guías de tendencias 2026 la ponen como bandera del revival serif. El eje WONK es un antídoto directo al look perfectamente pulido de la IA.

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,100..900&display=swap" rel="stylesheet">
/* font-family: "Fraunces", sans-serif; */
```

## 9. Gloock

- **Foundry:** Google Fonts
- **Licencia:** Gratis. SIL Open Font License, Google Fonts.
- **Link oficial:** https://fonts.google.com/specimen/Gloock
- **Estilo / personalidad:** Serif display pesada, editorial, de mucho contraste. Para un titular y nada más: no sirve de cuerpo. Las listas de 2026 la agrupan con Fraunces e Instrument Serif.
- **Mejor uso:** Landing, Editorial, Lujo
- **Pesos / ejes:** Un estilo display (Regular).
- **Variable:** No
- **Pareja recomendada:** Manrope o Figtree

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Gloock:wght@400&display=swap" rel="stylesheet">
/* font-family: "Gloock", sans-serif; */
```

## 10. GT Alpina

- **Foundry:** Grilli Type
- **Licencia:** Comercial. Licencia comercial Grilli Type.
- **Precio aproximado:** 75 USD por estilo; subfamilias desde 450 USD; familia completa (70 estilos) 945 USD (shop Grilli, 2026).
- **Link oficial:** https://www.grillitype.com/font/gt-alpina
- **Estilo / personalidad:** Serif de textura alpina, cálida, con muchos tamaños ópticos. Puede hacer de display y de texto. Fue la más vista en Typewolf en 2022 y siguió en el top en 2023.
- **Mejor uso:** Editorial, Lujo, Landing
- **Pesos / ejes:** 70 estilos en la familia completa, con cortes ópticos.
- **Variable:** No
- **Pareja recomendada:** GT America o Suisse Int'l

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "GT Alpina";
  src: url("/fonts/gt-alpina-standard-regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 11. GT Super

- **Foundry:** Grilli Type
- **Licencia:** Comercial. Licencia comercial Grilli Type.
- **Precio aproximado:** 75 USD por estilo; familia completa (20 estilos) 900 USD; subfamilias desde 600 USD (shop Grilli, 2026).
- **Link oficial:** https://www.grillitype.com/font/gt-super
- **Estilo / personalidad:** Serif display con un aire un poco naíf y muy editorial. Alternativa de pago a Fraunces cuando se busca más oficio de foundry.
- **Mejor uso:** Editorial, Landing, Lujo
- **Pesos / ejes:** 20 estilos en la familia completa.
- **Variable:** No
- **Pareja recomendada:** GT America o GT Walsheim
- **Nota:** Top 10 Typewolf 2025 y 2022.

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "GT Super";
  src: url("/fonts/gt-super-regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 12. Instrument Serif

- **Foundry:** Instrument / Google Fonts
- **Diseño:** Rodrigo Fuenzalida, Jordan Egstad
- **Licencia:** Gratis. SIL Open Font License, Google Fonts.
- **Link oficial:** https://fonts.google.com/specimen/Instrument+Serif
- **Estilo / personalidad:** Serif contemporánea, de contraste medio-alto y una itálica muy expresiva. Se volvió la serif default de landings de startups e IA en 2024-2026.
- **Mejor uso:** Landing, Editorial, Lujo
- **Pesos / ejes:** Solo Regular 400 e Italic.
- **Variable:** No
- **Pareja recomendada:** Instrument Sans o Geist
- **Nota:** En r/web_design (julio 2026) ya la señalaban como tendencia que va a envejecer mal. Sigue siendo bella: usala con criterio, no como atajo de 'editorial AI'.

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
/* font-family: "Instrument Serif", sans-serif; */
```

## 13. Migra

- **Foundry:** Sharp Type
- **Licencia:** Comercial. Licencia comercial Sharp Type. Igual que Ogg, la ficha en sharptype.co recibió 429 del crawler (challenge), no un 404.
- **Precio aproximado:** Comercial; consultar en Sharp Type.
- **Link oficial:** https://www.sharptype.co/typefaces/migra
- **Estilo / personalidad:** Serif de inspiración calligráfica, muy expresiva, usada en identidades culturales y editoriales. Typewolf la tuvo en su top 2022.
- **Mejor uso:** Editorial, Lujo, Landing
- **Pesos / ejes:** Familia Sharp Type (consultar cortes en la ficha).
- **Variable:** No
- **Pareja recomendada:** Graphik o Untitled Sans

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "Migra";
  src: url("/fonts/migra-regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 14. Ogg

- **Foundry:** Sharp Type
- **Licencia:** Comercial. Licencia comercial Sharp Type. La ficha oficial vive en sharptype.co; en esta investigación el sitio devolvió 429 (challenge de Vercel) al crawler, no un 404.
- **Precio aproximado:** Comercial; consultar en Sharp Type.
- **Link oficial:** https://www.sharptype.co/typefaces/ogg
- **Estilo / personalidad:** Serif display de altísimo contraste, muy fashion. Typewolf la ubica como la serif más popular de su ranking 2026, por encima de Times y Caslon.
- **Mejor uso:** Lujo, Editorial, Landing
- **Pesos / ejes:** Familia Sharp Type (display, con itálicas).
- **Variable:** No
- **Pareja recomendada:** Graphik o Neue Montreal
- **Nota:** Número 1 del top de serifs de Typewolf en 2026.

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "Ogg";
  src: url("/fonts/ogg-roman.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 15. Reckless

- **Foundry:** Displaay Type Foundry
- **Licencia:** Comercial. Licencia comercial Displaay. Los precios publicados incluyen variable. Reckless se amplió a una colección de varias familias (Reckless II).
- **Precio aproximado:** Desde 55 EUR un estilo (upright o italic); 16 estilos 352 EUR; colección completa publicada a 2.376 EUR. Confirmar tramo de licencia.
- **Link oficial:** https://displaay.net/typeface/reckless/
- **Estilo / personalidad:** Serif contemporánea con un punto salvaje y editorial. Muy presente en sitios de estudio y en producto con voz de revista. Top Typewolf 2024 (#2) y 2025.
- **Mejor uso:** Editorial, Landing, Lujo
- **Pesos / ejes:** Familia (y ahora colección) con muchos estilos; incluye variable.
- **Variable:** Sí
- **Pareja recomendada:** Roobert (misma foundry) o Monument Grotesk

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "Reckless";
  src: url("/fonts/reckless-regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 16. Self Modern

- **Foundry:** Bretagne Type Foundry
- **Diseño:** Lucas Le Bihan (Book, Semi-Bold y Bold con Roxane Gataud)
- **Licencia:** Comercial. Comercial; trials y licencias a pedido en Fonderie Bretagne.
- **Precio aproximado:** Comercial; consultar en fonderiebretagne.fr.
- **Link oficial:** https://www.fonderiebretagne.fr/font/self-modern-regular/
- **Estilo / personalidad:** Serif transicional contemporánea, de las favoritas de Typewolf (top 2024 y años previos). Menos 'fashion high-contrast' y más literatura / cultura.
- **Mejor uso:** Editorial, Lujo, Landing
- **Pesos / ejes:** Regular, Italic, Book, Semi-Bold y Bold (según las fichas de la foundry y Fonts In Use).
- **Variable:** No
- **Pareja recomendada:** Suisse Int'l o Cabinet Grotesk

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "Self Modern";
  src: url("/fonts/self-modern-regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 17. Signifier

- **Foundry:** Klim Type Foundry
- **Diseño:** Kris Sowersby
- **Licencia:** Comercial. Licencia perpetua Klim, pago único.
- **Precio aproximado:** Desde 60 USD el primer estilo (Klim).
- **Link oficial:** https://klim.co.nz/fonts/signifier/
- **Estilo / personalidad:** Serif contemporánea de alto contraste y dibujo muy afilado. Se siente cara, cultural y un poco inquietante. Excelente en titulares de lujo o media.
- **Mejor uso:** Editorial, Lujo, Landing
- **Pesos / ejes:** Familia Klim con cursivas y varios pesos.
- **Variable:** No
- **Pareja recomendada:** Söhne o Untitled Sans
- **Nota:** Top 10 de Typewolf en 2025 y en 2023 (llegó a ser la #3).

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "Signifier";
  src: url("/fonts/signifier-regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 18. Tiempos Headline

- **Foundry:** Klim Type Foundry
- **Diseño:** Kris Sowersby
- **Licencia:** Comercial. Licencia perpetua Klim, pago único.
- **Precio aproximado:** Desde 60 USD el primer estilo (Klim).
- **Link oficial:** https://klim.co.nz/fonts/tiempos-headline/
- **Estilo / personalidad:** Serif de titular, par de Tiempos Text: robusta, periodística, contemporánea. Menos 'fashion' que Signifier, más de medio y de producto editorial serio.
- **Mejor uso:** Editorial, Landing, SaaS
- **Pesos / ejes:** Familia de headline con cursivas; se completa con Tiempos Text.
- **Variable:** No
- **Pareja recomendada:** Söhne o Founders Grotesk
- **Nota:** Top 10 Typewolf 2024.

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "Tiempos Headline";
  src: url("/fonts/tiempos-headline-regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 19. Zodiak

- **Foundry:** Indian Type Foundry / Fontshare
- **Licencia:** Gratis. ITF Free Font License (FFL) 2.0: uso comercial gratis, sin modificar ni redistribuir el archivo.
- **Link oficial:** https://www.fontshare.com/fonts/zodiak
- **Estilo / personalidad:** Serif de contraste marcado, un poco más 'incisiva' y contemporánea que Boska. Muy buena para titulares de marca y para editoriales digitales.
- **Mejor uso:** Editorial, Landing, Lujo
- **Pesos / ejes:** Familia Fontshare con varios pesos y cursivas; hay variable.
- **Variable:** Sí
- **Pareja recomendada:** Clash Grotesk o Satoshi

Snippet de import:

```html
<link href="https://api.fontshare.com/v2/css?f[]=zodiak@400,500,700&display=swap" rel="stylesheet">
/* font-family: "Zodiak", sans-serif; */
/* Preferí autohospedar los archivos oficiales. La API de Fontshare no garantiza uptime.
   La licencia FFL no permite subsetear ni convertir el archivo. */
```

---

## Sumadas el 20 de noviembre de 2026

Fuentes de Google Fonts (SIL OFL) que entraron para las parejas 29–42 de [`pairings.md`](./pairings.md). El diseñador, los ejes y el ranking de popularidad salen del dataset de [ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) (MIT); la descripción es propia.

## 20. Bodoni Moda

- **Diseño:** Owen Earl
- **Licencia:** Gratis. SIL Open Font License, Google Fonts.
- **Link oficial:** https://fonts.google.com/specimen/Bodoni+Moda
- **Estilo / personalidad:** Bodoni didona con eje óptico (opsz 6–96): los trazos finos se engrosan en tamaño chico. Lujo y moda sin caer en Playfair.
- **Mejor uso:** Lujo, Moda, Editorial
- **Pesos / ejes:** Variable (opsz: 6..96 | wght: 400..900)
- **Variable:** Sí
- **Pareja recomendada:** Jost
- **Nota:** Ranking de popularidad en Google Fonts: 153 (dataset de ui-ux-pro-max-skill, nov. 2026).

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:wght@400..900&display=swap" rel="stylesheet">
/* font-family: "Bodoni Moda", serif; */
```

## 21. Libre Bodoni

- **Diseño:** Pablo Impallari, Rodrigo Fuenzalida
- **Licencia:** Gratis. SIL Open Font License, Google Fonts.
- **Link oficial:** https://fonts.google.com/specimen/Libre+Bodoni
- **Estilo / personalidad:** Bodoni pensada para texto en pantalla (Impallari y Fuenzalida). Titulares de revista y bajadas.
- **Mejor uso:** Editorial, Revistas, Cultura
- **Pesos / ejes:** Variable (wght: 400..700)
- **Variable:** Sí
- **Pareja recomendada:** Public Sans
- **Nota:** Ranking de popularidad en Google Fonts: 198 (dataset de ui-ux-pro-max-skill, nov. 2026).

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Libre+Bodoni:wght@400..700&display=swap" rel="stylesheet">
/* font-family: "Libre Bodoni", serif; */
```

## 22. Abril Fatface

- **Diseño:** TypeTogether
- **Licencia:** Gratis. SIL Open Font License, Google Fonts.
- **Link oficial:** https://fonts.google.com/specimen/Abril+Fatface
- **Estilo / personalidad:** Didona display muy pesada (TypeTogether). Carteles, menús, cervecerías: solo titulares.
- **Mejor uso:** Gastronomía, Cervecerías, Posters
- **Pesos / ejes:** Estáticos: 400
- **Variable:** No
- **Pareja recomendada:** Merriweather
- **Nota:** Ranking de popularidad en Google Fonts: 100 (dataset de ui-ux-pro-max-skill, nov. 2026).

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Abril+Fatface&display=swap" rel="stylesheet">
/* font-family: "Abril Fatface", serif; */
```


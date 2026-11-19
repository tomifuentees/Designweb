# Display y experimentales

14 familias en esta categoría. Catálogo armado en noviembre 2026 para el repo de diseño frontend. Solo se incluyen datos verificados (links oficiales que resolvieron, o —en el caso de Sharp Type— la URL canónica de la foundry, que respondió 429 por un challenge de bot, no 404).

Acá viven los titulares que evitan el 'look de template': displays condensadas o extendidas, flares, pixel, lettering humano, grotescas deliberadamente torpes. Se usan grandes, en pocas palabras, con mucho aire.

Clash Display y Syne son las entradas más aterrizables para un SaaS PyME. Druk, Obviously, Arizona Flare o Karrik sirven cuando la identidad puede (y debe) arriesgar más. Shantell Sans funciona como gesto hecho a mano, no como tipografía de producto.

---

## 1. ABC Arizona Flare

- **Foundry:** Dinamo Typefaces
- **Licencia:** Comercial. Licenciamiento Dinamo por tamaño de empresa. Arizona es una familia con varios sabores; Flare es el corte más expresivo, destacado por Typewolf en 2025.
- **Precio aproximado:** Comercial; consultar en Dinamo según tamaño de empresa.
- **Link oficial:** https://abcdinamo.com/typefaces/arizona
- **Estilo / personalidad:** Sans/display con terminales flare, un punto setentista y muy de identidad contemporánea. Typewolf la destacó en su portada de tendencias (sept. 2025).
- **Mejor uso:** Landing, Editorial, Lujo
- **Pesos / ejes:** Colección Arizona (varios cortes; Flare es uno de ellos).
- **Variable:** Sí
- **Pareja recomendada:** ABC Diatype o una serif quieta como Newsreader

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "ABC Arizona Flare";
  src: url("/fonts/abc-arizona-flare-regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 2. Agipo

- **Foundry:** RP Digital Type Foundry (Radim Peško)
- **Licencia:** Comercial. Licencia comercial de Radim Peško.
- **Precio aproximado:** Comercial; consultar en radimpesko.com.
- **Link oficial:** https://radimpesko.com/fonts/agipo
- **Estilo / personalidad:** Sans/display de autor, muy de escena gráfica contemporánea. Typewolf la destacó en 2025 junto a Topol y Maison Neue.
- **Mejor uso:** Editorial, Landing
- **Pesos / ejes:** Familia RP (consultar ficha).
- **Variable:** No
- **Pareja recomendada:** Una serif de texto como Self Modern o Tiempos Text

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "Agipo";
  src: url("/fonts/agipo-regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 3. Clash Display

- **Foundry:** Indian Type Foundry / Fontshare
- **Licencia:** Gratis. ITF Free Font License (FFL) 2.0: uso comercial gratis, sin modificar ni redistribuir el archivo.
- **Link oficial:** https://www.fontshare.com/fonts/clash-display
- **Estilo / personalidad:** Display geométrica, de contraste marcado y spacing ajustado. Para titulares cortos y ambiciosos, no para párrafos. Es una de las mejores gratis para que un hero no se vea de template.
- **Mejor uso:** Landing, Lujo, Tech / devtools
- **Pesos / ejes:** Varios pesos (de Extralight a Bold en la ficha de Fontshare).
- **Variable:** Sí
- **Pareja recomendada:** Satoshi o Manrope
- **Nota:** Segunda familia más vista en Fontshare en un snapshot de agosto 2026.

Snippet de import:

```html
<link href="https://api.fontshare.com/v2/css?f[]=clash-display@400,500,600,700&display=swap" rel="stylesheet">
/* font-family: "Clash Display", sans-serif; */
/* Preferí autohospedar los archivos oficiales. La API de Fontshare no garantiza uptime.
   La licencia FFL no permite subsetear ni convertir el archivo. */
```

## 4. Dia

- **Foundry:** Schick Toikka
- **Licencia:** Comercial. Licencia comercial de Schick Toikka.
- **Precio aproximado:** Comercial; consultar en schick-toikka.com/dia.
- **Link oficial:** https://www.schick-toikka.com/dia
- **Estilo / personalidad:** Tipo de foundry independiente, destacada por Typewolf en septiembre 2025 junto a Arizona Flare. Sirve para proyectos que quieren un display poco transitado, de estudio europeo.
- **Mejor uso:** Editorial, Landing, Lujo
- **Pesos / ejes:** Familia Schick Toikka (consultar ficha oficial).
- **Variable:** No
- **Pareja recomendada:** Una grotesca quieta (Untitled Sans o General Sans)

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "Dia";
  src: url("/fonts/dia-regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 5. Druk

- **Foundry:** Commercial Type
- **Licencia:** Comercial. Licencia comercial de Commercial Type. Display condensada de alto impacto.
- **Precio aproximado:** Alrededor de 60 USD por estilo en canales como type.today; confirmar en Commercial Type.
- **Link oficial:** https://commercialtype.com/catalog/druk
- **Estilo / personalidad:** Display ultra condensada, de cartel y de tapa de revista. Typewolf la recomendó como pareja de Feature. Para una línea, en grande, con mucho aire.
- **Mejor uso:** Landing, Editorial, Lujo
- **Pesos / ejes:** Colección amplia (Wide, Condensed, Super, etc.).
- **Variable:** No
- **Pareja recomendada:** Feature o Graphik

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "Druk";
  src: url("/fonts/druk-wide-bold.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 6. Karrik

- **Foundry:** Velvetyne / Phantom Foundry / Bretagne
- **Diseño:** Jean-Baptiste Morizot (Phantom Foundry) y Lucas Le Bihan (Bretagne Type Foundry)
- **Licencia:** Gratis. SIL Open Font License 1.1. El repo canónico está en GitLab. El sitio de Velvetyne (velvetyne.fr) en noviembre 2026 redirigía las fichas a una campaña; por eso el link oficial apunta al repositorio de la fuente.
- **Link oficial:** https://gitlab.com/phantomfoundry/karrik_fonts
- **Estilo / personalidad:** Grotesca libre, deliberadamente irregular y 'torpe', inspirada en sans naíf antiguas. Nació para un número de Le Cercle sobre fantasmas. Es un antídoto explícito al dibujo perfecto de la IA.
- **Mejor uso:** Editorial, Landing
- **Pesos / ejes:** Regular e Italic (según el repositorio).
- **Variable:** No
- **Pareja recomendada:** Una serif de lectura (Newsreader o EB Garamond) o Necto Mono
- **Nota:** También documentada en https://type-atlas.xyz/typeface/karrik/

Snippet de import:

```html
/* Descargá el WOFF2 oficial (OFL) y autohospedalo. Subsetear está permitido. */
@font-face {
  font-family: "Karrik";
  src: url("/fonts/karrik-regular.woff2") format("woff2");
  font-weight: 100 900;
  font-style: normal;
  font-display: swap;
}
```

## 7. Melodrama

- **Foundry:** Indian Type Foundry / Fontshare
- **Licencia:** Gratis. ITF Free Font License (FFL) 2.0: uso comercial gratis, sin modificar ni redistribuir el archivo.
- **Link oficial:** https://www.fontshare.com/fonts/melodrama
- **Estilo / personalidad:** Display de altísimo contraste, casi teatral. Alternativa gratis a las serifs fashion (Ogg, Canela, Playfair) cuando el titular tiene que ser la imagen.
- **Mejor uso:** Lujo, Editorial, Landing
- **Pesos / ejes:** Familia Fontshare de display; consultar pesos en la ficha.
- **Variable:** Sí
- **Pareja recomendada:** Switzer o Satoshi

Snippet de import:

```html
<link href="https://api.fontshare.com/v2/css?f[]=melodrama@400,500,700&display=swap" rel="stylesheet">
/* font-family: "Melodrama", sans-serif; */
/* Preferí autohospedar los archivos oficiales. La API de Fontshare no garantiza uptime.
   La licencia FFL no permite subsetear ni convertir el archivo. */
```

## 8. Obviously

- **Foundry:** Oh no Type Co.
- **Licencia:** Comercial. Licencia comercial de Oh no Type. Es una de las variables más expresivas del mercado (anchos extremos).
- **Precio aproximado:** Comercial; consultar en ohnotype.co/fonts/obviously.
- **Link oficial:** https://ohnotype.co/fonts/obviously
- **Estilo / personalidad:** Sans variable de anchos que van de ultra condensada a ultra extendida, con un dibujo suave y un punto humorístico. Perfecta para sistemas de marca que viven del movimiento del tipo.
- **Mejor uso:** Landing, Editorial, Lujo
- **Pesos / ejes:** Variable de peso y ancho (familia extensa de Oh no).
- **Variable:** Sí
- **Pareja recomendada:** Una serif de texto (Newsreader, Tiempos Text) o Degular para un sistema Oh no

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "Obviously";
  src: url("/fonts/obviously-regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 9. Panchang

- **Foundry:** Indian Type Foundry / Fontshare
- **Licencia:** Gratis. ITF Free Font License (FFL) 2.0: uso comercial gratis, sin modificar ni redistribuir el archivo.
- **Link oficial:** https://www.fontshare.com/fonts/panchang
- **Estilo / personalidad:** Display geométrica ancha, de mucha presencia. Para logotipos, un héroe y poco más.
- **Mejor uso:** Landing, Tech / devtools
- **Pesos / ejes:** Familia Fontshare, varios pesos; hay variable.
- **Variable:** Sí
- **Pareja recomendada:** Satoshi o General Sans

Snippet de import:

```html
<link href="https://api.fontshare.com/v2/css?f[]=panchang@400,500,700&display=swap" rel="stylesheet">
/* font-family: "Panchang", sans-serif; */
/* Preferí autohospedar los archivos oficiales. La API de Fontshare no garantiza uptime.
   La licencia FFL no permite subsetear ni convertir el archivo. */
```

## 10. Shantell Sans

- **Foundry:** Shantell Martin / Arrow Type / Google Fonts
- **Licencia:** Gratis. SIL Open Font License, Google Fonts. Variable, con ejes que recuerdan la letra hecha a mano.
- **Link oficial:** https://fonts.google.com/specimen/Shantell+Sans
- **Estilo / personalidad:** Sans informal, de trazo humano. Las guías 2026 la agrupan como tipografía 'anti-AI' / handmade, para marcas de fundador, anotaciones y stickers. No usarla como cuerpo de un SaaS serio.
- **Mejor uso:** Landing, Editorial
- **Pesos / ejes:** Variable, con cursivas y ejes de informalidad (consultar ficha: wght y ejes adicionales).
- **Variable:** Sí
- **Pareja recomendada:** Una grotesca quieta (Figtree, Onest) para el cuerpo

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Shantell+Sans:ital,wght@0,300..800;1,300..800&display=swap" rel="stylesheet">
/* font-family: "Shantell Sans", sans-serif; */
```

## 11. Sprat

- **Foundry:** Collletttivo
- **Diseño:** Ethan Nakache
- **Licencia:** Gratis. SIL Open Font License, con atribución. Catálogo Collletttivo.
- **Link oficial:** https://www.collletttivo.it/typefaces/sprat
- **Estilo / personalidad:** Display indie, de mucho carácter editorial. Una de las mejores gratis para un afiche o un hero que no se vea de Google Fonts 'de siempre'.
- **Mejor uso:** Editorial, Landing
- **Pesos / ejes:** Familia OFL de Collletttivo (consultar ficha).
- **Variable:** No
- **Pareja recomendada:** Apfel Grotezk

Snippet de import:

```html
/* Descargá el WOFF2 oficial (OFL) y autohospedalo. Subsetear está permitido. */
@font-face {
  font-family: "Sprat";
  src: url("/fonts/sprat-regular.woff2") format("woff2");
  font-weight: 100 900;
  font-style: normal;
  font-display: swap;
}
```

## 12. Syne

- **Foundry:** Bonjour Monde / The Designers Foundry / Google Fonts
- **Licencia:** Gratis. SIL Open Font License, Google Fonts.
- **Link oficial:** https://fonts.google.com/specimen/Syne
- **Estilo / personalidad:** Sans display de dibujo raro y un poco 'wonky', con trampas de tinta. Muy citada en 2025-2026 como alternativa con carácter para startups que no quieren serif.
- **Mejor uso:** Landing, Tech / devtools, Editorial
- **Pesos / ejes:** Regular a ExtraBold; hay variable. Existe Syne Mono y Syne Tactile en el ecosistema.
- **Variable:** Sí
- **Pareja recomendada:** Manrope o Onest

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400..800&display=swap" rel="stylesheet">
/* font-family: "Syne", sans-serif; */
```

## 13. Topol

- **Foundry:** Heavyweight Digital Type Foundry
- **Licencia:** Comercial. Licencia comercial Heavyweight. Publicada en 2013 como sans condensada (Light, Regular, Bold); Typewolf la volvió a destacar en 2025.
- **Precio aproximado:** Comercial; consultar en heavyweight-type.com.
- **Link oficial:** https://heavyweight-type.com/stuff/topol-poster
- **Estilo / personalidad:** Sans condensada de poster, de inspiración centroeuropea. Para titulares de una línea, eventos, cultura, no para UI.
- **Mejor uso:** Editorial, Landing
- **Pesos / ejes:** Light, Regular y Bold (información de la foundry / type.lol).
- **Variable:** No
- **Pareja recomendada:** Una grotesca de texto (Söhne, General Sans) o una mono

Snippet de import:

```html
/* Comprá la licencia web en la foundry y autohospedá el WOFF2 oficial. */
@font-face {
  font-family: "Topol";
  src: url("/fonts/topol-regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 14. Unbounded

- **Foundry:** Google Fonts
- **Licencia:** Gratis. SIL Open Font License, Google Fonts.
- **Link oficial:** https://fonts.google.com/specimen/Unbounded
- **Estilo / personalidad:** Display de formas extendidas y geométricas, citada en tendencias 2026 junto a Anton, Bebas y Archivo para afirmaciones de una línea (deportes, eventos, héroes enormes).
- **Mejor uso:** Landing, Tech / devtools
- **Pesos / ejes:** Variable, de Light a Black.
- **Variable:** Sí
- **Pareja recomendada:** Figtree o Onest

Snippet de import:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@200..900&display=swap" rel="stylesheet">
/* font-family: "Unbounded", sans-serif; */
```

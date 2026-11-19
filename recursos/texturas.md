# Texturas, grano y papel

Un grano liviano (CSS o un tile) mata el pulido de plantilla y va con el estilo grano-ruido. La textura es un acento, no un fondo que pelea con el texto. Si la animás, respetá prefers-reduced-motion.

Hay **6 recursos** en este grupo. El catálogo completo está en [`recursos.json`](./recursos.json).

## fffuel

`fffuel` — [https://www.fffuel.co/](https://www.fffuel.co/)

**Licencia:** Revisar cada generador (la mayoría de los SVG exportados son para uso propio; confirmá en el sitio).

**Cuándo usarlo.** Ruido, grain, papeles, ondas y fondos SVG rápidos, sobre todo para el estilo grano-ruido o riso.

**Cuándo no.** Como identidad completa. La textura es un acento, no un tema.

Suite de generadores SVG (rrrite, ss//lurry, etc.). Muy usada en web design 2024–2026.

## Haikei

`haikei` — [https://haikei.app/](https://haikei.app/)

**Licencia:** Revisar los términos de export (hay plan free y paid).

**Cuándo usarlo.** Blobs, waves, stacks y fondos SVG ‘organizados’, no un ruido suelto.

**Cuándo no.** Como fondo de un SaaS que quiere UI casi invisible.

Generadores: blob, wave, layered peaks, blurry gradients. Export SVG/PNG.

## Grano en CSS (SVG feTurbulence)

`grain-css` — [https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feTurbulence](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feTurbulence)

**Licencia:** Técnica (el snippet es tuyo).

**Cuándo usarlo.** Un grano liviano, sin request de imagen, para matar el pulido ‘de IA’. Va con el estilo grano-ruido.

**Cuándo no.** Un ruido pesado que ensucia el texto o que no se apaga en `prefers-reduced-motion` si está animado.

Un SVG de 64–128 px con feTurbulence + `mix-blend-mode: overlay` a 4–8 % suele alcanzar. No hace falta una librería.

## Shader Gradient

`shadergradient` — [https://www.shadergradient.co/](https://www.shadergradient.co/)

**Licencia:** Revisar términos y pack (hay herramientas free y assets pagos).

**Cuándo usarlo.** Un mesh 3D suave como recorte, no como fondo de toda la landing.

**Cuándo no.** Detrás de un hero de ‘AI platform’ (se parece demasiado al glow de plantilla si el color es violeta).

Útil en espacial-3d o como textura de un tile. Elegí colores de la paleta del proyecto.

## Hero Patterns

`hero-patterns` — [https://heropatterns.com/](https://heropatterns.com/)

**Licencia:** CC-BY-4.0 (Steve Schoger).

**Cuándo usarlo.** Un patrón SVG discreto (puntos, líneas, topografía) en un fondo, con el acento de la paleta.

**Cuándo no.** Un patrón gritón detrás de un bloque de lectura.

Clásico, atribuible, sigue siendo útil. Cambiá el color al token de borde o de acento al 8–12 %.

## Transparent Textures

`transparent-textures` — [https://www.transparenttextures.com/](https://www.transparenttextures.com/)

**Licencia:** Casi todos son libres para uso; leé el aviso de cada textura.

**Cuándo usarlo.** Papel, ruido o tela en un fondo de editorial o de realismo táctil.

**Cuándo no.** Texturas pesadas que pesan en mobile o que rompen el contraste del texto.

Tiles PNG. Mantené la opacidad baja.

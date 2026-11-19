# Dopamina / paletas saturadas

Figma describe un 2026 en el que el color sube el volumen: paletas saturadas, neón, contrastes altos, “dopamine design”, a menudo alimentado por nostalgia Y2K. Lo sitúa en lifestyle, beauty y marcas jóvenes, y cita Lush, Headspace y Starface. No es maximalismo de capas (aunque pueden convivir): acá el gesto principal es **el color a lo grande**, plano o en bloques, con tipo que aguanta el grito. Wix, en un polo más suave, habla de “retrofuture femme” (pasteles + metal); son vecinos, no el mismo idioma.

Ojo: un degradé violeta-índigo de plantilla *no* es dopamina. Es el default que este kit trata de evitar. La dopamina pide un color de marca, raro y específico (un lima, un naranja de envase, el amarillo de un parche), usado sin miedo.

## Cuándo usarlo y cuándo no

**Usalo** en belleza, wellness lúdico, F&B, juventud, apps de hábito con personaje, campañas.

**No lo uses** en banca, salud clínica, legal, ni en un dashboard de ops. Tampoco si no podés garantizar contraste (un rosa flúo sobre blanco no es un acto de diseño).

## Reglas concretas

- **Grilla:** Bloques de color a sangre, o un campo único de un color y el tipo encima. Puede ser simple: la paleta hace el trabajo.
- **Espaciado:** Medio a generoso. El color llena, el tipo no tiene que apelmazarse.
- **Radios:** Libres (un corte recto queda fuerte; un redondeo grande queda “juguete”). Elegí uno y repetilo.
- **Bordes:** O ninguno, o un borde negro que sujete el color (vecino del neo-brutalismo).
- **Sombras:** No hacen falta. Si hay, que sea dura o un glow del propio color de marca, no `shadow-lg`.
- **Color:** 1–2 colores de alta saturación + un neutro (negro o crema). Paleta extraída del producto (el parche, el envase, el logo), no de un generador de “SaaS palettes”.
- **Tipografía:** Displays y geométricas que no se deshagan sobre color plano.
  - [Clash Display](../tipografias/display-experimental.md), [Agrandir](../tipografias/sans-geometrica.md), [Syne](../tipografias/display-experimental.md), [Degular](../tipografias/sans-geometrica.md), [Outfit](../tipografias/sans-geometrica.md), [Plus Jakarta Sans](../tipografias/sans-grotesk.md), [Cabinet Grotesk](../tipografias/sans-grotesk.md).

## Sitios reales

- [starface.world](https://starface.world/) — citada por Figma; color de producto, stickers, energía de beauty joven. No usar `starface.com` (es otra compañía).
- [www.headspace.com](https://www.headspace.com/) — citada por Figma en el mismo lote de paletas vivas / dopamine.
- [drinkghia.com](https://drinkghia.com/) — blocking de color, tipo recortado, F&B.
- Lush es citada por Figma para este clima. `www.lush.com` devolvió 403 (antibot) desde este entorno: se menciona como cita de fuente, no como único ejemplo, y conviene abrirla en el navegador.

## Errores comunes

- Degradé índigo + Inter + “Unlock your potential”.
- Seis colores flúo sin un dominante.
- Texto claro sobre amarillo o lima sin comprobar el contraste.
- Aplicar la paleta también al flujo de checkout y perder legibilidad en forms.

## Snippet

Campo lima, tipo negro, Clash Display. Un solo color de marca.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=clash-display@600,700&display=swap">
  <style>body { font-family: "Clash Display", sans-serif; }</style>
</head>
<body class="bg-[#d6ff2f] text-black min-h-screen flex items-center">
  <main class="px-8 py-16 max-w-4xl">
    <p class="text-sm uppercase tracking-[0.16em]">Color de envase · no un índigo de UI kit</p>
    <h1 class="mt-4 text-6xl md:text-8xl font-bold leading-[0.9] tracking-tight">Un color que se ve desde el otro lado de la calle.</h1>
    <a href="#" class="inline-block mt-10 bg-black text-[#d6ff2f] px-6 py-3 text-lg font-semibold">Entrar</a>
  </main>
</body>
</html>
```

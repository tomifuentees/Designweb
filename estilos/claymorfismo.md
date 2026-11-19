# Claymorfismo

Soft UI “de arcilla”: radios muy altos, superficies pastel, una combinación de sombra exterior suave y dos sombras interiores que hacen que el objeto parezca inflado. The Plus Addons, en 2026, lo marca como **nicho estable**, no como tendencia en auge: onboarding, fintech amable, productos para chicos. Falla en formularios densos y en tablas. La receta CSS está bien documentada (Setproduct y otros tutorials de 2021–2026); lo que no apareció en esta investigación son tres sitios de marketing en producción cuyo *look completo* sea claymorfismo, comparables a Linear o Ghia.

Se documenta para usarlo con oficio en un componente (un CTA, un ilustrativo, un empty state), no como tema de un producto serio ni como default de un agente.

## Cuándo usarlo y cuándo no

**Usalo** en un onboarding, una app infantil o educativa, un momento lúdico de un fintech (un “felicitaciones”), un sticker tridimensional.

**No lo uses** en data tables, en settings, en landings B2B, ni como sistema completo. No lo uses para “humanizar” un SaaS oscuro: el choque queda infantil. No es un sustituto del [realismo táctil](./realismo-tactil.md) ni del [orgánico](./organico-terroso.md).

## Reglas concretas

- **Grilla:** La del producto. El clay es un tratamiento de componente, no una retícula.
- **Espaciado:** Interno generoso: el objeto inflado necesita carne. No apilés muchos “clay buttons” juntos, se pisan las sombras.
- **Radios:** Altos, 20–40 px o píldoras. El radio chico destruye el efecto.
- **Bordes:** Casi no. La forma la dan las sombras, no un stroke.
- **Sombras:** La receta típica es una sombra exterior suave y dos internas, una clara arriba-izquierda y una oscura abajo-derecha, del mismo tinte que el fondo (no un gris genérico). Ejemplo:

```css
.clay {
  background: #e7eef8;
  border-radius: 32px;
  box-shadow:
    8px 8px 20px rgba(80, 96, 128, .22),
    -6px -6px 18px rgba(255, 255, 255, .85),
    inset 2px 2px 6px rgba(255,255,255,.7),
    inset -2px -2px 6px rgba(80, 96, 128, .18);
}
```

- **Color:** Pasteles (celeste, menta, durazno, lila claro). Evitá el púrpura saturado de plantilla y los neones.
- **Tipografía:** Geométricas blandas, pesos medios, nada de display gritona.
  - [Satoshi](../tipografias/sans-geometrica.md), [Outfit](../tipografias/sans-geometrica.md), [Plus Jakarta Sans](../tipografias/sans-grotesk.md), [Agrandir](../tipografias/sans-geometrica.md) si hay licencia, [Figtree](../tipografias/sans-grotesk.md).

## Sitios reales

En esta pasada **no se pudieron verificar tres sitios de marketing en producción** cuyo idioma completo sea claymorfismo. Hay recetas y kits (y muchos shots de Dribbble / Behance, que no cuentan como producción). No se inventan URLs. Si aparece un producto real que lo sostenga de punta a punta, conviene sumarlo acá.

Hasta entonces, tratá el estilo como un componente, no como una referencia de sitio.

## Errores comunes

- Aplicarlo a un formulario de 12 campos o a una tabla: las sombras interiores ensucian la lectura.
- Usar sombras negras genéricas de Tailwind (`shadow-xl`) y llamarlo clay.
- Fondo blanco puro: el efecto pide un fondo pastel del mismo tinte, si no no hay “masa”.
- Combinarlo con glassmorfismo. Son idiomas distintos y juntos parecen un tutorial de 2021.

## Snippet

Un botón y una tarjeta inflados sobre un fondo pastel. Satoshi.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=satoshi@500,700&display=swap">
  <style>
    body { font-family: "Satoshi", sans-serif; background: #e7eef8; color: #2b3344; }
    .clay {
      background: #e7eef8;
      border-radius: 32px;
      box-shadow:
        8px 8px 20px rgba(80, 96, 128, .22),
        -6px -6px 18px rgba(255, 255, 255, .85),
        inset 2px 2px 6px rgba(255,255,255,.7),
        inset -2px -2px 6px rgba(80, 96, 128, .18);
    }
  </style>
</head>
<body class="min-h-screen flex items-center justify-center p-8">
  <div class="clay max-w-sm p-8 text-center">
    <p class="text-sm opacity-70">Componente · no un sistema</p>
    <h1 class="mt-3 text-3xl font-bold">Listo, ya quedó guardado.</h1>
    <p class="mt-3 text-sm leading-6">El clay funciona en un empty state o en un “felicitaciones”. En una tabla, no.</p>
    <button class="clay mt-8 px-6 py-3 font-semibold">Seguir</button>
  </div>
</body>
</html>
```

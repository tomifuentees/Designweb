# Bauhaus

Geometría primaria (círculo, cuadrado, triángulo), rojo, amarillo y azul sobre blanco o crudo, negro como estructura y una sans geométrica. No es nostalgia de 1925: en 2026 vuelve como sistema de **formas con función**, en marcas culturales, educación, apps móviles con mucha personalidad y señalética. El catálogo de [ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) (MIT) lo lista como estilo activo para mobile; esta ficha es una adaptación propia, no una copia.

## Cuándo usarlo y cuándo no

**Usalo** en instituciones culturales, escuelas de diseño o arte, museos, festivales, marcas de juguete o educación, productos que quieren parecer **construidos**, y en apps donde las formas pueden codificar categorías (cada sección con su forma).

**No lo uses** en salud, banca o legal como tema completo, ni en dashboards densos: los primarios saturados compiten con los datos. Tampoco como "decoración retro" con formas sueltas que no ordenan nada.

## Reglas concretas

- **Grilla:** estricta, modular, visible. Bloques de color que ocupan módulos enteros.
- **Espaciado:** generoso entre bloques, apretado dentro. El aire es blanco plano, no degradé.
- **Radios:** 0 px o círculo completo. Nada intermedio: el 12 px es de otra época.
- **Bordes:** negro de 2–4 px cuando separan; muchas veces no hay borde, el color es el borde.
- **Sombras:** ninguna.
- **Color:** rojo, amarillo y azul primarios **ajustados** (no `#ff0000`), negro y blanco crudo. Un primario domina por pantalla. Contraste: el amarillo nunca lleva texto blanco.
- **Formas:** cada forma significa algo (categoría, paso, estado). Si se puede borrar sin perder información, sobra.
- **Tipografía:** sans geométrica, pesos altos para titulares, minúsculas permitidas.
  - Titular: [Outfit](../tipografias/sans-geometrica.md), [GT Walsheim](../tipografias/sans-geometrica.md) o [Unbounded](../tipografias/display-experimental.md).
  - Cuerpo / UI: [General Sans](../tipografias/sans-geometrica.md) o [Sora](../tipografias/sans-geometrica.md).

## Sitios reales

- [bauhauskooperation.com](https://bauhauskooperation.com/) — la cooperación de las tres instituciones Bauhaus.
- [bauhaus.de](https://www.bauhaus.de/) — Bauhaus-Archiv / Museum für Gestaltung, Berlín.
- [bauhaus-dessau.de](https://www.bauhaus-dessau.de/en/) — Fundación Bauhaus Dessau.

## Errores comunes

- Primarios puros de pantalla (`#ff0000`, `#0000ff`, `#ffff00`): vibran y fallan contraste.
- Formas geométricas de fondo "para decorar". En este estilo la forma informa.
- Radios medianos y sombras suaves: rompen el idioma.
- Futura de sistema con kerning por defecto en titulares grandes.

## Snippet

```html
<section class="grid grid-cols-6 gap-0 font-[Outfit]" style="--rojo:#d2321e;--amarillo:#f2c230;--azul:#1f4fa3;--negro:#111">
  <div class="col-span-4 bg-white p-10">
    <h1 class="text-6xl font-bold leading-[0.95] tracking-tight text-[var(--negro)]">Taller abierto de tipografía</h1>
    <p class="mt-6 max-w-[40ch] text-lg">Sábados de 10 a 13, en la sala 2. Cupo de 12 personas.</p>
  </div>
  <div class="col-span-2 grid place-items-center bg-[var(--amarillo)]">
    <span class="block size-32 rounded-full bg-[var(--rojo)]" aria-hidden="true"></span>
  </div>
  <a href="#inscripcion" class="col-span-6 bg-[var(--azul)] p-6 text-xl font-semibold text-white focus-visible:outline-4 focus-visible:outline-offset-4 focus-visible:outline-[var(--negro)]">Inscribirme al taller</a>
</section>
```

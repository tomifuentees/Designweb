# Arquitectura de información y navegación

La arquitectura de información (AI, no confundir con IA) decide **dónde vive cada cosa y cómo se llama**. Si la persona no encuentra algo, da igual lo bien hecho que esté.

## Principios

1. **Organizá por tareas y modelo mental de la persona**, no por organigrama ni por base de datos.
2. **Nombres que la persona usaría** (validados con card sorting / tree testing).
3. **Pocos niveles, bien rotulados**: es mejor ancho y claro que profundo y adivinado. Cada clic tiene que dar *scent* (aroma de información) de que vas bien.
4. **Dónde estoy / adónde puedo ir / cómo vuelvo** siempre respondibles.
5. **Una URL por estado importante** (filtros, pestañas, búsquedas) para compartir, recargar y volver con el botón Atrás.

## Métodos

| Método | Cuándo | Salida |
|---|---|---|
| Inventario de contenido | Antes de rediseñar | Qué hay, quién lo usa, qué se borra |
| Card sorting abierto | Explorar cómo agrupa la gente | Grupos y nombres candidatos |
| Card sorting cerrado | Validar categorías propuestas | % de acuerdo por ítem |
| Tree testing | Validar la jerarquía sin UI | Tasa de éxito y directness por tarea |
| Analítica de búsqueda interna | Siempre | Términos que la navegación no resuelve |
| First-click test | Validar rótulos en pantalla | Si el primer clic es correcto (fuerte predictor de éxito) |

Herramientas: Optimal Workshop (Treejack, OptimalSort), Maze, UXtweak, Lyssna. Ver [`investigacion-testing.md`](investigacion-testing.md).

## Patrones de navegación: cuándo usar cuál

| Patrón | Usalo cuando | Evitalo cuando |
|---|---|---|
| Barra superior con 4–7 ítems | Sitios de marketing, apps simples | Más de ~7 secciones top-level |
| Sidebar persistente | Apps de producto, dashboards, docs | Sitios de contenido en mobile (colapsar) |
| Bottom navigation (mobile) | 3–5 destinos principales de uso frecuente | Más de 5 destinos o acciones (no es una toolbar) |
| Hamburguesa | Secundario o mobile con muchos destinos | Única vía a destinos clave en desktop (baja descubribilidad, NN/g) |
| Mega menú | E-commerce o institucional con muchas categorías | Pocos ítems; activarlo solo al hover sin delay |
| Tabs | Vistas hermanas del mismo objeto | Pasos secuenciales (usá stepper) |
| Breadcrumbs | Jerarquías de 3+ niveles, e-commerce, docs | Apps planas |
| Command palette (`⌘K`) | Apps con muchas acciones, usuarios frecuentes | Como única navegación |
| Búsqueda | Siempre que haya >~50 ítems de contenido | — ([`busqueda-filtros.md`](busqueda-filtros.md)) |

### Reglas concretas

- **Rótulos visibles** en navegación por íconos (el ícono solo no alcanza salvo universales: casa, buscar, carrito, y aun así con `aria-label`).
- **Ítem activo** con indicador visual que no sea solo color + `aria-current="page"`.
- **Logo → inicio**.
- **Mega menús**: abrir con clic o con hover + delay (~300–500 ms para entrar y salir) y triángulo de tolerancia para que el menú no se cierre al mover el mouse en diagonal.
- **Navegación consistente** entre páginas (WCAG 3.2.3) y ayuda en el mismo lugar (3.2.6).
- **Skip link** como primer elemento enfocable.
- **Footer como mapa del sitio** en sitios de contenido (la gente lo usa para encontrar contacto, legales, soporte).
- **No esconder el precio, el contacto ni el login.**

## Snippet: navegación accesible con disclosure (no ARIA menu)

Para navegación de sitio usá el patrón *disclosure* del [APG](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/examples/disclosure-navigation/), no `role="menu"` (que es para menús de aplicación tipo escritorio).

```html
<a class="skip-link" href="#main">Saltar al contenido</a>
<nav aria-label="Principal">
  <ul class="nav">
    <li><a href="/" aria-current="page">Inicio</a></li>
    <li>
      <button type="button" aria-expanded="false" aria-controls="sub-productos">Productos</button>
      <ul id="sub-productos" hidden>
        <li><a href="/productos/facturacion">Facturación</a></li>
        <li><a href="/productos/stock">Stock</a></li>
      </ul>
    </li>
    <li><a href="/precios">Precios</a></li>
  </ul>
</nav>
<main id="main" tabindex="-1">…</main>

<script>
document.querySelectorAll('nav button[aria-expanded]').forEach((btn) => {
  const panel = document.getElementById(btn.getAttribute('aria-controls'));
  btn.addEventListener('click', () => {
    const open = btn.getAttribute('aria-expanded') === 'true';
    btn.setAttribute('aria-expanded', String(!open));
    panel.hidden = open;
  });
  btn.parentElement.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && btn.getAttribute('aria-expanded') === 'true') {
      btn.setAttribute('aria-expanded', 'false'); panel.hidden = true; btn.focus();
    }
  });
});
</script>
<style>
.skip-link { position:absolute; left:-9999px; }
.skip-link:focus { left:1rem; top:1rem; z-index:100; }
[aria-current="page"] { text-decoration: underline; text-underline-offset: .3em; font-weight: 600; }
</style>
```

## Snippet: breadcrumb

```html
<nav aria-label="Ruta de navegación">
  <ol class="breadcrumb">
    <li><a href="/">Inicio</a></li>
    <li><a href="/zapatillas">Zapatillas</a></li>
    <li><a href="/zapatillas/running" aria-current="page">Running</a></li>
  </ol>
</nav>
<style>
.breadcrumb { display:flex; flex-wrap:wrap; gap:.25rem; list-style:none; padding:0; }
.breadcrumb li + li::before { content:"/"; margin-inline:.25rem; color: var(--muted); }
</style>
```

## Estado en la URL (React)

```tsx
// Filtros, pestañas y página viven en la URL: recargar, compartir y "Atrás" funcionan.
import { useSearchParams } from "react-router-dom"; // o next/navigation
export function useUrlState(key: string, fallback = "") {
  const [params, setParams] = useSearchParams();
  const value = params.get(key) ?? fallback;
  const set = (v: string) => {
    const next = new URLSearchParams(params);
    v ? next.set(key, v) : next.delete(key);
    setParams(next, { replace: false });
  };
  return [value, set] as const;
}
```

## SPA: navegación que no rompa la experiencia

- Al cambiar de ruta: mover el foco al `<h1>` o a `<main>` y anunciar el título (lector de pantalla no se entera si no).
- Actualizar `document.title` en cada ruta.
- Restaurar el scroll al volver; arriba al ir a una nueva.
- Con View Transitions (Baseline desde 14/10/2025 para mismo documento, según web-features 3.46.0) respetá `prefers-reduced-motion`. Ver [`../animaciones/`](../animaciones/README.md).
- CrUX empezó a medir *soft navigations* de SPA en 2026 y planea incluirlas en Core Web Vitals desde mayo de 2027 ([CrUX release notes, 11/11/2026](https://developer.chrome.com/docs/crux/release-notes)).

## Anti-patrones de arquitectura y navegación

- Rótulos ingeniosos ("Explorá el universo") en lugar de descriptivos ("Productos").
- Duplicar el mismo destino con nombres distintos.
- Navegación que cambia de lugar según la página.
- Tabs que en realidad son pasos, o pasos que en realidad son tabs.
- Infinite scroll en páginas donde el footer tiene información necesaria.
- Filtros y paginación que no viven en la URL.

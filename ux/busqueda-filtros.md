# Búsqueda y filtros

Baymard: en sus tests, aproximadamente la mitad de las personas usa la búsqueda como primera estrategia y la otra mitad la navegación. En su benchmark 2026 (170+ sitios, 10.000+ puntuaciones), el **56 % de los sitios no soporta bien la búsqueda** ([Baymard, actualizado 29/04/2026](https://baymard.com/research-articles/ecommerce-search-query-types)).

## Los 8 tipos de consulta que tu búsqueda tiene que entender (Baymard)

| Tipo | Ejemplo | % de sitios con problemas (2026) |
|---|---|---|
| Exacta | "Nike Pegasus 41" / un número de modelo | 12 % |
| Tipo de producto | "zapatillas" | 20 % |
| Característica | "campera impermeable roja" | 39 % |
| Caso de uso | "zapatillas para correr en montaña" | 43 % |
| Abreviaturas y símbolos | "tv 55\"", "usb c", "1/2 pulgada" | 54 % |
| Compatibilidad | "funda iphone 16" | 44 % |
| Síntoma | "piel seca", "pantalla que parpadea" | 37 % |
| No-producto | "devoluciones", "horario", "envío gratis" | 66 % |

Implicancia para devs: sinónimos, tolerancia a typos, unidades normalizadas, datos de producto estructurados y que el buscador también indexe páginas de ayuda.

## Caja de búsqueda

- **Visible como campo** (no solo una lupa) en sitios con mucho contenido; en desktop ≥ ~27 caracteres de ancho visible.
- `<search>` + `<input type="search">` + `<label>` (puede ser visualmente oculto) + botón con texto accesible.
- **La consulta queda en el campo** en la página de resultados, editable.
- Atajo `/` o `⌘K` para usuarios frecuentes (sin robar el foco al cargar).

## Autocompletado

- Sugerencias desde la 1.ª–2.ª letra, en <~100–200 ms; máximo ~8–10 en desktop, menos en mobile (Baymard).
- **Resaltá la parte que completa** (no la que la persona escribió).
- Mezclar tipos: consultas, categorías ("en Zapatillas"), productos con imagen, búsquedas recientes (borrables).
- Teclado: ↑↓ navegan, Enter elige, Esc cierra. Patrón [Combobox del APG](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/) con `aria-activedescendant`.

## Resultados

- Contador ("128 resultados para 'campera'").
- **Sin resultados ≠ callejón sin salida**: corrección ("¿Quisiste decir…?"), consultas relacionadas, categorías, contacto. Ver [`estados.md`](estados.md).
- Orden por relevancia por defecto, con opción de ordenar.
- Mantener filtros, orden y página en la URL ([`arquitectura-informacion-navegacion.md`](arquitectura-informacion-navegacion.md)).

## Filtros (facetas)

- **Facetas relevantes a la categoría** (talle y color en ropa; RAM y pantalla en notebooks), no las mismas para todo.
- Mostrar **cantidad por opción** y deshabilitar/ocultar las que dan 0.
- **Filtros aplicados visibles** como "chips" con ✕ y "Borrar todo", arriba de los resultados.
- Desktop: sidebar izquierda o barra horizontal; mobile: botón "Filtrar (3)" que abre un panel de pantalla completa con "Ver 42 resultados" fijo abajo.
- **Aplicación**: en desktop, inmediata (con feedback y sin saltos de scroll); en mobile, por lote con botón "Aplicar" para no recargar a cada toque. Anunciá el nuevo conteo con una región `aria-live="polite"`.
- Rango de precio: dos inputs editables (+ slider opcional).
- No reinicies el scroll ni pierdas filtros al volver desde un producto.

## Snippet: chips de filtros aplicados + anuncio de resultados

```tsx
export function AppliedFilters({ filters, onRemove, onClear, count }: {
  filters: { key: string; label: string }[]; onRemove: (k: string) => void; onClear: () => void; count: number }) {
  return (
    <div className="flex flex-wrap items-center gap-2">
      <p aria-live="polite" className="me-2 font-medium tabular-nums">{count} resultados</p>
      {filters.map((f) => (
        <button key={f.key} type="button" onClick={() => onRemove(f.key)}
          className="inline-flex items-center gap-1 rounded-full border px-3 min-h-[2.75rem] sm:min-h-8"
          aria-label={`Quitar filtro ${f.label}`}>
          {f.label} <span aria-hidden="true">✕</span>
        </button>
      ))}
      {filters.length > 1 && <button type="button" onClick={onClear} className="underline">Borrar todo</button>}
    </div>
  );
}
```

## Paginación vs "cargar más" vs scroll infinito

| Patrón | Usalo cuando | Cuidado |
|---|---|---|
| Paginación | Buscar algo concreto, comparar, volver a un punto | — |
| "Cargar más" | E-commerce (Baymard lo prefiere como balance) | Mantener posición al volver (guardar en URL / sessionStorage) |
| Scroll infinito | Feeds de descubrimiento sin meta | Footer inalcanzable, sin sentido de fin, problemas de teclado y lector |

## Búsqueda con IA / semántica (2026)

- Baymard incorporó la guía #3458: un asistente de IA a nivel sitio para intenciones vagas o complejas cuando búsqueda y menús no alcanzan ([guía #3458](https://baymard.com/guidelines/3458-providing-a-sitewide-ai-assistant)).
- Mantené la búsqueda clásica como camino principal y rápido; la IA como complemento ("Preguntale al asistente") con fuentes y productos linkeados, no solo texto.
- Ver [`ux-ia.md`](ux-ia.md).

# Tablas, datos y dashboards

Visual de tablas y dashboards: [`../componentes/tables.md`](../componentes/tables.md) y [`../componentes/dashboards.md`](../componentes/dashboards.md). Acá: **qué decisiones** soporta cada pantalla y cómo se usa.

## Dashboards: diseñá decisiones, no gráficos

1. **¿Quién lo mira, cada cuánto y qué decide?** Un dashboard operativo (¿qué hago ahora?) no es uno analítico (¿por qué pasó?) ni uno estratégico (¿vamos bien?).
2. **Arriba a la izquierda, lo más importante** (patrón de lectura en Z/F en dashboards densos).
3. **Cada número con contexto**: comparación (vs. período anterior, vs. meta), unidad, período y fecha de actualización. "Ventas: $4,2 M" no dice nada; "$4,2 M · +8 % vs. oct · meta $4,5 M · actualizado 14:05" sí.
4. **Pocos KPIs** (3–6 por vista); el resto, en drill-down.
5. **Del resumen al detalle**: cada KPI clickeable lleva a la tabla filtrada que lo explica.
6. **Alertas por excepción**: resaltar solo lo que se sale de lo normal.
7. **Estado de los datos**: cargando, parciales, desactualizados, error de fuente ([`estados.md`](estados.md)).

## Elegir el gráfico

| Pregunta | Gráfico | Evitar |
|---|---|---|
| Comparar categorías | Barras horizontales ordenadas | Torta con > 3–4 partes |
| Evolución en el tiempo | Línea (barras si son pocos períodos discretos) | Área apilada para comparar series |
| Parte de un todo | Barra apilada al 100 % o torta con ≤ 3 | Donut 3D |
| Distribución | Histograma, box plot | Promedios solos |
| Relación entre dos variables | Dispersión | Doble eje Y (engaña) |
| Un número | Número grande + sparkline + delta | Velocímetro |

Reglas: eje Y de barras **desde cero**; color con significado (no arcoíris); **no solo color** para distinguir series (patrones, labels directos, WCAG 1.4.1); etiquetado directo mejor que leyenda; tabla accesible alternativa para cada gráfico.

## Tablas

- **Alinear números a la derecha** con `font-variant-numeric: tabular-nums`; texto a la izquierda; misma precisión decimal por columna.
- **Encabezado fijo** (`position: sticky`) y primera columna fija si hay scroll horizontal.
- **Orden** por columna con indicador y `aria-sort`; el orden actual siempre visible.
- **Filtros y búsqueda** en la tabla; estado en la URL.
- **Densidad ajustable** (cómoda / compacta) para usuarios intensivos.
- **Acciones por fila**: las frecuentes visibles; las demás en menú "Más acciones" con label accesible. No acciones solo al hover.
- **Selección masiva**: checkbox en encabezado con estado mixto, barra de acciones contextual ("3 seleccionadas · Exportar · Archivar").
- **Paginación** con tamaño de página y total; virtualización para miles de filas (manteniendo semántica de tabla).
- **Mobile**: priorizá columnas, convertí filas en cards o permití scroll horizontal con la primera columna fija. No escondas datos críticos.
- **Edición inline**: solo para campos simples; Enter guarda, Esc cancela, feedback por celda.
- **Exportar** (CSV/Excel) con lo filtrado.

## Snippet: tabla ordenable accesible

```tsx
type Col<T> = { key: keyof T; label: string; numeric?: boolean };
export function SortableTable<T extends Record<string, any>>({ rows, cols }: { rows: T[]; cols: Col<T>[] }) {
  const [sort, setSort] = React.useState<{ key: keyof T; dir: "ascending" | "descending" } | null>(null);
  const data = React.useMemo(() => !sort ? rows : [...rows].sort((a, b) => {
    const r = a[sort.key] > b[sort.key] ? 1 : a[sort.key] < b[sort.key] ? -1 : 0;
    return sort.dir === "ascending" ? r : -r; }), [rows, sort]);
  return (
    <div className="overflow-x-auto" role="region" aria-labelledby="t-cap" tabIndex={0}>
      <table className="w-full border-collapse">
        <caption id="t-cap" className="text-left font-semibold mb-2">Facturas de noviembre</caption>
        <thead className="sticky top-0 bg-[var(--surface)]">
          <tr>{cols.map((c) => {
            const active = sort?.key === c.key;
            return (
              <th key={String(c.key)} scope="col" aria-sort={active ? sort!.dir : "none"}
                  className={c.numeric ? "text-right" : "text-left"}>
                <button type="button" className="inline-flex items-center gap-1 py-2"
                  onClick={() => setSort({ key: c.key, dir: active && sort!.dir === "ascending" ? "descending" : "ascending" })}>
                  {c.label}<span aria-hidden="true">{active ? (sort!.dir === "ascending" ? "▲" : "▼") : "↕"}</span>
                </button>
              </th>);
          })}</tr>
        </thead>
        <tbody>{data.map((r, i) => (
          <tr key={i} className="border-t">{cols.map((c) => (
            <td key={String(c.key)} className={c.numeric ? "text-right tabular-nums py-2" : "py-2"}>{r[c.key]}</td>))}
          </tr>))}
        </tbody>
      </table>
    </div>
  );
}
import React from "react";
```

## Formato de números y fechas

- `Intl.NumberFormat` y `Intl.DateTimeFormat` con el locale de la persona; nunca formateo a mano.
- Números grandes abreviados en KPIs (`notation: "compact"` → "4,2 M") pero exactos en tablas.
- Fechas relativas para lo reciente ("hace 5 min", `Intl.RelativeTimeFormat`) con la absoluta en `title`/`<time datetime>`.
- Zona horaria explícita cuando importa.

## Anti-patrones

- Dashboard "bonito" con 14 gráficos y ninguna decisión clara.
- KPIs sin comparación ni período.
- Tortas de 9 colores; doble eje Y; ejes truncados en barras.
- Tablas con números centrados y fuentes proporcionales.
- Acciones de fila que solo aparecen con hover.
- Sin "última actualización".

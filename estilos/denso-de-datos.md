# Denso de datos

El estilo de las herramientas donde la gente trabaja ocho horas: terminales financieras, monitoreo, trading, logística, back-office. Mucha información por pantalla, filas de 28–32 px, cifras tabulares, color solo para significado. Es lo contrario del dashboard de marketing con 12 cards redondeadas. [ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) (MIT) lo cataloga como "Data-Dense Dashboard"; la ficha es propia y se apoya en [`../ux/tablas-datos-dashboards.md`](../ux/tablas-datos-dashboards.md).

## Cuándo usarlo y cuándo no

**Usalo** en back-office, conciliaciones, inventario, caja, monitoreo, analítica operativa, herramientas internas y paneles para gente experta que vuelve todos los días.

**No lo uses** en landings, onboarding de consumidores ni en apps para gente que entra una vez al mes.

## Reglas concretas

- **Grilla:** shell que llena el viewport (sidebar de 220–260 px, contenido fluido); paneles redimensionables si hace falta.
- **Espaciado:** grilla de 4 px. Filas de tabla de 28–32 px, celdas con 8–12 px de padding horizontal. Navegación: filas de 32–36 px.
- **Radios:** 4–6 px en controles, 0–8 px en paneles.
- **Bordes:** filetes de 1 px de bajo contraste para separar filas y paneles; nada de cards anidadas.
- **Sombras:** ninguna en la superficie de trabajo; solo en menús y popovers.
- **Color:** neutros casi grises (la gente los mira horas), un acento para selección y acción primaria, y semánticos apagados (subió / bajó / error). Nunca un fondo de color de marca.
- **Números:** `tabular-nums`, alineados a la derecha, un formato por pantalla, unidades en el encabezado.
- **Motion:** casi nada. Cambios de valor con un destello de fondo de ≤ 300 ms, apagable.
- **Tipografía:** sans de UI muy legible en tamaños chicos y una mono para cifras o ids.
  - UI: [IBM Plex Sans](../tipografias/sans-grotesk.md), [Public Sans](../tipografias/sans-grotesk.md) o [Untitled Sans](../tipografias/sans-grotesk.md).
  - Cifras / ids: [JetBrains Mono](../tipografias/mono.md), [Commit Mono](../tipografias/mono.md) o [IBM Plex Mono](../tipografias/mono.md).

## Sitios reales

- [tradingview.com](https://www.tradingview.com/) — gráficos y tablas densas, color solo para subidas y bajadas.
- [grafana.com](https://grafana.com/) — paneles de monitoreo; mirá el producto, no la landing.
- [datadoghq.com](https://www.datadoghq.com/) — observabilidad con mucha información por vista.

## Errores comunes

- Cards con radio grande y sombra para cada KPI: se pierde la mitad de la pantalla.
- Texto funcional de 10 px "para que entre": el piso es 11 px (12–13 en tablas).
- Rojo y verde como única señal: sumá ícono o signo (▲ ▼) por daltonismo.
- Animar cada número que cambia.

## Snippet

```html
<table class="w-full border-collapse font-[IBM_Plex_Sans] text-[13px] text-[oklch(0.25_0_0)]">
  <thead class="sticky top-0 bg-[oklch(0.97_0_0)] text-left text-[12px] font-medium text-[oklch(0.45_0_0)]">
    <tr><th scope="col" class="h-8 px-3">Sucursal</th><th scope="col" class="h-8 px-3 text-right">Esperado ($)</th><th scope="col" class="h-8 px-3 text-right">Contado ($)</th><th scope="col" class="h-8 px-3 text-right">Diferencia ($)</th></tr>
  </thead>
  <tbody class="[&>tr]:h-8 [&>tr]:border-t [&>tr]:border-[oklch(0.92_0_0)]">
    <tr><td class="px-3">Centro</td><td class="px-3 text-right tabular-nums">412.300</td><td class="px-3 text-right tabular-nums">412.300</td><td class="px-3 text-right tabular-nums">0</td></tr>
    <tr><td class="px-3">Norte</td><td class="px-3 text-right tabular-nums">388.900</td><td class="px-3 text-right tabular-nums">383.900</td><td class="px-3 text-right tabular-nums text-[oklch(0.5_0.17_28)]">▼ −5.000</td></tr>
  </tbody>
</table>
```

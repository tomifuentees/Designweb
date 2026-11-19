# Tablas

Una tabla es para comparar filas. Si el dato no se compara, capaz es una lista. Si se compara y lo metés en cards apiladas, el usuario no puede barrer con la vista una columna.

Tono de referencia: [`../estilos/catalogo-tecnico.md`](../estilos/catalogo-tecnico.md). Kibo y shadcn tienen data tables; Tremor, con la salvedad de ritmo (ver [bibliotecas.md](./bibliotecas.md)), está pensado para esto.

## Cuándo usarlo y cuándo no

**Usalo** en depósitos, diferencias, cuentas, logs, stocks. **No lo uses** para tres ítems de marketing, ni para un “leaderboard” decorativo en una landing.

## Qué se ve con terminación pro

- Encabezados fijos al hacer scroll, alineación según el tipo (texto a la izquierda, números a la derecha, fechas en mono).
- Densidad consciente: una tabla de operaciones es más junta que una de onboarding. El default `p-4` de shadcn suele quedar flojo para datos.
- Estados de fila: hover, seleccionado, deshabilitado. Acciones al final o en un menú, no siete íconos Lucide por fila.
- Vacío y carga: skeleton o un empty state de tabla (ver [empty-states.md](./empty-states.md)), no una tabla “sin filas” muda.
- Ordenar, filtrar y paginar con indicadores claros (“23 resultados, página 2 de 5”). El sort no se esconde en un ícono invisible.
- Números tabulares (`font-variant-numeric: tabular-nums`) para que los montos no bailen.
- En mobile: una tabla que scrollea en horizontal *o* se convierte en filas-bloque, no un shrink ilegible.

## Qué hace mal el default de IA

- Cada registro es una card `rounded-2xl` con el mismo dato en vertical.
- Tabla de shadcn default, con badges índigo “Active” / “Pending” y un avatar en la primera columna aunque no haga falta.
- Montos a la izquierda, fechas en lenguaje natural inconsistente, sin `tabular-nums`.
- Acciones “Edit” “Delete” en texto rojo en cada fila, sin confirmación.
- Cero consideración de 200 filas: no hay paginación, virtualización ni un filtro.

## Tipografía del kit

- UI: [Satoshi](../tipografias/sans-geometrica.md) o [IBM Plex Sans](../tipografias/sans-grotesk.md) si está en el kit como apoyo.
- Cifras y fechas: [IBM Plex Mono](../tipografias/mono.md) o la sans con `tabular-nums`.

## Snippet

Montos a la derecha, estado en texto, captions en mono.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=satoshi@400,500,600&display=swap">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
  <style>
    body { font-family: "Satoshi", sans-serif; background: #f5f3ee; color: #171513; }
    .mono { font-family: "IBM Plex Mono", ui-monospace, monospace; font-variant-numeric: tabular-nums; }
  </style>
</head>
<body class="max-w-4xl mx-auto px-6 py-16">
  <h1 class="text-xl font-medium">Depósitos de la semana</h1>
  <p class="mono text-xs text-neutral-500 mt-1">3 filas de ejemplo · montos alineados</p>
  <div class="mt-6 overflow-x-auto border-t border-black/15">
    <table class="w-full text-sm">
      <thead class="text-left text-xs uppercase tracking-[0.12em] text-neutral-500">
        <tr class="border-b border-black/10">
          <th class="py-2 font-medium">Fecha</th>
          <th class="py-2 font-medium">Sucursal</th>
          <th class="py-2 font-medium text-right">Monto</th>
          <th class="py-2 font-medium">Estado</th>
        </tr>
      </thead>
      <tbody>
        <tr class="border-b border-black/10">
          <td class="py-3 mono">16.11</td>
          <td>Cruz del Sur</td>
          <td class="text-right mono">1.376.550</td>
          <td>Depositado</td>
        </tr>
        <tr class="border-b border-black/10">
          <td class="py-3 mono">17.11</td>
          <td>Naciones Unidas</td>
          <td class="text-right mono">1.524.600</td>
          <td>Depositado</td>
        </tr>
        <tr>
          <td class="py-3 mono">17.11</td>
          <td>Oro</td>
          <td class="text-right mono">230.000</td>
          <td>Pendiente</td>
        </tr>
      </tbody>
    </table>
  </div>
</body>
</html>
```

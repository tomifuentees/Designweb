# Estados de la interfaz

Una pantalla no es una imagen: es una máquina de estados. La IA casi siempre diseña solo el "ideal". Este archivo cubre el **comportamiento** de cada estado; el aspecto visual de empty y toasts ya está en [`../componentes/empty-states.md`](../componentes/empty-states.md) y [`../componentes/toasts.md`](../componentes/toasts.md).

## La matriz mínima (por cada vista con datos)

| Estado | Pregunta | Qué mostrar |
|---|---|---|
| **Primera vez (vacío inicial)** | ¿Qué es esto y cómo empiezo? | Explicación de 1 línea + acción primaria + ejemplo/plantilla |
| **Vacío por filtro/búsqueda** | ¿Por qué no hay nada? | "Sin resultados para X" + quitar filtros / sugerencias |
| **Vacío "limpio"** (inbox zero, todo hecho) | ¿Está bien? | Confirmación positiva, sin CTA forzado |
| **Cargando (inicial)** | ¿Está funcionando? | Skeleton con la forma real (si >~300 ms); nada si es más rápido |
| **Cargando (parcial / refresco)** | ¿Se actualiza? | Indicador local; mantener datos viejos visibles |
| **Parcial** | ¿Falta algo? | Lo que hay + aviso de lo que falló |
| **Ideal** | — | — |
| **Error recuperable** | ¿Qué pasó y qué hago? | Mensaje claro + "Reintentar" + conservar input |
| **Error no recuperable / sin permiso** | ¿Puedo hacer algo? | Explicar, a quién pedir acceso, link a soporte. No es un "error de validación" (GOV.UK) |
| **Offline** | ¿Se perdió lo que hice? | Banner persistente, cola de cambios, sincronizar al volver |
| **Éxito** | ¿Salió bien? | Confirmación proporcional al impacto (inline, toast o página) |
| **Demasiados datos** | ¿Escala? | Paginación, virtualización, truncado con "ver más" |

Agente: listá la matriz en el brief y marcá cuáles aplican antes de codear.

## Cargas: cuál indicador

Basado en [NN/g, Skeleton Screens](https://www.nngroup.com/articles/skeleton-screens/) (actualizado 02/09/2026) y [Progress Indicators](https://www.nngroup.com/articles/progress-indicators/).

| Duración esperada | Indicador |
|---|---|
| < ~300 ms | Nada (un spinner que parpadea se siente más lento) |
| 300 ms – 2 s | Skeleton (carga de página/sección) o spinner local (acción en un botón) |
| 2 – 10 s | Skeleton + texto de qué pasa; spinner con label |
| > 10 s | Barra de progreso determinada con estimación, opción de seguir con otra cosa y aviso al terminar |

- Skeleton = **forma real** del contenido (no barras genéricas), sin shimmer si hay `prefers-reduced-motion`.
- Retrasá el indicador ~300 ms para no "flashear" en cargas rápidas; si aparece, mantenelo un mínimo (~500 ms) para no parpadear.
- `aria-busy="true"` en la región que carga; anunciar el fin si es relevante.
- **No uses skeleton para acciones** (guardar, enviar): usá estado pending en el botón.

```css
.skeleton { background: color-mix(in oklch, var(--text) 8%, transparent); border-radius: var(--radius-sm, 4px); }
@media (prefers-reduced-motion: no-preference) {
  .skeleton { background-image: linear-gradient(90deg, transparent, color-mix(in oklch, var(--text) 6%, transparent), transparent);
    background-size: 200% 100%; animation: sk 1.4s ease-in-out infinite; }
  @keyframes sk { from { background-position: 200% 0 } to { background-position: -200% 0 } }
}
```

```tsx
// Mostrar el skeleton solo si la carga supera 300 ms
import { useEffect, useState } from "react";
export function useDelayedFlag(active: boolean, delay = 300) {
  const [show, setShow] = useState(false);
  useEffect(() => { if (!active) { setShow(false); return; }
    const t = setTimeout(() => setShow(true), delay); return () => clearTimeout(t); }, [active, delay]);
  return show;
}
```

## UI optimista

Mostrar el resultado antes de que el servidor confirme, y revertir si falla.

**Usala** en acciones frecuentes, reversibles y con alta tasa de éxito: like, marcar como hecho, mover tarjeta, renombrar.
**No la uses** en pagos, envíos de dinero, borrados definitivos, nada con efectos externos o validación compleja.

```tsx
// React 19: useOptimistic
import { useOptimistic, startTransition } from "react";
export function TodoItem({ todo, save }: { todo: { id: string; done: boolean; title: string };
  save: (id: string, done: boolean) => Promise<void> }) {
  const [optimisticDone, setOptimisticDone] = useOptimistic(todo.done);
  async function toggle() {
    startTransition(async () => {
      setOptimisticDone(!optimisticDone);
      try { await save(todo.id, !optimisticDone); }
      catch { /* React revierte solo; avisá: */ toast.error("No se pudo guardar. Probá de nuevo."); }
    });
  }
  return (
    <label className="flex items-center gap-2 min-h-11">
      <input type="checkbox" checked={optimisticDone} onChange={toggle} /> {todo.title}
    </label>
  );
}
declare const toast: { error: (m: string) => void };
```

## Errores

- **Distinguí** error de validación (la persona lo arregla, [`formularios-inputs.md`](formularios-inputs.md)), error del sistema (reintentar), sin permiso (pedir acceso) y no encontrado (404 útil).
- Mensaje: qué pasó, si se perdió algo, qué hacer. Nunca culpar. Código técnico solo como dato secundario para soporte ("Código: 8F2A").
- **Reintento automático** con backoff para fallos de red transitorios; manual después de 2–3 intentos.
- **404**: buscador, links principales, reportar link roto.
- **Errores de React**: `ErrorBoundary` por sección, no una pantalla blanca para toda la app.

```tsx
<ErrorBoundary fallback={({ reset }) => (
  <div role="alert" className="grid gap-2 p-4 border rounded">
    <p className="font-semibold">No pudimos cargar tus facturas.</p>
    <p>Tus datos están a salvo. Revisá la conexión y probá otra vez.</p>
    <button type="button" onClick={reset} className="justify-self-start underline">Reintentar</button>
  </div>
)}>
  <Facturas />
</ErrorBoundary>
```

## Offline y conexión inestable

- Detectá con `navigator.onLine` + eventos `online`/`offline` (y fallos reales de fetch: `onLine` puede mentir).
- Banner persistente, no un toast que se va: "Sin conexión. Tus cambios se guardan y se envían cuando vuelva."
- Cola local (IndexedDB) + sincronización; indicador por ítem pendiente.
- Deshabilitar solo lo que de verdad no funciona offline (y decir por qué).

```js
const banner = document.getElementById('offline');
const update = () => { banner.hidden = navigator.onLine; };
addEventListener('online', update); addEventListener('offline', update); update();
// <div id="offline" role="status" hidden>Sin conexión. Guardamos tus cambios y los enviamos cuando vuelva.</div>
```

## Éxito proporcional

| Impacto | Feedback |
|---|---|
| Bajo, reversible (guardar ajuste) | Cambio inline ("Guardado ✓") |
| Medio (enviar mensaje, mover) | Toast con "Deshacer" |
| Alto o irreversible (pago, envío de formulario oficial) | Página de confirmación con número, resumen y próximos pasos |

## Anti-patrones

- Spinner de página completa para cualquier cosa.
- Skeleton que no se parece al contenido, o que queda para siempre si falla la carga.
- Empty igual para "primera vez", "sin resultados" y "sin permiso".
- "Algo salió mal" sin acción.
- Toast verde que se va en 2 s para algo irreversible.
- Botón que no cambia al hacer clic (doble envío).
- Layout shift cuando llegan los datos (reservá espacio: CLS, [`rendimiento-percibido.md`](rendimiento-percibido.md)).

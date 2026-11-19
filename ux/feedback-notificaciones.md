# Feedback, notificaciones, modales y confirmaciones

El aspecto visual de los toasts está en [`../componentes/toasts.md`](../componentes/toasts.md). Acá: **cuándo** usar cada mecanismo y cómo se comporta.

## Elegir el canal

| Situación | Canal | Por qué |
|---|---|---|
| Resultado de una acción en un campo / ítem | **Inline**, al lado de lo que cambió | El ojo ya está ahí |
| Acción completada, reversible, no crítica | **Toast** (con Deshacer si aplica) | No interrumpe |
| Error que impide seguir | **Inline** (+ resumen) | Un toast se va y se pierde |
| Estado persistente del sistema (offline, plan vencido, mantenimiento) | **Banner** persistente, descartable si no es crítico | Tiene que seguir visible |
| Decisión obligatoria antes de seguir, consecuencia seria | **Modal (dialog)** | Interrumpe a propósito |
| Tarea secundaria sin perder el contexto (editar un ítem) | **Drawer / panel lateral** o página | Mejor que un modal largo |
| Algo que pasó mientras la persona no estaba | **Centro de notificaciones / email / push** | Asíncrono |
| Ayuda breve sobre un control | **Tooltip** (solo info no esencial) o *toggletip* | No esconder info crítica en hover |

## Deshacer > confirmar

Aza Raskin, ["Never Use a Warning When You Mean Undo"](https://alistapart.com/article/neveruseawarning/) (A List Apart, 2007): la gente confirma diálogos en automático; el diálogo no previene errores, el undo sí.

- **Reversible** (archivar, mover, borrar a papelera, quitar del carrito) → hacelo ya + toast "Archivado · Deshacer" (≥ ~5–10 s, pausa al hover/foco).
- **Irreversible y grave** (borrar cuenta, eliminar proyecto con datos, enviar pago) → confirmación **específica**:
  - Título con la consecuencia: "¿Eliminar el proyecto 'Ventas 2026' y sus 214 facturas?"
  - Botones con el verbo: "Eliminar proyecto" / "Cancelar" (nunca "Sí / No" ni "OK").
  - Para lo muy grave: escribir el nombre para confirmar.
  - Foco inicial en la opción segura (Cancelar) o en el campo de confirmación.
- NN/g, [Confirmation Dialogs](https://www.nngroup.com/articles/confirmation-dialog/) (actualizado 07/08/2026): no abuses, porque si todo pide confirmación, nada se lee.

## Toasts: reglas de comportamiento

- Para feedback **no crítico**. Nada que la persona *necesite* leer para seguir.
- Duración: proporcional al texto, ~5 s mínimo; **no se va mientras tiene hover o foco**; con acción (Deshacer) más tiempo. WCAG 2.2.1 (*Timing Adjustable*) aplica a contenido con tiempo límite.
- Región `role="status"` (`aria-live="polite"`) para éxito/info; `role="alert"` solo para errores urgentes. La región tiene que existir en el DOM **antes** de insertar el mensaje.
- Una acción como máximo; accesible por teclado (atajo para saltar al toast, como el atajo `Alt+T` de Sonner).
- Posición consistente; no tapes el CTA principal ni la barra de navegación en mobile.
- Apilar como máximo ~3.

## Modales: el `<dialog>` nativo resuelve casi todo

`<dialog>` + `showModal()` (Baseline amplio) da foco atrapado, `inert` en el fondo, `Esc` para cerrar y top layer. Las *invoker commands* (`commandfor` / `command`) son Baseline desde 12/12/2025 (web-features 3.46.0) y permiten abrir y cerrar sin JS. `closedby="any"` (cerrar al tocar afuera) **no** está en Safari todavía: mantené un botón de cierre visible.

```html
<button type="button" commandfor="del-dlg" command="show-modal">Eliminar proyecto</button>

<dialog id="del-dlg" aria-labelledby="del-t" aria-describedby="del-d" closedby="any">
  <form method="dialog">
    <h2 id="del-t">¿Eliminar "Ventas 2026"?</h2>
    <p id="del-d">Se borran 214 facturas. No se puede deshacer.</p>
    <label for="confirm">Escribí <strong>Ventas 2026</strong> para confirmar</label>
    <input id="confirm" autocomplete="off" autofocus>
    <div class="actions">
      <button value="cancel" formnovalidate>Cancelar</button>
      <button value="delete" class="danger">Eliminar proyecto</button>
    </div>
  </form>
</dialog>
<script>
const dlg = document.getElementById('del-dlg');
dlg.addEventListener('close', () => {
  if (dlg.returnValue === 'delete' && dlg.querySelector('#confirm').value === 'Ventas 2026') {/* borrar */}
});
</script>
<style>
dialog::backdrop { background: rgb(0 0 0 / .5); }
dialog { max-inline-size: min(32rem, 100vw - 2rem); border: 0; border-radius: var(--radius, 12px); padding: 1.5rem; }
.actions { display:flex; justify-content:flex-end; gap:.75rem; margin-block-start:1.5rem; }
</style>
```

Reglas de modal:
- **Nunca** un modal al cargar la página (newsletter, cookies gigantes, "¿te vas?") sin que la persona lo pida. Ver [`patrones-oscuros-etica.md`](patrones-oscuros-etica.md).
- No modal sobre modal.
- Al cerrar, el foco vuelve al elemento que lo abrió (el `<dialog>` nativo lo hace).
- Si el contenido es largo o tiene formularios complejos, usá una página o un drawer.
- En mobile, modal = pantalla completa o bottom sheet con handle y botón de cerrar.

## Banners

- Persistentes para estados que siguen vigentes; descartables solo si no son críticos (y recordá que se descartaron).
- Un banner a la vez; prioridad: bloqueos > avisos > promos.
- Cuidado con la ceguera de banners: lo crítico va inline donde se actúa.

## Notificaciones (push / email / in-app)

- **Opt-in explícito y granular** (por tipo y canal), con frecuencia elegible ("resumen diario").
- Cada notificación: qué pasó, por qué me importa, una acción, link directo al lugar exacto.
- **Batching** de eventos repetidos ("5 comentarios nuevos en Ventas 2026").
- Horario silencioso y zona horaria de la persona.
- Darse de baja en 1 clic desde la propia notificación (en EE.UU. CAN-SPAM exige opt-out en emails comerciales; en la UE, el GDPR y la ePrivacy).
- La propuesta de Digital Fairness Act (UE, 11/2026) apunta contra notificaciones y prompts persistentes diseñados para compulsión ([Comisión Europea](https://commission.europa.eu/news-and-media/news/making-your-online-experience-fairer-2026-11-11_en)).

## Tooltips

- Solo texto complementario; **nunca** información o acciones esenciales.
- Aparecen con hover **y** foco, se cierran con `Esc`, se pueden recorrer con el mouse sin desaparecer (WCAG 1.4.13 *Content on Hover or Focus*).
- En touch no hay hover: usá un *toggletip* (botón "ⓘ" que muestra el texto al tocar).
- `popover="hint"` / `interestfor` todavía son solo Chromium (web-features 3.46.0): no los uses como única vía.

## Anti-patrones

- "¿Estás seguro?" para todo.
- Botones "Sí / No" en confirmaciones.
- Toast para errores de formulario.
- Toasts que desaparecen en 2 s con información importante.
- Modales encadenados en la primera visita.
- Notificaciones push pedidas al abrir.
- Tooltips con el único texto de un botón de ícono en mobile.

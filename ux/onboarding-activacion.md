# Onboarding y activación

Onboarding no es un tour. Es **el camino más corto hasta el primer valor real** (el "aha"): la primera factura emitida, el primer proyecto con datos, la primera canción guardada.

Referencias: [Growth.Design case studies](https://growth.design/case-studies) (análisis en formato cómic de onboarding y activación de productos reales); Samuel Hulick, *The Elements of User Onboarding*; NN/g sobre tutoriales ("los usuarios saltean los tutoriales", paradoja del usuario activo).

## Principios

1. **Definí la métrica de activación** (acción que predice retención) antes de diseñar. Ej.: "crea un proyecto e invita a 1 persona en 7 días".
2. **Postergá todo lo que no lleva al aha**: verificación de email, perfil, preferencias, tour de features.
3. **Aprender haciendo**: datos de ejemplo, plantillas, el primer paso ya hecho a medias.
4. **Ayuda en contexto**, no por adelantado: tooltip la primera vez que la persona llega a una función, empty states que enseñan ([`estados.md`](estados.md)).
5. **Progreso visible** (goal-gradient) con un checklist corto y real (3–5 ítems), descartable.
6. **Personalización solo si cambia algo**: si preguntás "¿para qué lo vas a usar?", la respuesta tiene que cambiar lo que se ve.
7. **No bloquees**: todo modal de bienvenida se cierra con Esc y "Ahora no".

## Flujo recomendado (SaaS)

```
Landing (propuesta + prueba) → Registro (email/passkey o SSO; 1 pantalla)
  → [opcional] 1 pregunta que personaliza → Producto con plantilla o datos de ejemplo
  → Primer valor guiado (1 acción) → Checklist corto descartable
  → Pedido de permisos / invitaciones / verificación cuando hacen falta
```

## Patrones y cuándo usarlos

| Patrón | Bien para | Mal cuando |
|---|---|---|
| Plantillas / datos de ejemplo | Editores, dashboards, CRMs | Los datos de ejemplo se confunden con reales (marcalos y borrables en 1 clic) |
| Checklist de activación | SaaS con varias piezas | Más de ~5 ítems o ítems que no aportan valor ("completá tu perfil") |
| Tooltip contextual (1 vez) | Funciones no obvias | Encadenar 8 tooltips al entrar |
| Product tour secuencial | Casi nunca | Se saltea; no se recuerda |
| Video corto | Conceptos nuevos (≤ 60 s, subtítulos) | Reemplaza a una UI clara |
| Empty state educativo | Siempre | — |
| Pedido de permisos en contexto | Notificaciones, cámara, ubicación | Pedir al abrir la app sin explicar (se responde "no" y en iOS no se vuelve a preguntar fácil) |

## Permisos: pre-prompt honesto

```html
<!-- Se muestra cuando la persona activa algo que lo necesita, no al cargar -->
<div role="dialog" aria-labelledby="pp-t" aria-describedby="pp-d">
  <h2 id="pp-t">¿Te avisamos cuando llegue tu pedido?</h2>
  <p id="pp-d">Solo para cambios de estado del envío. Podés apagarlo en Ajustes.</p>
  <button type="button" id="allow">Sí, avisame</button>
  <button type="button" id="later">Ahora no</button>
</div>
<script>
document.getElementById('allow').onclick = async () => {
  const p = await Notification.requestPermission(); // el prompt del sistema solo si dijo que sí
  // guardar p y cerrar; si 'denied', explicar cómo activarlo desde el navegador
};
</script>
```

## Snippet: checklist de activación (React + Tailwind)

```tsx
type Step = { id: string; label: string; done: boolean; href: string };
export function ActivationChecklist({ steps, onDismiss }: { steps: Step[]; onDismiss: () => void }) {
  const done = steps.filter((s) => s.done).length;
  if (done === steps.length) return null;
  return (
    <aside aria-labelledby="act-t" className="rounded-[var(--radius)] border p-4 grid gap-3">
      <div className="flex items-center justify-between">
        <h2 id="act-t" className="font-semibold">Primeros pasos</h2>
        <button type="button" onClick={onDismiss} className="text-sm underline">Ocultar</button>
      </div>
      <progress value={done} max={steps.length} aria-label={`${done} de ${steps.length} completos`} className="w-full" />
      <ol className="grid gap-1">
        {steps.map((s) => (
          <li key={s.id}>
            <a href={s.href} className="flex items-center gap-2 min-h-11">
              <span aria-hidden="true">{s.done ? "✓" : "○"}</span>
              <span className={s.done ? "line-through text-[var(--muted)]" : ""}>{s.label}</span>
              <span className="sr-only">{s.done ? "(hecho)" : "(pendiente)"}</span>
            </a>
          </li>
        ))}
      </ol>
    </aside>
  );
}
```

## Medir

- **Tasa de activación**, **tiempo hasta el primer valor**, retención D1/D7/D30 por cohorte de registro.
- Embudo paso a paso del onboarding (dónde se cae la gente).
- Tests de primera vez con 5 personas nuevas por iteración (cognitive walkthrough antes, ver [`heuristicas.md`](heuristicas.md)).

## Anti-patrones

- Registro obligatorio antes de ver cualquier cosa (si se puede probar sin cuenta, dejá).
- Tour de 8 pasos al primer login.
- "Completá tu perfil al 100 %" como meta de activación.
- Pedir notificaciones, ubicación y cámara en la primera pantalla.
- Encuesta de 6 preguntas que no cambia nada.
- Verificación de email que bloquea el uso (verificá después, o con magic link que ya inicia sesión).
- "Welcome to your Dashboard ✨" vacío ([`../anti-patrones/catalogo.md`](../anti-patrones/catalogo.md) #15).

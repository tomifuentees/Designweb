# UX de productos con IA (2025–2026)

La IA cambia el contrato con la persona: las salidas son **probabilísticas**, pueden ser erróneas con total seguridad, y los agentes **actúan** en nombre de alguien. El trabajo de UX es calibrar la confianza, mantener el control y hacer barato verificar y corregir.

## Contexto 2026

- NN/g, *State of UX 2026* (16/01/2026): 2026 es "el año de la fatiga de IA"; los equipos que ganan usan IA de forma selectiva, con transparencia, control, consistencia y soporte cuando falla ([NN/g](https://www.nngroup.com/articles/state-of-ux-2026/)).
- NN/g define agente como un sistema que persigue una meta tomando acciones, evaluando el progreso y decidiendo los próximos pasos ([03/04/2026](https://www.nngroup.com/articles/definition-ai-agent/)), y el *harness* como el loop que maneja contexto, permisos y límites del agente ([06/11/2026](https://www.nngroup.com/articles/agent-harness/)).
- Los agentes ya son usuarios de tus interfaces ([NN/g, 10/04/2026](https://www.nngroup.com/articles/ai-agents-as-users/)): semántica y accesibilidad = legibilidad para agentes.
- Baymard 2026: IA bienvenida para investigar productos, humanos preferidos para resolver problemas ([27/10/2026](https://baymard.com/research-articles/ai-engagement-quantitative-ux-insights-2026)).
- r/UXDesign en 2026 discute mucho el *design drift* de interfaces generadas con vibe coding: patrones inventados, sistemas de diseño ignorados, accesibilidad rota ([hilo](https://www.reddit.com/r/UXDesign/comments/1s7e3d1/the_design_drift_created_by_vibe_coding_is_insane/)). Es una discusión de comunidad, no un estudio.

## Marcos de referencia

| Marco | Qué aporta | Link |
|---|---|---|
| **Microsoft HAX Guidelines** (Amershi et al., CHI 2019) | 18 guías en 4 momentos: al inicio, durante la interacción, cuando falla, con el tiempo | [HAX Toolkit](https://www.microsoft.com/en-us/haxtoolkit/ai-guidelines/) |
| **Google PAIR Guidebook** | Modelos mentales, explicabilidad y confianza, feedback y control, errores | [pair.withgoogle.com/guidebook](https://pair.withgoogle.com/guidebook/) |
| **Shape of AI** (Emily Campbell) | Biblioteca de patrones: wayfinders, prompt actions, tuners, governors, trust builders, identifiers; en 2026 sumó las "capas de AiUX" (interfaz, contexto, harness, modelo, gobernanza) | [shapeof.ai](https://www.shapeof.ai/); [Substack](https://shapeofai.substack.com/p/designing-beneath-the-surface-the) |
| **Smashing, Design Patterns for AI Interfaces** (Vitaly Friedman, 07/2025) | Controles orientados a tareas (presets, sliders, plantillas) en vez de solo chat | [Smashing](https://www.smashingmagazine.com/2025/07/design-patterns-ai-interfaces/) |
| **NN/g AI** | Alucinaciones (02/2025), los chatbots desalientan verificar (05/2025), explicaciones que no explican (12/2025), lecciones de agentes (05/2026) | Ver [`fuentes-investigacion.md`](fuentes-investigacion.md) |

### HAX, resumido en reglas de UI

| Momento | Guías | En la UI |
|---|---|---|
| Inicio | Dejar claro qué puede hacer y qué tan bien | Ejemplos de tareas reales, límites explícitos ("No tiene acceso a tu email") |
| Durante | Contexto, oportunidad, normas sociales, sin sesgos | Sugerencias en el momento justo, no interrupciones |
| Cuando falla | Invocar, descartar y corregir fácil; aclarar ante ambigüedad; explicar por qué | Botones editar/regenerar/descartar; preguntas de aclaración; fuentes |
| Con el tiempo | Recordar interacciones, aprender con cuidado, actualizar con prudencia, pedir feedback, notificar cambios, controles globales | Memoria visible y borrable, 👍/👎 con motivo, changelog del modelo, ajustes |

## ¿Chat o IA embebida?

| | Chat | IA embebida (en el flujo) |
|---|---|---|
| Bien para | Preguntas abiertas, exploración, tareas sin UI previa | Tareas conocidas: resumir este hilo, completar este campo, sugerir categoría |
| Problema | Página en blanco (¿qué le pregunto?), salidas largas difíciles de verificar, se pierde el contexto | Descubribilidad |
| Regla | Chat como complemento con *starters* concretos | **Por defecto, embebé** la IA donde ya está la tarea; el resultado aparece como sugerencia editable |

NN/g y Smashing coinciden: las interfaces solo-chat cargan a la persona con escribir prompts; los controles explícitos (presets, tonos, largo, filtros) bajan la carga.

## Patrones esenciales

### Antes (entrada)
- **Starters / ejemplos** de tareas reales, no "Preguntame lo que quieras".
- **Contexto visible**: qué archivos, páginas o datos va a usar ("Usando: Ventas_nov.xlsx ✕").
- **Controles explícitos** (tono, largo, formato, alcance) en vez de esperar que la persona los escriba.
- **Aclaración** ante ambigüedad antes de gastar tiempo.

### Durante (generación)
- **Streaming** del texto para que la espera se sienta corta; **botón Detener** siempre visible.
- **Indicador de qué está haciendo** ("Buscando en 3 documentos…", pasos del agente), no un spinner mudo.
- Accesibilidad: **no anuncies cada token** en `aria-live` (inunda el lector). Marcá la región `aria-busy="true"` y anunciá al terminar.

### Después (salida)
- **Fuentes/citas** junto a cada afirmación, que lleven al pasaje exacto. NN/g: las citas tienen que ser prominentes, ligadas a la afirmación y profundas ([02/2025](https://www.nngroup.com/articles/ai-hallucinations/)).
- **Incertidumbre honesta**: "No encontré esto en tus documentos" mejor que inventar. Evitá porcentajes de confianza falsos.
- **Editar, regenerar, copiar, deshacer**; versiones comparables.
- **Feedback** 👍/👎 con motivo opcional, sin bloquear.
- **Invitar a verificar**: NN/g encontró que las interfaces de chat fomentan aceptar la salida tal cual ([05/2025](https://www.nngroup.com/articles/ai-chatbots-discourage-error-checking/)). Ofrecé "Ver fuentes", "¿Qué tan seguro estás?", resaltado de lo no verificado.
- **Explicaciones útiles**: NN/g (12/2025) vio que los textos de "explicación" actuales muchas veces no ayudan a entender la salida. Mostrá datos usados y pasos, no párrafos genéricos.
- **Identificación**: contenido generado marcado como tal (y en imágenes de producto, mejor fotos reales: Baymard 2026).

### Agentes (actúan por la persona)
1. **Plan antes de actuar**: mostrar los pasos y pedir OK para tareas largas.
2. **Permisos con alcance mínimo** y visibles ("Puede leer tu calendario; no puede enviar emails").
3. **Puntos de control** antes de lo irreversible o externo: pagar, enviar, borrar, publicar. Card de aprobación con el detalle exacto.
4. **Progreso y bitácora** de lo hecho, interrumpible en cualquier momento.
5. **Deshacer / rollback** cuando se pueda; si no, decirlo antes.
6. **Traspaso a humano** claro (y en soporte, temprano: Baymard).
7. **Autonomía de la persona**: NN/g (05/2026, estudio de Qwen) resalta descubribilidad, reusar patrones familiares, cuidar datos personales y proteger la autonomía ([NN/g](https://www.nngroup.com/articles/designing-ai-agents/)).

## Snippets

### Respuesta en streaming con Detener, fuentes y acciones (React + Tailwind)

```tsx
import { useRef, useState } from "react";
type Source = { id: string; title: string; url: string; quote: string };

export function AiAnswer({ ask }: { ask: (q: string, signal: AbortSignal, onToken: (t: string) => void) => Promise<Source[]> }) {
  const [text, setText] = useState(""); const [sources, setSources] = useState<Source[]>([]);
  const [status, setStatus] = useState<"idle" | "streaming" | "done" | "stopped" | "error">("idle");
  const ctrl = useRef<AbortController | null>(null);

  async function run(q: string) {
    ctrl.current = new AbortController(); setText(""); setSources([]); setStatus("streaming");
    try { setSources(await ask(q, ctrl.current.signal, (t) => setText((s) => s + t))); setStatus("done"); }
    catch (e: any) { setStatus(e?.name === "AbortError" ? "stopped" : "error"); }
  }
  return (
    <section aria-labelledby="ai-h" className="grid gap-3">
      <h2 id="ai-h" className="sr-only">Respuesta del asistente</h2>
      <div aria-busy={status === "streaming"} className="whitespace-pre-wrap">{text}</div>
      {/* Solo se anuncian los cambios de estado, no cada token */}
      <p role="status" className="sr-only">
        {status === "done" ? "Respuesta lista" : status === "stopped" ? "Generación detenida" : status === "error" ? "Hubo un error" : ""}
      </p>
      {status === "streaming" && <button type="button" onClick={() => ctrl.current?.abort()} className="justify-self-start border rounded px-3 min-h-11">Detener</button>}
      {status === "error" && <p>No pude responder. <button type="button" className="underline" onClick={() => run("")}>Reintentar</button></p>}
      {sources.length > 0 && (
        <details open className="border-t pt-2">
          <summary className="font-medium">Fuentes ({sources.length})</summary>
          <ol className="grid gap-2 mt-2">{sources.map((s, i) => (
            <li key={s.id}><a href={s.url} className="underline">[{i + 1}] {s.title}</a>
              <blockquote className="text-sm text-[var(--muted)]">"{s.quote}"</blockquote></li>))}
          </ol>
        </details>
      )}
      {status === "done" && (
        <div className="flex gap-2 text-sm">
          <button type="button" className="border rounded px-2 min-h-11">Copiar</button>
          <button type="button" className="border rounded px-2 min-h-11">Regenerar</button>
          <button type="button" aria-label="Útil" className="border rounded px-2 min-h-11">👍</button>
          <button type="button" aria-label="No útil" className="border rounded px-2 min-h-11">👎</button>
        </div>
      )}
      <p className="text-xs text-[var(--muted)]">Generado con IA. Puede tener errores: revisá las fuentes.</p>
    </section>
  );
}
```

### Card de aprobación de un agente (antes de una acción externa)

```html
<section class="approval" aria-labelledby="ap-t">
  <h3 id="ap-t">El asistente quiere enviar un email</h3>
  <dl>
    <dt>Para</dt><dd>ana@cliente.com</dd>
    <dt>Asunto</dt><dd>Factura N.º 0042 de noviembre</dd>
    <dt>Adjunto</dt><dd>factura-0042.pdf (182 KB)</dd>
  </dl>
  <details><summary>Ver el texto completo</summary><p>Hola Ana, te adjunto…</p></details>
  <p class="note">No se puede deshacer una vez enviado.</p>
  <div class="actions">
    <button type="button">Editar</button>
    <button type="button">No enviar</button>
    <button type="button" class="primary">Enviar email</button>
  </div>
</section>
```

## Checklist de UX de IA (ids `AI-*`)

- [ ] `AI-01` Dice qué puede y qué no puede hacer, con ejemplos reales.
- [ ] `AI-02` Contexto y datos usados visibles y editables.
- [ ] `AI-03` IA embebida en la tarea cuando la tarea es conocida; chat solo como complemento.
- [ ] `AI-04` Streaming con Detener; estado de lo que hace.
- [ ] `AI-05` Fuentes ligadas a afirmaciones; "no sé" honesto.
- [ ] `AI-06` Editar, regenerar, deshacer; feedback con motivo.
- [ ] `AI-07` Contenido generado identificado.
- [ ] `AI-08` Agentes: plan visible, permisos mínimos, aprobación antes de lo irreversible, bitácora, interrupción.
- [ ] `AI-09` Traspaso a humano visible en soporte y problemas.
- [ ] `AI-10` Memoria visible y borrable; controles globales.
- [ ] `AI-11` Accesible: sin anunciar tokens, foco correcto, todo operable por teclado.
- [ ] `AI-12` Falla con dignidad: errores de modelo, timeout y rate limit con salida clara.

## Anti-patrones de IA

- Chat vacío con "¿En qué te ayudo hoy? ✨".
- Respuestas largas sin fuentes ni estructura.
- Barras de "confianza 97 %" sin calibración real.
- Agente que ejecuta acciones externas sin confirmación.
- Bot de soporte sin salida a humano.
- "AI" en cada botón, sin que la tarea lo necesite (fatiga, NN/g 2026).
- Imágenes de producto generadas presentadas como reales.

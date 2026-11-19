# Heurísticas de usabilidad (Nielsen) y evaluación heurística

Las 10 heurísticas de Jakob Nielsen (1994; texto actualizado por NN/g el 30/01/2024) siguen siendo la forma más barata de encontrar problemas antes de testear con personas. Fuente: [NN/g, 10 Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/).

Cada heurística tiene un id `H1`…`H10` que usan [`checklist-ux.md`](checklist-ux.md) y [`ux.json`](ux.json).

## Las 10, con ejemplos web y lo que hace mal la IA

### H1 · Visibilidad del estado del sistema
El sistema informa qué está pasando, con feedback apropiado y a tiempo.
- ✅ Botón "Guardando…" → "Guardado hace 3 s"; paso 2 de 4; ítem activo en la navegación (`aria-current="page"`).
- ❌ Click sin respuesta durante 2 s; uploads sin progreso; filtros que se aplican sin decir cuántos resultados quedan.
- IA: genera el happy path sin estados de carga ni de éxito.

### H2 · Coincidencia entre el sistema y el mundo real
Palabras, conceptos y orden que la persona conoce.
- ✅ "Envío" y no "Fulfillment"; fechas en formato local (`Intl.DateTimeFormat('es-AR')`); moneda con símbolo correcto.
- ❌ Códigos de error internos ("ERR_422"), jerga del equipo, íconos metafóricos raros.

### H3 · Control y libertad
Salidas de emergencia claras: deshacer, cancelar, volver.
- ✅ Undo en toast tras borrar; botón "Atrás" del navegador que funciona en SPA; `Esc` cierra modales.
- ❌ Wizards sin "Anterior"; modales sin cerrar; borrar sin recuperación.

### H4 · Consistencia y estándares
Interna (mismo término, mismo componente) y externa (convenciones de plataforma, ley de Jakob).
- ✅ Un solo nombre para cada cosa; el primario siempre en la misma posición.
- ❌ "Eliminar" en una pantalla y "Borrar" en otra; links que a veces abren pestaña nueva y a veces no.

### H5 · Prevención de errores
Mejor que un buen mensaje de error es que el error no ocurra.
- ✅ Constraints (`type="email"`, `min`/`max`), defaults seguros, confirmación solo para lo irreversible, detectar typos de email ("¿Quisiste decir gmail.com?").
- ❌ Campo de fecha libre sin formato; botón destructivo al lado del primario con el mismo estilo.

### H6 · Reconocer antes que recordar
- ✅ Búsquedas recientes, valores previos, opciones visibles, comparar lado a lado.
- ❌ Pedir un código mostrado en la pantalla anterior; menús de íconos sin label.

### H7 · Flexibilidad y eficiencia
Atajos para expertos sin estorbar a novatos.
- ✅ `⌘K`, atajos de teclado documentados, acciones masivas, plantillas, personalización.
- ❌ Obligar a 6 clics para una acción diaria.

### H8 · Diseño estético y minimalista
Cada elemento extra compite con lo relevante. **No es "minimalismo visual"**, es señal sobre ruido.
- ✅ Una acción primaria por vista; información secundaria colapsada.
- ❌ Banners promocionales sobre formularios; tres CTA con el mismo peso.

### H9 · Ayudar a reconocer, diagnosticar y recuperarse de errores
Lenguaje llano, problema preciso, solución constructiva.
- ✅ "La tarjeta venció en 08/26. Probá con otra o actualizá la fecha."
- ❌ "Algo salió mal." / "Invalid input." / solo borde rojo.
- Ver [`ux-writing-microcopy.md`](ux-writing-microcopy.md) y [`formularios-inputs.md`](formularios-inputs.md).

### H10 · Ayuda y documentación
Idealmente no hace falta; si hace falta, que esté en contexto y sea buscable.
- ✅ Tooltip de "¿Qué es el CVV?", centro de ayuda con buscador, ayuda en el mismo lugar en todas las páginas (WCAG 3.2.6 *Consistent Help*).
- ❌ PDF de 40 páginas; chatbot como única vía de soporte (Baymard 2026: ~2/3 prefieren un humano para resolver problemas de pedido, [27/10/2026](https://baymard.com/research-articles/ai-engagement-quantitative-ux-insights-2026)).

## Heurísticas complementarias que conviene sumar

| id | Fuente | Para qué |
|---|---|---|
| `X-A11Y` | WCAG 2.2 ([`accesibilidad.md`](accesibilidad.md)) | Las 10 de Nielsen no cubren accesibilidad |
| `X-PERF` | Core Web Vitals | Lento = inusable |
| `X-TRUST` | Baymard / Stanford Web Credibility | Señales de confianza en checkout y datos |
| `X-AI` | Microsoft HAX 18 guidelines, Shape of AI | Productos con IA ([`ux-ia.md`](ux-ia.md)) |
| `X-ETHICS` | Patrones oscuros | [`patrones-oscuros-etica.md`](patrones-oscuros-etica.md) |

## Procedimiento de evaluación heurística

Basado en [NN/g, How to Conduct a Heuristic Evaluation](https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/).

1. **Alcance**: 1–3 flujos críticos (ej.: registro, checkout, crear proyecto). No "todo el sitio".
2. **Evaluadores**: 3–5, cada uno solo. Un evaluador encuentra una fracción de los problemas; varios en paralelo encuentran muchos más (Nielsen 1992). Si sos un agente, hacé **pasadas separadas por heurística** en lugar de una sola pasada general.
3. **Dos pasadas por flujo**: una para entender, otra para anotar.
4. **Anotar cada hallazgo** con: pantalla, heurística violada, descripción, evidencia (captura/selector), severidad, recomendación.
5. **Consolidar** (deduplicar), priorizar por severidad × frecuencia.
6. **Validar con usuarios** los hallazgos dudosos: la evaluación heurística genera hipótesis, no verdades.

### Escala de severidad (Nielsen)

| Nivel | Nombre | Criterio | Acción |
|---|---|---|---|
| 0 | No es problema | Desacuerdo de gusto | Nada |
| 1 | Cosmético | No afecta la tarea | Si sobra tiempo |
| 2 | Menor | Fricción, se resuelve solo | Baja prioridad |
| 3 | Mayor | Mucha fricción o error frecuente | Antes del próximo release |
| 4 | Catástrofe | Impide completar la tarea / pérdida de datos / plata | Bloquea el release |

Severidad = frecuencia × impacto × persistencia (¿se repite cada vez?).

### Plantilla de hallazgo (markdown)

```md
### [S3] El error de tarjeta vacía el formulario completo
- Flujo / pantalla: Checkout → Pago
- Heurística: H9, H5 · WCAG 3.3.1
- Evidencia: al rechazar la tarjeta se recarga la página y se pierden dirección y email.
- Impacto: alto (abandono); frecuencia: cada rechazo.
- Recomendación: validar sin recargar, conservar valores, mensaje junto al campo con causa y salida.
```

### Plantilla de hallazgo (JSON, para agentes)

```json
{ "id": "HE-007", "severidad": 3, "heuristicas": ["H9", "H5"], "wcag": ["3.3.1"],
  "pantalla": "checkout/pago", "evidencia": "selector #card-number; captura 07.png",
  "problema": "El rechazo de tarjeta vacía el formulario",
  "recomendacion": "Conservar valores y mostrar error en línea" }
```

## Cognitive walkthrough (complemento)

Para cada paso de una tarea, preguntá (Wharton et al., 1994):
1. ¿La persona va a intentar lograr el efecto correcto?
2. ¿Va a notar que la acción correcta está disponible?
3. ¿Va a asociar la acción correcta con el efecto que busca?
4. Después de actuar, ¿va a ver que progresó?

Ideal para onboarding y primeras veces ([`onboarding-activacion.md`](onboarding-activacion.md)).

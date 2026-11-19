# Métricas de UX

Medí la experiencia con métricas que reflejen tareas y percepciones, no solo tráfico. Combiná **conducta** (lo que hace) con **actitud** (lo que siente).

## Métricas de tarea (las más directas)

| Métrica | Cómo | Nota |
|---|---|---|
| **Éxito de tarea** | % que completa la tarea (binaria o con parcial) | La métrica de usabilidad fundamental |
| **Tiempo en tarea** | Mediana o media geométrica (los tiempos son asimétricos) | Solo en tareas exitosas, o reportar ambos |
| **Errores** | Cantidad / tasa por tarea | Definí qué cuenta como error antes |
| **SEQ** (Single Ease Question) | "En general, ¿qué tan fácil o difícil fue esta tarea?" 1–7, después de cada tarea | Sauro; corta y sensible |
| **Lostness / directness** | Pasos extra vs. camino óptimo (tree testing: directness) | |

## Cuestionarios estandarizados

### SUS (System Usability Scale)
- 10 ítems, escala 1–5, alterna positivos y negativos (Brooke, 1986/1996).
- Cálculo: ítems impares `respuesta − 1`, pares `5 − respuesta`, suma × 2,5 → 0–100.
- **Promedio de referencia ≈ 68** (Sauro, a partir de cientos de estudios; [MeasuringU](https://measuringu.com/sus/)). No es un porcentaje.
- Útil para comparar versiones o contra benchmark; no dice *qué* arreglar.

```ts
export function sus(r: number[]): number { // r = 10 respuestas 1..5 en orden
  if (r.length !== 10) throw new Error("SUS requiere 10 respuestas");
  return r.reduce((acc, v, i) => acc + (i % 2 === 0 ? v - 1 : 5 - v), 0) * 2.5;
}
```

### UMUX-Lite
- 2 ítems (escala 1–7): "Las capacidades de [producto] cumplen con mis necesidades" y "[Producto] es fácil de usar" (Lewis, Utesch y Maher, CHI 2013).
- Corto para encuestas en producto; existe una fórmula de regresión para aproximarlo a la escala SUS.

```ts
export const umuxLite = (cap: number, ease: number) => ((cap - 1) + (ease - 1)) / 12 * 100; // 0..100 crudo
```

### Otras
- **CES** (Customer Effort Score): "¿Qué tan fácil fue resolver tu problema?". Útil en soporte.
- **CSAT**: satisfacción con una interacción concreta.
- **UEQ / AttrakDiff**: dimensiones pragmáticas y hedónicas.

## NPS: usalo con cuidado

"¿Qué tan probable es que recomiendes X?" 0–10; promotores (9–10) − detractores (0–6).
- NN/g: correlaciona razonablemente con la percepción de usabilidad y es fácil de administrar, pero **solo** no sirve para entender ni evaluar UX ([21/06/2024](https://www.nngroup.com/articles/nps-ux/)).
- Críticas comunes: una sola pregunta hipotética, descarta información al agrupar (un 6 y un 0 cuentan igual), muy sensible al momento y al canal, difícil de mover con cambios de diseño concretos (Jared Spool, *Net Promoter Score Considered Harmful*, 2017).
- Si la empresa lo exige, **sumá siempre** la pregunta abierta "¿Por qué?" y métricas de tarea.

## Marcos para elegir métricas

### HEART + Goals-Signals-Metrics (Google; Rodden, Hutchinson y Fu, CHI 2010)

| Dimensión | Ejemplo de métrica |
|---|---|
| **H**appiness | SUS, CSAT, UMUX-Lite |
| **E**ngagement | Sesiones por usuario activo por semana, acciones clave |
| **A**doption | % de nuevos usuarios que usan la función en 7 días |
| **R**etention | Retención D30 por cohorte |
| **T**ask success | Éxito, tiempo, errores en tareas clave |

Para cada dimensión: **Goal** (qué queremos) → **Signal** (qué conducta lo evidencia) → **Metric** (cómo lo medimos). No hace falta usar las cinco.

### Métricas de producto relacionadas
- **Activación** y **tiempo hasta el primer valor** ([`onboarding-activacion.md`](onboarding-activacion.md)).
- **Conversión por paso** de embudos ([`checkout-ecommerce.md`](checkout-ecommerce.md)).
- **Búsquedas sin resultados**, **tasa de refinamiento** ([`busqueda-filtros.md`](busqueda-filtros.md)).
- **Tickets de soporte por tema** (los temas repetidos son bugs de UX).
- **Core Web Vitals** p75 ([`rendimiento-percibido.md`](rendimiento-percibido.md)).
- **Defectos de accesibilidad** abiertos por severidad.

## Reglas para reportar

- Reportá **intervalos de confianza** cuando la muestra es chica (con 8 personas, un 75 % de éxito tiene un intervalo muy ancho).
- Compará contra una **línea de base** (versión anterior o competidor), no en el vacío.
- Separá por **segmento** (nuevo vs. recurrente, mobile vs. desktop).
- Una métrica que se convierte en objetivo deja de ser buena métrica (ley de Goodhart): acompañala de *guardrails*.

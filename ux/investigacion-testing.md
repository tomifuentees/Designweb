# Investigación y testing de UX

Diseñar sin investigar es adivinar con confianza. Este archivo es una guía práctica para elegir el método, correrlo bien y no sacar conclusiones de más.

Base: [NN/g, When to Use Which UX Research Methods](https://www.nngroup.com/articles/which-ux-research-methods/) (20 métodos según actitud/conducta y cuali/cuanti); [Usability Testing 101](https://www.nngroup.com/articles/usability-testing-101/); Steve Krug, *Rocket Surgery Made Easy* (2010); Erika Hall, *Just Enough Research* (2.ª ed., 2019).

## Elegir método por pregunta

| Pregunta | Método | Tipo |
|---|---|---|
| ¿Qué necesita la gente y por qué? | Entrevistas, estudios de campo, diary studies | Actitudinal, cuali |
| ¿Cómo agrupa y nombra la información? | Card sorting | Actitudinal |
| ¿Encuentra las cosas en esta jerarquía? | Tree testing, first-click | Conductual |
| ¿Puede completar la tarea con este diseño? | **Test de usabilidad moderado** | Conductual, cuali |
| ¿Cuántos tienen el problema? / ¿cuánto tarda? | Test no moderado cuantitativo, analítica | Conductual, cuanti |
| ¿Qué versión rinde más? | A/B test | Conductual, cuanti |
| ¿Qué opina / cómo se siente? | Encuestas (SUS, UMUX-Lite, SEQ) | Actitudinal, cuanti |
| ¿Dónde abandona? | Embudos, grabaciones de sesión, mapas de calor | Conductual |
| ¿Hay problemas obvios antes de testear? | Evaluación heurística, cognitive walkthrough ([`heuristicas.md`](heuristicas.md)) | Experto |
| ¿Es accesible? | Auditoría WCAG + tests con personas con discapacidad ([`accesibilidad.md`](accesibilidad.md)) | Mixto |

**Lo que la gente dice ≠ lo que hace.** Para decisiones de diseño, priorizá métodos conductuales.

## Test de usabilidad (el método más rentable)

### Cuántas personas: los "5 usuarios" con letra chica
Nielsen (2000) sostiene que 5 personas encuentran la mayoría de los problemas de un diseño, basado en un modelo de Nielsen y Landauer (1993) ([NN/g](https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/)). Lo que suele omitirse:
- Vale para **test cualitativo e iterativo**, con **un perfil de usuario** y tareas acotadas. Con 3 perfiles distintos, 3–5 por perfil.
- El supuesto es que el problema afecta a una proporción alta de usuarios; los problemas raros necesitan más gente. Faulkner (2003) mostró que con 5 personas el porcentaje encontrado varía mucho según qué 5 salgan.
- **No** sirve para métricas cuantitativas (tasas, tiempos con intervalos de confianza): ahí necesitás ~20–40+ por grupo según la precisión buscada (Sauro y Lewis, *Quantifying the User Experience*, 2.ª ed. 2016).
- La recomendación real es: **muchos tests chicos**, arreglar, volver a testear.

### Cómo correrlo
1. **Objetivo** y 3–5 tareas realistas con escenario ("Querés devolver las zapatillas que compraste la semana pasada"). Sin palabras de la UI en la consigna.
2. **Reclutá** gente del perfil real (no compañeros). Screener corto.
3. **Piloto** con 1 persona.
4. **Pensar en voz alta**; el moderador no ayuda ni explica ("¿Qué harías si yo no estuviera?").
5. Medí por tarea: éxito (sí / parcial / no), tiempo, errores, SEQ (1–7) al final de cada tarea.
6. **Debrief** y SUS/UMUX-Lite al final.
7. **Síntesis** el mismo día: problemas con frecuencia y severidad, citas, clips. Affinity diagram si hay muchos datos.
8. **Compartí** en formato accionable: top 5 problemas, evidencia, recomendación.

### Guion mínimo

```md
Intro (2 min): estamos probando el sitio, no a vos. No hay respuestas incorrectas. Pensá en voz alta.
Contexto (3 min): ¿Cómo hacés hoy [tarea]? ¿Qué herramienta usás?
Tareas (25 min): 1) … 2) … 3) …  → después de cada una: "¿Qué tan fácil fue, de 1 a 7?"
Cierre (5 min): ¿Qué fue lo más confuso? ¿Qué esperabas que pasara en [momento]? → SUS
```

## Encuestas

- Preguntas neutras, una idea por pregunta, escalas balanceadas, "No sé / No aplica".
- Cortas (≤ 5 min). Cada pregunta tiene que cambiar una decisión.
- Intercepciones en contexto (post-tarea) > encuestas genéricas por email.
- Abiertas para el "por qué"; cerradas para el "cuántos".
- Métricas estándar en [`metricas.md`](metricas.md).

## Analítica y experimentos

- **Instrumentá eventos** que reflejen tareas (no solo pageviews): `checkout_started`, `payment_failed{reason}`, `search_no_results{query}`.
- **Embudos** por paso y por dispositivo; **búsquedas sin resultados** como backlog de contenido.
- **Grabaciones y heatmaps** (con consentimiento y enmascarado de datos sensibles) para entender el "por qué" de un embudo.

### A/B tests sin autoengaño
1. Hipótesis escrita con métrica primaria y *guardrails* (ej.: conversión ↑ sin que suban las devoluciones).
2. **Tamaño de muestra calculado antes** (efecto mínimo detectable, potencia 80 %, α 5 %).
3. **No mires y cortes antes** ("peeking"): infla falsos positivos (salvo métodos secuenciales).
4. Chequeá *sample ratio mismatch* (si 50/50 llega 52/48, algo está roto).
5. Corré semanas completas (estacionalidad semanal).
6. Un test que "gana" por una métrica de corto plazo con un patrón oscuro, pierde (ver [`patrones-oscuros-etica.md`](patrones-oscuros-etica.md)).
7. Para tráfico bajo, A/B no sirve: usá tests de usabilidad.

## IA en la investigación (2025–2026)

- **Usuarios sintéticos** (personas generadas por IA): NN/g concluye que pueden servir para preparar o explorar hipótesis, pero la investigación necesita personas reales ([21/06/2024](https://www.nngroup.com/articles/synthetic-users/)); su revisión de tres estudios (15/08/2025) encontró que las simulaciones rinden mejor con mucho contexto y para tendencias poblacionales, no para individuos ([NN/g](https://www.nngroup.com/articles/ai-simulations-studies/)).
- IA útil para: transcribir, primer borrador de síntesis (verificado contra los datos), generar variantes de tareas, analizar respuestas abiertas a escala.
- **Research-in-the-loop**: con desarrollo a velocidad de IA, NN/g propone que la investigación defina qué debe medir cada release y qué puede ayudar a descubrir ([13/11/2026](https://www.nngroup.com/articles/research-in-the-loop/)).
- NN/g (30/10/2026): en ciclos de desarrollo agénticos, la UX corre el riesgo de quedar reducida a "contexto para la IA"; su rol es descubrir necesidades, dar forma a lo que se construye y evaluarlo antes y después del lanzamiento ([NN/g](https://www.nngroup.com/articles/ux-agentic-software-factories/)).

## Ética de la investigación

Consentimiento informado, grabación con permiso, compensación justa, datos personales minimizados y protegidos, derecho a retirarse, cuidado especial con menores y personas en situación vulnerable.

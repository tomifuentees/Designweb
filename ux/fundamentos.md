# Fundamentos de UX

La UI es lo que se ve. La UX es si la persona logra lo que vino a hacer, cuánto le cuesta y cómo se siente después. Una UI linda con un flujo roto es mala UX. Una UI sobria con un flujo claro casi siempre gana.

> Regla para agentes: antes de diseñar una pantalla, escribí **quién**, **qué tarea**, **en qué contexto** (dispositivo, apuro, conocimiento previo) y **qué pasa si falla**. Si no lo sabés, preguntalo o dejalo como supuesto explícito.

## UX vs UI vs "experience design"

| Término | Qué abarca | Pregunta que responde |
|---|---|---|
| UI | Pantallas, componentes, tipografía, color | ¿Se ve y se lee bien? |
| UX | Flujo, tareas, errores, contenido, rendimiento, soporte | ¿Puede lograrlo sin fricción innecesaria? |
| Usabilidad | Eficacia, eficiencia, satisfacción (ISO 9241-11) | ¿Funciona para estas personas en este contexto? |
| Experience design | UX que también contempla agentes de IA que actúan por la persona | ¿Funciona para la persona y para el agente que la representa? |

NN/g propuso en octubre de 2026 hablar de *experience design* porque los agentes también usan las interfaces, sin dejar de centrar las metas de las personas ([NN/g, 30/10/2026](https://www.nngroup.com/articles/ux-vs-experience-design/); [AI Agents as Users, 10/04/2026](https://www.nngroup.com/articles/ai-agents-as-users/)). Consecuencia práctica: HTML semántico y labels claros ahora sirven a lectores de pantalla **y** a agentes. Ver [`ux-ia.md`](ux-ia.md).

## Don Norman: los 6 conceptos que siguen vigentes

De *The Design of Everyday Things* (ed. revisada 2013):

1. **Affordance**: lo que el objeto permite hacer. En pantalla casi no existe "física": dependés de signifiers.
2. **Signifier**: la señal de que algo se puede hacer (un botón que parece botón, un link subrayado, un cursor).
3. **Mapping**: la relación entre control y efecto (el slider a la derecha sube el valor).
4. **Feedback**: respuesta inmediata e informativa a cada acción.
5. **Constraints**: limitar lo que se puede hacer mal (deshabilitar fechas imposibles, `inputmode="numeric"`).
6. **Modelo conceptual**: la explicación que la persona se arma de cómo funciona el sistema.

Los dos golfos: **ejecución** (¿sé cómo hacer lo que quiero?) y **evaluación** (¿entiendo qué pasó?). Casi todo problema de UX cae en uno de los dos.

**Do**: botones con aspecto de botón, links con aspecto de link, estado visible siempre.
**Don't**: texto plano clickeable, íconos sin label como única señal, acciones que solo aparecen al hover (en touch no existe el hover).

## Modelos mentales

La persona trae un modelo de cómo "debería" funcionar algo, armado con los otros productos que usa. Cuando tu sistema contradice ese modelo, lo que pasa es un error que la persona cree que es suyo.

- Investigá el modelo mental (entrevistas, card sorting, ver [`investigacion-testing.md`](investigacion-testing.md)) antes de inventar uno nuevo.
- Si tenés que cambiarlo (algo genuinamente nuevo), enseñalo en contexto, no con un tour.
- La IA generativa rompe modelos mentales: las personas esperan determinismo de una computadora. NN/g documentó que los chatbots desalientan la verificación ([16/05/2025](https://www.nngroup.com/articles/ai-chatbots-discourage-error-checking/)).

## Carga cognitiva

Tres tipos (Sweller): **intrínseca** (la dificultad propia de la tarea), **extrínseca** (la que agrega el diseño: la que hay que eliminar) y **germana** (la que ayuda a aprender).

Cómo bajar la extrínseca:
- Reconocer en vez de recordar (mostrar opciones, historial, valores previos).
- Agrupar (chunking) y ordenar por frecuencia de uso.
- Defaults inteligentes; preguntar solo lo necesario.
- Un foco por pantalla; acciones secundarias menos prominentes.
- Lenguaje de la persona, no del sistema.

## Leyes de UX: aplicación y evidencia

Base: [lawsofux.com](https://lawsofux.com/) (Jon Yablonski, 30 leyes en el índice actual). La columna "evidencia" importa: varias son heurísticas útiles, no leyes científicas.

| Ley | Qué dice | Aplicación concreta | Evidencia / cuidado |
|---|---|---|---|
| **Jakob** | La gente pasa la mayor parte del tiempo en otros sitios y espera que el tuyo funcione igual | Carrito arriba a la derecha, logo lleva al inicio, filtros a la izquierda en desktop | Observacional (NN/g). No es "copiá todo": innová en lo que te diferencia, no en la navegación |
| **Hick** | Más opciones (y más complejas) = más tiempo de decisión | Menús cortos, opción recomendada marcada, divulgación progresiva | Hick-Hyman 1952 mide tiempos de reacción con estímulos simples; no escala lineal a menús reales donde la gente escanea |
| **Fitts** | El tiempo para alcanzar un objetivo depende de distancia y tamaño | CTA grande cerca de donde está el pulgar o el cursor; bordes y esquinas en desktop son "infinitos" | Muy robusta (1954, replicada mil veces). Base de WCAG 2.5.8 (24 px) |
| **Miller** | 7±2 elementos en memoria de trabajo | No obliga a cortar menús en 7. Sí: no pedir recordar códigos entre pantallas | Cowan (2001) estima ~4 chunks. **Mal citada**: la memoria importa cuando hay que *recordar*, no cuando se *ve* la lista |
| **Tesler** | Hay complejidad que no se puede eliminar, solo mover | Que la absorba el sistema (detectar tarjeta, autocompletar dirección), no la persona | Principio de diseño, no empírico |
| **Doherty** | La productividad sube si el sistema responde en <400 ms | Feedback inmediato (<100 ms), optimistic UI, skeletons | Paper de IBM 1982 sobre tiempos de respuesta de mainframe. Hoy: INP ≤200 ms ([`rendimiento-percibido.md`](rendimiento-percibido.md)) |
| **Peak-end** | Se recuerda el pico y el final | Cuidá la confirmación, el error más doloroso y el último paso | Kahneman y otros (1993), experimentos con dolor; extrapolación a productos es razonable, no medida |
| **Postel** | Ser liberal con lo que se acepta | Aceptar teléfonos con espacios o guiones, fechas con distintos separadores, emails con mayúsculas | Principio de ingeniería |
| **Goal-gradient** | La motivación sube al acercarse a la meta | Barra de progreso en onboarding, "te falta 1 paso" | Kivetz et al. 2006 (tarjetas de café). Sin progreso falso |
| **Zeigarnik** | Se recuerdan las tareas incompletas | Checklists de activación, guardar borradores | Replicación mixta; usalo con moderación y sin culpa manipuladora |
| **Serial position** | Se recuerda lo primero y lo último | Acciones clave al principio y al final de navegaciones | Robusto en memoria de listas |
| **Von Restorff** | Lo distinto se recuerda | Un solo acento para la acción primaria | No uses solo color (accesibilidad) |
| **Aesthetic-usability** | Lo lindo se percibe más usable | Terminación visual sí importa; pero tapa problemas en tests (la gente perdona) | Kurosu y Kashimura 1995. Google 2025–2026 (M3 Expressive) reportó mejoras de ubicación de elementos con diseño expresivo ([Google Design](https://design.google/library/expressive-material-design-google-research); [CHI 2026](https://dl.acm.org/doi/10.1145/3772318.3790373)) |
| **Choice overload** | Muchas opciones paralizan | Comparadores, "más vendido", filtros | El estudio de la mermelada (2000) tiene replicaciones débiles; el efecto depende del contexto |
| **Paradox of the active user** | Nadie lee el manual | Ayuda en contexto, no tours largos | Carroll y Rosson 1987 |
| **Parkinson** | La tarea se expande al tiempo disponible | Autocompletar, checkout express | Ley de oficina, no de UX en sentido estricto |
| **Gestalt** (proximidad, región común, similitud, conexión, Prägnanz) | Agrupación perceptual | Ver [`../layout/jerarquia-composicion.md`](../layout/jerarquia-composicion.md) | Robusta |
| **Pareto** | 80/20 | Optimizá los flujos más frecuentes primero (analítica) | Heurística |
| **Occam** | La explicación más simple | Elegí la solución con menos partes móviles | Heurística |
| **Selective attention / banner blindness** | Se ignora lo que parece publicidad | No pongas información crítica en banners de colores | NN/g, eye tracking |
| **Working memory / Cognitive load** | Ver arriba | | |
| **Flow** | Inmersión total | Sin interrupciones en tareas largas (editor, checkout) | Csikszentmihalyi |

`ux.json` → `leyes` tiene cada una con `id`, `aplicacion` y `evidencia`.

## Tiempos de respuesta (Miller 1968, Nielsen 1993)

| Tiempo | Percepción | Qué mostrar |
|---|---|---|
| ≤ 0,1 s | Instantáneo | Nada extra |
| ≤ 1 s | El flujo de pensamiento no se corta | Cambio de estado (pressed, pending) |
| 1–10 s | Se nota la espera | Spinner o skeleton; indicar qué se hace |
| > 10 s | Se pierde la atención | Barra de progreso con estimación, permitir seguir con otra cosa, notificar al terminar |

Fuente: [NN/g, Response Times: The 3 Important Limits](https://www.nngroup.com/articles/response-times-3-important-limits/) (actualizado 31/01/2024).

## Principios de producto que resuelven el 80 %

1. **Visibilidad del estado**: siempre se sabe dónde estoy, qué pasó y qué puedo hacer.
2. **Prevenir > corregir > explicar**: primero que no pueda equivocarse, después que pueda deshacer, último un mensaje.
3. **Deshacer > confirmar** para acciones reversibles ([`feedback-notificaciones.md`](feedback-notificaciones.md)).
4. **Pedir lo mínimo, cuando hace falta** (no al registrarse "por las dudas").
5. **No perder nunca el trabajo** de la persona (borradores, campos que no se vacían, sesión que avisa antes de expirar).
6. **Lenguaje de la persona** y consistencia de términos.
7. **Accesible por defecto** ([`accesibilidad.md`](accesibilidad.md)): no es una fase posterior.
8. **Rápido, o que se sienta rápido** ([`rendimiento-percibido.md`](rendimiento-percibido.md)).
9. **Honesto**: sin patrones oscuros ([`patrones-oscuros-etica.md`](patrones-oscuros-etica.md)).

## Regla de decisión rápida

```
¿La persona entiende qué es esto en 5 segundos?          → si no: contenido / jerarquía
¿Sabe cuál es el siguiente paso?                          → si no: CTA / navegación
¿Puede hacerlo sin leer instrucciones?                    → si no: signifiers / defaults
¿Sabe si salió bien?                                      → si no: feedback / estados
¿Puede volver atrás o deshacer?                           → si no: undo / navegación
¿Funciona con teclado, lector de pantalla y en 320 px?    → si no: accesibilidad / responsive
```

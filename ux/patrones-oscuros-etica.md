# Patrones oscuros, ética y regulación

Un patrón oscuro (*deceptive pattern*) es un diseño que hace que la persona haga algo que no habría elegido con información clara. Suben una métrica esta semana y destruyen confianza, generan reclamos y hoy también multas.

Referencias: Harry Brignull, [deceptive.design](https://www.deceptive.design/) (taxonomía original, 2010–); FTC, *Bringing Dark Patterns to Light* (informe de staff, 09/2022; [resumen de Arnold & Porter](https://www.arnoldporter.com/en/perspectives/advisories/2022/09/ftc-shines-a-little-light-on-dark-patterns)); Mathur et al., *Dark Patterns at Scale* (CSCW 2019, 11.000 sitios de compras).

## Catálogo (con la alternativa honesta)

| Patrón | Qué es | Alternativa honesta |
|---|---|---|
| **Roach motel / cancelación obstruida** | Fácil entrar, difícil salir (llamar por teléfono, 6 pantallas) | Cancelar por el mismo canal y con la misma facilidad que el alta |
| **Confirmshaming** | "No, prefiero seguir pagando de más" | "No, gracias" |
| **Pre-tildado / sneak into basket** | Seguros, donaciones o suscripciones agregados por defecto | Opt-in explícito |
| **Drip pricing / costos ocultos** | Fees que aparecen al final | Precio total desde el inicio |
| **Falsa urgencia** | Contadores que se reinician, "oferta termina hoy" eterna | Solo plazos reales |
| **Falsa escasez / popularidad** | "Quedan 2", "12 personas mirando" inventados | Datos reales o nada |
| **Trampa de prueba gratis** | La prueba se convierte en cobro sin aviso | Aviso antes del cobro, cancelar en 1 clic, recordatorio |
| **Preguntas engañosas (trick questions)** | Dobles negaciones en opt-outs | Lenguaje directo, opciones con el mismo peso |
| **Interfaz desigual (visual interference)** | "Aceptar" grande, "Rechazar" gris escondido | Opciones equivalentes con el mismo peso visual |
| **Nagging** | Pedir lo mismo una y otra vez (notificaciones, app, review) | Preguntar una vez y respetar el "no" |
| **Privacy zuckering / consentimiento forzado** | Compartir datos como condición o con defaults invasivos | Defaults privados, granularidad |
| **Bait and switch** | Un botón hace algo distinto de lo esperado | Etiquetas veraces |
| **Disfrazar anuncios** | Publicidad que parece contenido | Identificación clara |
| **Diseño adictivo** | Scroll infinito + autoplay + recompensas variables, sobre todo con menores | Puntos de corte, autoplay desactivable, límites |

## Regulación y casos (EE.UU. primero; estado al 19/11/2026)

**EE.UU.**
- **"Click-to-cancel" de la FTC: no está vigente.** La regla de 2024 fue anulada por el 8.º Circuito el **08/07/2025**; el **12/02/2026** la FTC restauró la regla de 1973, que solo cubre planes de "prenotificación"; el **13/03/2026** publicó un ANPRM para una regla nueva, sin texto propuesto todavía ([Federal Register 12/02/2026](https://www.federalregister.gov/documents/2026/02/12/2026-02866/revision-of-the-negative-option-rule-withdrawal-of-the-cars-rule-removal-of-the-non-compete-rule-to); [ANPRM 13/03/2026](https://www.federalregister.gov/documents/2026/03/13/2026-04952/rule-concerning-the-use-of-prenotification-negative-option-plans)).
- **ROSCA sigue vigente**: para ventas online con renovación exige informar los términos antes de tomar los datos de pago, consentimiento expreso y un mecanismo simple para dejar de pagar.
- **Amazon Prime (FTC, 25/09/2025)**: acuerdo de **US$2.500 M** (US$1.000 M de multa civil + US$1.500 M para consumidores) por alta engañosa y cancelación difícil de Prime; obliga a que rechazar y cancelar sean claros y simples ([Reuters](https://www.reuters.com/world/amazon-pay-25-billion-settle-prime-deception-allegations-2025-09-25/); [orden](https://search.ftc.gov/system/files/ftc_gov/pdf/Amazon-ROSCA-Order-Filed_0.pdf)).
- **California AB 2863** (desde **01/07/2025**): consentimiento afirmativo, cancelación online sin obstáculos; las ofertas de retención solo se permiten si se muestra un botón prominente de "click to cancel" junto a la oferta ([texto](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240AB2863); [AG de California](https://oag.ca.gov/news/press-releases/attorney-general-bonta-issues-consumer-alert-california%E2%80%99s-automatic-renewal-law)). Otros estados tienen leyes similares.
- **Regla de fees de la FTC** (desde 12/05/2025): precio total con cargos obligatorios en entradas para eventos y alojamiento de corta estadía ([Federal Register](https://www.federalregister.gov/documents/2025/01/10/2024-30293/trade-regulation-rule-on-unfair-or-deceptive-fees)).
- **Reseñas falsas**: regla de la FTC de 2024 (prohíbe reseñas falsas o compradas y suprimir negativas).
- Privacidad: leyes estatales (CCPA/CPRA en California y otras) consideran inválido el consentimiento obtenido con patrones oscuros.

**Unión Europea**
- **DSA, art. 25** (aplicable a plataformas online desde 17/02/2024): prohíbe interfaces que engañen o manipulen.
- **Digital Fairness Act**: **propuesta** de la Comisión Europea presentada en noviembre de 2026. Incluye prohibir patrones oscuros como la falsa escasez, transparencia de precios, opción de desactivar funciones adictivas, cancelar suscripciones más fácil y terminar con pruebas gratis que se vuelven trampas ([Comisión Europea, 11/11/2026](https://commission.europa.eu/news-and-media/news/making-your-online-experience-fairer-2026-11-11_en)). Todavía tiene que pasar por Parlamento y Consejo.
- GDPR + guías del EDPB sobre patrones engañosos en redes sociales; banners de cookies con "Rechazar" al mismo nivel que "Aceptar".

No es asesoramiento legal. Ante dudas de cumplimiento, consultá con un abogado.

## Patrón honesto: cancelación de suscripción

```html
<section aria-labelledby="cx-t">
  <h1 id="cx-t">Cancelar el plan Pro</h1>
  <p>Tu plan sigue activo hasta el <strong>12 de diciembre de 2026</strong>. Después pasás al plan gratis y <strong>no se te cobra de nuevo</strong>.</p>
  <p>Tus proyectos se conservan. Si superás el límite gratis (3 proyectos) quedan en solo lectura.</p>

  <!-- Oferta de retención opcional, con el botón de cancelar igual de visible (AB 2863) -->
  <aside class="offer"><p>¿Preferís pausar 1 mes en lugar de cancelar?</p><button type="button">Pausar 1 mes</button></aside>

  <form method="post" action="/cuenta/cancelar">
    <label for="motivo">¿Por qué cancelás? (opcional)</label>
    <select id="motivo" name="motivo"><option value="">Prefiero no decir</option><option>Precio</option><option>No lo uso</option><option>Me falta una función</option></select>
    <div class="actions">
      <button type="submit" class="primary">Cancelar plan</button>
      <a href="/cuenta">Mantener plan</a>
    </div>
  </form>
</section>
```
Después: página y email de confirmación con fecha efectiva y número de referencia.

## Banner de consentimiento con opciones equivalentes

```html
<div role="region" aria-label="Cookies" class="cookie">
  <p>Usamos cookies necesarias para que el sitio funcione y, si aceptás, de analítica para mejorarlo. <a href="/privacidad">Más info</a></p>
  <div class="actions">
    <button type="button" data-consent="reject">Rechazar opcionales</button>
    <button type="button" data-consent="settings">Elegir</button>
    <button type="button" data-consent="accept">Aceptar todas</button>
  </div>
</div>
<style>.cookie .actions button { /* mismo tamaño, mismo peso visual */ min-block-size: 2.75rem; padding-inline: 1rem; }</style>
```
Y que el banner no tape el foco ni el contenido principal (WCAG 2.4.11).

## Test rápido de ética (antes de shippear)

1. ¿La persona haría lo mismo si entendiera todo? 
2. ¿Rechazar cuesta lo mismo que aceptar?
3. ¿Cancelar cuesta lo mismo que contratar?
4. ¿Algún número de urgencia o escasez es inventado?
5. ¿Hay algo pre-tildado que cueste plata o datos?
6. ¿Te sentirías cómodo si saliera en una nota periodística o en un fallo?

Si alguna respuesta incomoda, rediseñá.

# Checkout y e-commerce

Fuente principal: Baymard Institute (700+ guías basadas en tests de usabilidad; muchas detrás de pago: acá van solo las públicas y citadas).

## Los números que importan (Baymard, actualizado 28/10/2026)

- Abandono de carrito promedio documentado: **70,22 %** (promedio simple de 50 estudios 2006–2025, rango 55–84 %). No es un benchmark en vivo ([Baymard](https://baymard.com/blog/cart-abandonment-rate)).
- 42 % de compradores de EE.UU. abandonó "solo mirando". **Sin ese grupo**, los motivos principales son: costos extra muy altos (40 %), entrega lenta (20 %), desconfianza con la tarjeta (19 %), obligar a crear cuenta (18 %), checkout largo o complicado (17 %), errores del sitio (17 %), política de devolución (13 %), no poder ver el total antes (12 %), tarjeta rechazada (10 %), pocos medios de pago (9 %).
- Checkout ideal: 12–14 elementos de formulario (7–8 campos). Promedio en EE.UU.: 23,48 elementos (14,88 campos).
- Estimación de Baymard: un e-commerce grande promedio podría subir ~35 % la conversión solo con mejoras de checkout (es una **estimación** de Baymard, no un resultado garantizado).

## Reglas de checkout (orden de impacto)

1. **Total real lo antes posible.** Envío, impuestos y fees visibles en el carrito o antes (calculadora por CP). En EE.UU. la regla de la FTC sobre *fees* engañosos exige precio total con cargos obligatorios en entradas para eventos y alojamiento corto desde el 12/05/2025 ([Federal Register](https://www.federalregister.gov/documents/2025/01/10/2024-30293/trade-regulation-rule-on-unfair-or-deceptive-fees)); California (SB 478) lo exige en general desde 2024. Ver [`patrones-oscuros-etica.md`](patrones-oscuros-etica.md).
2. **Compra como invitado** visible y prioritaria. Ofrecé crear cuenta **después** de pagar (solo pedir contraseña o passkey).
3. **Menos campos** ([`formularios-inputs.md`](formularios-inputs.md)): nombre en un campo, facturación = envío por defecto, dirección línea 2 colapsada, autocompletado de dirección (con opción de cargarla a mano).
4. **Medios de pago exprés** (Apple Pay, Google Pay, PayPal, Shop Pay, Link) arriba, pero sin esconder la tarjeta.
5. **Confianza en el campo de tarjeta**: agrupado visualmente, ícono de candado/seguridad *cerca* del campo, marcas aceptadas, sin salir del sitio sin aviso. Baymard: la percepción de seguridad depende más de la presentación que de la seguridad real.
6. **Errores recuperables**: tarjeta rechazada con causa clara y sin perder datos; validación de dirección que sugiere y no bloquea.
7. **Fechas de entrega** como fecha ("Llega el jueves 26"), no como "3–5 días hábiles".
8. **Resumen del pedido siempre visible** (sidebar en desktop, colapsable arriba en mobile) con imagen, variante y cantidad editable.
9. **Cupón**: campo colapsado detrás de un link ("¿Tenés un código?"). Un campo de cupón grande manda a la gente a buscar cupones afuera.
10. **Página de confirmación** útil (peak-end): número de pedido, fecha estimada, qué sigue, cómo cambiar o cancelar, email enviado a X.
11. **Política de devoluciones** linkeada en el carrito y en el checkout.

## Listado y ficha de producto

- **Imágenes reales**, varias, con zoom y en contexto/escala. Baymard (encuesta de junio 2026, 2.273 compradores de EE.UU.): 60 % dice que saber que una foto es generada por IA le baja la confianza de compra ([27/10/2026](https://baymard.com/research-articles/ai-engagement-quantitative-ux-insights-2026)).
- Precio, variantes, stock y fecha de entrega cerca del botón de agregar.
- Selección de variante clara (talle/color con estado agotado visible, no oculto).
- Reseñas con distribución, filtros y negativas visibles (esconderlas destruye confianza; en EE.UU. la FTC prohíbe reseñas falsas desde 2024).
- Specs en tabla escaneable; comparar productos.
- "Agregado al carrito": feedback claro sin sacar a la persona de la página (mini-cart o toast con link), no redirigir al carrito sin pedirlo.

## IA en e-commerce (2026)

Baymard publicó guías nuevas sobre asistentes de IA (#3458, #3461, #3464, #3467) y su encuesta 2026 marca una línea clara:
- La gente **acepta** IA para investigar: comparar características (63 %), stock (59 %), recomendaciones (56 %).
- **Prefiere humanos** para problemas: producto dañado/incorrecto (69 %), pedido atrasado/perdido (67 %), errores de envío o cobro (66 %).
- Regla: IA embebida en descubrimiento; escalado a humano visible en postventa. Ver [`ux-ia.md`](ux-ia.md).

## Snippet: resumen de costos honesto (React + Tailwind)

```tsx
type Line = { label: string; amount: number; hint?: string };
const fmt = new Intl.NumberFormat("es-AR", { style: "currency", currency: "ARS" });

export function OrderSummary({ lines, total, delivery }: { lines: Line[]; total: number; delivery: string }) {
  return (
    <section aria-labelledby="resumen" className="rounded-[var(--radius)] border p-5 grid gap-3">
      <h2 id="resumen" className="font-semibold">Resumen</h2>
      <dl className="grid gap-2">
        {lines.map((l) => (
          <div key={l.label} className="flex justify-between gap-4">
            <dt>{l.label}{l.hint && <span className="block text-sm text-[var(--muted)]">{l.hint}</span>}</dt>
            <dd className="tabular-nums">{fmt.format(l.amount)}</dd>
          </div>
        ))}
        <div className="flex justify-between border-t pt-3 font-semibold text-lg">
          <dt>Total</dt><dd className="tabular-nums">{fmt.format(total)}</dd>
        </div>
      </dl>
      <p className="text-sm">Llega <strong>{delivery}</strong>. Devolución gratis por 30 días. <a href="/devoluciones" className="underline">Ver política</a></p>
    </section>
  );
}
```

## Checklist de checkout

- [ ] Total con envío e impuestos visible antes de pedir datos de pago.
- [ ] Invitado disponible; cuenta opcional después.
- [ ] ≤ 8 campos por defecto; `autocomplete` en todos.
- [ ] Errores en línea + resumen; nada se borra.
- [ ] Pago exprés + tarjeta; marcas aceptadas visibles.
- [ ] Fecha de entrega concreta; política de devolución linkeada.
- [ ] Confirmación con número de pedido, próximos pasos y cómo cancelar.
- [ ] Nada pre-tildado que agregue costo (seguros, donaciones, suscripciones).
- [ ] Funciona con teclado y en 320 px; botones ≥ 24 × 24 px (mejor 44).

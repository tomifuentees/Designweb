# Dashboards

Un dashboard no es una colección de widgets. Es una respuesta a “¿qué tengo que mirar ahora?”. La terminación pro está en la jerarquía: un número o un problema primero, el detalle después.

Se lleva bien con [`../estilos/ui-casi-invisible.md`](../estilos/ui-casi-invisible.md) y [`../estilos/catalogo-tecnico.md`](../estilos/catalogo-tecnico.md). El SaaS oscuro premium ([`../estilos/saas-oscuro-premium.md`](../estilos/saas-oscuro-premium.md)) funciona si el producto ya vive de noche; no es obligatorio.

## Cuándo usarlo y cuándo no

**Usalo** cuando hay datos que cambian y una persona tiene que actuar. **No lo uses** como home de marketing, ni como un “analytics” decorativo con charts inventados.

## Qué se ve con terminación pro

- Un orden de lectura: alerta o KPI principal, recorte temporal (hoy / esta semana), tabla o lista de trabajo, charts al servicio de una pregunta.
- Pocas tarjetas de métrica (3–5), con contexto (“vs. ayer”, “faltan 2 sucursales”). Un número solo no dice nada.
- Densidad alta, butones chicos, tipografía de UI, no un hero.
- Filtros persistentes y visibles (sucursal, fecha). El usuario no tiene que redescubrirlos.
- Permisos: lo que no se puede ver no es un gráfico vacío, es una frase clara.
- Charts sobrios, mismos ejes, sin arcoíris ni 3D. Si Tremor u otra lib entra, que herede tus tokens, no los de la demo.

## Qué hace mal el default de IA

- Muro de 8–12 KPI cards con íconos Lucide, sparkline índigo y “+12.5%” sin fuente.
- Sidebar oscura + topbar con blur + “Welcome back, John 👋”.
- Charts de barras y donuts que no contestan nada, en un bento de 9.
- Un único breakpoint: en mobile es ilegible.
- Datos de placeholder (“$124,592 MRR”) que después se quedan en producción, o que un agente inventa como si fueran reales.

**Nunca inventes métricas financieras ni de negocio.** Si no hay número, mostrá el estado vacío.

## Tipografía del kit

- UI: [Satoshi](../tipografias/sans-geometrica.md) o [Switzer](../tipografias/sans-grotesk.md).
- Cifras: [IBM Plex Mono](../tipografias/mono.md), `tabular-nums`.
- Evitá [Geist](../tipografias/sans-grotesk.md) como personalidad si el producto no es un devtool: ya es el default de las landings de IA.

## Snippet

Un KPI con contexto, una alerta, una tabla chica. Sin sparkline decorativa.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=satoshi@400,500,600&display=swap">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
  <style>
    body { font-family: "Satoshi", sans-serif; background: #f3f1ec; color: #171513; }
    .mono { font-family: "IBM Plex Mono", ui-monospace, monospace; font-variant-numeric: tabular-nums; }
  </style>
</head>
<body class="max-w-5xl mx-auto px-6 py-10">
  <header class="flex items-end justify-between gap-4">
    <div>
      <h1 class="text-xl font-medium">Cierres de hoy</h1>
      <p class="text-sm text-neutral-600">Viernes 19.11 · tres sucursales</p>
    </div>
    <p class="mono text-xs text-neutral-500">Actualizado 09:40</p>
  </header>
  <p class="mt-6 text-sm border-l-2 border-[#8b1e1e] pl-3" role="status">Falta el cierre de Oro. No está en el depósito de las 11.</p>
  <section class="mt-8 grid md:grid-cols-3 gap-8 border-t border-black/10 pt-6">
    <div>
      <p class="text-xs uppercase tracking-[0.14em] text-neutral-500">Efectivo a depositar</p>
      <p class="mono text-3xl mt-1">3.290.850</p>
      <p class="text-xs text-neutral-500 mt-1">Según sistema · no incluye pendientes de Jere y Nerina</p>
    </div>
    <div>
      <p class="text-xs uppercase tracking-[0.14em] text-neutral-500">Sucursales cerradas</p>
      <p class="mono text-3xl mt-1">2 / 3</p>
      <p class="text-xs text-neutral-500 mt-1">Cierra Oro para completar el corte</p>
    </div>
    <div>
      <p class="text-xs uppercase tracking-[0.14em] text-neutral-500">Diferencias abiertas</p>
      <p class="mono text-3xl mt-1">1</p>
      <p class="text-xs text-neutral-500 mt-1">Cecilia Matas · $17.300 a confirmar</p>
    </div>
  </section>
</body>
</html>
```

# Formularios e inputs

El formulario es donde la UX se gana o se pierde en plata. Este archivo es el **criterio de comportamiento**; el criterio visual (estados, label, tipografía) ya está en [`../componentes/forms.md`](../componentes/forms.md). No lo repito.

Fuentes base: [GOV.UK Design System, Validation](https://design-system.service.gov.uk/patterns/validation/) y [Error message](https://design-system.service.gov.uk/components/error-message/); [Baymard, checkout](https://baymard.com/blog/checkout-flow-ux-optimization); Adam Silver, *Form Design Patterns* (2018); [WAI Forms Tutorial](https://www.w3.org/WAI/tutorials/forms/); [web.dev, Sign-in form best practices](https://web.dev/articles/sign-in-form-best-practices).

## 1. Antes de diseñar: cada campo se justifica

- **Preguntá solo lo que vas a usar ahora.** Baymard: el checkout ideal tiene 7–8 campos (12–14 elementos), el promedio en EE.UU. muestra 14,88 campos (23,48 elementos) ([Baymard, actualizado 28/10/2026](https://baymard.com/blog/cart-abandonment-rate)).
- Nombre completo en **un solo campo** salvo que el negocio necesite separarlo (Baymard #557).
- "Dirección línea 2" detrás de un link (Baymard #562). Facturación = envío por defecto (#566).
- No pidas confirmar email o contraseña: mostrá lo escrito (botón mostrar) y dejá corregir después.
- Si un dato se puede deducir (ciudad por código postal, tipo de tarjeta por número), deducilo.

## 2. Layout y labels

- **Una columna.** Excepciones: campos que van juntos naturalmente (ciudad / CP, vencimiento / CVV).
- **Label arriba del campo, visible siempre.** No placeholder como label, no floating labels que achican el texto a 11 px.
- **Ancho del campo ≈ largo esperado de la respuesta** (CP corto, dirección larga): es una pista.
- **Marcá lo opcional** "(opcional)"; si casi todo es opcional, replanteá. Si marcás obligatorios con `*`, explicá el asterisco. Baymard recomienda marcar ambos explícitamente.
- **Hint text** entre label y campo, conectado con `aria-describedby`.
- Agrupá con `<fieldset>` + `<legend>` (radios, checkboxes, fecha en tres campos, dirección).
- Botón primario alineado al borde izquierdo del form (donde está el ojo), texto con verbo + objeto: "Crear cuenta", "Pagar $12.400".

## 3. Tipos de input y `autocomplete`: la mejora más barata

| Dato | Markup |
|---|---|
| Email | `type="email" autocomplete="email" spellcheck="false" autocapitalize="off"` |
| Teléfono | `type="tel" autocomplete="tel"` (no `type="number"`) |
| Nombre | `autocomplete="name"` (o `given-name` / `family-name`) |
| Dirección | `autocomplete="street-address"`, `address-line1`, `address-level2` (ciudad), `address-level1` (provincia/estado), `postal-code`, `country` |
| Código postal / DNI / CVV / códigos | `type="text" inputmode="numeric" pattern="[0-9]*"` (nunca `type="number"`: borra ceros, suma flechas y scroll) |
| Monto | `type="text" inputmode="decimal"` |
| Tarjeta | `autocomplete="cc-number"`, `cc-exp`, `cc-csc`, `cc-name` + `inputmode="numeric"` |
| Usuario / contraseña | `autocomplete="username"`, `current-password`, `new-password` |
| OTP / código SMS | `autocomplete="one-time-code" inputmode="numeric"` (un solo campo, no 6 cajitas) |
| Passkey en el campo usuario | `autocomplete="username webauthn"` |
| Fecha conocida (nacimiento) | Tres campos día/mes/año (GOV.UK) o uno con formato explícito. Date picker solo para fechas cercanas / relativas |
| Búsqueda | `type="search"` dentro de `<search>` (Baseline) |
| Texto largo | `<textarea>` con `field-sizing: content` (Baseline desde 16/06/2026, web-features 3.46.0) |

WCAG 1.3.5 (*Identify Input Purpose*, AA) exige `autocomplete` correcto en datos personales.

## 4. Validación: cuándo, dónde y cómo

Hay dos escuelas con evidencia:

| | GOV.UK | Baymard / Wroblewski |
|---|---|---|
| Cuándo | **Al enviar**. "No valides cuando el usuario sale del campo" salvo que la investigación lo justifique | **Inline al salir del campo** (on blur), nunca mientras escribe; quitar el error en cuanto se corrige |
| Por qué | Usuarios lentos, lectores de pantalla y dictado sufren con validación prematura | Encontrar el error en contexto reduce idas y vueltas en forms largos |
| Evidencia | Investigación con usuarios de servicios públicos (amplio espectro, incluye baja alfabetización digital) | Estudio de Luke Wroblewski en [A List Apart, 2009](https://alistapart.com/article/inline-validation-in-web-forms/) (muestra chica, de hace años) + tests de checkout de Baymard |

**Regla de decisión del kit:**
1. Siempre validar en servidor. Siempre mostrar al enviar: **resumen de errores arriba** (con links a cada campo, foco movido ahí, `Error: ` al inicio del `<title>`) **+ mensaje junto a cada campo**.
2. Inline **on blur** solo para campos con formato verificable (email, tarjeta, CP) y **solo después de que la persona escribió algo**. Nunca marcar "requerido" en un campo que todavía no tocó.
3. Mientras escribe: solo para ayudas que no son errores (contador de caracteres, fuerza de contraseña, requisitos que se van tildando).
4. Una vez mostrado un error inline, **revalidá en cada input** para sacarlo apenas se corrige.
5. **Desactivá la validación HTML5 nativa** (`novalidate`) si tenés la tuya: sus burbujas no se pueden estilizar ni traducir de forma consistente (GOV.UK).
6. **Nunca vacíes campos** tras un error (excepto contraseña/CVV si lo exige seguridad, y decilo).
7. **No deshabilites el botón de enviar** hasta que el form esté perfecto: dejá enviar y mostrá qué falta. El botón deshabilitado no explica nada y no se puede enfocar.
8. Ignorá caracteres basura: espacios, guiones y puntos en números, tarjetas, CP, teléfonos (GOV.UK; ley de Postel).

### Cómo escribir el error

Qué pasó + cómo arreglarlo, en lenguaje llano, específico al campo (GOV.UK):
- ❌ "Campo inválido" · "Error 422" · "Por favor ingrese un valor" · "Te olvidaste…"
- ✅ "Ingresá un email con el formato nombre@ejemplo.com"
- ✅ "La fecha de nacimiento tiene que ser anterior a hoy"
- ✅ "Ingresá el CVV, son los 3 números del dorso de la tarjeta"

Más ejemplos (ES/EN) en [`ux-writing-microcopy.md`](ux-writing-microcopy.md).

## 5. Snippet completo: resumen + errores por campo (HTML + JS accesible)

```html
<form id="alta" novalidate>
  <div id="error-summary" class="error-summary" role="alert" tabindex="-1" hidden>
    <h2>Hay un problema</h2>
    <ul></ul>
  </div>

  <div class="field">
    <label for="email">Email</label>
    <p id="email-hint" class="hint">Te mandamos el recibo acá.</p>
    <p id="email-error" class="error" hidden></p>
    <input id="email" name="email" type="email" autocomplete="email"
           spellcheck="false" autocapitalize="off" aria-describedby="email-hint" required>
  </div>

  <div class="field">
    <label for="cp">Código postal</label>
    <p id="cp-error" class="error" hidden></p>
    <input id="cp" name="cp" type="text" inputmode="numeric" autocomplete="postal-code"
           class="w-cp" required>
  </div>

  <button type="submit">Crear cuenta</button>
</form>

<script>
const rules = {
  email: (v) => !v ? 'Ingresá tu email' :
    !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v) ? 'Ingresá un email con el formato nombre@ejemplo.com' : '',
  cp: (v) => { v = v.replace(/[\s.-]/g, ''); // ignorar caracteres basura
    return !v ? 'Ingresá tu código postal' : !/^\d{4}$|^[A-Z]\d{4}[A-Z]{3}$/i.test(v) ? 'El código postal tiene 4 números o el formato A1234ABC' : ''; },
};
const form = document.getElementById('alta');
const touched = new Set();

function setError(input, msg) {
  const err = document.getElementById(input.id + '-error');
  const hint = document.getElementById(input.id + '-hint');
  err.hidden = !msg; err.textContent = msg ? 'Error: ' + msg : '';
  input.setAttribute('aria-invalid', msg ? 'true' : 'false');
  input.setAttribute('aria-describedby', [hint && hint.id, msg && err.id].filter(Boolean).join(' '));
}

// Inline: solo al salir de un campo con contenido; luego se limpia al corregir.
form.addEventListener('focusout', (e) => {
  const i = e.target; if (!rules[i.name] || !i.value) return;
  touched.add(i.name); setError(i, rules[i.name](i.value));
});
form.addEventListener('input', (e) => {
  const i = e.target; if (touched.has(i.name)) setError(i, rules[i.name](i.value));
});

form.addEventListener('submit', (e) => {
  const errors = [];
  for (const [name, rule] of Object.entries(rules)) {
    const i = form.elements[name]; const msg = rule(i.value.trim());
    setError(i, msg); touched.add(name);
    if (msg) errors.push({ id: i.id, msg });
  }
  const box = document.getElementById('error-summary');
  if (errors.length) {
    e.preventDefault();
    box.querySelector('ul').innerHTML = errors.map(x => `<li><a href="#${x.id}">${x.msg}</a></li>`).join('');
    box.hidden = false; box.focus();
    document.title = 'Error: ' + document.title.replace(/^Error: /, '');
  }
});
</script>
<style>
.field { display:grid; gap:.25rem; margin-block-end: var(--space-5, 1.5rem); }
.hint { color: var(--muted); margin:0; }
.error { color: var(--danger-text, #b42318); font-weight:600; margin:0; }
[aria-invalid="true"] { border: 2px solid var(--danger, #b42318); }
.error-summary { border: 3px solid var(--danger, #b42318); padding: 1rem; margin-block-end: 1.5rem; }
.error-summary:focus { outline: 3px solid var(--focus, #ffbf47); }
.w-cp { max-inline-size: 10ch; }
</style>
```

### Variante React + react-hook-form + zod (validación on blur, revalida al cambiar)

```tsx
import React from "react";
import { useForm } from "react-hook-form";
import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";

const schema = z.object({
  email: z.string().min(1, "Ingresá tu email").email("Ingresá un email con el formato nombre@ejemplo.com"),
  nombre: z.string().min(1, "Ingresá tu nombre completo"),
});
type Data = z.infer<typeof schema>;

export function Alta({ onSubmit }: { onSubmit: (d: Data) => Promise<void> }) {
  const { register, handleSubmit, setFocus, formState: { errors, isSubmitting } } =
    useForm<Data>({ resolver: zodResolver(schema), mode: "onTouched", reValidateMode: "onChange",
                    shouldFocusError: true });
  return (
    <form noValidate onSubmit={handleSubmit(onSubmit)} className="grid gap-6 max-w-md">
      {Object.keys(errors).length > 0 && (
        <div role="alert" className="border-2 border-red-700 p-4">
          <h2 className="font-semibold">Hay un problema</h2>
          <ul>{Object.entries(errors).map(([k, v]) => (
            <li key={k}><a href={`#${k}`} onClick={(e) => { e.preventDefault(); setFocus(k as keyof Data); }}
              className="underline">{v?.message}</a></li>))}</ul>
        </div>
      )}
      <Field id="nombre" label="Nombre completo" error={errors.nombre?.message}>
        <input id="nombre" autoComplete="name" {...register("nombre")} />
      </Field>
      <Field id="email" label="Email" hint="Te mandamos el recibo acá." error={errors.email?.message}>
        <input id="email" type="email" autoComplete="email" spellCheck={false} {...register("email")} />
      </Field>
      <button type="submit" aria-disabled={isSubmitting} className="justify-self-start">
        {isSubmitting ? "Creando cuenta…" : "Crear cuenta"}
      </button>
    </form>
  );
}

function Field({ id, label, hint, error, children }: {
  id: string; label: string; hint?: string; error?: string; children: React.ReactElement }) {
  const describedBy = [hint && `${id}-hint`, error && `${id}-error`].filter(Boolean).join(" ") || undefined;
  return (
    <div className="grid gap-1">
      <label htmlFor={id} className="font-medium">{label}</label>
      {hint && <p id={`${id}-hint`} className="text-sm text-[var(--muted)]">{hint}</p>}
      {error && <p id={`${id}-error`} className="font-semibold text-red-700">Error: {error}</p>}
      {React.cloneElement(children, { "aria-invalid": !!error, "aria-describedby": describedBy,
        className: "border rounded px-3 py-2 aria-[invalid=true]:border-red-700 aria-[invalid=true]:border-2" })}
    </div>
  );
}
```

Nota: el submit usa `aria-disabled` y bloquea el doble envío en el handler, en vez de `disabled` (que saca el foco del botón y no se anuncia).

## 6. Formularios multipaso

- **Una cosa por página** (GOV.UK "question pages") funciona muy bien en mobile y para gente con poca experiencia; en desktop con usuarios expertos, agrupá.
- **Stepper con nombres de pasos**, no solo números; paso actual con `aria-current="step"`.
- **Guardá el progreso** en cada paso (servidor o `localStorage`) y permití volver sin perder datos.
- **Página de revisión** antes de confirmar ("Revisá tus respuestas", con "Cambiar" por ítem).
- Baymard: los pasos importan menos que la cantidad total de campos ([Baymard](https://baymard.com/research-articles/checkout-flow-average-form-fields)).
- No mostrar el paso 1 de 9 si son 9 pantallas de un campo: decí "Unos 3 minutos".

## 7. Contraseñas, passkeys y login

**Passkeys primero en 2026.** El Passkey Index de la FIDO Alliance (15/10/2026) reporta que el 36 % de los inicios de sesión exitosos de los participantes ya usan passkey (26 % en 2025), que tienen 93 % de éxito contra 78 % del MFA tradicional y ahorran ~27 s por inicio ([FIDO, Passkey Index 2026](https://fidoalliance.org/passkey-index-2026/)). Son datos de las empresas participantes, no de toda la web.

- Ofrecé crear una passkey **después** de un login o compra exitosa ("¿Querés entrar más rápido la próxima vez?"), no como barrera de registro.
- Usá *conditional UI* (autofill de passkeys en el campo usuario: `autocomplete="username webauthn"`) para que no haga falta un botón extra.
- Mantené un camino alternativo (email + código o contraseña) y gestión visible de passkeys en la cuenta.
- Patrones y textos oficiales: [FIDO Passkey Design Guidelines / Passkey Central](https://www.passkeycentral.org/design-user-journeys/).

**Contraseñas (si existen):**
- `autocomplete="new-password"` en registro para que el gestor sugiera una fuerte.
- Botón "Mostrar" (toggle `type`), con `aria-pressed`.
- Requisitos visibles **antes** de escribir, tildándose en vivo. Preferí largo mínimo (NIST SP 800-63B rev. 4 favorece largo y chequeo contra contraseñas filtradas por sobre reglas de composición).
- **Permití pegar** (WCAG 3.3.8 *Accessible Authentication*, AA: no exigir pruebas cognitivas como recordar o transcribir sin alternativa; pegar y gestores de contraseñas deben funcionar).
- No pongas CAPTCHA de rompecabezas sin alternativa (3.3.8).
- "Olvidé mi contraseña" junto al campo, no al final de la página.
- Un solo campo para OTP con `one-time-code`; si usás cajitas, que pegar el código completo funcione.

```html
<label for="user">Email</label>
<input id="user" name="username" type="email" autocomplete="username webauthn">
<label for="pw">Contraseña</label>
<div class="pw">
  <input id="pw" name="password" type="password" autocomplete="current-password">
  <button type="button" aria-pressed="false" aria-controls="pw"
    onclick="const i=document.getElementById('pw');const s=i.type==='password';i.type=s?'text':'password';this.setAttribute('aria-pressed',s);this.textContent=s?'Ocultar':'Mostrar'">Mostrar</button>
</div>
<a href="/recuperar">¿Olvidaste tu contraseña?</a>
```

## 8. Controles: cuál usar

| Necesidad | Control | Por qué |
|---|---|---|
| 2–5 opciones excluyentes | Radios visibles | Se ven todas sin abrir nada |
| >~7 opciones excluyentes | `<select>` o combobox con búsqueda | Ahorra espacio |
| Lista enorme (países, ciudades) | Combobox con autocompletado ([APG](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/)) | Escribir es más rápido que scrollear |
| Sí/No con efecto inmediato | Switch (`role="switch"`) | Comunica "se aplica ya" |
| Sí/No que se envía con el form | Checkbox | El switch sugiere efecto inmediato |
| Cantidad pequeña | Stepper (− 1 +) con input editable | — |
| Rango | Dos inputs o slider con inputs | Slider solo no es preciso ni accesible por sí mismo |

`<select>` estilizable (`appearance: base-select`) todavía **no es Baseline** (Chrome 135+, Safari 27; falta Firefox según web-features 3.46.0): usalo como mejora progresiva.

## 9. Anti-patrones de formularios

- Placeholder como label; floating label; label que desaparece.
- Validar mientras escribe ("email inválido" al tipear la primera letra).
- Botón deshabilitado sin explicación.
- `type="number"` para códigos, teléfonos o tarjetas.
- Errores solo con color o solo arriba.
- Reset/"Limpiar" al lado de "Enviar".
- Pedir datos "por las dudas" (teléfono, fecha de nacimiento, género) sin explicar para qué.
- Captcha antes de que la persona haga algo.
- Bloquear pegar en email/contraseña.
- Tiempo de sesión que expira sin aviso y borra el formulario (WCAG 2.2.1: avisar y permitir extender).

# UX writing y microcopy

Las palabras son interfaz. La copy de modelo de IA (hype, em-dash a granel, "Seamless", "Unlock") ya está en [`../anti-patrones/catalogo.md`](../anti-patrones/catalogo.md) #12, #14 y #25. Acá: cómo escribir la copy **funcional**.

Fuentes: [GOV.UK, Writing for GOV.UK / Style guide](https://www.gov.uk/guidance/content-design/writing-for-gov-uk); [Mailchimp Content Style Guide](https://styleguide.mailchimp.com/); [Material, Writing](https://m3.material.io/foundations/content-design/overview); Torrey Podmajersky, *Strategic Writing for UX* (2019); Kinneret Yifrah, *Microcopy: The Complete Guide*; [NN/g, Error-Message Guidelines](https://www.nngroup.com/articles/error-message-guidelines/).

## Principios

1. **Claro > ingenioso.** Si hay que pensar, falló.
2. **Útil y específico**: qué pasó, qué hago, qué pasa después.
3. **Palabras de la persona**, no del equipo ni de la base de datos.
4. **Primero lo importante** (la gente escanea las 2 primeras palabras).
5. **Verbos en botones**, que describan el resultado: "Guardar cambios", "Pagar $12.400", "Enviar solicitud".
6. **Consistencia terminológica**: un glosario por producto (ej.: siempre "proyecto", nunca "espacio" en otro lado).
7. **Tono que se adapta al momento**: más cálido en éxito, más sobrio y directo en errores y en temas de plata o salud. Sin chistes en errores.
8. **Inclusivo**: sin culpar ("Te olvidaste…"), sin capacitismo, género neutro cuando se pueda reformular.
9. **Corto, pero no críptico.** Quitar palabras que no cambian el significado.
10. **Localizar, no traducir**: formatos, moneda, ejemplos, voseo/tuteo/usted según mercado.

## Fórmulas

**Error**: [qué pasó] + [cómo arreglarlo]. Sin "por favor" (GOV.UK: implica que es opcional), sin "lo sentimos" vacío, sin jerga.
**Empty state**: [qué va acá] + [beneficio o próximo paso] + [acción].
**Confirmación destructiva**: [¿Verbo + objeto concreto?] + [consecuencia] + botones con verbo.
**Éxito**: [qué se logró] + [qué sigue].
**Botón**: [verbo] + [objeto] (+ dato clave).

## Banco de ejemplos (ES rioplatense / EN-US)

| Situación | ❌ Evitar | ✅ ES | ✅ EN |
|---|---|---|---|
| Email inválido | "Email inválido" | "Ingresá un email con el formato nombre@ejemplo.com" | "Enter an email address like name@example.com" |
| Campo vacío | "Campo requerido" | "Ingresá tu nombre completo" | "Enter your full name" |
| Fecha futura no permitida | "Fecha inválida" | "La fecha de nacimiento tiene que ser anterior a hoy" | "Date of birth must be in the past" |
| Tarjeta rechazada | "Pago fallido" | "Tu banco rechazó la tarjeta. Probá con otra o contactá al banco." | "Your bank declined this card. Try another card or contact your bank." |
| Error del servidor | "Error 500" | "No pudimos guardar los cambios. Tus datos siguen acá; probá de nuevo en un minuto." | "We couldn't save your changes. Your work is still here. Try again in a minute." |
| Sin conexión | "Network error" | "Sin conexión. Guardamos tus cambios y los enviamos cuando vuelva." | "You're offline. We'll save your changes and sync when you're back." |
| Sin resultados | "No results" | "No encontramos 'zapatilas'. ¿Quisiste decir **zapatillas**?" | "No results for 'sneekers'. Did you mean **sneakers**?" |
| Empty inicial | "Nothing here yet ✨" | "Todavía no hay facturas. Creá la primera o importalas desde Excel." | "No invoices yet. Create your first one or import from a spreadsheet." |
| Sin permiso | "403 Forbidden" | "No tenés acceso a este proyecto. Pedíselo a Ana (dueña del proyecto)." | "You don't have access to this project. Ask Ana (owner) for access." |
| Borrar | "¿Estás seguro?" Sí / No | "¿Eliminar 'Ventas 2026'? Se borran 214 facturas." Eliminar proyecto / Cancelar | "Delete 'Sales 2026'? This removes 214 invoices." Delete project / Cancel |
| Deshacer | "Elemento eliminado" | "Factura archivada · Deshacer" | "Invoice archived · Undo" |
| Guardado | "Success!" | "Cambios guardados" | "Changes saved" |
| Botón de alta | "Submit" | "Crear cuenta" | "Create account" |
| Botón de pago | "Continuar" | "Pagar $12.400" | "Pay $124.00" |
| Contraseña | "Contraseña débil" (después de fallar) | "Usá 12 caracteres o más. Una frase sirve." (antes) | "Use 12 or more characters. A phrase works." |
| Cancelar suscripción | "¿Seguro que querés perder todos tus beneficios?" | "Tu plan sigue activo hasta el 12/12. No se te va a cobrar de nuevo." | "Your plan stays active until Dec 12. You won't be charged again." |
| Opt-out (confirmshaming) | "No, prefiero pagar más" | "No, gracias" | "No thanks" |
| Carga larga | "Loading…" | "Generando el reporte (unos 30 s). Te avisamos cuando esté." | "Generating your report (about 30 sec). We'll let you know when it's ready." |
| IA incierta | (respuesta segura sin fuente) | "No encontré esto en tus documentos. ¿Querés que busque en la web?" | "I couldn't find this in your documents. Want me to search the web?" |

## Botones y links

- El texto del link dice adónde lleva: "Ver la política de devoluciones", no "Hacé clic acá" (WCAG 2.4.4; también ayuda a agentes).
- Mismo verbo en el botón que abre algo y en el que lo confirma ("Eliminar" → dialog → "Eliminar proyecto").
- "Cancelar" ambiguo en flujos de cancelación: "Mantener plan" / "Cancelar plan".
- Mayúscula solo inicial (sentence case) en español; en inglés-US, elegí una convención y mantenela.

## Números, fechas, unidades

- Formato local con `Intl.*`. Moneda con símbolo y código si hay ambigüedad ($ ARS vs US$).
- Fechas absolutas para plazos ("vence el 12/12"), relativas para actividad reciente ("hace 5 min").
- Números en cifras en UI ("3 archivos", no "tres archivos").

## Plurales e i18n

```ts
const pr = new Intl.PluralRules("es-AR");
const msg = (n: number) => ({ one: `${n} archivo`, other: `${n} archivos` } as Record<string, string>)[pr.select(n)];
// Nunca concatenes fragmentos traducidos: "Se eliminó " + n + " archivo(s)". Usá ICU MessageFormat (FormatJS, i18next).
```

Reservá ~30–40 % de espacio extra para traducciones al alemán/español frente al inglés en botones y labels (regla de oficio, no un estándar).

## Proceso

1. Escribí la copy **antes** del layout (content-first): fuerza decisiones de jerarquía.
2. Leé en voz alta. Si suena a robot o a abogado, reescribí.
3. Probá la comprensión con 5 personas ("¿qué pasa si toco este botón?").
4. Mantené un **glosario** y una lista de voz y tono en el repo del producto.

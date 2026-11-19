# Checklist de revisión (antes de shippear)

Pasada corta, pensada para un humano o para un agente que ya armó una UI. Si marcás tres o más “sí”, volvé al [catálogo](./catalogo.md) y a las reglas antes de mergear. Una sola cosa, elegida a propósito, puede quedar.

## Color y forma

- [ ] ¿Hay un degradé índigo–violeta (o `bg-indigo-500` / `violet-600`) usado como identidad?
- [ ] ¿Hay un heading con `bg-clip-text` o un halo/glow detrás del hero?
- [ ] ¿Cada bloque tiene un color distinto, sin una paleta de roles?
- [ ] ¿Todas las cajas comparten un `rounded-2xl`/`3xl` y la misma sombra suave?
- [ ] ¿Hay “fingernail cards” (raya de acento a la izquierda en cada card)?
- [ ] ¿Hay glassmorphism como tema, o un brutalismo de plantilla que no se pidió?
- [ ] ¿El cuerpo o el muted fallan 4.5:1 (sobre todo en oscuro)?

## Layout y motion

- [ ] ¿El hero está centrado, con un titular que le serviría a cualquiera y dos CTAs genéricos?
- [ ] ¿Hay una fila de tres cards idénticas con ícono + párrafo?
- [ ] ¿La página sigue el orden hero → logos → 3 features → testimonials → pricing → CTA sin una razón?
- [ ] ¿Hay cards anidadas dentro de cards?
- [ ] ¿Cada sección entra con fade/slide-up, o hay badges con `animate-pulse`?
- [ ] ¿Cada botón lleva una flecha, y cada H2 un kicker en versales o un 01 / 02 / 03?

## Tipo, ícono e imagen

- [ ] ¿La única familia es Inter, Geist, Poppins, Montserrat o Roboto?
- [ ] ¿Los íconos son Lucide “porque sí”?
- [ ] ¿Hay emojis haciendo de ícono, bullet o saludo de dashboard?
- [ ] ¿La imagen es un render 3D de stock, un retrato de IA o un MacBook genérico?
- [ ] ¿Falta prueba real (precios, horarios, nombres, captura del producto)?

## Copy y resto

- [ ] ¿Aparecen Elevate, Seamless, Supercharge, Unleash, Empower, cutting-edge, “build the future of…”?
- [ ] ¿Un dashboard arranca con “Welcome to your Dashboard, [Name] ✨”?
- [ ] ¿Hay frases que huelen al prompt (“Built with…”, “no mocks”, justificación técnica)?
- [ ] ¿La prosa está llena de em-dash, openers de stock o hedging?
- [ ] ¿El title, el alt, el OG o el favicon son los de la plantilla o del bundler?
- [ ] ¿Hay hex, radios o duraciones sueltos, distintos a los tokens del proyecto?

Si el proyecto todavía no tiene tokens, paleta ni pareja tipográfica, **empezá por ahí**. Sin eso, el checklist se va a poner rojo en cada pasada.

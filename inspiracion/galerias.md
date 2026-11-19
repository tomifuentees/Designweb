# Galerías

URLs comprobadas el 19 de noviembre de 2026. Donde el GET devolvió antibot (403), rate limit (429) o un redirect raro, queda anotado: **no es un 404**. No se inventaron premios ni “site of the day”.

## Las que más rinden

### Recent (antes Godly)

- [recent.design](https://recent.design/) (GET 200).
- `https://godly.website/` redirige a `http://recent.design/?ref=godly`. En esta pasada esa URL con query devolvió **500**; el origen `https://recent.design/` sí respondió 200. Usá **recent.design** como canónica, no godly.website.
- Para qué: landings y sitios de marketing con terminación alta, un feed diario. Sesgo hacia lo llamativo. Colorlib y otros describieron el cambio de nombre en 2026 (ya citado en [`../estilos/fuentes-investigacion.md`](../estilos/fuentes-investigacion.md)).

### Awwwards

- [awwwards.com](https://www.awwwards.com/) — GET **403** (antibot) desde este entorno, el dominio está vivo. También 403 en `/inspiration/`.
- Para qué: SOTY, nominees, estudios de motion y WebGL. Sesgo fuerte a lo espectacular y a agencias. No tomes un nominee como receta para un SaaS de trabajo. Se cita como observatorio, no se inventaron case studies no leídos.

### Land-book

- [land-book.com](https://land-book.com/) (GET 200).
- Para qué: landings filtrables por estilo, paleta, tipo de producto. Muy útil para un agente que necesita “tres SaaS claros, no Oscars”.

### Lapa Ninja

- [lapa.ninja](https://www.lapa.ninja/) y [categoría SaaS](https://www.lapa.ninja/category/saas/) (GET 200).
- Para qué: capturas de landings, mucho volumen, calidad irregular. Sirve para barrer, no para copiar el primer resultado.

### Mobbin

- [mobbin.com](https://mobbin.com/) (GET 200).
- Para qué: **flujos de producto** reales (apps y web apps), no landings de marketing. Onboarding, settings, empty states, tablas. De pago en lo profundo; la home responde.

### Siteinspire

- [siteinspire.com](https://www.siteinspire.com/) — GET **429** en esta pasada (rate limit, no 404). El dominio está vivo.
- Para qué: curaduría clásica, más “sitio de estudio / editorial” que “SaaS 2026”. Útil como contrapeso de Recent.

### Minimal Gallery

- [minimal.gallery](https://minimal.gallery/) (GET 200), listado en [minimal.gallery/websites](https://minimal.gallery/websites/).
- Para qué: sitios contenidos, tipográficos, poco cromo. Buen filtro si el brief es [`../estilos/expresivo-minimo.md`](../estilos/expresivo-minimo.md) o [`../estilos/minimalismo-monocromo.md`](../estilos/minimalismo-monocromo.md).

### SaaS Landing Page

- [saaslandingpage.com](https://saaslandingpage.com/) (GET 200).
- Para qué: landings de SaaS y startups, a veces ordenadas por tipo de sección (pricing, features, etc.). Complementa Land-book y Lapa.

### Dark Design

- [dark.design](https://dark.design/) redirige a [www.dark.design](https://www.dark.design/) (GET 200).
- Para qué: sitios oscuros curados (producto, agencia, hardware). Útil junto a [`../estilos/saas-oscuro-premium.md`](../estilos/saas-oscuro-premium.md), no como excusa para un dark mode de plantilla.

### One Page Love

- [onepagelove.com](https://onepagelove.com/) (GET 200).
- Para qué: one-pagers, portfolios, lanzamientos de una sola vista. No es el cajón de un dashboard.

### Refero

- [refero.design](https://refero.design/) (GET 200).
- Para qué: patrones de UI de producto real (marketing sites y apps), cercano a Mobbin en intención. Buen lugar para un form, un pricing o un settings.

### Page Flows (Screenlane apunta acá)

- [pageflows.com](https://pageflows.com/) (GET 200). En esta pasada, `https://screenlane.com/` **redirige a pageflows.com**. Si una lista de 2024–2025 te manda a Screenlane, usá Page Flows.
- Para qué: flows grabados de producto (onboarding, checkout, empty states).

## Otras que valen, con matiz

| Galería | URL | GET | Para qué / matiz |
|---|---|---|---|
| Httpster | [httpster.net](https://httpster.net/) | 200 | Sitios con carácter, mix editorial y experimental |
| Hoverstat.es | [hoverstat.es](https://www.hoverstat.es/) | 200 (`www`) | Sitios raros, “internet como medio”. Contrapeso anti-plantilla |
| CSS Design Awards | [cssdesignawards.com](https://www.cssdesignawards.com/) | 202 (vivo) | Premios, sesgo de agencia, similar a Awwwards |
| Brutalist Websites | [brutalistwebsites.com](https://www.brutalistwebsites.com/) | 200 | Observatorio de brutalismo / anti-diseño, no un producto |
| Curated Design | [curated.design](https://curated.design/) | 200 | UI curada, más producto que SOTY |
| Landingfolio | [landingfolio.com](https://www.landingfolio.com/) (`www` canónico, 200) | 200 | Landings y componentes de marketing, calidad mixta |
| Landing Love | [landing.love](https://www.landing.love/) | 200 | Landings; sirve de barrido |
| Layers | [layers.to](https://layers.to/) | 200 | Comunidad de archivos y tincadas; no es prueba de producción |
| Saaspo | [saaspo.com](https://saaspo.com/) | **429** (vivo) | SaaS y dashboards; citado en listas de 2026 (p. ej. un hilo de @pat_baranowski, 9 de julio de 2026). Reintentar si rate-limitea |
| Design Spells | [designspells.com](https://www.designspells.com/) | **429** (vivo) | Microdetalles de interfaz; reintentar |
| Dribbble | [dribbble.com](https://dribbble.com/) | no se re-curleó acá; en estilos dio 202 | Exploración, **no** prueba de que un look esté en producción |

Godly, como nombre, quedó atrás: no lo uses como URL canónica. UI Movement aparece en listas de Twitter de 2026; **no se verificó un URL estable en esta pasada**, así que no se cita como galería activa.

# Fuentes de la investigación (animaciones)

Investigación del 19 de noviembre de 2026 (zona America/Argentina/Salta). Licencias y homes se contrastaron con curl y, cuando aplica, con la API de GitHub (`license.spdx_id`, `pushed_at`, stars). No se inventaron anuncios de soporte de browsers: donde no se abrió Can I Use en esta pasada, se cita la nota de web.dev o MDN y se pide verificar al implementar.

## Docs y anuncios oficiales

- Motion — [motion.dev](https://motion.dev/) (GET 200). [Framer Motion is now independent, introducing Motion](https://motion.dev/magazine/framer-motion-is-now-independent-introducing-motion) (noviembre de 2024, GET 200). Repo [motiondivision/motion](https://github.com/motiondivision/motion), MIT, push el 19/11/2026. Cuenta verificada [@motiondotdev](https://x.com/motiondotdev).
- GSAP — [gsap.com](https://gsap.com/), [pricing](https://gsap.com/pricing/), [Standard License](https://gsap.com/community/standard-license/) (effective 30 de abril de 2025, last modified 30 de mayo de 2025, GET 200). [3.13 release, 29 de abril de 2025](https://gsap.com/blog/3-13/) (GET 200): plugins de Club en el npm público, SplitText reescrito. [Webflow, 30 de abril de 2025](https://webflow.com/updates/gsap-becomes-free) (GET 200).
- Lenis — [lenis.dev](https://lenis.dev/) (GET 200; `lenis.darkroom.engineering` redirige). Repo [darkroomengineering/lenis](https://github.com/darkroomengineering/lenis), MIT, push el 19/11/2026. Cuentas [@darkroomdevs](https://x.com/darkroomdevs) y [@LenisSmooth](https://x.com/LenisSmooth) verificadas con la API de X.
- View Transitions — [MDN](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API) (GET 200). [web.dev, same-document view transitions are now Baseline Newly available](https://web.dev/blog/same-document-view-transitions-are-now-baseline-newly-available) (GET 200): 14 de octubre de 2025, Firefox 144.
- `@starting-style` — [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@starting-style) (GET 200).
- Scroll-driven — [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations) (GET 200).
- Rive — [rive.app](https://rive.app/) (GET 200). [rive-app/rive-react](https://github.com/rive-app/rive-react), MIT, push 9/11/2026.
- Lottie — [lottiefiles.com](https://lottiefiles.com/) (GET 200). [airbnb/lottie-web](https://github.com/airbnb/lottie-web), MIT, último push visto 1/9/2025.
- Theatre.js — [theatrejs.com](https://www.theatrejs.com/) (GET 200). [theatre-js/theatre](https://github.com/theatre-js/theatre), Apache-2.0, último push visto **14 de agosto de 2024**.
- Auto-Animate — [auto-animate.formkit.com](https://auto-animate.formkit.com/) (GET 200). [formkit/auto-animate](https://github.com/formkit/auto-animate), MIT, push 7/11/2026.

## Posts de X (reales, con fecha)

- [@osmosupply, 7 de mayo de 2025](https://x.com/osmosupply/status/1920138413539303725): celebra, con Codrops y GreenSock, que los plugins de Club pasaron a ser gratis gracias a Webflow, y anuncia recursos semanales.
- [@jh3yy, 19 de julio de 2025](https://x.com/jh3yy/status/1946371056047931675): CSS scroll-snap + scroll-driven animation.
- [@jh3yy, 28 de agosto de 2026](https://x.com/jh3yy/status/2093465874321563782): microinteracciones de carousel nativo con `view-timeline` y `::scroll-marker`.
- [@jh3yy, 31 de octubre de 2026](https://x.com/jh3yy/status/2116321049851908266): esfera de emoji con scroll-driven en dos ejes.
- [@greatfrontend, 16 de octubre de 2026](https://x.com/greatfrontend/status/2111091192750657787): pares que se confunden, entre ellos transition vs `@starting-style`, y scroll-driven vs listener de scroll.

No se usó como fuente oficial de GSAP un post de mayo de 2026 de @GithubProjects que hablaba de “official AI skills for GSAP”: no se contrastó un anuncio en gsap.com, así que no se documenta como hecho del equipo.

## Qué no se pudo verificar

- La tabla completa de Can I Use para scroll-driven animations en Firefox, el 19/11/2026, no se abrió en esta pasada. Se documenta soporte sólido en Chromium y Safari 26, y se pide verificar Firefox al implementar. Una ficha de web-features-explorer apareció en la búsqueda, pero no se usó un número de versión de Firefox sin abrir la fuente.
- Si DotLottie reemplazó de facto a `lottie-web` en proyectos nuevos: el runtime clásico sigue publicado; el ritmo del repo es más calmo (último push visto en septiembre de 2025).
- El detalle contractual de los planes de Rive (cuándo un `.riv` de equipo se puede embeber en un cliente). Se avisa que hay que leer el plan; no se inventaron límites.
- Que Theatre.js esté “muerto”: no está archivado, el sitio responde 200, pero sin push desde agosto de 2024 no se recomienda como default.
- Un anuncio oficial de skills de GSAP para agentes (se vio solo un post de terceros).

# DESIGN BRIEF — ASTROPULSE AGENCY (v2.0 · Astro Traffic × SpaceX Edition)

> Generado y validado conforme al flujo obligatorio de [`creative_brief_builder.html`](file:///C:/Users/Jose/Downloads/creative_brief_builder.html), [`taste-skill`](file:///C:/Users/Jose/.agents/skills/taste-skill/SKILL.md) y [`spacex/DESIGN.md`](file:///E:/WEBS/REPOS_DISENO/awesome-design-md/design-md/spacex/DESIGN.md).

---

## 01 · Proyecto
- **Nombre del proyecto:** `ASTROPULSE AGENCY`
- **Tipo de web / sector:** Agencia de Marketing en Redes Sociales, Paid Social Media Buying (TikTok, Meta, YouTube Shorts) y Escala Algorítmica con temática Aeroespacial.
- **Objetivo y público:** Captar marcas de alto crecimiento (eCommerce, SaaS, Consumer Tech) mediante una interfaz que fusiona la precisión editorial suiza de *Astro Traffic* con la ingeniería aeroespacial de *SpaceX*.
- **Dirección visual general:**
  - **Swiss Brutalist Grid (`Astro Traffic`):** Retícula asimétrica visible de 4 columnas (`440px | 172px | 172px | 596px` → `31.88% | 12.46% | 12.46% | 43.19%`), fotografía monocromática de alto contraste con bloques duotono carmesí (`#AF181A`) y titulares de pesos combinados (*Medium 500 + Light 300*).
  - **Aerospace Telemetry (`SpaceX`):** Bandas oscuras en grafito/carbono (`#0B0C10`, `#14161D`, `#222530`), micro-telemetría en mayúsculas condensadas (`D-DIN` / `Barlow Condensed`) con tracking positivo (`+1.2px` a `+1.6px`), botones cápsula fantasma (*ghost pill buttons* con `border-radius: 32px`), y una escala rica de grises arquitectónicos y titanio.

---

## 02 · Webs de referencia
1. **Astro Traffic Website (Ihor Muntian — Behance):**
   - **URL:** `https://www.behance.net/gallery/228872083/Astro-Traffic-Website`
   - **Elementos replicados al milímetro:**
     - Sistema de 4 columnas asimétricas con líneas divisorias continuas de `1px`.
     - Tipografía `Inter` en pesos **Light (300), Regular (400) y Medium (500)** — nunca *Black 900* pesado — combinando grosores en una misma línea (`WHAT` 500 + `WE` 300 + `OFFER` 500; `ASTROPULSE` 500 + `AS` 300 + `A` 500 / `GLOBAL` 400 rojo + `AGENCY` 300).
     - Composición del Hero con astronauta a la derecha sobre bloque horizontal carmesí `#AF181A` y botón cuadrado negro `↗` en la esquina inferior izquierda del bloque.
     - Sección `OUR EXPERIENCE — OUR PRIDE` con el título insertado entre la primera y la segunda tarjeta de caso de éxito.
     - Sección `OUR TEAM` con 6 retratos alineados en la base pero con **alturas escalonadas (skyline asimétrico)** y bandas rojas en miembros clave.
2. **SpaceX Official Design System (`spacex/DESIGN.md`):**
   - **Referencia local:** [`E:\WEBS\REPOS_DISENO\awesome-design-md\design-md\spacex\DESIGN.md`](file:///E:/WEBS/REPOS_DISENO/awesome-design-md/design-md/spacex/DESIGN.md)
   - **Elementos fusionados:**
     - Botones *Ghost Pill* (`rounded-pill: 32px`, borde `1px`, texto en mayúsculas con `letter-spacing: 1.17px`).
     - Banda inmersiva de telemetría orbital en tonos carbono/grafito (`#0A0B0E` / `#161820` / `#262934`) con visualización de satélite/cápsula y telemetría de campaña en vivo.
     - Uso de `Barlow Condensed` / `D-DIN` para etiquetas técnicas, coordenadas y cabeceras de misión.

---

## 03 · Tipografías
1. **Principal (Display Editorial & Cuerpo — Estilo *Astro Traffic*):**
   - **Fuente:** `Inter` (`https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap`)
   - **Uso y Pesos:**
     - Titulares gigantes (`H1`, `H2`): Combinación estricta de `500 (Medium)`, `400 (Regular)` y `300 (Light)` con `letter-spacing: -0.03em` y `line-height: 0.96`.
     - Numerales de servicio (`01`–`04`) y métricas (`140M+`, `18+`, `4`, `97%`): `Inter 400 Regular` limpio y arquitectónico.
     - Cuerpo de texto: `Inter 400` (`12.5px`–`14px`, `line-height: 1.55`).
2. **Secundaria (Telemetría & Botones Aeroespaciales — Estilo *SpaceX*):**
   - **Fuente:** `Barlow Condensed` / `D-DIN` fallback (`https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400;500;600;700&display=swap`)
   - **Uso y Pesos:**
     - Eyebrows técnicos, coordenadas orbitales, barra de telemetría SpaceX y botones *ghost pill* en mayúsculas con `letter-spacing: 0.12em`.

---

## 04 · Paleta de colores (Gama Extendida de Grises, Titanio, Carbono y Carmesí)
| Token | Código HEX | Rol en el sistema |
|---|---|---|
| `--bg-mist-gray` | `#ECECEE` | Lienzo principal claro (gris niebla arquitectónico, evita el blanco puro cegador) |
| `--bg-concrete-gray` | `#E2E3E7` | Fondo de tarjetas Bento (`140M+`, `18+`), bloques secundarios y footer superior |
| `--bg-steel-gray` | `#D5D7DE` | Bloques de contraste medio, estados hover de celdas y paneles técnicos |
| `--text-titanium` | `#767984` | Texto secundario, descripciones técnicas y subtítulos de métricas |
| `--text-silver-mute` | `#9CA0AC` | Micro-telemetría sobre fondos oscuros y etiquetas de formulario |
| `--spacex-graphite` | `#232630` | Superficies de transición estilo SpaceX, tarjetas de telemetría oscura |
| `--spacex-carbon` | `#14161D` | Banda orbital SpaceX y cabeceras técnicas de alto contraste |
| `--spacex-void` | `#0A0B0E` | Negro profundo aeroespacial y botones de acción cuadrados |
| `--astro-crimson` | `#AF181A` | Acento carmesí quirúrgico (bloques duotono en fotos, numerales `01-04`, palabras clave) |
| `--grid-line-light` | `rgba(20, 22, 29, 0.11)` | Líneas estructurales continuas de `1px` sobre fondo gris claro |
| `--grid-line-dark` | `rgba(255, 255, 255, 0.10)` | Líneas estructurales continuas de `1px` sobre las bandas oscuras SpaceX |

---

## 05 · Componentes, animaciones y efectos
- **Retícula Estructural de 4 Columnas (`31.88% | 12.46% | 12.46% | 43.19%`):** Líneas verticales visibles a lo largo de todas las secciones claras y oscuras.
- **Hero con Astronauta Original + Bloque Carmesí:** Imagen generada a medida (`custom_hero_astronaut.png`) con casco blanco/titanio y visor oscuro sobre fondo `#E4E4E4`, atravesada en su mitad inferior por el bloque `#AF181A` y el botón negro `↗`.
- **Banda Fusionada SpaceX ("ORBITAL TELEMETRY ENGINE"):** Sección en carbono `#0A0B0E` y grafito `#14161D` con visualización orbital (`custom_spacex_orbital.png`), telemetría de campañas en tiempo real y CTA *ghost pill* de SpaceX.
- **Tira Editorial `OUR EXPERIENCE — OUR PRIDE`:** Título encajado en las columnas centrales (Col 2 y Col 3) flanqueado por `custom_case_1.png` a la izquierda y `custom_case_2.png` + `custom_case_3.png` a la derecha.
- **Skyline de Equipo (`OUR TEAM`):** 6 retratos originales (`custom_crew_1.png` a `custom_crew_6.png`) alineados en su base inferior con alturas superiores escalonadas (`270px`, `330px`, `390px`, `250px`, `320px`, `330px`).

---

## 06 · Capturas y archivos visuales
- **Referencia original:** [`referencias/astro_traffic_design.png`](file:///E:/WEBS/astropulse-agency/referencias/astro_traffic_design.png)
- **Activos originales generados a medida (`assets/custom_*.png`):**
  - `assets/custom_hero_astronaut.png`: Astronauta principal con banda carmesí.
  - `assets/custom_faq_astronaut.png`: Astronauta secundario mirando a órbita para FAQ y footer.
  - `assets/custom_spacex_orbital.png`: Satélite/nave en órbita terrestre baja estilo SpaceX con telemetría roja/blanca.
  - `assets/custom_astronaut_thumb.png`: Detalle cuadrado monocromo de guante espacial y control de misión.
  - `assets/custom_case_1.png`, `custom_case_2.png`, `custom_case_3.png`: 3 retratos editoriales originales para casos de estudio.
  - `assets/custom_crew_1.png` a `custom_crew_6.png`: 6 retratos originales monocromos/duotono para el equipo.

---

## 07 · Requisitos e instrucciones
- **Qué hacer:**
  - Replicar fielmente la ligereza y contraste tipográfico de `Inter` (`300 Light` + `400 Regular` + `500 Medium`) del diseño de Behance junto con la ingeniería visual de SpaceX (`Barlow Condensed` / `D-DIN`).
  - Jugar con múltiples tonos de gris (niebla `#ECECEE`, hormigón `#E2E3E7`, acero `#D5D7DE`, titanio `#767984`, grafito `#232630`, carbono `#14161D`) para dar profundidad y sofisticación.
  - Usar exclusivamente las nuevas imágenes originales generadas (`custom_*.png`) para astronautas, casos y equipo.
- **Qué evitar:**
  - Prohibido usar pesos `900 Black` gruesos que deformen la estética limpia de *Astro Traffic*.
  - Prohibido reutilizar los recortes antiguos del mockup de Behance.

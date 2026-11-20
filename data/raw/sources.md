# Sources: Carlos Julián Ramírez Gómez research corpus

Fetched 2026-11-19. All records in the JSON files come from the sources below. Raw responses are under `api/` (JSON) and `html/` (HTML, PDF, CSS).

## Identity and IDs

| URL | What it gave |
|---|---|
| https://scienti.minciencias.gov.co/ciencia-war/enRecursoHumanoBusqueda.do (POST `txtNamesRh=Carlos Julian Ramirez Gomez`) | CvLAC `cod_rh=0001396742` (RAMIREZ GOMEZ CARLOS JULIAN, Investigador Junior). Saved as `html/minciencias_busqueda_rh.html` |
| https://scienti.minciencias.gov.co/cvlac/visualizador/generarCurriculoCv.do?cod_rh=0001396742 | Full CvLAC: education, experience, research lines, awards, 28 articles, 2 books, 2 chapters, 2 divulgation books, 6 supervised theses, 3 thesis juries, 3 events, peer review. Google Scholar link (`BcgHqLYAAAAJ`) and ORCID link (`0000-0003-0099-0932`). Projects, software, patents and technical production sections are empty. Saved as `html/cvlac_0001396742.html`, parsed to `api/cvlac_parsed.json` |
| https://pub.orcid.org/v3.0/0000-0003-0099-0932/record and `/works` | Employment (U. Caldas, Desarrollo Rural), education (UNAL PhD, USP postdoc), keywords, 27 works |
| https://pub.orcid.org/v3.0/0000-0003-2669-8593/record and `/works` | Second ORCID account of the same person (ResearcherID E-2568-2016, 1 work: Acta Agronómica 2015) |
| https://api.openalex.org/authors?search=Carlos%20Julian%20Ramirez%20Gomez | Two author profiles: A5067927754 (24 works, ORCID 0000-0003-0099-0932) and A5102991225 (15 works, ORCID 0000-0003-2669-8593) |
| https://api.openalex.org/works/doi:10.22267/rcia.163301.2 | Revealed a third OpenAlex author profile A5040563903 (2 works, U. Antioquia, 2016) |
| https://api.openalex.org/works?filter=author.id:{A5067927754,A5102991225,A5040563903} | Works with abstracts (inverted index), venues, DOIs, topics, citation counts, funders (`api/oa_full/`) |
| https://www.datos.gov.co/resource/bqtm-4y2h.json?id_persona_pr=0001396742 | Minciencias recognition history: Investigador Junior in Convocatorias 781/2017 (U. Antioquia), 833/2018 (FAO), 894/2021. Trimmed to non-sensitive fields |
| https://www.datos.gov.co/resource/33dq-ab5a.json?id_persona_pd=0001396742 | 2 products endorsed in Conv. 894/2021 for groups COL0057811 (Innovación y Gestión Tecnológica, UNAL) and COL0057043 (DELTA, Lasallista) |
| https://www.datos.gov.co/resource/hrhc-c4wu.json | Group names, institutions and categories for those codes; list of U. Caldas groups in Conv. 894 |

## Universidad de Caldas pages

| URL | What it gave |
|---|---|
| https://www.ucaldas.edu.co/portal/facultad-de-ciencias-agropecuarias-realizo-la-primera-jornada-de-empleabilidad-para-estudiantes/ (WP REST post 75946) | "docente del Departamento Desarrollo Rural y Recursos Naturales", event coordinator (2023-05) |
| https://www.ucaldas.edu.co/portal/inscripciones-abiertas-para-la-especializacion-en-administracion-y-evaluacion-de-proyectos-agropecuarios-y-agroindustriales-2/ (post 85470) | Teacher in the Especialización en Administración y Evaluación de Proyectos Agropecuarios y Agroindustriales (2024-11) |
| https://www.ucaldas.edu.co/portal/wp-json/wp/v2/search?search=Ramírez Gómez | Index of posts; the 2 above are the only ones naming him |
| https://revistas.unal.edu.co/index.php/agrocol/article/view/125596 | Affiliation confirmed: Facultad de Ciencias Agropecuarias, Departamento de Desarrollo Rural y Recursos Naturales; no funding statement |
| https://investigacionesyposgrados.ucaldas.edu.co/wp-content/uploads/Resultados-Convocatoria-General-2023-Firmada.pdf | Funded project #12 "Innovación y ecosistema de emprendimiento rural…" (vigencia 2024). The PDF lists titles only; attribution to him is inferred (low confidence) |
| https://investigacionesyposgrados.ucaldas.edu.co/wp-content/uploads/Resultados-Convocatoria-Grupos-12-dic-2024-1.pdf and `Resultados-Convocatoria-Grupos-09-abr-2026.pdf` | U. Caldas group codes used to search GrupLAC (his cod_rh not found) |
| Other U. Caldas PDFs checked without hits: Resultados-Convocatoria-General-VIP-2024, Resultados-convocatoria-general, Resultados-Conv-Conjunta-2024, Publicacion-Resultados-Definitivos-Requisitos-Minimos-Conv-Gral-2025, semilleros 2023/2024/2025 | No mention of his name |

## Abstract and DOI enrichment

| URL | What it gave |
|---|---|
| https://api.crossref.org/works?query.bibliographic=… (several) | DOI 10.21897/rta.v20i1.746 for "Factores que influencian la adopción de tecnología de gestión en producción lechera" (Temas Agrarios) |
| https://api.crossref.org/works/10.21897/rta.v20i1.746 | Abstract (Crossref JATS) |
| https://api.semanticscholar.org/graph/v1/paper/search/match?query=… | DOI 10.31910/rudca.v25.n2.2022.2219 (UDCA 2022) and confirmation for 10.22267/rcia.163301.2; hit the rate limit after 2 calls |
| https://api.openalex.org/works/doi:10.31910/rudca.v25.n2.2022.2219 | Abstract for the UDCA 2022 article (not attached to his OpenAlex profiles) |

## Brand

| URL | What it gave |
|---|---|
| https://www.ucaldas.edu.co/portal/ | Header/footer logo PNGs, inline CSS: `--primary-color:#003B70`, `--secondary-color:#d5bb87`, faculty heading colors, Roboto font use |
| https://www.ucaldas.edu.co/portal/wp-content/litespeed/ucss/a80704751ea29cc67cde69673ae20996.css | Frequent colors #003b70, #d7b860; Work Sans |
| https://fonts.googleapis.com/css2?family=Work+Sans:wght@400;500;900&family=Roboto:wght@500;900 | Web fonts loaded by the site |
| https://www.ucaldas.edu.co/portal/wp-content/uploads/2024/09/1100-1612.pdf | Manual de Identidad Institucional 2024 (Acuerdo 23/2024): official hex/Pantone/CMYK palette, typography (Roboto, Roboto Condensed, Times New Roman wordmark), faculty colors; page 11 holds the vector supersigno and lockups used to cut the SVG/PNG logos |

## Gaps and blockers

- **Google Scholar blocked**: both curl and WebFetch were redirected to `google.com/sorry` (captcha). Only the profile ID `BcgHqLYAAAAJ` (from CvLAC) is known; no Scholar citations or work list.
- **Current research group not confirmed**: CvLAC lists no group membership. Searching the 34 U. Caldas GrupLAC pages linked from VIP result PDFs found no member with his `cod_rh`. GrupLAC `visualizagr.jsp?nro=` IDs are not derivable from COL codes, and the institution listing needs an unknown `codInst`. The groups known are from 2021 product endorsements (UNAL Medellín, Lasallista), not U. Caldas.
- **No research projects in CvLAC**: `projects.json` is built from the postdoctoral stays, consultancies and research activities in the CvLAC experience section, plus one U. Caldas 2023 funded project whose PI is not named in the source (low confidence).
- **No software, patents or technological products** in CvLAC or elsewhere.
- **Abstracts missing** for 8 records (books, chapters, FAO divulgation books, the 2006 Ideas Ambientales article, the 2004 Agronomía article, and the 2022 "Abordaje metodológico integrador" chapter).
- **Possible duplicate**: OpenAlex has a 2004 "Análisis económico del cultivo de la coca…" in *Agronomía (Manizales)*, while CvLAC has a 2006 article in *Ideas Ambientales* and a 2013 chapter with near-identical titles. They are kept separate (different venues/years); a person should check them.
- **OpenAlex-only records (medium confidence)**: 2026 UTP book "Dinamización de sistemas territoriales de innovación…", 2026 *Acta Universitaria* article on orange producers in Mexico, 2022 UdeA book "Innovación en la investigación agropecuaria" (likely the edited volume holding his 2022 chapter), 2020 Javeriana master's thesis, 2004 Agronomía coca article.
- **Logo SVGs**: cut from the manual PDF by viewBox (the rest of the page is still in the file, outside the view). Not render-checked, since no SVG renderer was available; the 300 dpi PNG cuts were checked visually.
- The Función Pública (SIGEP) record found by web search lists a different department ("Estudios Educativos"); it was not fetched or used.

Objective: research bank of Prof. Carlos Julián Ramírez Gómez (Universidad de Caldas): one .md per article/project/product, clusters, 3D constellation dashboard on GitHub Pages and an MCP server, with Universidad de Caldas branding. Based on github.com/LIAUNAL/bancoProyectosPapersLIA.
Branch: main (public repo github.com/amalvarezme/bancoJuli). Delivery: single feature branch, GitHub Pages from main/docs. Test runner: python -m unittest (tests/test_bank_db.py) + structural checks (counts, duplicates, JSON validity) + Playwright QA (tools/qa_constellation.py).

## Specs
- S1 Base: "toma como base el proyecto banco proyectos lia inal. vamos a realizar el mismo tipo de proyecto" (same pipeline: md files per item, bank.json, clusters, constellation, MCP).
- S2 Deploy: "con despliegue en girhub pages, mcp"
- S3 Branding: "ajustando a logos y estilo de presentacion de la Universidad de caldas"
- S4 Views: "presenvsndo constelacion 3d, cluster ides y demas paneles y secciones"
- S5 Subject: "para los trabajos del profesor carlos julian ramirez gomez de la universidad de caldas"
- S6 Sources: "busca google scholar, cvlac, paginas u caldas y lo que consideres para armar sus peoyectos, paper y demas artefactos de investigacion que consideres"

## Tasks
- T1 S5-S6 research corpus into data/raw (delegated explorer: external research) — done: 46 publications, 11 projects, products, profile, brand
- T2 S1 scaffold from base, rename banco-lia -> banco-juli (inline) — done, 16 unit tests pass
- T3 S6 dedupe + sources.json + taxonomy (inline) — done: tools/import_raw.py, data/taxonomy.md T01-T10
- T4 S1 structured summaries (delegated, 3 parallel writers: art_1 A001-A023, art_2 A024-A046, proj_1 P001-P011) — done: 57/57 ids, no extras; only empty field is productos_tecnologicos on P001/P003/P008/P010 (none reported)
- T5 S3-S4 U Caldas look: header, logos, colors, lead profile; build docs/ (inline) — done: N_CLUSTERS=6 named, MIN_YEAR=0, reported project->publication links, Perfil tab, U Caldas palette in dashboard + constellation
- T6 S2 MCP server banco-juli + tests (inline) — done: instructions rewritten, new researcher_profile tool (RED 2 errors -> GREEN 18/18), wheel builds (64 files)
- T7 S4 Playwright QA of constellation and views (inline) — done: qa_constellation 112/112 (QA_HEADLESS=1); qa_memory 6/7, fps 20 < 40 is the headless SwiftShader environment (no display here); screenshots of all 6 views x 2 widths reviewed
- T8 S2 GitHub repo amalvarezme/bancoJuli (public) + Pages from main/docs (inline) — pending

## Log
- L1 (2026-11-19) User request verbatim: "toma como base el proyecto banco proyectos lia inal. vamos a realizar el mismo tipo de proyecto con despliegue en girhub pages, mcp, ajustando a logos y estilo de presentacion de la Universidad de caldas, presenvsndo constelacion 3d, cluster ides y demas paneles y secciones para los trabajos del profesor carlos julian ramirez gomez de la universidad de caldas. busca google scholar, cvlac, paginas u caldas y lo que consideres para armar sus peoyectos, paper y demas artefactos de investigacion que consideres"
- L2 Base reviewed: tools/build_bank.py (TF-IDF+SVD+k-means, links, md writer, papersmith atlas + VIEWER_PATCHES), dashboard_template.html (tabs: constelacion, ideas, sistema, explorar, tiempo), banco_lia_mcp.py + bank_db.py (FTS5), bin/bancoLIA. Base Pages = main/docs (no workflow). Skeleton copied without LIA data/site.
- L3 (2026-11-19) User: "en amalvarezme y publico" -> repo github.com/amalvarezme/bancoJuli, public, Pages from main/docs.
- L4 Research: CvLAC cod_rh 0001396742, Scholar BcgHqLYAAAAJ (captcha, not fetched), ORCID 0000-0003-0099-0932, OpenAlex A5067927754/A5102991225/A5040563903; U. Caldas, Fac. Ciencias Agropecuarias, Depto. Desarrollo Rural y Recursos Naturales. Current U. Caldas research group not confirmed. P001 attribution low confidence. A043/A045/A046 coca items kept separate (different venues).
- L5 Brand: manual 2024 colors primary #003e70 (dark #00284d, light #045389), gold #d5bb87 (#efd9af, #b5a27c); Roboto/Roboto Condensed, Times New Roman wordmark. tools/assets now holds transparent + white PNG logos (horizontal, vertical, supersigno), favicon.png/.ico, apple-touch-icon.png.
- L6 Next: verify summaries; adapt build_bank.py (MIN_YEAR off, N_CLUSTERS~6, pub_type labels, explicit project->publication links from sources.json products, assets list, constellation title); restyle dashboard_template.html to U. Caldas (header logo, colors, profile panel with ids/lines/education, theses-supervised panel); MCP instructions; README; build, unittest, Playwright QA; create public repo amalvarezme/bancoJuli and enable Pages main/docs.
- L7 (2026-11-19) Resumed session. T4 verified. build_bank.py: hermes/ESTADOS removed, PUB_TYPES labels, explicit links from sources.json products (11 reported + 2 semantic), Spanish attribution notes in data/summaries/proj_1.jsonl (nota_atribucion) for P001/P005/P011, profile+products in bank.json. Dashboard restyled to U. Caldas (navy band, white horizontal logo, supersigno hero, vertical logo footer, Roboto), Perfil tab, product-type filter. Phone header hid department line so iframe starts at 356px (QA needs < 380). QA scripts gained QA_HEADLESS=1; qa_memory prints verdicts with flush. README rewritten. Brand manual PDF (7.1 MB) git-ignored.

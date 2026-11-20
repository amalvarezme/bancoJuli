# Banco Juli

Banco de publicaciones, proyectos e ideas de investigación del **Prof. Carlos Julián Ramírez Gómez**, Universidad de Caldas (Facultad de Ciencias Agropecuarias, Departamento de Desarrollo Rural y Recursos Naturales). **Tablero en línea: <https://amalvarezme.github.io/bancoJuli/>**, con constelación 3D, clústeres e ideas, sistema temático, buscador, línea de tiempo y perfil del investigador, más un [servidor MCP](#servidor-mcp) para redactar artículos y propuestas a partir de su trabajo previo.

Sigue el mismo esquema de [LIAUNAL/bancoProyectosPapersLIA](https://github.com/LIAUNAL/bancoProyectosPapersLIA), con la identidad visual de la Universidad de Caldas (manual de identidad 2024: azul `#003e70`, dorado `#d5bb87`, Roboto / Roboto Condensed y logos oficiales).

## Contenido

| Ruta | Qué contiene |
|------|--------------|
| `articulos/` | Una ficha `.md` por publicación (46: 36 artículos, 6 libros, 3 capítulos y 1 tesis, 2004–2026): aplicación, problema, propuesta o novedad, resultados, conclusiones, métodos, idea futura y relacionados |
| `proyectos/` | Una ficha `.md` por proyecto (11): lo anterior más rol, institución, financiador, productos, apropiación social, aliados y, si aplica, la nota de atribución |
| `docs/` | Sitio estático publicado en GitHub Pages: `index.html` (constelación 3D, clústeres e ideas, sistema temático, explorar, línea de tiempo, perfil), `constelacion.html` con el visor de papersmith-ai y `data/bank.json` |
| `data/bank.json` | Todos los registros con temas, clúster y relaciones, más el perfil y los productos no bibliográficos |
| `data/taxonomy.md` | Taxonomía de 10 temas (T01–T10): sistemas territoriales de innovación, redes, extensión rural, adopción tecnológica, asociatividad, cadenas de valor, emprendimiento rural, abastecimiento, economía agrícola y educación rural |
| `data/cluster_names.json` | Nombres de los 6 clústeres. Al regenerar, cada registro conserva su clúster y los nuevos van al centroide más cercano; `build_bank.py --recluster` reagrupa desde cero y obliga a revisar los nombres |
| `data/raw/` | Corpus de la investigación: `sources.json` (registros normalizados), `profile.json` (formación, experiencia, líneas, premios), `products.json` (tesis dirigidas, jurados, cursos, eventos), `brand.json` y `sources.md` con cada URL consultada |
| `data/summaries/*.jsonl` | Resúmenes estructurados en español de cada registro |
| `pyproject.toml`, `tools/banco_juli_mcp.py`, `tools/bank_db.py` | Paquete `banco-juli` con el servidor MCP y su índice SQLite FTS5 |
| `odd/tasks/banco-juli.md` | Especificación y bitácora del trabajo |

## Fuentes

- CvLAC `cod_rh=0001396742`, ORCID [`0000-0003-0099-0932`](https://orcid.org/0000-0003-0099-0932) (y la cuenta duplicada `0000-0003-2669-8593`), OpenAlex (tres perfiles del mismo autor) y Google Scholar `user=BcgHqLYAAAAJ` (solo como enlace: Scholar exige captcha).
- Portal de la Universidad de Caldas y Vicerrectoría de Investigaciones y Posgrados (resultados de convocatorias).
- Datos abiertos de Minciencias en datos.gov.co (categoría de investigador y grupos que avalaron sus productos).
- Abstracts: OpenAlex y Crossref (38 de 46 publicaciones). Las fichas sin abstract se redactaron desde el CvLAC (`fuente_resumen: cvlac`) o, de forma conservadora y sin cifras, desde el título (`fuente_resumen: titulo`).

El detalle de cada URL y lo que aportó está en `data/raw/sources.md`.

## Ver el tablero

En línea: **<https://amalvarezme.github.io/bancoJuli/>** (la constelación a pantalla completa está en [`constelacion.html`](https://amalvarezme.github.io/bancoJuli/constelacion.html)). GitHub Pages publica la carpeta `docs/` de la rama `main`; cada push que regenere `docs/` actualiza el sitio en uno o dos minutos.

En local:

```bash
bancoJuli ui              # http://localhost:8000, abre el navegador
bancoJuli ui 9000         # otro puerto
bancoJuli ui --no-open    # sin abrir el navegador
bancoJuli build           # regenera articulos/, proyectos/ y docs/
```

Instalación del comando (una vez): `ln -s "$PWD/bin/bancoJuli" ~/.local/bin/bancoJuli`. Sin el comando: `./tools/serve.sh [puerto]`. El servidor escucha solo en `127.0.0.1`.

### Vistas

- **Constelación 3D:** cada publicación (sol dorado) o proyecto (sol azul) es un sistema solar cuyos planetas son aplicación, problema, novedad, clúster, temas, resultados, conclusiones y productos. Clic ilumina el nodo con sus conexiones y abre la ficha con los 5 más relacionados; doble clic vuela hasta él; `constelacion.html?focus=A020` abre con un sistema seleccionado. Sin GPU para WebGL muestra una vista 2D (`?view=2d` la fuerza). En pantallas angostas la barra muestra solo el buscador, el filtro de clúster y **⋯ más**, que despliega los controles de cámara, rotación, nombres y la leyenda. Para ahorrar batería, el visor deja de dibujar 4 s después de la última interacción cuando no está rotando, y también cuando sale de la vista o se cambia de pestaña. En teléfonos y equipos modestos la rotación automática se detiene tras 20 s sin interacción.
- **Clústeres e ideas:** novedades recientes e ideas de trabajo futuro por clúster, con «Copiar base de redacción».
- **Sistema temático:** los temas como planetas con las publicaciones y proyectos en órbita, agrupables por tema o clúster.
- **Explorar:** buscador con filtros por tipo, tema, clúster, año y tipo de producto (artículo, libro, capítulo, tesis, proyecto).
- **Línea de tiempo:** producción por año apilada por clúster.
- **Perfil:** biografía, identificadores, formación, trayectoria, líneas, trabajos de grado dirigidos y jurados, docencia, eventos, reconocimientos y grupos.

### Pruebas visuales

Con el tablero levantado (Playwright con el Chrome del sistema; `QA_HEADLESS=1` sin pantalla):

```bash
uv run --no-project --with playwright --with pillow python tools/qa_constellation.py http://localhost:8000/
uv run --no-project --with playwright python tools/qa_memory.py http://localhost:8000/ [vueltas]
```

La primera verifica la constelación en 1440×900, 1280×720, 390×844 y 5760×3088 al 50 % (grafo centrado, hover, panel con top 5, controles, filtro, buscador y ausencia de errores de JavaScript). La segunda falla si la memoria o los listeners crecen al cambiar de pestaña o si la constelación oculta sigue consumiendo CPU.

## Servidor MCP

El servidor MCP (stdio) expone el banco como insumo para escribir artículos y propuestas. Busca sobre un índice SQLite FTS5 (BM25, sin tildes) que se regenera solo cuando cambia `data/bank.json`; el índice no se versiona.

Se instala desde GitHub con [uv](https://docs.astral.sh/uv/), sin clonar el repositorio:

```bash
uvx --from git+https://github.com/amalvarezme/bancoJuli banco-juli-mcp
```

El paquete trae el servidor, `data/bank.json` y las fichas; el índice queda en `~/.cache/banco-juli/bank.db`. Para tomar una versión nueva: `uvx --refresh --from git+https://github.com/amalvarezme/bancoJuli banco-juli-mcp`. Desde un clon local, `bancoJuli mcp` sirve los datos del clon y guarda el índice en `data/bank.db`.

| Herramienta | Para qué |
|---|---|
| `search_bank` | Búsqueda por texto con filtros `kind`, `cluster`, `topic`, `year_from`; `match` `any` (alguna palabra) o `all` (todas) |
| `get_item` | Registro completo y ficha Markdown de una publicación (`A###`) o proyecto (`P###`) |
| `related_items` | Enlaces proyecto → publicación y publicación → publicación, top 5 similares y mismo clúster |
| `lab_capabilities` | Aliados, financiadores, productos y métodos para un tema, con los ítems que los respaldan |
| `taxonomy` | Temas y clústeres con su número de ítems |
| `researcher_profile` | Perfil del investigador y productos no bibliográficos (tesis dirigidas, jurados, cursos, eventos) |
| `export_to_insumos` | Copia fichas Markdown a una carpeta existente, p. ej. `proposals/<run>/insumos/background` |

Registro en un proyecto (`.mcp.json`):

```json
"banco-juli": {
  "type": "stdio",
  "command": "uvx",
  "args": ["--from", "git+https://github.com/amalvarezme/bancoJuli", "banco-juli-mcp"]
}
```

Pruebas del índice: `python3 -m unittest discover -s tests`. Consulta rápida: `python3 tools/bank_db.py search "emprendimiento rural"`.

## Regenerar

```bash
uv run --no-project --with scikit-learn --with numpy python tools/build_bank.py
```

Los logos del sitio se generan con `uv run --no-project --with pillow python tools/web_logos.py` a partir de los originales en `tools/assets/src/`. `tools/import_raw.py` normaliza `data/raw/articles.json` y `data/raw/projects.json` en `data/raw/sources.json`. Los resúmenes viven en `data/summaries/*.jsonl`; edítelos ahí y regenere.

## Notas de calidad

- **P001** (emprendimiento rural, convocatoria U. Caldas 2023): el acta solo lista títulos; la atribución se infiere por coincidencia temática (confianza baja). **P005** y **P011** tienen confianza media. Cada ficha explica por qué.
- Las relaciones «produjo» (proyecto → publicación) provienen de los productos que reporta la fuente; las demás relaciones son similitud semántica, no vínculos declarados. Confírmelas antes de citarlas.
- No se confirmó su grupo actual de GrupLAC en la Universidad de Caldas; el perfil muestra los grupos que avalaron sus productos en convocatorias de Minciencias.
- Los tres registros sobre coca (A043, A045, A046) se mantienen separados: son publicaciones distintas en medios distintos.

El visor 3D en `vendor/papersmith/` proviene de LIAUNAL/papersmith-ai (Apache-2.0) y empaqueta three.js (MIT). Se conserva idéntico a upstream; la plantilla `tools/constellation_template.html` y los parches `VIEWER_PATCHES` de `tools/build_bank.py` se aplican al generar el sitio. Los logos son propiedad de la Universidad de Caldas.

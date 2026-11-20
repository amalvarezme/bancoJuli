"""Normalize the research corpus (data/raw/articles.json, data/raw/projects.json) into data/raw/sources.json.

Run: python3 tools/import_raw.py
Publications get stable ids A001.. (newest first, then title) and projects P001.. (newest start first).
The mapping from the research ids (pub-###) is kept in each record as "raw_id", so a project's
"products" list becomes explicit project -> publication links in tools/build_bank.py.
Re-running keeps existing ids: records already in sources.json (matched by raw_id) keep their id and new
records take the next free number.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data/raw"
OUT = RAW / "sources.json"

PUB_TYPES = {"journal": "Artículo en revista", "book": "Libro", "chapter": "Capítulo de libro",
             "thesis": "Tesis de maestría", "preprint": "Preprint", "conference": "Ponencia"}


def year_of(value):
    s = str(value or "")[:4]
    return s if s.isdigit() else ""


def assign(records, prefix, previous, sort_key):
    """Keep previous ids by raw_id; number the new ones after the highest previous id."""
    taken = {previous[r["raw_id"]] for r in records if r["raw_id"] in previous}
    nxt = max([int(i[1:]) for i in taken] or [0]) + 1
    for r in sorted(records, key=sort_key):
        if r["raw_id"] in previous:
            r["id"] = previous[r["raw_id"]]
        else:
            r["id"] = f"{prefix}{nxt:03d}"
            nxt += 1
    return sorted(records, key=lambda r: r["id"])


def main():
    arts = json.loads((RAW / "articles.json").read_text(encoding="utf-8"))
    projs = json.loads((RAW / "projects.json").read_text(encoding="utf-8"))
    prev = {}
    if OUT.exists():
        old = json.loads(OUT.read_text(encoding="utf-8"))
        prev = {r["raw_id"]: r["id"] for r in old["articles"] + old["projects"] if r.get("raw_id")}

    articles = []
    for a in arts:
        sources = a.get("sources") or []
        articles.append({
            "raw_id": a["id"], "src": sources[0] if sources else "openalex", "also_in": sources[1:],
            "pub_type": a.get("type") or "journal", "kind": PUB_TYPES.get(a.get("type"), a.get("type") or ""),
            "title": a["title"].strip(), "authors": a.get("authors") or [], "journal": a.get("venue") or "",
            "year": year_of(a.get("year")), "doi": (a.get("doi") or "").lower() or None,
            "url": a.get("url") or a.get("oa_url") or "", "abstract": a.get("abstract") or "",
            "abstract_source": a.get("abstract_source") or "", "cited_by": a.get("cited_by_count"),
            "language": a.get("language") or "", "confidence": a.get("confidence") or "",
            "keywords_source": (a.get("oa_keywords") or []) + (a.get("topics") or [])})
    articles = assign(articles, "A", prev, lambda r: (-int(r["year"] or 0), r["title"].lower()))
    raw2id = {r["raw_id"]: r["id"] for r in articles}

    projects = []
    for k, p in enumerate(projs):
        raw_id = p.get("id") or f"proj-{k + 1:03d}"
        projects.append({
            "raw_id": raw_id, "src": p.get("source") or "cvlac", "type": p.get("kind") or "",
            "name": p["title"].strip(), "start": year_of(p.get("start")), "end": year_of(p.get("end")),
            "start_raw": p.get("start") or "", "end_raw": p.get("end") or "",
            "role": p.get("role") or "", "financiador": p.get("funder") or "",
            "institution": p.get("institution") or "", "partners": p.get("partners") or [],
            "summary": p.get("summary") or "", "url": p.get("url") or "", "confidence": p.get("confidence") or "",
            "attribution_note": p.get("attribution_note") or "",
            "products": [raw2id[x] for x in p.get("products") or [] if x in raw2id],
            "related_by_topic": [raw2id[x] for x in p.get("related_products_by_topic") or [] if x in raw2id]})
    projects = assign(projects, "P", prev,
                      lambda r: (-int(r["start"] or r["end"] or 0), r["name"].lower()))
    OUT.write_text(json.dumps({"articles": articles, "projects": projects}, ensure_ascii=False, indent=1),
                   encoding="utf-8")
    print(f"articles={len(articles)} projects={len(projects)} -> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Regenera indice-rapido.json en la raiz del kit a partir de estilos.json,
paletas.json y fonts.json. Correr desde la raiz: python3 recursos/generar-indice-rapido.py
Hay que volver a correrlo cada vez que cambia alguno de esos tres JSON."""
import json, os, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def load(p): return json.load(open(os.path.join(ROOT, p), encoding="utf-8"))

est = load("estilos/estilos.json")
pal = load("paletas/paletas.json")
fon = load("tipografias/fonts.json")

MD_FAMILIA = {"saas-producto": "saas-producto", "expresiva": "expresivas", "cultural": "culturales",
              "organica": "organicas", "editorial": "editoriales", "monocroma": "monocromas"}
ROLES = ["bg", "surface", "border", "text", "muted", "accent", "accent_foreground"]
def hexes(modo):
    t = modo.get("tokens", {})
    out = {}
    for r in ROLES:
        v = t.get(r) or t.get(r.replace("_", "-"))
        if isinstance(v, dict) and "hex" in v:
            out[r] = v["hex"]
    return out

idx = {
    "meta": {
        "descripcion": "Índice compacto del kit Designweb para elegir sin abrir los JSON grandes. "
                       "Es el único archivo del kit que la skill frontend-design lee entero en modo restyling.",
        "generado": datetime.date.today().isoformat(),
        "generador": "recursos/generar-indice-rapido.py",
        "fuentes": ["estilos/estilos.json", "paletas/paletas.json", "tipografias/fonts.json"],
        "como_seguir": {
            "paleta_completa": "jq '.paletas[] | select(.slug==\"<slug>\")' paletas/paletas.json, o la sección ## del archivo md_familia",
            "fuente_completa": "jq '.fuentes[] | select(.id==\"<id>\")' tipografias/fonts.json",
            "estilo_completo": "estilos/<slug>.md",
        },
        "totales": {},
    },
    "estilos": [
        {k: e.get(k) for k in ("slug", "nombre", "mood", "mejor_para", "evitar_en", "fuentes_recomendadas")}
        for e in est["estilos"]
    ],
    "por_rubro": est.get("por_rubro", []),
    "paletas": [],
    "fuentes": [
        {k: f.get(k) for k in ("id", "nombre", "categoria", "licencia", "mejor_uso", "pareja_recomendada")}
        for f in fon["fuentes"]
    ],
}
for p in pal["paletas"]:
    m = p.get("modos", {})
    idx["paletas"].append({
        "slug": p["slug"], "familia": p.get("familia"), "mood": p.get("mood"),
        "mejor_para": p.get("mejor_para"), "evitar_en": p.get("evitar_en"),
        "estilos": p.get("estilos"),
        "md_familia": f"paletas/{MD_FAMILIA.get(p.get('familia'), p.get('familia'))}.md",
        "claro": hexes(m.get("light", {})), "oscuro": hexes(m.get("dark", {})),
    })
idx["meta"]["totales"] = {k: len(idx[k]) for k in ("estilos", "por_rubro", "paletas", "fuentes")}
with open(os.path.join(ROOT, "indice-rapido.json"), "w", encoding="utf-8") as fh:
    # Un ítem por línea: compacto y a la vez buscable con rg por slug.
    c = lambda o: json.dumps(o, ensure_ascii=False, separators=(",", ":"))
    parts = ['  "meta": ' + json.dumps(idx["meta"], ensure_ascii=False, indent=2).replace("\n", "\n  ")]
    for k in ("estilos", "por_rubro", "paletas", "fuentes"):
        parts.append(f'  "{k}": [\n' + ",\n".join("    " + c(x) for x in idx[k]) + "\n  ]")
    fh.write("{\n" + ",\n".join(parts) + "\n}\n")
print(idx["meta"]["totales"], os.path.getsize(os.path.join(ROOT, "indice-rapido.json")), "bytes")

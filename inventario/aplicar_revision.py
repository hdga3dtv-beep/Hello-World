#!/usr/bin/env python3
"""Aplica el resultado de la verificación cruzada a datos/.

Entrada (JSON en la ruta pasada como argumento):
  {
    "corrections_dir": "<carpeta con <lote>.json de correcciones>",
    "accepted": [{"chunk": "<lote>", "index": 0}],            # contrastadas y aceptadas
    "new_files": ["<ruta a 11-complementos-*.json>"],
    "new_corrections": {"<ruta complemento>": "<ruta correcciones>"},
    "new_min_confidence": "alta" | "media",   # qué correcciones de los nuevos aplicar
    "duplicates": [{"keep_id": "...", "remove_ids": ["..."]}]
  }

Las correcciones reemplazan el campo completo indicado. De los duplicados se
borra el elemento sobrante y sus nombres/alias/tiendas pasan al que se queda.

Uso: python3 inventario/aplicar_revision.py plan.json
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "datos"
FIELDS = {"pinout", "packages", "specs", "common_values", "mounting", "category",
          "subcategory", "name", "description", "notes", "schematic_symbol"}


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def save(path, data):
    Path(path).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def apply_correction(items_by_id, corr, log):
    item = items_by_id.get(corr["id"])
    if item is None:
        log.append(f"omitida (id no existe): {corr['id']}")
        return False
    if corr["field"] not in FIELDS:
        log.append(f"omitida (campo no permitido '{corr['field']}'): {corr['id']}")
        return False
    value = corr["new_value"]
    if isinstance(value, str) and corr["field"] in {"pinout", "packages", "specs", "common_values"}:
        value = json.loads(value)
    item[corr["field"]] = value
    log.append(f"{corr['id']}.{corr['field']}: {corr.get('problem', '')}")
    return True


def main():
    plan = load(sys.argv[1])
    files = {p.name: load(p) for p in sorted(DATA_DIR.glob("*.json"))}
    items_by_id = {i["id"]: i for d in files.values() for i in d["items"]}
    log = []

    corr_dir = Path(plan["corrections_dir"])
    cache = {}
    for acc in plan.get("accepted", []):
        chunk = acc["chunk"]
        if chunk not in cache:
            cache[chunk] = {c["index"]: c for c in load(corr_dir / f"{chunk}.json")}
        corr = cache[chunk].get(acc["index"])
        if corr is None:
            log.append(f"omitida (índice {acc['index']} no está en {chunk})")
            continue
        apply_correction(items_by_id, corr, log)

    levels = {"alta", "media"} if plan.get("new_min_confidence") == "media" else {"alta"}
    for new_file in plan.get("new_files", []):
        data = load(new_file)
        corr_file = plan.get("new_corrections", {}).get(new_file)
        if corr_file and Path(corr_file).exists():
            new_by_id = {i["id"]: i for i in data["items"]}
            for corr in load(corr_file):
                if corr.get("confidence") in levels:
                    apply_correction(new_by_id, corr, log)
        fresh = [i for i in data["items"] if i["id"] not in items_by_id]
        skipped = len(data["items"]) - len(fresh)
        if skipped:
            log.append(f"{Path(new_file).name}: {skipped} ids ya existían, omitidos")
        data["items"] = fresh
        files[Path(new_file).name] = data
        items_by_id.update({i["id"]: i for i in fresh})
        log.append(f"{Path(new_file).name}: +{len(fresh)} elementos")

    removed = set()
    for dup in plan.get("duplicates", []):
        keep = items_by_id.get(dup["keep_id"])
        if keep is None:
            log.append(f"duplicado omitido (keep no existe): {dup['keep_id']}")
            continue
        for rid in dup["remove_ids"]:
            gone = items_by_id.get(rid)
            if gone is None or rid == dup["keep_id"]:
                continue
            for extra in [gone["name"], *gone.get("aliases", [])]:
                if extra not in keep.setdefault("aliases", []) and extra != keep["name"]:
                    keep["aliases"].append(extra)
            for store in gone.get("stores", []):
                if store not in keep.setdefault("stores", []):
                    keep["stores"].append(store)
            removed.add(rid)
            log.append(f"duplicado: {rid} → {dup['keep_id']}")

    for name, data in files.items():
        data["items"] = [i for i in data["items"] if i["id"] not in removed]
        save(DATA_DIR / name, data)

    print("\n".join(log))
    print(f"\n{len(log)} cambios registrados")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Une los archivos de datos/ en el inventario final.

Genera:
  componentes.json  - todos los componentes en un solo archivo (para la app)
  componentes.csv   - vista plana para hoja de cálculo
  INVENTARIO.md     - catálogo legible por categoría

Uso: python3 inventario/build.py
"""
import csv
import json
import sys
from collections import Counter, OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "datos"

CATEGORIES = OrderedDict([
    ("resistores", "Resistores, potenciómetros y afines"),
    ("capacitores", "Capacitores"),
    ("inductivos_y_frecuencia", "Inductores, transformadores y cristales"),
    ("proteccion", "Protección (fusibles, varistores, TVS)"),
    ("semiconductores_discretos", "Semiconductores discretos (diodos, transistores, tiristores)"),
    ("optoelectronica", "Optoelectrónica (LEDs, optoacopladores, displays de LED)"),
    ("circuitos_integrados", "Circuitos integrados"),
    ("placas_desarrollo", "Placas de desarrollo (Arduino, ESP, Raspberry Pi) y programadores"),
    ("modulos_comunicacion", "Módulos de comunicación"),
    ("sensores", "Sensores"),
    ("displays", "Displays y pantallas"),
    ("actuadores_y_audio", "Actuadores y audio (motores, servos, buzzers, bocinas)"),
    ("modulos_potencia", "Módulos de potencia y control"),
    ("modulos_varios", "Módulos varios (RTC, SD, audio, ADC...)"),
    ("electromecanicos", "Electromecánicos (botones, interruptores, relevadores)"),
    ("conectores", "Conectores, bases y portapilas"),
    ("cables", "Cables y alambres"),
    ("mecanicos", "Mecánicos (disipadores, separadores, gabinetes)"),
    ("materiales_pcb", "Materiales para fabricar PCB"),
    ("soldadura_y_consumibles", "Soldadura y consumibles"),
    ("herramientas", "Herramientas e instrumentos"),
    ("energia", "Energía (pilas, baterías, fuentes)"),
])

MOUNTING = {"THT", "SMD", "THT/SMD", "modulo", "panel", "n/a"}
POPULARITY = ["muy_alta", "alta", "media"]
REQUIRED = ["id", "name", "category", "description", "mounting"]
DEFAULTS = OrderedDict([
    ("id", None), ("name", None), ("aliases", []), ("category", None),
    ("subcategory", None), ("description", ""), ("mounting", "n/a"),
    ("packages", []), ("pinout", []), ("common_values", []), ("specs", {}),
    ("schematic_symbol", "ninguno"), ("typical_uses", []), ("stores", []),
    ("popularity", "media"), ("price_mxn_approx", None), ("notes", ""),
])


def normalize(item):
    out = OrderedDict()
    for key, default in DEFAULTS.items():
        value = item.get(key, default)
        if value is None and isinstance(default, (list, dict)):
            value = type(default)()
        out[key] = value
    # Conserva campos extra que un grupo haya agregado.
    for key, value in item.items():
        if key not in out:
            out[key] = value
    return out


def package_summary(pkg):
    parts = []
    if pkg.get("pins"):
        parts.append(f"{pkg['pins']}p")
    if pkg.get("pitch_mm"):
        parts.append(f"{pkg['pitch_mm']} mm")
    if pkg.get("row_spacing_mm"):
        parts.append(f"filas {pkg['row_spacing_mm']} mm")
    name = pkg.get("name") or "?"
    return f"{name} ({', '.join(parts)})" if parts else name


def md_escape(text):
    return str(text).replace("|", "\\|").replace("\n", " ")


def truncate(values, limit=8):
    values = [str(v) for v in values]
    if len(values) > limit:
        return ", ".join(values[:limit]) + f", … (+{len(values) - limit})"
    return ", ".join(values)


def main():
    errors, warnings = [], []
    items, sources, groups = [], [], []
    seen = {}

    files = sorted(DATA_DIR.glob("*.json"))
    if not files:
        sys.exit(f"No hay archivos en {DATA_DIR}")

    for path in files:
        data = json.loads(path.read_text(encoding="utf-8"))
        groups.append(data.get("group", path.stem))
        sources.extend(data.get("sources", []))
        for raw in data["items"]:
            where = f"{path.name}:{raw.get('id')}"
            for key in REQUIRED:
                if not raw.get(key):
                    errors.append(f"{where}: falta '{key}'")
            if raw.get("category") not in CATEGORIES:
                errors.append(f"{where}: categoría desconocida '{raw.get('category')}'")
            if raw.get("mounting") not in MOUNTING:
                errors.append(f"{where}: mounting inválido '{raw.get('mounting')}'")
            if raw.get("popularity", "media") not in POPULARITY:
                warnings.append(f"{where}: popularity '{raw.get('popularity')}' → 'media'")
                raw["popularity"] = "media"
            if raw.get("id") in seen:
                errors.append(f"{where}: id duplicado (ya está en {seen[raw['id']]})")
            seen[raw.get("id")] = path.name
            item = normalize(raw)
            item["group"] = data.get("group", path.stem)
            items.append(item)

    for w in warnings:
        print("aviso:", w)
    if errors:
        for e in errors:
            print("error:", e)
        sys.exit(f"{len(errors)} errores; no se generó nada.")

    cat_order = list(CATEGORIES)
    items.sort(key=lambda i: (cat_order.index(i["category"]), i["subcategory"] or "",
                              POPULARITY.index(i["popularity"]), i["name"].lower()))
    by_cat = Counter(i["category"] for i in items)

    combined = OrderedDict([
        ("schema_version", 1),
        ("description", "Inventario de componentes electrónicos comunes en tiendas de "
                        "México/Latinoamérica (Steren, AG Electrónica, UNIT Electronics, etc.) "
                        "para una app de diseño de pistas/PCB caseras."),
        ("total_items", len(items)),
        ("categories", [OrderedDict([("id", c), ("name", n), ("count", by_cat.get(c, 0))])
                        for c, n in CATEGORIES.items()]),
        ("items", items),
        ("sources", sorted(set(sources))),
    ])
    (ROOT / "componentes.json").write_text(
        json.dumps(combined, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    with open(ROOT / "componentes.csv", "w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(["id", "nombre", "categoria", "subcategoria", "montaje",
                         "encapsulados", "valores_comunes", "simbolo", "popularidad",
                         "tiendas", "precio_mxn_aprox", "descripcion"])
        for i in items:
            writer.writerow([
                i["id"], i["name"], i["category"], i["subcategory"] or "", i["mounting"],
                "; ".join(package_summary(p) for p in i["packages"]),
                "; ".join(str(v) for v in i["common_values"]),
                i["schematic_symbol"], i["popularity"], "; ".join(i["stores"]),
                i["price_mxn_approx"] or "", i["description"],
            ])

    lines = [
        "# Inventario de componentes electrónicos",
        "",
        "Catálogo generado por `build.py` a partir de `datos/`. No editar a mano.",
        "",
        f"**Total: {len(items)} componentes** en {sum(1 for c in CATEGORIES if by_cat.get(c))} categorías.",
        "",
        "| Categoría | Elementos |",
        "|---|---:|",
    ]
    for c, n in CATEGORIES.items():
        if by_cat.get(c):
            lines.append(f"| [{n}](#{c}) | {by_cat[c]} |")
    lines.append("")

    for c, n in CATEGORIES.items():
        cat_items = [i for i in items if i["category"] == c]
        if not cat_items:
            continue
        lines += [f'<a id="{c}"></a>', f"## {n}", "",
                  "| Componente | Montaje | Encapsulado / huella | Valores o variantes comunes | Popularidad |",
                  "|---|---|---|---|---|"]
        for i in cat_items:
            pkgs = "; ".join(package_summary(p) for p in i["packages"]) or "—"
            vals = truncate(i["common_values"]) or "—"
            lines.append(
                f"| **{md_escape(i['name'])}**<br><sub>`{i['id']}`</sub> | {i['mounting']} | "
                f"{md_escape(pkgs)} | {md_escape(vals)} | {i['popularity'].replace('_', ' ')} |")
        lines.append("")

    (ROOT / "INVENTARIO.md").write_text("\n".join(lines), encoding="utf-8")

    print(f"{len(items)} componentes de {len(files)} archivos")
    for c in CATEGORIES:
        if by_cat.get(c):
            print(f"  {c}: {by_cat[c]}")


if __name__ == "__main__":
    main()

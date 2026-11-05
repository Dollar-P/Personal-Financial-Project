"""Check notebook structure, syntax, provenance and split-cell order without data."""
import ast
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    seen = {}
    code_count = 0
    notebooks = sorted((ROOT / "notebooks").rglob("*.ipynb"))
    for path in notebooks:
        notebook = json.loads(path.read_text())
        assert notebook["nbformat"] == 4
        ids = set()
        for cell in notebook["cells"]:
            assert cell["id"] not in ids, (path, cell["id"])
            ids.add(cell["id"])
            source = "".join(cell["source"])
            if cell["cell_type"] == "code":
                assert isinstance(cell.get("outputs"), list), path
                count = cell.get("execution_count")
                assert count is None or isinstance(count, int), path
                ast.parse(source, filename=f"{path}:{cell['id']}")
                code_count += 1
            origin = cell["metadata"].get("tradinguni_source")
            if origin:
                key = (origin["notebook"], origin["cell"])
                assert key not in seen, key
                seen[key] = (path.relative_to(ROOT).as_posix(), cell["id"], hashlib.sha256(source.encode()).hexdigest())
    provenance = json.loads((ROOT / "docs/source_map.json").read_text())
    assert len(provenance["cells"]) == len(seen)
    for entry in provenance["cells"]:
        assert seen[(entry["source"], entry["cell"])] == (entry["destination"], entry["cell_id"], entry["curated_sha256"])
    for name, paths in json.loads((ROOT / "notebook_series.json").read_text()).items():
        indices = []
        for path in paths:
            for cell in json.loads((ROOT / path).read_text())["cells"]:
                origin = cell["metadata"].get("tradinguni_source")
                if origin:
                    indices.append(origin["cell"])
        assert indices == list(range(len(indices))), name
    print(f"PASS: {len(notebooks)} notebooks, {code_count} code cells, {len(seen)} original cells; syntax, output structure, hashes and series order.")


if __name__ == "__main__":
    main()

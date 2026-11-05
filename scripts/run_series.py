"""Compose split notebooks into their original cell order, optionally execute."""
import argparse
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def compose(series):
    manifest = json.loads((ROOT / "notebook_series.json").read_text())
    paths = manifest[series]
    result = None
    for relative in paths:
        notebook = json.loads((ROOT / relative).read_text())
        if result is None:
            result = copy.deepcopy(notebook)
            result["cells"] = []
        result["cells"].extend(notebook["cells"])
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("series", choices=["microstructure", "barrier_hit", "all_for_one"])
    parser.add_argument("--export", required=True, type=Path, help="Destination notebook; relative to the repository root.")
    parser.add_argument("--execute", action="store_true", help="Execute research in one fresh kernel; requires local data and nbclient.")
    parser.add_argument("--timeout", type=int, default=3600, help="Per-cell execution timeout in seconds.")
    args = parser.parse_args()
    dest = args.export if args.export.is_absolute() else ROOT / args.export
    # Exported notebooks can be large and contain results. Keep them outside source notebooks.
    if dest.resolve().is_relative_to((ROOT / "notebooks").resolve()):
        parser.error("Export into outputs/ or a separate directory, not notebooks/.")
    notebook = compose(args.series)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(notebook, ensure_ascii=False, indent=1) + "\n")
    print(f"Composed {len(notebook['cells'])} cells into {dest}")
    if args.execute:
        import nbformat
        from nbclient import NotebookClient
        notebook = nbformat.from_dict(notebook)
        try:
            NotebookClient(notebook, timeout=args.timeout, kernel_name="python3",
                           resources={"metadata": {"path": str(ROOT)}}).execute()
        finally:
            # Keep failure context locally as well as successful outputs.
            nbformat.write(notebook, dest)
        print("Execution completed.")


if __name__ == "__main__":
    main()

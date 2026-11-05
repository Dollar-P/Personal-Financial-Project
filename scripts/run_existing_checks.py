"""Run the six existing synthetic checks from All for One, without market data."""
import ast
import json
import sys
import types
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


def main():
    paths = json.loads((ROOT / "notebook_series.json").read_text())["all_for_one"]
    module = types.ModuleType("tradinguni_existing_checks")
    sys.modules[module.__name__] = module
    scope = module.__dict__
    tests = []
    for relative in paths:
        for cell in json.loads((ROOT / relative).read_text())["cells"]:
            origin = cell["metadata"].get("tradinguni_source")
            if cell["cell_type"] != "code" or not origin:
                continue
            index = origin["cell"]
            source = "".join(cell["source"])
            if 5 <= index < 246:
                # Definitions/configuration only: data loading and experiment runners excluded.
                exec(compile(source, f"{relative}:original-cell-{index}", "exec"), scope)
            elif index in (291, 292):
                # These later cells define checks but require no research results.
                tree = ast.parse(source)
                assert all(isinstance(node, ast.FunctionDef) for node in tree.body)
                exec(compile(source, f"{relative}:original-cell-{index}", "exec"), scope)
    for name in ["test_basic_asof_alignment", "test_state_expiration", "test_keltner_signal_logic",
                 "test_regime_filter_logic", "test_walk_forward_fold_generation", "test_candidate_selection"]:
        scope[name]()
        tests.append(name)
        print(f"PASS: {name}")
    print(f"{len(tests)} existing synthetic checks passed. This does not validate historical performance.")


if __name__ == "__main__":
    main()

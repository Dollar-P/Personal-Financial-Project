"""Local paths for the curated research notebooks."""
import os
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
DATA_ROOT = Path(os.environ.get("TRADINGUNI_DATA_DIR", str(REPO_ROOT / "data"))).expanduser().resolve()
OUTPUT_ROOT = Path(os.environ.get("TRADINGUNI_OUTPUT_DIR", str(REPO_ROOT / "outputs"))).expanduser().resolve()


def data_path(relative):
    """Resolve an input or intermediate under the private local data tree."""
    return DATA_ROOT / relative


def output_path(relative):
    """Resolve a local generated artifact; create its parent directory."""
    path = OUTPUT_ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    return path

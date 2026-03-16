"""Vision helpers reserved for the YOLO training and inference phases."""

from __future__ import annotations

from pathlib import Path
from typing import Any


def load_model(model_path: str | Path = "modelo/best.pt") -> Any:
    """Lazy-load YOLO so Day 1 diagnostics work without the full CV stack."""

    model_path = Path(model_path)
    if not model_path.exists():
        raise FileNotFoundError(
            f"Model file not found at {model_path}. Train or export the model first."
        )

    try:
        from ultralytics import YOLO
    except ImportError as exc:
        raise RuntimeError(
            "Ultralytics is not installed. Run `python3 -m pip install -r requirements.txt`."
        ) from exc

    return YOLO(str(model_path))


def detect(frame: Any, model_path: str | Path = "modelo/best.pt", confidence: float = 0.25) -> Any:
    """Run inference on a frame and return the raw Ultralytics result."""

    model = load_model(model_path)
    return model(frame, conf=confidence)


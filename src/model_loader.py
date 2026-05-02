import pickle
import threading
from pathlib import Path
from src.config import MODEL_DIR
from src.logger import logger


class _ModelLoader:
    def __init__(self) -> None:
        self._model = None
        self._lock = threading.Lock()

    def load(self, model_path: Path = MODEL_DIR):
        if self._model is not None:
            return self._model

        with self._lock:
            if self._model is not None:
                return self._model

            if not Path(model_path).exists():
                msg = f"Model file not found: {model_path}"
                logger.error(msg)
                raise FileNotFoundError(msg)

            try:
                with open(model_path, "rb") as fh:
                    self._model = pickle.load(fh)
                logger.info(f"Model loaded from {model_path}")
            except Exception as e:
                logger.error(f"Failed to deserialise model: {e}")
                raise RuntimeError(f"Model loading failed: {e}") from e

        return self._model


_loader = _ModelLoader()


def get_model():
    return _loader.load()

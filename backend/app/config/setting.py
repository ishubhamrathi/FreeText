from pathlib import Path


# =========================
# PROJECT PATHS
# =========================

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATA_DIR = BASE_DIR / "data"

RECORDINGS_DIR = DATA_DIR / "recordings"

MODELS_DIR = BASE_DIR / "models"


# =========================
# AUDIO SETTINGS
# =========================

SAMPLE_RATE = 16000

CHANNELS = 1

DEFAULT_RECORD_DURATION = 5


# =========================
# WHISPER SETTINGS
# =========================

WHISPER_MODEL_NAME = "base"

WHISPER_MODEL_PATH = (
    MODELS_DIR
    / "whisper"
    / WHISPER_MODEL_NAME
)

WHISPER_DEVICE = "cpu"

WHISPER_COMPUTE_TYPE = "int8"


# =========================
# APP SETTINGS
# =========================

APP_NAME = "FreeText"

SUPPORTED_LANGUAGES = [
    "en",
    "hi"
]
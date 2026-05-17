from pathlib import Path


# =========================
# PROJECT PATHS
# =========================

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATA_DIR = BASE_DIR / "data"

RECORDINGS_DIR = DATA_DIR / "recordings"

MODELS_DIR = BASE_DIR / "models"

OLLAMA_MODEL = "qwen3:4b"

# =========================
# AUDIO SETTINGS
# =========================

SAMPLE_RATE = 16000

CHANNELS = 1

DEFAULT_RECORD_DURATION = 5


# =========================
# WHISPER SETTINGS
# =========================

WHISPER_MODEL_NAME = "small"

WHISPER_MODEL_PATH = (
    MODELS_DIR
    / "whisper"
    / WHISPER_MODEL_NAME
)

WHISPER_DEVICE = "cuda"

WHISPER_COMPUTE_TYPE = "float16"


# =========================
# APP SETTINGS
# =========================

APP_NAME = "FreeText"

SUPPORTED_LANGUAGES = [
    "en",
    "hi"
]

CLEANUP_PROVIDER = "languagetool"

OLLAMA_MODEL = "qwen3:4b"

OPENAI_API_KEY = ""

DEFAULT_PROFILE = "casual"

PUSH_TO_TALK_KEYS = {
    "Key.cmd",
    "Key.alt_l"
}

CLEANUP_MODE = "local"
# local
# ollama
# openai
# gemini
# claude

LOCAL_AI_PROVIDER = "ollama"

LOCAL_ENGLISH_PROVIDER = "languagetool"

LOCAL_MULTILINGUAL_PROVIDER = "ollama"

LIVE_CHUNK_SECONDS = 4

LIVE_OVERLAP_SECONDS = 1

LIVE_STRIDE_SECONDS = (
    LIVE_CHUNK_SECONDS
    - LIVE_OVERLAP_SECONDS
)
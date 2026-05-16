from faster_whisper import WhisperModel

from config.settings import (
    WHISPER_MODEL_PATH,
    WHISPER_DEVICE,
    WHISPER_COMPUTE_TYPE
)


model = WhisperModel(
    str(WHISPER_MODEL_PATH),
    device=WHISPER_DEVICE,
    compute_type=WHISPER_COMPUTE_TYPE
)


def transcribe_audio(audio_path):
    segments, info = model.transcribe(audio_path)

    print(f"Detected language: {info.language}")

    transcript = ""

    for segment in segments:
        transcript += segment.text + " "

    return transcript.strip()
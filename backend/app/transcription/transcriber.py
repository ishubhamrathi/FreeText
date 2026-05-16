import time

from faster_whisper import WhisperModel

from config.settings import (
    WHISPER_MODEL_PATH,
    WHISPER_DEVICE,
    WHISPER_COMPUTE_TYPE
)

from models.transcription_result import (
    TranscriptionResult
)


model = WhisperModel(
    str(WHISPER_MODEL_PATH),
    device=WHISPER_DEVICE,
    compute_type=WHISPER_COMPUTE_TYPE
)


def transcribe_audio(audio_path):
    start_time = time.time()

    segments, info = model.transcribe(
        audio_path,
        beam_size=5
    )

    transcript = ""

    for segment in segments:
        transcript += segment.text + " "

    processing_time = round(
        time.time() - start_time,
        2
    )

    return TranscriptionResult(
        text=transcript.strip(),
        language=info.language,
        processing_time=processing_time
    )
import time

from faster_whisper import WhisperModel

from config.settings import (
    WHISPER_MODEL_PATH,
    WHISPER_DEVICE,
    WHISPER_COMPUTE_TYPE
)

from transcription.result import (
    SegmentResult,
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
        beam_size=1,
        vad_filter=True,
        condition_on_previous_text=True
    )

    segments = list(segments)

    transcript_parts = []

    segment_results = []

    for segment in segments:

        text = segment.text.strip()

        transcript_parts.append(
            text
        )

        segment_results.append(
            SegmentResult(
                text=text,
                start=segment.start,
                end=segment.end
            )
        )

    processing_time = round(
        time.time() - start_time,
        2
    )

    return TranscriptionResult(
        text=" ".join(
            transcript_parts
        ),
        language=info.language,
        processing_time=processing_time,
        segments=segment_results
    )

from audio.recorder import record_audio

from transcription.transcriber import (
    transcribe_audio
)

from typing_service.service import TypingService


class PipelineService:

    def __init__(self):
        self.typing_service = TypingService()

    def execute(self):
        audio_file = record_audio()

        result = transcribe_audio(audio_file)

        return result

    def execute_and_type(self):
        result = self.execute()

        self.typing_service.type_text(
            result.text
        )

        return result
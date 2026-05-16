from audio.recorder import record_audio

from transcription.transcriber import (
    transcribe_audio
)

from typing_service.service import TypingService

from ai.cleanup_service import (
    CleanupService
)


class PipelineService:

    def __init__(self):
        self.typing_service = TypingService()

        self.cleanup_service = (
            CleanupService()
        )

    def execute(self):
        audio_file = record_audio()

        transcription_result = (
            transcribe_audio(audio_file)
        )

        cleaned_text = (
            self.cleanup_service.cleanup_text(
                transcription_result.text
            )
        )

        transcription_result.text = (
            cleaned_text
        )

        return transcription_result

    def execute_and_type(self):
        result = self.execute()

        self.typing_service.type_text(
            result.text
        )

        return result
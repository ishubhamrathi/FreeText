from audio.recorder import record_audio

from transcription.transcriber import (
    transcribe_audio
)


class PipelineService:

    def execute(self):
        audio_file = record_audio()

        result = transcribe_audio(audio_file)

        return result
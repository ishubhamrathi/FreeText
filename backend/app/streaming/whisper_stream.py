from streaming.token import (
    TranscriptToken
)

from transcription.transcriber import (
    transcribe_audio
)


class WhisperStream:

    def transcribe(
        self,
        audio_path
    ):
        
        print(
            "Starting transcription"
        )

        result = transcribe_audio(
            audio_path
        )

        print(
            result.text
        )

        tokens = []

        for segment in result.segments:

            tokens.append(
                TranscriptToken(
                    text=segment.text,
                    start=segment.start,
                    end=segment.end
                )
            )

        return tokens
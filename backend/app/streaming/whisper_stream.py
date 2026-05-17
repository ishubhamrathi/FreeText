from streaming.token import (
    TranscriptToken
)

from transcription.transcriber import (
    transcribe_audio
)


class WhisperStream:

    def transcribe(
        self,
        audio
    ):

        result = (
            transcribe_audio(
                audio
            )
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
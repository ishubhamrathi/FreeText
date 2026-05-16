from faster_whisper import WhisperModel


MODEL_PATH = "models/whisper/base"


model = WhisperModel(
    MODEL_PATH,
    device="cpu",
    compute_type="int8"
)


def transcribe_audio(audio_path):
    segments, info = model.transcribe(audio_path)

    print(f"Detected language: {info.language}")

    transcript = ""

    for segment in segments:
        transcript += segment.text + " "

    return transcript.strip()
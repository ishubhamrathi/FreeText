import ollama


class CleanupService:

    def cleanup_text(self, text):
        prompt = f"""
You are an AI writing assistant.

Clean the following speech transcript.

Rules:
- Remove filler words
- Fix grammar
- Fix punctuation
- Keep original meaning
- Keep response concise
- Return ONLY cleaned text

Transcript:
{text}
"""

        response = ollama.chat(
            model="qwen2.5:3b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"].strip()
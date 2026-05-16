import time

from services.pipeline_service import (
    PipelineService
)


def main():
    input(
        "Open any text editor.\n"
        "Press Enter to start recording..."
    )

    pipeline = PipelineService()

    result = pipeline.execute()

    print("\nTranscript:")
    print(result.text)

    print(
        "\nSwitch to target window..."
    )

    time.sleep(5)

    pipeline.typing_service.type_text(
        result.text
    )

    print("\nTyping completed.")


if __name__ == "__main__":
    main()
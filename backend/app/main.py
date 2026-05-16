from services.pipeline_service import (
    PipelineService
)


def main():
    input("Press Enter to start recording...")

    pipeline = PipelineService()

    result = pipeline.execute()

    print("=" * 50)

    print(f"Detected Language : {result.language}")

    print(
        f"Processing Time  : "
        f"{result.processing_time}s"
    )

    print("\nTranscript:\n")

    print(result.text)

    print("=" * 50)


if __name__ == "__main__":
    main()
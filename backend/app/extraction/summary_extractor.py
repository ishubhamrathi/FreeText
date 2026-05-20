class SummaryExtractor:

    def extract(
        self,
        text,
        max_sentences=3
    ):

        sentences = []

        for sentence in text.split(
            "."
        ):

            sentence = (
                sentence.strip()
            )

            if sentence:

                sentences.append(
                    sentence
                )

        return ". ".join(
            sentences[
                :max_sentences
            ]
        )
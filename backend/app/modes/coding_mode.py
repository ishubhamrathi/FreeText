class CodingMode:

    def process(
        self,
        text
    ):

        lower = text.lower()

        tags = []

        keywords = {

            "bug":
            "bug",

            "fix":
            "bug",

            "api":
            "backend",

            "spring":
            "backend",

            "react":
            "frontend",

            "deploy":
            "deployment",

            "database":
            "database",

            "sql":
            "database",

            "refactor":
            "refactor",

            "test":
            "testing"
        }

        for key, tag in keywords.items():

            if key in lower:

                tags.append(
                    tag
                )

        return list(
            set(tags)
        )
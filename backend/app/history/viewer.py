from history.service import (
    HistoryService
)


class HistoryViewer:

    def __init__(self):

        self.service = (
            HistoryService()
        )

    def show_recent(self):

        items = (
            self.service.get_recent()
        )

        print(
            "\n=== HISTORY ==="
        )

        for item in items:

            print(
                f"""
ID: {item.session_id}

Time:
{item.started_at}

Text:
{item.cleaned_text}

-------------------
"""
            )
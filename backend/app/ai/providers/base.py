from abc import ABC, abstractmethod


class CleanupProvider(ABC):

    @abstractmethod
    def cleanup_text(self, text: str) -> str:
        pass
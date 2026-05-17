from abc import ABC
from abc import abstractmethod


class CleanupProvider(ABC):

    @abstractmethod
    def cleanup_text(
        self,
        text: str
    ) -> str:
        pass

    @property
    def uses_prompt(self) -> bool:
        return False
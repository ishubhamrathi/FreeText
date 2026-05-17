from abc import ABC
from abc import abstractmethod


class CleanupProfile(ABC):

    @abstractmethod
    def build_prompt(
        self,
        text: str
    ) -> str:
        pass
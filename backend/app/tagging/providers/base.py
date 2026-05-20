from abc import ABC
from abc import abstractmethod


class TagProvider(ABC):

    @abstractmethod
    def generate(
        self,
        text: str
    ) -> str:

        pass
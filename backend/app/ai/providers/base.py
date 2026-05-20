from abc import ABC
from abc import abstractmethod

from ai.models.cleanup_result import (
    CleanupResult
)


class AiProvider(
    ABC
):

    @abstractmethod
    def process(
        self,
        text,
        language="auto"
    ) -> CleanupResult:

        pass
from abc import ABC
from abc import abstractmethod


class Exporter(ABC):

    @abstractmethod
    def export(
        self,
        session,
        output_path
    ):

        pass
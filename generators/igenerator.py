from abc import ABC, abstractmethod

class IGenerator(ABC):

    @abstractmethod
    def generate(self, indent: int) -> str:
        pass

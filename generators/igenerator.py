from abc import ABC, abstractmethod
import global_vars

class IGenerator(ABC):
    
    def __init__(self) -> None:
        self.__from_imports = []
        self.__imports = []
    
    def add_from_import(self, from_path: str, imports: list[str]):
        global_vars.from_imports.append(global_vars.FromImport(from_path, imports))

    def add_import(self, import_path: str):
        global_vars.imports.append(import_path)

    @abstractmethod
    def generate(self, indent: int) -> str:
        pass

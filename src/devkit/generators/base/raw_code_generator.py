from devkit.generators.igenerator import IGenerator

class RawCodeGenerator(IGenerator):
    
    __code: str
    
    def __init__(self) -> None:
        super().__init__()
        self.__code = ""
    
    def set_code(self, code: str):
        self.__code = code
        
    def generate(self, indent: int) -> str:
        return self.__code
    
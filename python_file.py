from contextlib import contextmanager
from generators.igenerator import IGenerator
from typing import Literal
import global_vars

@contextmanager
def python_file(file_name: str):
    """
    Create a new Python file using generators.
    """
    
    python_file = PythonFile()
    try:
        global_vars.from_imports = []
        global_vars.imports = []
        yield python_file
    finally:
        # Generate the generators
        generators_result = ""
        
        for generator in python_file.get_generators():
            generators_result += generator.generate(0)
            generators_result += "\n"
        
        # Collect the imports
        from_imports: dict[str, set[str]] = {}
        
        for imp in global_vars.from_imports:
            if imp.path not in from_imports:
                from_imports[imp.path] = set(imp.imports)
            else:
                from_imports[imp.path] = from_imports[imp.path].union(set(imp.imports))
        
        imports: set[str] = set()
        for imp in global_vars.imports:
            imports.add(imp)
        
        # Generate the imports
        imports_result = ""
        
        if len(python_file.get_future_imports()) != 0:
            imports_result += f"from __future__ import {', '.join(python_file.get_future_imports())}\n\n"
        
        for imp in imports:
            imports_result += f"import {imp}\n"
        
        for path, imports in from_imports.items():
            imports_result += f"from {path} import " + ", ".join(imports) + "\n"
        
        # Generate the result
        result = f"{imports_result}\n{generators_result}"
        
        # Clear the imports for further usage
        global_vars.from_imports = []
        global_vars.imports = []
        
        with open(file_name, "w") as f:
            f.write(result)

class PythonFile:
    
    __generators: list[IGenerator]
    __future_imports: list[str]
    
    def __init__(self) -> None:
        self.__generators = []
        self.__future_imports = []
    
    def add_future_import(self, future_import: Literal["annotations"]):
        self.__future_imports.append(future_import)    
    
    def get_future_imports(self) -> list[str]:
        return self.__future_imports
    
    def add_generator(self, generator: IGenerator):
        self.__generators.append(generator)
        
    def get_generators(self) -> list[IGenerator]:
        return self.__generators

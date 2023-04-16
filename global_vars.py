from dataclasses import dataclass

@dataclass
class FromImport:
    path: str
    imports: list[str]

from_imports: list[FromImport] = []
imports: list[str] = []
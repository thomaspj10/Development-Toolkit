from __future__ import annotations
from typing import Any

class HTMLElement:

    _tag: str
    _attributes: dict[str, Any]
    _children: list[HTMLElement]
    _text: str | None
    
    def __init__(self, tag: str, attributes: dict[str, Any], children: list[HTMLElement], text: str | None) -> None:
        self._tag = tag
        self._attributes = attributes
        self._children = children
        self._text = text

    def __str__(self) -> str:
        attributes_str = " ".join([f'{item[0]}="{item[1]}"' for item in self._attributes.items() if item[1] != None])
        if len(attributes_str) > 0:
            attributes_str = " " + attributes_str

        children_str = "".join([str(item) for item in self._children])
        text_str = self._text if self._text != None else ""

        return f"<{self._tag}{attributes_str}>{text_str}{children_str}</{self._tag}>"

    def get_children_from_args(self, args: tuple[Any]) -> list[HTMLElement]:
        children: list[HTMLElement] = []
        for element in args:
            if isinstance(element, list):
                for list_item in element: # type: ignore
                    children.append(list_item) # type: ignore
            else:
                children.append(element)

        return children

from __future__ import annotations
from typing import Self
from devkit.html.htmlelement import HTMLElement

class Div(HTMLElement):

    def __call__(self, *args: Div | P | list[Div | P]) -> Self:
        return Div(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def div(text: str | None = None, classes: str | None = None, id: str | None = None):
    attributes = {
        "class": classes,
        "id": id
    }

    return Div("div", attributes, [], text)

class P(HTMLElement):

    def __call__(self, *args: P | list[P]) -> Self:
        return P(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def p(text: str | None = None):
    attributes = {
        
    }
    return P("p", attributes, [], text)

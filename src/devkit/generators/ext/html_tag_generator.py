from devkit.generators.igenerator import IGenerator
from devkit.generators.base import FunctionGenerator, ClassGenerator

class HtmlTagGenerator(IGenerator):
    
    __tag: str
    __text: bool
    __children: list[str]
    
    def __init__(self) -> None:
        super().__init__()
        self.__text = False
        self.__children = []
    
    def set_tag(self, tag: str):
        self.__tag = tag

    def set_text(self, text: bool):
        self.__text = text

    def set_children(self, children: list[str]):
        self.__children = children
    
    def generate(self, indent: int) -> str:
        types = "HTMLElement" if len(self.__children) == 0 else " | ".join([child.capitalize() for child in self.__children])
        class_name = self.__tag.capitalize()

        call_function = FunctionGenerator()
        call_function.set_name("__call__")
        call_function.add_argument("self", "Self")
        call_function.add_argument("*args", f"{types} | list[{types}]")
        call_function.set_return_type("Self")
        call_function.set_body(f"return {class_name}(self._tag, self._attributes, self.get_children_from_args(args), self._text)")

        call_function.add_from_import("typing", ["Self"])
        call_function.add_from_import("devkit.html.htmlelement", ["HTMLElement"])

        class_generator = ClassGenerator()
        class_generator.set_name(class_name)
        class_generator.add_inherited_class("HTMLElement")
        class_generator.add_function(call_function)
        
        use_tag_function = FunctionGenerator()
        use_tag_function.set_name(self.__tag)
        use_tag_function.set_return_type(class_name)

        if self.__text:
            use_tag_function.add_argument("text", "str | None = None")
            use_tag_function.set_body(f"return {class_name}('{self.__tag}', " + "{}" + f", [], text)")
        else:
            use_tag_function.set_body(f"return {class_name}('{self.__tag}', " + "{}" + f", [], '')")


        return class_generator.generate(indent) + use_tag_function.generate(indent)
    
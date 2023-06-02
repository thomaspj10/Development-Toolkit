import json
from devkit.generators.python_file import python_file
from devkit.generators.ext import HtmlTagGenerator
from devkit.generators.base import RawCodeGenerator

with open("html5.json", "r") as f:
    specification = json.load(f)

with python_file("tags2.py") as pf:
    pf.add_future_import("annotations")

    for element in specification["elements"]:
        tag_generator = HtmlTagGenerator()
        tag_generator.set_tag(element["name"])
        tag_generator.set_children(element["children"])
        tag_generator.set_text(element["text"])

        pf.add_generator(tag_generator)

    for element_group in specification["element_groups"]:
        name = element_group["name"].capitalize()
        types = ", ".join([child.capitalize() for child in element_group["elements"]])

        group_generator = RawCodeGenerator()
        group_generator.set_code(f"{name} = TypeVar('{name}', {types})")
        group_generator.add_from_import("typing", ["TypeVar"])

        pf.add_generator(group_generator)

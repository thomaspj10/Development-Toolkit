from __future__ import annotations
from html.parser import HTMLParser

# Automate the migration of native html into the html DSL provided by devkit.

file = input("HTML file: ")

with open(file, "r") as f:
    html = f.read()

result = "from devkit.html import *\n\n"
indent = 0

TAB = "    "

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]):
        global result, indent

        attributes_str = ", ".join([f"{attribute[0].replace('-', '_')}=\"{attribute[1]}\"" for attribute in attrs if attribute[0] != "class"])
        class_str = "".join([f"\"{attribute[1]}\"" for attribute in attrs if attribute[0] == "class"])
        if len(attributes_str) > 0:
            class_str += ", "

        indent_str = TAB * indent

        result += f"{indent_str}{tag}({class_str}{attributes_str})(\n"
        indent += 1

    def handle_endtag(self, tag: str):
        global result, indent

        indent -= 1

        indent_str = TAB * indent
        result += f"{indent_str})\n"

    def handle_data(self, data: str):
        global result

        indent_str = TAB * indent

        result += f"{indent_str}\"{data}\",\n"

parser = MyHTMLParser()
parser.feed(html)

print("Converted the HTML file to Python.")

with open(f"{file.replace('.html', '.py')}", "w") as f:
    f.write(result)

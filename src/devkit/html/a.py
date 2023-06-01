import re

with open("elements.xsd", "r") as f:
    content = f.read()

    new_content = re.sub(r"<xsd:attribute(.*?)</xsd:attribute>", "", content, flags=re.MULTILINE | re.S)

with open("elements2.xsd", "w") as f:
    f.write(new_content)

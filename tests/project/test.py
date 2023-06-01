from devkit.html import *

def info_element():
    return div()(
        div(id = "thomas"),
        div(classes = "margin--default"),
        div()(
            p(text = "Hello world!"),
        )
    )

result = div()(
    info_element(),
    p(text = "Welcome to my site")
)

print(result)

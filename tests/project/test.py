from devkit.html import *

def info_element():
    return div()(
        div(),
        div(),
        div()(
            p()("Hello world!"),
        )
    )

result = div()(
    info_element(),
    p()
)

print(result)

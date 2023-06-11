from devkit.html import *

def homepage(motd: str):
    return html()(
        head()(
            script()
        ),
        body()(
            div()(
                h1()(
                    motd
                )
            )
        )
    )

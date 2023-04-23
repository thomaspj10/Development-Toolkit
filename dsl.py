from contextlib import contextmanager

class Head:
    pass

class Html:
    pass
    
@contextmanager
def head():
    head = Head()
    yield head
    print(head)

@contextmanager
def html():
    html = Html()
    yield html
    print(html)

with html() as body:
    with head() as h:
        print("Hello !")

from contextlib import contextmanager

@contextmanager
def func():
    def enter():
        yield
        
    return enter

class Head:
    pass

class Html:
    
    @contextmanager
    def head(self):
        head = Head()
        yield head
        print(head)

@contextmanager
def html():
    html = Html()
    yield html
    print(html)

with html() as body:
    with body.head() as head:
        print("Hello !")
    
    

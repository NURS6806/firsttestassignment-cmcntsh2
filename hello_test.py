import hello;

def test_hello():
    assert hello.hello_world() == "Hello World!"
    
def test_add():
    assert hello.add(1,2) == 3
    
def test_diff():
    assert hello.diff(1,2) == -1

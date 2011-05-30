from compiler import pcompile

def module_wrap(cont):
    return ".sub 'main' :main\n{0}.end".format(cont)

def test_name():
    assert pcompile('a') == module_wrap('a')

def test_add():
    assert pcompile('a + b') == module_wrap('a + b')

def test_assign():
    assert pcompile('a = 2') == module_wrap('.local int a\na = 2\n')

def test_print():
    assert pcompile('print(2)') == module_wrap('say 2\n')

def test_assign_add():
    assert pcompile('a = 1 + 2') == module_wrap('.local int a\na = 1 + 2\n')

def test_assign_add_print():
    assert pcompile('a = 1 + 2; print(a)') == module_wrap(
            '.local int a\na = 1 + 2\nsay a\n')

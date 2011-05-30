import subprocess
import os

from compiler import pcompile

def module_wrap(cont):
    return ".sub 'main' :main\n{0}.end".format(cont)

class TestGeneratedCode():
    def test_name(self):
        assert pcompile('a') == module_wrap('a')

    def test_add(self):
        assert pcompile('a + b') == module_wrap('a + b')

    def test_assign(self):
        assert pcompile('a = 2') == module_wrap('.local int a\na = 2\n')

    def test_print(self):
        assert pcompile('print(2)') == module_wrap('say 2\n')

    def test_add_print(self):
        assert pcompile('print(1+2)') == module_wrap('say 1 + 2\n')

    def test_assign_add(self):
        assert pcompile('a = 1 + 2') == module_wrap(
            '.local int a\na = 1 + 2\n')

    def test_assign_add_print(self):
        assert pcompile('a = 1 + 2; print(a)') == module_wrap(
            '.local int a\na = 1 + 2\nsay a\n')

def parrot(code):
    with open('in.pir', 'w') as f:
        f.write(code)

    output = subprocess.Popen(['parrot', 'in.pir'],
                stdout=subprocess.PIPE).communicate()[0]

    os.remove('in.pir')

    return output

class TestOutput():
    def test_print(self):
        assert parrot(pcompile('print(2)')) == b'2\n'

    def test_add_print(self):
        assert parrot(pcompile('print(1+2)')) == b'3\n'

    def test_assign_add_print(self):
        assert parrot(pcompile('a=1+2;print(a)')) == b'3\n'


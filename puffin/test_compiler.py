from compiler import compile
from util import parrot

class TestOutput():
    def test_null(self):
        assert parrot(compile('')) == b'';

    def test_print(self):
        assert parrot(compile('print(2)')) == b'2\n'

    def test_add_print(self):
        assert parrot(compile('print(1+2)')) == b'3\n'

    def test_assign_add_print(self):
        assert parrot(compile('a=1+2;print(a)')) == b'3\n'


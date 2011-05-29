import ast

class Codegen(ast.NodeVisitor):

    def __init__(self):
        super().__init__()

        self.pir = ""

    def generic_visit(self, node):
        #print(type(node).__name__)

        super().generic_visit(node)

    #def visit_Module(self, node):
    #    pass #ignore all scope for now

    def visit_Add(self, node):
        self.pir += '+'

    def visit_Num(self, node):
        self.pir += str(node.n)

if __name__ == '__main__':
    t = ast.parse('1+2')
    c = Codegen()
    c.visit(t)

    print(c.pir)

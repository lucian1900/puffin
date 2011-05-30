import ast

class Codegen(ast.NodeVisitor):

    def __init__(self):
        super().__init__()

        self.pir = ""

    def generic_visit(self, node):
        print(type(node).__name__)

        super().generic_visit(node)

    def visit_Module(self, node):
        self.pir += ".sub 'main' :main\n"
        
        super().generic_visit(node)

        self.pir += ".end"

    def visit_BinOp(self, node):
        #nothing to do for now
        super().generic_visit(node)

    def visit_Load(self, node):
        #nothing to do for now
        super().generic_visit(node)

    def visit_Add(self, node):
        self.pir += ' + '

    def visit_Num(self, node):
        self.pir += str(node.n)

    def visit_Expr(self, node):
        super().generic_visit(node)

    def visit_Call(self, node):
        if node.func.id == 'print':
            self.pir += 'say '

            args = []
            for i in node.args:
                if hasattr(i, 'id'):
                    args += i.id
                elif hasattr(i, 'n'):
                    args += str(i.n)

            self.pir += ', '.join(args) + '\n'

    def visit_Assign(self, node):
        self.pir += '.local int {0}\n'.format(node.targets[0].id)
        
        super().generic_visit(node)

        self.pir += '\n'

    def visit_Name(self, node): 
        self.pir += node.id

        super().generic_visit(node)

    def visit_Store(self, node):
        self.pir += ' = '

def pcompile(code):
    t = ast.parse(code)
    c = Codegen()
    c.visit(t)

    return c.pir

if __name__ == '__main__':
    #print(pcompile('a = 1+2;print(a)'))
    print(pcompile('print(2)'))


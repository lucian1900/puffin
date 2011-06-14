#!/usr/bin/env python3

import ast

head = '''
.sub initial_load_bytecode :anon :load :init
    load_bytecode 'boot.pbc'
.end

.sub 'main' :main
    get_hll_global $P3, [ 'Python' ] , 'builtins'
    $P1 = $P3()
'''
tail = '.end'

class Codegen(ast.NodeVisitor):

    def __init__(self):
        super().__init__()

        self.pir = []
    
    @property
    def code(self):
        return ''.join(self.pir)

    def generic_visit(self, node):
        # this helps show unimplemented nodes
        print(type(node).__name__)

        super().generic_visit(node)

    def visit_Module(self, node):
        self.pir += head

        super().generic_visit(node)

        self.pir += tail

    def visit_Add(self, node):
        self.pir += '+'

    def visit_Num(self, node):
        self.pir += str(node.n)

    def visit_Str(self, node):
        self.pir += "{0}".format(node.s)

    def visit_Expr(self, node):
        super().generic_visit(node)

    def visit_Call(self, node):
        if node.func.id == 'print':
            self.pir += '\nsay '
 
            for i in node.args:
                super().visit(i)

            self.pir += '\n'

    def visit_Assign(self, node):
        self.pir += '.local pmc {0}\n'.format(node.targets[0].id)
        
        super().generic_visit(node)

        self.pir += '\n'

    def visit_AugAssign(self, node):
        super().generic_visit(node.target)
        super().generic_visit(node.op)

        super().generic_visit(node)

        super().generic_visit(node.value)

    def visit_Name(self, node): 
        self.pir += node.id

        super().generic_visit(node)

    def visit_Store(self, node):
        self.pir += '='

def compile(code):
    t = ast.parse(code)
    c = Codegen()
    c.visit(t)

    return c.code

if __name__ == '__main__':
    import os
    import sys
    
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            code = f.read()
        
        pir = compile(code)
        
        name = os.path.basename(sys.argv[1])
        name = name.replace('.py', '.pir')
        with open(name, 'w') as f:
            f.write(pir)

#!/usr/bin/env python3

import ast

head = '''
.sub initial_load_bytecode :anon :load :init
    load_bytecode 'boot.pbc'
.end

.sub 'main' :main
    get_hll_global $P2, [ 'Python' ] , 'builtins'
    .local pmc builtins
    builtins = $P2()

    .local pmc globals
    globals = new "Hash"
'''
tail = '.end'

get_attr = '''$P1 = builtins["{0}"]
$P2 = getattribute $P1, "{1}"\n'''

class Block:
    def __init__(self):
        pass

class Codegen(ast.NodeVisitor):

    def __init__(self):
        super().__init__()

        self.decls = []
        self.pir = []
    
    @property
    def code(self):
        pir = head
        pir += ''.join(self.decls + self.pir)
        pir += tail
        return pir

    def generic_visit(self, node):
        # this helps show unimplemented nodes
        print(type(node).__name__)

        super().generic_visit(node)

    def visit_Module(self, node):
        super().generic_visit(node)

    def visit_Add(self, node):
        self.pir += ' + '

    def visit_Num(self, node):
        self.decls += get_attr.format('int', '__new__')
        self.decls += "$P3 = $P2({0})\n".format(node.n)

        self.pir += "$P3"

    def visit_Str(self, node):
        self.pir += "'{0}'".format(node.s)

    def visit_Call(self, node):
        # special-case for print. for now
        if node.func.id == 'print':
            self.pir += '\n'

            regs = []
            for i, e in enumerate(node.args):
                regs += '$P{0}'.format(i)
                self.pir += '$P{0} = '.format(i)

                super().visit(e)
                self.pir += '\n'

            self.pir += 'say '
            for i in regs:
                self.pir += i
            self.pir += '\n'

    def visit_AugAssign(self, node):
        super().generic_visit(node.target)
        super().generic_visit(node.op)

        #super().generic_visit(node)

        super().generic_visit(node.value)

    def visit_Name(self, node): 
        self.pir += "globals['{0}']".format(node.id)

        super().generic_visit(node)

    def visit_Store(self, node):
        self.pir += ' = '

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

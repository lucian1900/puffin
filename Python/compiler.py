import ast



class Codegen(ast.NodeVisitor):
    
    def generic_visit(self, node):
        print(type(node).__name__)

        super().generic_visit(node)

#    def visit_Load(

if __name__ == '__main__':
    t = ast.parse('1+2')
    Codegen().visit(t)

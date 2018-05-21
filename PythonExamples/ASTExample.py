'''
    This is an small example that aims to show how the workflow of ast is so we can study the suitability of this
    library for the project we will be working on

    On this example, we take the previous CarController.py development and we work on it.
    We have defined two classes here:
        - MyVisitor: When calling visit  Takes the nodes that have been previously parsed using ast and print them
        - MyTransformer: Once visit in called, uses the parsed nodes and transform them as specified
        in the visit_Str function. This is useful to add prefixes or suffixes on featured nodes for example
'''
import ast


class MyVisitor(ast.NodeVisitor):
    def visit_keyword(self, node):
        print('KEYWORD')

    def visit_Str(self, node):
        for text in node:
            if isinstance(text, ast.Call):
                self.visit_Call(text)
            else:
                print('Found String: "' + text.s + '"')

    def visit_Name(self, node):
        if isinstance(node, list):
            for name in node:
                print(' --- Name: ' + name.id)
        else:
            print(' --- Name: ' + node.id)

    def visit_FunctionDef(self, node):
        print('Function Definition: ' + str(node.name))
        self.visit_arguments(node.args)
        for node in node.body:
            if isinstance(node, ast.Str):
                self.visit_Str(node)
            elif isinstance(node, ast.Expr):
                self.visit_Expr(node)
            elif isinstance(node, ast.Assign):
                self.visit_Assign(node)
            elif isinstance(node, ast.While):
                self.visit_While(node)

    def visit_Expr(self, node):
        if isinstance(node, list):
            for nod in node:
                print(' ---- Expression: ' + str(nod.value))
                self.visit_Call(nod.value)
        else:
            print(' - Expression: ' + str(node.value))
            self.visit_Call(node.value)

    def visit_Call(self, node):
        print(' -- Call: ' + str(node.func))
        self.visit_Name(node.func)
        self.visit_Str(node.args)

    def visit_Assign(self, node):
        if isinstance(node, list):
            for nod in node:
                if isinstance(nod, ast.If):
                    self.visit_If(nod)
                else:
                    print(' -- Assign Targets: ' + str(nod.targets))
                    self.visit_Name(nod.targets)
                    print(' -- Assign: ' + str(nod.value))
                    self.visit_Call(nod.value)
        else:
            print(' -- Assign Targets: ' + str(node.targets))
            self.visit_Name(node.targets)
            print(' -- Assign: ' + str(node.value))
            self.visit_Num(node.value)

    def visit_Num(self, node):
        if isinstance(node, list):
            for nod in node:
                print(' --- Num: ' + str(nod.n))
        elif isinstance(node, ast.UnaryOp):
            print(' --- UnaryOp: ')
        else:
            print(' --- Num: ' + str(node.n))

    def visit_While(self, node):
        print(' - While: ' + str(node.test))
        self.visit_Compare(node.test)
        self.visit_Try(node.body)

    def visit_Try(self, nodes):
        for node in nodes:
            if isinstance(node, ast.Expr):
                self.visit_Expr(node)
            elif isinstance(node, ast.Try):
                self.visit_Assign(node.body)
                print(' -- Try: ' + str(node.handlers))
                self.visit_ExceptHandler(node.handlers)

    def visit_ExceptHandler(self, node):
        print(' --- ExceptHandler: ' + str(node[0].type))
        self.visit_Name(node[0].type)
        print(' --- ExceptHandler: ' + str(node[0].body))
        self.visit_Expr(node[0].body)

    def visit_arguments(self, node):
        print(' - arguments: ' + str(node.args))

    def visit_Compare(self, node):
        print('Comparision')
        self.visit_Name(node.left)
        self.visitGt()
        self.visit_Num(node.comparators)

    def visitGt(self):
        print(' --- Greater than')

    def visit_If(self, node):
        self.visit_Compare(node.test)
        for body_part in node.body:
            if isinstance(body_part, ast.Expr):
                self.visit_Expr(body_part)
        for or_else_part in node.orelse:
            if isinstance(or_else_part, ast.If):
                self.visit_If(or_else_part)
            elif isinstance(or_else_part, ast.Expr):
                self.visit_Expr(or_else_part)


class MyTransformer(ast.NodeTransformer):
    def visit_Str(self, node):
        return ast.Str('str: ' + node.s)


# First part: prints the nodes retrieved by the parsed after transform them
controller_file = open('CarController.py').read()
car_controller = ast.parse(controller_file)
MyTransformer().visit(car_controller)
MyVisitor().visit(car_controller)
print()

'''
    Second part: Lets you execute the file itself
    fix_missing_locations generates lineno and col_offset attributes for every single node because when we call
    compile, it excepts this attributes to be set. 
    After that we call exec and can actually execute the python file
'''
car_controller = ast.fix_missing_locations(car_controller)
exec(compile(car_controller, '<string>', 'exec'))

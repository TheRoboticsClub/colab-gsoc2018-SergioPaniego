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

    def visit_Str(self, node, depth):
        depth = depth + 1
        separator = ' ' + depth * '-'
        for text in node:
            if isinstance(text, ast.Call):
                self.visit_Call(text, depth)
            else:
                print(separator + ' Found String: "' + text.s + '"')

    def visit_Name(self, node, depth):
        depth = depth + 1
        separator = ' ' + depth * '-'
        if isinstance(node, list):
            for name in node:
                print(separator + ' Name: ' + name.id)
        else:
            print(separator + ' Name: ' + node.id)

    def visit_FunctionDef(self, node):
        depth = 0
        print('Function Definition: ' + str(node.name))
        self.visit_arguments(node.args, depth)
        for node in node.body:
            if isinstance(node, ast.Str):
                self.visit_Str(node, depth)
            elif isinstance(node, ast.Expr):
                self.visit_Expr(node, depth)
            elif isinstance(node, ast.Assign):
                self.visit_Assign(node, depth)
            elif isinstance(node, ast.While):
                self.visit_While(node, depth)

    def visit_Expr(self, node, depth):
        depth = depth + 1
        separator = ' ' + depth * '-'
        if isinstance(node, list):
            for nod in node:
                print(separator + ' Expression: ' + str(nod.value))
                self.visit_Call(nod.value, depth)
        else:
            print(separator + ' Expression: ' + str(node.value))
            self.visit_Call(node.value, depth)

    def visit_Call(self, node, depth):
        depth = depth + 1
        separator = ' ' + depth * '-'
        print(separator + ' Call: ' + str(node.func))
        self.visit_Name(node.func ,depth)
        self.visit_Str(node.args, depth)

    def visit_Assign(self, node, depth):
        depth = depth + 1
        separator = ' ' + depth * '-'
        if isinstance(node, list):
            for nod in node:
                if isinstance(nod, ast.If):
                    self.visit_If(nod, depth)
                else:
                    self.visit_Name(nod.targets, depth)
                    print(separator + ' Assign: ' + str(nod.value))
                    self.visit_Call(nod.value, depth)
        else:
            self.visit_Name(node.targets, depth)
            print(separator + ' Assign: ' + str(node.value))
            self.visit_Num(node.value, depth)

    def visit_Num(self, node, depth):
        depth = depth + 1
        separator = ' ' + depth * '-'
        if isinstance(node, list):
            for nod in node:
                print(separator + ' Num: ' + str(nod.n))
        elif isinstance(node, ast.UnaryOp):
            print(separator + ' UnaryOp: ')
        else:
            print(separator + ' Num: ' + str(node.n))

    def visit_While(self, node, depth):
        depth = depth + 1
        separator = ' ' + depth * '-'
        print(separator + ' While: ' + str(node.test))
        self.visit_Compare(node.test, depth)
        self.visit_Try(node.body, depth)

    def visit_Try(self, nodes, depth):
        depth = depth + 1
        separator = ' ' + depth * '-'
        for node in nodes:
            if isinstance(node, ast.Expr):
                print(separator + ' Try: ')
                self.visit_Expr(node, depth)
            elif isinstance(node, ast.Try):
                print(separator + ' Try: ')
                self.visit_Assign(node.body, depth)
                self.visit_ExceptHandler(node.handlers, depth)

    def visit_ExceptHandler(self, node, depth):
        depth = depth + 1
        separator = ' ' + depth * '-'
        print(separator + ' ExceptHandler: ' + str(node[0].type))
        self.visit_Name(node[0].type, depth)
        print(separator + ' ExceptHandler: ' + str(node[0].body))
        self.visit_Expr(node[0].body, depth)

    def visit_arguments(self, node, depth):
        depth = depth + 1
        separator = ' ' + depth * '-'
        print(separator + ' arguments: ' + str(node.args))

    def visit_Compare(self, node, depth):
        depth = depth + 1
        separator = ' ' + depth * '-'
        print(separator + ' Comparision')
        self.visit_Name(node.left, depth)
        self.visitGt(depth)
        self.visit_Num(node.comparators, depth)

    def visitGt(self, depth):
        depth = depth + 1
        separator = ' ' + depth * '-'
        print(separator + ' Greater than')

    def visit_If(self, node, depth):
        depth = depth + 1
        separator = ' ' + depth * '-'
        self.visit_Compare(node.test, depth)
        for body_part in node.body:
            if isinstance(body_part, ast.Expr):
                self.visit_Expr(body_part, depth)
        for or_else_part in node.orelse:
            if isinstance(or_else_part, ast.If):
                print(separator + ' ElIf')
                self.visit_If(or_else_part, depth)
            elif isinstance(or_else_part, ast.Expr):
                print(separator + ' Else')
                self.visit_Expr(or_else_part, depth)


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

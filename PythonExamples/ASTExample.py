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
    def visit_Str(self, node):
        print('Found String: "' + node.s + '"')
    def visit_Name(self, node):
        print('Name: ' + node.id)
    def visit_FunctionDef(self, node):
        print('Function Definition: ' + str(node.name))

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

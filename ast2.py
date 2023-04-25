# map with all the variables declared with their respective values
variables = {}

'''
Statements
'''
class Statements:
    def __init__(self, nodes):
        self.nodes = nodes

    def eval(self):
        for node in self.nodes:
            node.eval()

'''
Number (INT)

this class returns an integer when it evaluates itself
'''
class Number():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)
    
'''
Number (REAL)

this class returns a float when it evaluates itself
'''
class RealNumber():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return float(self.value)
    
'''
String

this class returns a string when evaluating itself
'''
class String():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return str(self.value)
    
# class needed for two-sided operations
# ex: 4 + 5
# ex: 8 * 2
class BinaryOp():
    def __init__(self, left, right):
        self.left = left
        self.right = right

'''
Arithmetic Operations
'''
class Sum(BinaryOp):
    def eval(self):
        print()
        return self.left.eval() + self.right.eval()

class Sub(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()
    
class Mult(BinaryOp):
    def eval(self):
        return self.left.eval() * self.right.eval()
    
class Div(BinaryOp):
    def eval(self):
        return self.left.eval() / self.right.eval()
    
'''
Relational Operations
'''
class LessEqual(BinaryOp):
    def eval(self):
        return self.left.eval() <= self.right.eval()

class GreaterEqual(BinaryOp):
    def eval(self):
        return self.left.eval() >= self.right.eval()
    
class LessThan(BinaryOp):
    def eval(self):
        return self.left.eval() < self.right.eval()
    
class GreaterThan(BinaryOp):
    def eval(self):
        return self.left.eval() > self.right.eval()
    
class NotEqualTo(BinaryOp):
    def eval(self):
        return self.left.eval() != self.right.eval()
    
class EqualTo(BinaryOp):
    def eval(self):
        return self.left.eval() == self.right.eval()

'''
Logic Operators
'''
class And(BinaryOp):
    def eval(self):
        return self.left.eval() and self.right.eval()
    
class Or(BinaryOp):
    def eval(self):
        return self.left.eval() or self.right.eval()

'''
Variable Declaration
int :: x

this class receives a name.
it adds the name to the variables map, with a NoneType value.
'''
class Declare:
    def __init__(self, name):
        self.name = name

    def eval(self):
        variables[self.name] = None

'''
Variable Declaration - Aux Function

if the name exists in the variable map, assign a value
else, it's not declared so return a runtime error
'''
class DeclareAux:
    def __init__(self, name):
        self.name = name
    
    def eval(self):
        if self.name in variables.keys():
            return variables[self.name]
        else: 
            raise RuntimeError("Variable not declared:", self.name)
        
'''
Variable Assignation
x = 3

this class takes a name and value, and it assigns it to the existing variable.
at this point, DeclareAux has checked that the variable is declared.
'''
class Assign:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def eval(self):
        variables[self.name] = self.value.eval()

'''
For Loop
'''
class ForLoop:
    def __init__(self, identifier, condition, increment, body):
        self.id = identifier
        self.condition = condition
        self.increment = increment
        self.body = body
    
    def eval(self):
        while(self.condition.eval()):
            self.body.eval()
            self.increment.eval()

'''
Do While
'''
class DoWhileLoop:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def eval(self):
        while(self.condition.eval()):
            self.body.eval()

'''
If Then / Else 
'''
class If():
    def  __init__(self, condition, body, else_body = None):
       self.condition = condition
       self.body = body
       self.else_body = else_body
    
    def eval(self):
       if self.condition.eval() == True:
           return self.body.eval()
       elif self.else_body is not None:
           return self.else_body.eval()
       return Null()

'''
Print
'''
# eval returns a value that is being evaluated
class Print():
    def __init__(self, value):
        self.value = value

    def eval(self):
        print(self.value.eval())

# eval returns a string
class PrintString():
    def __init__(self, value):
        self.value = value

    def eval(self):
        print(self.value.getstr()[1:-1])
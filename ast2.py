# map with all the variables declared with their respective values
variables = {}

'''
Procedures
'''
class Procedures:
    def __init__(self, nodes):
        self.nodes = nodes

    def eval(self):
        for node in self.nodes:
            node.eval()

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
Variable Assignation
x = 3

this class takes a name and value.
if the name exists in the variable map, assign a value
else, it's not declared so return a runtime error
'''
class Assign:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def eval(self):
        # variables[self.name] = self.value.eval()
        if self.name in variables.keys():
            variables[self.name] = self.value.eval()
            return variables[self.name]
        else:
            raise RuntimeError("debuglog: Assign - Not Declared:", self.name)

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
        print("debuglog: Declare - ", self.name)

'''
Variable Declaration - Aux Function

'''
class DeclareAux:
    def __init__(self, name):
        self.name = name

    def eval(self):
        if self.name in variables.keys():
            return variables[self.name]
        else:
            raise RuntimeError("debuglog: DeclareAux - Not declared:", self.name)

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

'''
Program
'''
class Program():
    def __init__(self, value):
        self.value = value

    def eval(self):
        print("Successful program")
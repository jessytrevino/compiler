# map with all the variables declared with their respective values
# variableMap = 
variableMap = {}

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
    
class Boolean():
    def __init__(self, value):
        self.value = value
    
    def eval(self):
        if (self.value.getstr() == 'true'):
            return True
        return False
    
'''
String

this class returns a string when evaluating itself
'''
class String:
    def __init__(self, value):
        self.value = value

    def eval(self):
        return str(self.value)
    
'''
String Concat
'''
class StringConcat:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
    
    def eval(self):
        return str(self.str1.value) + str(self.str2.value)

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

this class receives a dataType and a list of ids.
it iterates through the list to add each id to dictionary with NoneType value.
it also defines the data type of each id.
dataType --> 0 - int
             1 - str
             2 - float (real)
             3 - bool
'''
class Declare:
    def __init__(self, dataType, ids):
        self.dataType = dataType
        self.ids = ids

    def eval(self):
        for i in self.ids:
            print(i)
            variableMap[i] = [ None , self.dataType ]

'''
Variable Declaration - Aux Function

if the name exists in the variable map, assign a value
else, it's not declared so return a runtime error
'''
class DeclareAux:
    def __init__(self, name):
        self.name = name
    
    def eval(self):
        if self.name in variableMap.keys():
            return variableMap[self.name][0]
        else: 
            raise RuntimeError("DeclareAux: Not declared or assigned", self.name)
        
'''
Variable Assignation
x = 3

this class takes a name and value, and it assigns it to the existing variable.
eval function assesses if the type of value.eval is the same as the one stored in
variableMap[name].
if type stored in variableMap is the same as the type of value.eval, assign the value
else, 
'''
class Assign:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def eval(self):
        dtypeM = variableMap[self.name][1];
        if (isinstance(self.value.eval(), int) and dtypeM == 0) :
            '''
            # remove/add block comment to enable/disable edge case handling
            # edge case when int type = False or int type = True
            # (False is 0 and True is 1) 
            # this code does not treat booleans as integers.
            if (self.value.eval() != False and self.value.eval() != True):
                variableMap[self.name][0] = int(self.value.eval())
            else:
                raise RuntimeError("Assign: variable is being assigned a value of incompatible type boolean")
            '''
            
            # following assignment treats booleans as integers
            # if the block above is uncommented, comment next line.
            variableMap[self.name][0] = int(self.value.eval())

        elif (isinstance(self.value.eval(), str) and dtypeM == 1):
            variableMap[self.name][0] = self.value.eval()
        elif (isinstance(self.value.eval(), float) and dtypeM == 2):
            variableMap[self.name][0] = self.value.eval()
        elif (isinstance(self.value.eval(), bool) and dtypeM == 3):
            variableMap[self.name][0] = self.value.eval()
        else:
            raise RuntimeError("Assign: variable is being assigned a value of incompatible type")

'''
For Loop

this class takes an identifier, a condition, an increment and a body.
these params follow the next structure:

for (identifier; condition; increment) {
    body
}
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

this class takes a condition and a body.
these params follow the next structure:

while (condition) do {
    body
}
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

this class takes a condition, a body, and an else_body.
these params follow the next structure:

if (condition) {
    body
} else {
    else_body
}
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

# eval returns a string without the quotation marks
class PrintString():
    def __init__(self, value):
        self.value = value

    def eval(self):
        print(self.value.getstr()[1:-1])
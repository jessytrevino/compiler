variables = {}

class Procedures:
    def __init__(self, nodes):
        self.nodes = nodes

    def eval(self):
        for node in self.nodes:
            node.eval()

class Statements:
    def __init__(self, nodes):
        self.nodes = nodes

    def eval(self):
        for node in self.nodes:
            node.eval()

class Assign:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def eval(self):
        variables[self.name] = self.value.eval()


class Declare:
    def __init__(self, name):
        self.name = name

    def eval(self):
        if self.name in variables.keys():
            return variables[self.name]
        else:
            raise RuntimeError("Not Declared:", self.name)

class Number():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)
    
class RealNumber():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return float(self.value)
    
class String():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return str(self.value)
    
class BinaryOp():
    def __init__(self, left, right):
        self.left = left
        self.right = right

# class Assign(BinaryOp):
#     def eval(self):
#         return self.left.eval() = self.right.eval()

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

class Print():
    def __init__(self, value):
        self.value = value

    def eval(self):
        print(self.value.eval())

class PrintString():
    def __init__(self, value):
        self.value = value

    def eval(self):
        print(self.value.getstr()[1:-1])

class Program():
    def __init__(self, value):
        self.value = value

    def eval(self):
        print("Successful program")
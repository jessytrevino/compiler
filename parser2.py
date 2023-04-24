from rply import ParserGenerator
from ast2 import Number, Sum, Sub, Mult, Div, LessEqual, GreaterEqual, LessThan, GreaterThan, NotEqualTo, EqualTo, Print


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN',
             'SEMI_COLON', 'SUM', 'SUB', 'MULT', 'DIV',
             'LESSEQUAL', 'GREATEREQUAL', 'LESSTHAN', 'GREATERTHAN',
             'NOTEQUALTO', 'EQUALTO'],
            precedence = [
            ('left', ['LESSTHAN', 'GREATERTHAN']),
            ('left', ['LESSEQUAL', 'GREATEREQUAL']),
            ('left', ['EQUALTO', 'NOTEQUALTO']),
            ('left', ['SUM', 'SUB']),
            ('left', ['MULT', 'DIV']),

            ]
        )

    def parse(self):
        @self.pg.production('program : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def program(p):
            return Print(p[2])
        
        # parenthesis PEMDAS
        @self.pg.production('expression : OPEN_PAREN expression CLOSE_PAREN')
        def expression_parens(p):
            return p[1]

        # arithmetic operations
        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : expression MULT expression')
        @self.pg.production('expression : expression DIV expression')
        def expression_arithmetics(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SUM':
                return Sum(left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(left, right)
            elif operator.gettokentype() == 'MULT':
                return Mult(left, right)
            elif operator.gettokentype() == 'DIV':
                return Div(left, right)
            
        # relational operations
        @self.pg.production('expression : expression LESSEQUAL expression')
        @self.pg.production('expression : expression GREATEREQUAL expression')
        @self.pg.production('expression : expression LESSTHAN expression')
        @self.pg.production('expression : expression GREATERTHAN expression')
        @self.pg.production('expression : expression NOTEQUALTO expression')
        @self.pg.production('expression : expression EQUALTO expression')
        def expression_relationals(p):
            left = p[0]
            right = p[2]
            relOperator = p[1]
            if relOperator.gettokentype() == 'LESSEQUAL':
                return LessEqual(left, right)
            elif relOperator.gettokentype() == 'GREATEREQUAL':
                return GreaterEqual(left, right)
            elif relOperator.gettokentype() == 'LESSTHAN':
                return LessThan(left, right)
            elif relOperator.gettokentype() == 'GREATERTHAN':
                return GreaterThan(left, right)
            elif relOperator.gettokentype() == 'NOTEQUALTO':
                return NotEqualTo(left, right)
            elif relOperator.gettokentype() == 'EQUALTO':
                return EqualTo(left, right)


        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(p[0].value)

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
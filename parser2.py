from rply import ParserGenerator
from ast2 import Number, Sum, Sub, Mult, Div, LessEqual, GreaterEqual, LessThan, GreaterThan, NotEqualTo, EqualTo, Print, String, PrintString


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN',
            'SUM', 'SUB', 'MULT', 'DIV',
             'LESS_EQUAL', 'GREATER_EQUAL', 'LESS_THAN', 'GREATER_THAN',
             'NOT_EQUAL_TO', 'EQUAL_TO', 'EQUALS',
             'PROGRAM', 'MAIN', 'END', 'INT',
             #'INT', 'STRING', 'REAL', 'BOOL',
             'IDENTIFIER', 'STRING_VAL',
             'DUB_COL'],
            # A list of precedence rules with ascending precedence, to
            # disambiguate ambiguous production rules.
            precedence = [
            ('left', ['LESS_THAN', 'GREATER_THAN']),
            ('left', ['LESS_EQUAL', 'GREATER_EQUAL']),
            ('left', ['EQUAL_TO', 'NOT_EQUAL_TO']),
            ('left', ['SUM', 'SUB']),
            ('left', ['MULT', 'DIV']),
            ]
        )

    def parse(self):
        
        
        # main program
        @self.pg.production('program : PROGRAM MAIN body END PROGRAM MAIN')
        def program(p):
            return p[2]
    
        # program body
        @self.pg.production('body : proc')
        @self.pg.production('body : varDec')
        @self.pg.production('body : varAssign')
        def body(p):
            return p[0]
        
        # procedures
        @self.pg.production('proc : PRINT OPEN_PAREN expression CLOSE_PAREN')
        @self.pg.production('proc : PRINT OPEN_PAREN STRING_VAL CLOSE_PAREN')
        # @self.pg.production('program : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def proc(p):
            if p[2].gettokentype() == 'STRING_VAL':
                return PrintString(p[2])
            return Print(p[2])
        
        # variable declaration
        @self.pg.production('varDec : INT DUB_COL IDENTIFIER')
        # @self.pg.production('varDec : STRING DUB_COL IDENTIFIER')
        # @self.pg.production('varDec : REAL DUB_COL IDENTIFIER')
        # @self.pg.production('varDec : BOOL DUB_COL IDENTIFIER')
        def varDec(p):
            return String(p[2])
        
        # variable assignation
        @self.pg.production('varAssign : IDENTIFIER EQUALS NUMBER')
        def varAssign(p):
            return p[2]
        
        # parenthesis PEMDAS
        @self.pg.production('expression : OPEN_PAREN expression CLOSE_PAREN')
        def expression_parenths(p):
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
        @self.pg.production('expression : expression LESS_EQUAL expression')
        @self.pg.production('expression : expression GREATER_EQUAL expression')
        @self.pg.production('expression : expression LESS_THAN expression')
        @self.pg.production('expression : expression GREATER_THAN expression')
        @self.pg.production('expression : expression NOT_EQUAL_TO expression')
        @self.pg.production('expression : expression EQUAL_TO expression')
        def expression_relationals(p):
            left = p[0]
            right = p[2]
            relOperator = p[1]
            if relOperator.gettokentype() == 'LESS_EQUAL':
                return LessEqual(left, right)
            elif relOperator.gettokentype() == 'GREATER_EQUAL':
                return GreaterEqual(left, right)
            elif relOperator.gettokentype() == 'LESS_THAN':
                return LessThan(left, right)
            elif relOperator.gettokentype() == 'GREATER_THAN':
                return GreaterThan(left, right)
            elif relOperator.gettokentype() == 'NOT_EQUAL_TO':
                return NotEqualTo(left, right)
            elif relOperator.gettokentype() == 'EQUAL_TO':
                return EqualTo(left, right)


        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(p[0].value)
        
        @self.pg.error
        def error_handler(token):
            raise ValueError("Ran into a '%s' where it wasn't expected" % token.gettokentype())

    def get_parser(self):
        return self.pg.build()
from rply import ParserGenerator
from ast2 import *

class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['PROGRAM', 'MAIN', 'END',

             'OPEN_PAREN', 'CLOSE_PAREN', 'OPEN_BRACES', 'CLOSE_BRACES',
             'DUB_COL', 'COMMA', 'SEMI_COLON',

             'AND', 'OR',

             'SUM', 'SUB', 'MULT', 'DIV',
             'LESS_EQUAL', 'GREATER_EQUAL', 'LESS_THAN', 'GREATER_THAN',
             'NOT_EQUAL_TO', 'EQUAL_TO', 'EQUALS',
             
             'INT_TYPE', 'STRING_TYPE', 'REAL_TYPE', 'BOOL_TYPE',
             'STRING_LITERAL', 'INT_LITERAL', 'REAL_LITERAL', 'BOOL_LITERAL',

             'IDENTIFIER',
             'PRINT', 'IF', 'ELSE', 'THEN', 'FOR', 'WHILE', 'DO'
             ],
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
        
        '''
        main
        '''
        # main program
        @self.pg.production('program : PROGRAM MAIN body END PROGRAM MAIN')
        def program(p):
            return p[2]
    
        '''
        body
        '''
        # body --> procedures, statements or expressions
        @self.pg.production('body : statements')
        @self.pg.production('body : expression')
        def body(p):
            return p[0]
        
        '''
        statements
        '''
        # statements --> multiple statements, a single statement, a procedure or an expression
        @self.pg.production('statements : statements statements')
        @self.pg.production('statements : statement')
        @self.pg.production("statement : expression")
        def all_statements(p):
            return Statements(p)
        
        # statement --> If / Else
        @self.pg.production('block : OPEN_BRACES statements CLOSE_BRACES')
        @self.pg.production('block : OPEN_BRACES statement CLOSE_BRACES')
        @self.pg.production('block : OPEN_BRACES  CLOSE_BRACES')
        def closureStatements(p):
            # if empty
            if len(p[1:-1]) == 0:
                 return Statements([])
            else:
                return p[1]
        
        @self.pg.production('statement : IF OPEN_PAREN expression CLOSE_PAREN THEN block')
        @self.pg.production('statement : IF OPEN_PAREN expression CLOSE_PAREN THEN block ELSE block')
        def ifStatements(p):
            # print(p)
            if len(p) > 6:
                return If(p[2], p[5], p[7])
            else:
                return If(p[2], p[5])
        
        # statement --> For Loop
        @self.pg.production('statement : FOR OPEN_PAREN IDENTIFIER SEMI_COLON expression SEMI_COLON statement CLOSE_PAREN block')
        def forLoop(p):
            return ForLoop(p[2], p[4], p[6], p[8])
        
        # statement --> Do While Loop
        @self.pg.production('statement : WHILE OPEN_PAREN expression CLOSE_PAREN DO block')
        def whileLoop(p):
            return DoWhileLoop(p[2], p[5])

        # statement --> print expression
        @self.pg.production('statement : PRINT OPEN_PAREN expression CLOSE_PAREN')
        def printExp(p):
            return Print(p[2])
        
        # statement --> print string
        @self.pg.production('statement : PRINT OPEN_PAREN STRING_LITERAL CLOSE_PAREN')
        def printStr(p):
            return PrintString(p[2])
        
        # statement --> Variable Assignation 
        # ex: x = 2
        @self.pg.production('statement : IDENTIFIER EQUALS expression')
        def variableAssignation(p):
            return Assign(p[0].getstr(), p[2])
        
        # statement --> Variable declaration
        # ex: int :: x
        @self.pg.production('idlist : IDENTIFIER')
        def variableDeclarationFinal(p):
            return [p[0].getstr()]
        
        @self.pg.production('idlist : IDENTIFIER COMMA idlist')
        def variableDeclarationList(p):
            return [p[0].getstr()] + p[2]
        
        @self.pg.production('statement : dataType DUB_COL idlist')
        def variable_declaration(p):
            ptype = p[0].gettokentype()
            if ptype == 'INT_TYPE':
                return Declare(0, p[2])
            elif ptype == 'STRING_TYPE':
                return Declare(1, p[2])
            elif ptype == 'REAL_TYPE':
                return Declare(2, p[2])
            elif ptype == 'BOOL_TYPE':
                return Declare(3, p[2])
            
        '''
        data types
        '''
        @self.pg.production('dataType : INT_TYPE')
        @self.pg.production('dataType : STRING_TYPE')
        @self.pg.production('dataType : REAL_TYPE')
        @self.pg.production('dataType : BOOL_TYPE')
        def data_types(p):
            return p[0]

        '''
        expressions
        '''
        # expression --> var ID
        @self.pg.production('expression : IDENTIFIER')
        def call(p):
            return DeclareAux(p[0].getstr())

        # expression --> parenthesis PEMDAS
        @self.pg.production('expression : OPEN_PAREN expression CLOSE_PAREN')
        def expression_parenths(p):
            return p[1]
        
        # expression --> type literal (numbers)
        @self.pg.production('expression : REAL_LITERAL')
        @self.pg.production('expression : INT_LITERAL')
        def number(p):
            if (p[0].gettokentype() == 'REAL_LITERAL'):
                return RealNumber(p[0].value)
            else:
                return Number(p[0].value)
        
        # expression --> type literal (string)
        @self.pg.production('expression : STRING_LITERAL')
        def string(p):
            return String(p[0].value[1:-1])
        
        # TO-DO: expression --> type literal (bool)
        @self.pg.production('expression : BOOL_LITERAL')
        def boolean(p):
            print(p[0].getvalue().getstr() == 'true')
            return Boolean(p[0].value)

        '''
        String concat
        '''
        @self.pg.production('expression : STRING_LITERAL SUM STRING_LITERAL')
        def string_concat(p):
            return StringConcat(p[0], p[2])

        '''
        arithmetic operations
        '''
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
            
        '''
        relational operations
        '''
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
            
        '''
        logic operators
        '''
        @self.pg.production('expression : expression AND expression')
        @self.pg.production('expression : expression OR expression')
        def expression_logic(p):
            left = p[0]
            right = p[2]
            if (p[1].gettokentype() == 'AND'):
                return And(left, right)
            else:
                return Or(left, right)
        
        @self.pg.error
        def error_handler(token):
            raise ValueError("Ran into a '%s' where it wasn't expected" % token.gettokentype())

    def get_parser(self):
        return self.pg.build()
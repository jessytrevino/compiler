from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):

        # Main program
        self.lexer.add('PROGRAM', r'program')
        self.lexer.add('MAIN', r'main')
        self.lexer.add('END', r'end')

        # Print
        self.lexer.add('PRINT', r'print')

        # Parenthesis
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')

        # Braces
        self.lexer.add('OPEN_BRACES', r'\{')
        self.lexer.add('CLOSE_BRACES', r'\}')

        # Semi Colon
        self.lexer.add('SEMI_COLON', r'\;')

        # Double Colon
        self.lexer.add('DUB_COL', r'::')

        # Coma
        self.lexer.add('COMA', r'\,')

        # Quotation Mark
        # self.lexer.add('QUOTES', r'\"')

        # equal =
        self.lexer.add('EQUALS', r'\=')

        # Arithmetic Operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        self.lexer.add('MULT', r'\*')
        self.lexer.add('DIV', r'\/')

        # Relational Operators
        self.lexer.add('LESS_EQUAL', r'<=')
        self.lexer.add('GREATER_EQUAL', r'>=')
        self.lexer.add('LESS_THAN', r'<')
        self.lexer.add('GREATER_THAN', r'>')
        self.lexer.add('NOT_EQUAL_TO', r'!=')
        self.lexer.add('EQUAL_TO', r'==')

        # and / or
        self.lexer.add('AND', r'and')
        self.lexer.add('OR', r'or')

        # Data Types
        self.lexer.add('INT_TYPE', r'int')
        self.lexer.add('STRING_TYPE', r'string')
        self.lexer.add('REAL_TYPE', r'real')
        self.lexer.add('BOOL_TYPE', r'bool')

        # Type Literals
        self.lexer.add("REAL_LITERAL",  r"\d+(\.\d+)")
        self.lexer.add('INT_LITERAL', r'\d+')
        self.lexer.add('STRING_LITERAL', r'".*"')
        self.lexer.add("BOOL_LITERAL", r"(true|false)")

        # Variable Names
        self.lexer.add('IDENTIFIER', r'[_\w]*[_\w0-9]+')
        
        # Ignore spaces
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
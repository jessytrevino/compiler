from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Print
        self.lexer.add('PRINT', r'print')

        # Parenthesis
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')

        # braces
        self.lexer.add('OPEN_BRACES', r'\{')
        self.lexer.add('CLOSE_BRACES', r'\}')

        # Semi Colon
        self.lexer.add('SEMI_COLON', r'\;')

        # Coma
        self.lexer.add('COMA', r'\,')

        # dot
        self.lexer.add('DOT', r'\.')

        # Arithmetic Operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        self.lexer.add('MULT', r'\*')
        self.lexer.add('DIV', r'\/')

        # Relational Operators
        self.lexer.add('LESSEQUAL', r'<=')
        self.lexer.add('GREATEREQUAL', r'>=')
        self.lexer.add('LESSTHAN', r'<')
        self.lexer.add('GREATERTHAN', r'>')
        self.lexer.add('NOTEQUALTO', r'!=')
        self.lexer.add('EQUALTO', r'==')

        # Number
        self.lexer.add('NUMBER', r'\d+')
        
        # Ignore spaces
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
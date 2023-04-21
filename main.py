from lexer import Lexer
from parser2 import Parser

text_input = """
print(1 + 2 * 4 + 3);
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

# for token in tokens:
#     print(token)

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()
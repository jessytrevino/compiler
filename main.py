from lexer import Lexer
from parser2 import Parser

text_input = """
print(2 * 3 == 2 + 2);
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

# for token in tokens:
#     print(token)

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()
'''
A00827044 Jessica Trevino

used tutorial:
https://medium.com/@marcelogdeandrade/writing-your-own-programming-language-and-compiler-with-python-a468970ae6df
'''
from lexer import Lexer
from parser2 import Parser

# read input file
fname = "input.mocha"
with open(fname) as f:
    text_input = f.read()

# get all the tokens
lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

# for token in tokens:
#     print(token)

# parse tokens generated
pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()
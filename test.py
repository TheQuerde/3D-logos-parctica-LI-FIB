from antlr4 import *
import sys
from Logos3DLexer import Logos3DLexer 
from Logos3DParser import Logos3DParser
from Logos3DVisitor import Logos3DVisitor
input_stream = InputStream(input('? '))
lexer = Logos3DLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = Logos3DParser(token_stream)
tree = parser.root()
l = []
if len(sys.argv) > 1:
    l = sys.argv.copy()
    l.pop(0)
    l.pop(0)
    visitor = Logos3DVisitor(sys.argv[1], l);
else:
    visitor = Logos3DVisitor("main", l)
visitor.visit(tree);
# print(tree.toStringTree(recog=parser))

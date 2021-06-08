from antlr4 import *
import sys
from Logos3DLexer import Logos3DLexer 
from Logos3DParser import Logos3DParser
from Logos3DVisitor import Logos3DVisitor
from Turtle3D import  Turtle3D 

input_stream = FileStream(sys.argv[1])
lexer = Logos3DLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = Logos3DParser(token_stream)
tree = parser.root()
l = []
if len(sys.argv) > 2:
    l = sys.argv.copy()
    l.pop(0)
    l.pop(0)
    l.pop(0)
    visitor = Logos3DVisitor(sys.argv[2], l);
else:
    visitor = Logos3DVisitor("main", l)
# print(tree.toStringTree(recog=parser))
visitor.visit(tree)

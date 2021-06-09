from antlr4 import *
import sys
from Logos3DLexer import Logos3DLexer 
from Logos3DParser import Logos3DParser
from Logos3DVisitor import Logos3DVisitor
from Turtle3D import  Turtle3D 


if len(sys.argv) > 2:
    input_stream = FileStream(sys.argv[1])
    lexer = Logos3DLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = Logos3DParser(token_stream)
    tree = parser.root()
    l = []
    l = sys.argv.copy()
    l.pop(0)
    l.pop(0)
    l.pop(0)
    visitor = Logos3DVisitor(sys.argv[2], l);
    visitor.visit(tree)
else:
    input_stream = InputStream(input('main: '))
    lexer = Logos3DLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = Logos3DParser(token_stream)
    tree = parser.root()
    l = []
    visitor = Logos3DVisitor("main", l)
    visitor.visit(tree)
# print(tree.toStringTree(recog=parser))

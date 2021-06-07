from antlr4 import *
from Logos3DLexer import Logos3DLexer 
from Logos3DParser import Logos3DParser
from Logos3DVisitor import Logos3DVisitor
input_stream = InputStream(input('? '))
lexer = Logos3DLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = Logos3DParser(token_stream)
tree = parser.root()
visitor = Logos3DVisitor();
visitor.visit(tree);
print(tree.toStringTree(recog=parser))

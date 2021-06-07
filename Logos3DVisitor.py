# Generated from Logos3D.g by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Logos3DParser import Logos3DParser
else:
    from Logos3DParser import Logos3DParser

# This class defines a complete generic visitor for a parse tree produced by Logos3DParser.

class Logos3DVisitor(ParseTreeVisitor):

    def __init__(self):
       self.pilaPrograma = []
       main = {}
       self.pilaPrograma.append(main)
       self.proc = {}
    
    # Visit a parse tree produced by Logos3DParser#root.
    def visitRoot(self, ctx:Logos3DParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Logos3DParser#statement.
    def visitStatement(self, ctx:Logos3DParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Logos3DParser#assigna_variable.
    def visitAssigna_variable(self, ctx:Logos3DParser.Assigna_variableContext): 
        l = list(ctx.getChildren())
        context = self.pilaPrograma[len(self.pilaPrograma)-1]
        aux = self.visit(l[2])
        context[l[0].getText()] = aux

    def visitNumerical(self, ctx:Logos3DParser.NumericalContext):
        l = list(ctx.getChildren())
        return float(l[0].getText())
    
    # Visit a parse tree produced by Logos3DParser#bucle_for.
    def visitBucle_for(self, ctx:Logos3DParser.Bucle_forContext):
        l = list(ctx.getChildren())
        context = self.pilaPrograma[len(self.pilaPrograma)-1].copy()
        self.pilaPrograma.append(context)
        if l[len(l)-1].getText() != "END":
            print ("Sintaxi incorrecta: FOR (condicio) FROM enter TO enter DO (clausules) END ")
            return
        iterador = l[1].getText()
        context[iterador] = int(l[3].getText())
        limit = int(l[5].getText())
        while(context[iterador] < limit):
             i = 7
             while(l[i].getText() != "END"):
                self.visit(l[i])
                i+=1
             context[iterador] += 1
        #Actualizar valors del context que existeixin i s'han modificat
        thisContext = self.pilaPrograma.pop()
        antContext = self.pilaPrograma[len(self.pilaPrograma)-1]
        for key in antContext.keys():
            antContext[key] = thisContext[key]


    # Visit a parse tree produced by Logos3DParser#crea_procediment.
    def visitCrea_procediment(self, ctx:Logos3DParser.Crea_procedimentContext):
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Logos3DParser#bucle_while.
    def visitBucle_while(self, ctx:Logos3DParser.Bucle_whileContext):
        l = list(ctx.getChildren())
        context = self.pilaPrograma[len(self.pilaPrograma)-1].copy()
        self.pilaPrograma.append(context)
        if l[len(l)-1].getText() != "END" or l[2].getText() != "DO":
            print ("Sintaxi incorrecta: WHILE (condicio) DO (clausules) END")
            return
        condicio = self.visit(l[1])
        while(condicio):
             i = 3
             while(l[i].getText() != "END"):
                self.visit(l[i])
                i+=1
             condicio = self.visit(l[1])
        #Actualizar valors del context que existeixin i s'han modificat
        thisContext = self.pilaPrograma.pop()
        antContext = self.pilaPrograma[len(self.pilaPrograma)-1]
        for key in antContext.keys():
            antContext[key] = thisContext[key]

    # Visit a parse tree produced by Logos3DParser#condicional.
    def visitCondicional(self, ctx:Logos3DParser.CondicionalContext):
        l = list(ctx.getChildren())
        i = 3
        context = self.pilaPrograma[len(self.pilaPrograma)-1].copy()
        self.pilaPrograma.append(context)
        if l[len(l)-1].getText() != "END" or l[2].getText() != "THEN":
            print ("Error de sintaxi en la clausula condicional: IF (condicio) THEN (clausules) END o bé IF (condicio) THEN (clausules) ELSE (clausules) END")
            return
        if (self.visit(l[1])):
            i = 3
            while l[i].getText() != "END" and l[i].getText() != "ELSE":
                self.visit(l[i])
                i+=1
        else:
            i = 3
            while l[i].getText() != "ELSE":
                i+=1
            i += 1
            while l[i].getText() != "END":
                self.visit(l[i])
                i+=1
        #Actualizar valors del context que existeixin i s'han modificat
        thisContext = self.pilaPrograma.pop()
        antContext = self.pilaPrograma[len(self.pilaPrograma)-1]
        for key in antContext.keys():
            antContext[key] = thisContext[key]

    # Visit a parse tree produced by Logos3DParser#procediment.
    def visitProcediment(self, ctx:Logos3DParser.ProcedimentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Logos3DParser#variable.
    def visitVariable(self, ctx:Logos3DParser.VariableContext):
        l = list(ctx.getChildren())
        context = self.pilaPrograma[len(self.pilaPrograma)-1]
        if context.get(l[0].getText()) == None:
            print("La variable " + l[0].getText() +" no existeix")
            return 0
        return (context[l[0].getText()])


    # Visit a parse tree produced by Logos3DParser#parametre.
    def visitParametre(self, ctx:Logos3DParser.ParametreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Logos3DParser#expr.
    def visitExpr(self, ctx:Logos3DParser.ExprContext):
        l = list(ctx.getChildren())
        context = self.pilaPrograma[len(self.pilaPrograma)-1]
        if l[0].getText() == "<<":
            print(self.visit(l[1]))
        elif l[0].getText() == ">>":
            entrada = input()
            context[l[1].getText()] = float(entrada)
        else:
            return self.visitChildren(ctx)


    # Visit a parse tree produced by Logos3DParser#eqexpr.
    def visitEqexpr(self, ctx:Logos3DParser.EqexprContext):
        l = list(ctx.getChildren())
        if len(l) == 1:
            return l[0]
        else:  # len(l) == 3
            op = l[1].getText()
            if op == '=':
                return self.visit(l[0]) == self.visit(l[2])
            if op == '>':
                return self.visit(l[0]) > self.visit(l[2])
            if op == '<':
                return self.visit(l[0]) < self.visit(l[2])    
            if op == '>=':
                return self.visit(l[0]) >= self.visit(l[2])
            if op == '<=':
                return self.visit(l[0]) <= self.visit(l[2])
            if op == '!=':
                return self.visit(l[0]) != self.visit(l[2])


    # Visit a parse tree produced by Logos3DParser#opexpr.
    def visitOpexpr(self, ctx:Logos3DParser.OpexprContext):
        l = list(ctx.getChildren())
        if len(l) == 1:
            return self.visit(l[0])
        else:  # len(l) == 3
            op = l[1].getText()
            if op == '+':
                return self.visit(l[0]) + self.visit(l[2])
            if op == '-':
                return self.visit(l[0]) - self.visit(l[2])
            if op == '*':
                return self.visit(l[0]) * self.visit(l[2])    
            if op == '/':
                return self.visit(l[0]) / self.visit(l[2])
            if op == '^':
                return pow(self.visit(l[0]), self.visit(l[2]))


del Logos3DParser

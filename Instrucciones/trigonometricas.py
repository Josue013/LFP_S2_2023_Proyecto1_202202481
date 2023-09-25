from Abstract.abstract import Expression
from math import *

class Trigonometrica(Expression):

    def __init__(self, left, tipo, fila, columna):
        self.left = left
        self.tipo = tipo
        super().__init__(fila, columna)

    def operar(self, arbol):
        leftValue = ''
        if self.left != None:
            leftValue = self.left.operar(arbol)

        operacion = self.tipo.operar(arbol)

        if operacion == 'Inverso' or operacion == 'inverso':
            resultados = round(1/leftValue,2)
            return resultados
        elif operacion == 'Seno' or operacion == 'seno':
            resultados = round(sin(radians(leftValue)), 2)
            return resultados
        elif operacion == 'Coseno' or operacion == 'coseno':
            resultados = round(cos(radians(leftValue)), 2)
            return resultados
        elif operacion == 'Tangente' or operacion == 'tangente':
            resultados = round(tan(radians(leftValue)), 2)
            return resultados
        else:
            return None            
    
    def getFila(self):
        return super().getFila()
    
    def getColumna(self):
        return super().getColumna()    

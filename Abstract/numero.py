from Abstract.abstract import Expression

class Numero(Expression):

    def __init__(self, valor, fila, columna):
        self.valor = valor
        super().__init__(fila, columna)
        
    def operar(self, arbol):
        return self.valor
    
    def getfila(self):
        return super().getFila()
    
    def getcolumna(self):
        return super().getColumna()

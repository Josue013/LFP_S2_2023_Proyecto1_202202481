from Abstract.abstract import Expression

class Error(Expression):
    def __init__(self, lexema, fila, columna):
        self.lexema = lexema
        super().__init__(fila, columna)
    
    def operar(self, no):
        lex = "Error: " + self.lexema
        return lex
    
    def getFila(self):
        return super().getFila()
    
    def getColumna(self):
        return super().getColumna()
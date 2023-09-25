from Abstract.abstract import Expression

class Aritmetica(Expression):
    def __init__(self, left, right, tipo, fila, columna):
        self.left = left
        self.right = right
        self.tipo = tipo
        super().__init__(fila, columna)

    def operar(self, arbol):
        leftValue = ''
        rightValue = ''
        if self.left != None:
            leftValue = self.left.operar(arbol)
        if self.right != None:
            rightValue = self.right.operar(arbol)    

        operacion = self.tipo.operar(arbol)

        if operacion == 'Suma' or operacion == 'suma':
            resultados = round(leftValue + rightValue,2)
            return resultados
        elif operacion == 'Resta' or operacion == 'resta':
            resultados = round(leftValue - rightValue,2)
            return resultados
        elif operacion == 'Multiplicacion' or operacion == 'multiplicacion':
            resultados = round(leftValue * rightValue,2)
            return resultados
        elif operacion == 'Division' or operacion == 'division':
            resultados = round(leftValue / rightValue,2)
            return resultados
        elif operacion == 'Potencia' or operacion == 'potencia':
            resultados = round(leftValue ** rightValue,2)
            return resultados
        elif operacion == 'Raiz' or operacion == 'raiz':
            resultados = round(leftValue ** (1/rightValue),2)
            return resultados
        elif operacion == 'Mod' or operacion == 'mod':
            resultados = round(leftValue % rightValue,2)
            return resultados
        else:
            return None
        
    def getFila(self):
        return super().getFila()
    
    def getColumna(self):
        return super().getColumna()    
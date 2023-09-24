from abc import ABC, abstractmethod

class Expression(ABC):

    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        
    @abstractmethod
    def operar(self, arbol):
        pass

    @abstractmethod
    def getfila(self):
        return self.fila

    @abstractmethod
    def getcolumna(self):
        return self.columna
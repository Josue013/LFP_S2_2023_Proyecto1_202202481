from Instrucciones.aritmeticas import *
from Instrucciones.trigonometricas import *
from Instrucciones.texto import *
from Abstract.lexema import *
from Abstract.numero import *
from Errores.Error import *


# Patron, Lexema y Token

reserved = {
    'ROPERACION'            : 'Operacion',
    'RVALOR1'               : 'Valor1',
    'RVALOR2'               : 'Valor2',
    'RSUMA'                 : 'Suma',
    'RRESTA'                : 'Resta',
    'RMULTIPLICACION'       : 'Multiplicacion',
    'RDIVISION'             : 'Division',
    'RPOTENCIA'             : 'Potencia',
    'RRAIZ'                 : 'Raiz',
    'RINVERSO'              : 'Inverso',
    'RSENO'                 : 'Seno',
    'RCOSENO'               : 'Coseno',
    'RTANGENTE'             : 'Tangente',
    'RMOD'                  : 'Modulo',
    'RCONFIGURACIONES'      : 'Configuraciones',
    'RTEXTO'                : 'Texto',
    'RFONDO'                : 'Fondo',
    'RFUENTE'               : 'Fuente',
    'RFORMA'                : 'Forma',
    'COMA'                  : ',',
    'PUNTO'                 : '.',
    'DOSPUNTOS'             : ':',
    'CORIZQ'                : '[',
    'CORDER'                : ']',
    'LLAVEIZQ'              : '{',
    'LLAVEDER'              : '}',

}

lexemas = list(reserved.values())
global n_linea
global n_columna
global instrucciones
global lista_lexemas

n_linea = 1
n_columna = 1
lista_lexemas = []
instrucciones = []
lista_errores = []

def instruccion(cadena):
    global n_linea
    global n_columna
    global lista_lexemas
    lexema = ""
    puntero = 0
    
    while cadena:
        char = cadena[puntero]
        puntero += 1
        
        if char == '\"':
            lexema, cadena = armar_lexema(cadena[puntero:])
            if lexema and cadena:
                n_columna +=1
                # Armar lexema como clase
                l = Lexema(lexema, n_linea, n_columna)
                # Agregar lexema a lista de lexemas
                lista_lexemas.append(l)
                n_columna += len(lexema) + 1
                puntero = 0
        elif char.isdigit():
            token, cadena = armar_numero(cadena)
            if token and cadena:
                n_columna +=1
                # Aqui armo mi lexema como clase
                n = Numero(token, n_linea, n_columna)
                # Aqui agregamos el lexema a la lista de lexemas
                lista_lexemas.append(n)
                n_columna += len(str(token)) + 1
                puntero = 0
        elif char == '[' or char == ']':
            # Aqui armo mi lexema como clase
            c = Lexema(char, n_linea, n_columna)
            # Aqui agregamos el lexema a la lista de lexemas
            lista_lexemas.append(c)            
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1                           
        elif char == '\t':
            n_columna += 4
            cadena = cadena[4:]
            puntero = 0
        elif char == '\n':
            cadena = cadena[1:]
            puntero = 0
            n_linea = 1
            n_columna = 1    
        elif char == ' ' or char == '\r' or char == '{' or char == '}' or char == ',' or char == '.' or char == ':':
            n_columna += 1
            cadena = cadena[1:]
            puntero = 0    
        else: 
            lista_errores.append(Error(char, n_linea, n_columna))
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1   

    return lista_lexemas
    


def armar_lexema(cadena):
    global n_linea
    global n_columna
    global lista_lexemas
    lexema = ""
    puntero = ''
    
    for char in cadena:
        puntero += char
        if char == '\"':
            return lexema, cadena[len(puntero):] 
        else:
            lexema += char
    return None, None

def armar_numero(cadena):
    token = ''
    puntero = ''
    is_decimal = False
    for char in cadena:
        puntero += char
        if char == '.':
            is_decimal = True
        if char == '"' or char == ' ' or char == '\n' or char == '\t': 
            if is_decimal:
                return float(token), cadena[len(puntero)-1:]
            else:
                return int(token), cadena[len(puntero)-1:]   
        else:
            if char != ',':
                token += char
    return None, None        

def operar():
    global lista_lexemas
    global instrucciones
    operacion = ''
    n1 = ''
    n2 = ''
    while lista_lexemas:
        lexema = lista_lexemas.pop(0)
        if lexema.operar(None) == 'operacion' or lexema.operar(None) == 'Operacion':
            operacion = lista_lexemas.pop(0)
        elif lexema.operar(None) == 'Valor1' or lexema.operar(None) == 'valor1':
            n1 = lista_lexemas.pop(0)
            if n1.operar(None) == '[':
                n1 = operar()
        elif lexema.operar(None) == 'Valor2' or lexema.operar(None) == 'valor2':
            n2 = lista_lexemas.pop(0)
            if n2.operar(None) == '[':
                n2 = operar()

        if lexema.operar(None) == 'texto':
            tipo = 'texto'
            text = lista_lexemas.pop(0)
            return Texto(text, tipo, f'Inicio: {text.getFila()}', f'Fin: {text.getColumna()}')

        if lexema.operar(None) == 'fondo':
            tipo = 'fondo'
            text = lista_lexemas.pop(0)
            return Texto(text, tipo, f'Inicio: {text.getFila()}', f'Fin: {text.getColumna()}')

        if lexema.operar(None) == 'fuente':
            tipo = 'fuente'
            text = lista_lexemas.pop(0)
            return Texto(text, tipo, f'Inicio: {text.getFila()}', f'Fin: {text.getColumna()}')

        if lexema.operar(None) == 'forma':
            tipo = 'forma'
            text = lista_lexemas.pop(0)
            return Texto(text, tipo, f'Inicio: {text.getFila()}', f'Fin: {text.getColumna()}')

        if operacion and n1 and n2:
            return Aritmetica(n1, n2, operacion, f'Inicio: {operacion.getFila()}:{operacion.getColumna()}', f'Fin: {n2.getFila()}:{n2.getColumna()}')

        elif operacion and n1 and ((operacion.operar(None) == 'inverso') or (operacion.operar(None) == 'seno') or (operacion.operar(None) == 'coseno') or (operacion.operar(None) =='tangente')):
            return Trigonometrica(n1, operacion, f'Inicio: {operacion.getFila()}:{operacion.getColumna()}', f'Fin: {n1.getFila()}:{n1.getColumna()}')
        
        elif operacion and n1 and ((operacion.operar(None) == 'Inverso') or (operacion.operar(None) == 'Seno') or (operacion.operar(None) == 'Coseno') or (operacion.operar(None) =='Tangente')):
            return Trigonometrica(n1, operacion, f'Inicio: {operacion.getFila()}:{operacion.getColumna()}', f'Fin: {n1.getFila()}:{n1.getColumna()}')
    
    return None

def operar_():
    global instrucciones
    while True:
        operacion = operar()
        if operacion:
            instrucciones.append(operacion)
        else:
            break
    
    return instrucciones

def getErrores():
    global lista_errores
    return lista_errores

entrada = '''
    {
        "operacion": "Resta"
        "Valor1": 5
        "Valor2": 2
    },
    {
        "operacion": "Suma"
        "Valor1": 4
        "Valor2": [
            "operacion": "Potencia"
            "Valor1": 2
            "Valor2": [
                "operacion": "Raiz"
                "Valor1": 9
                "Valor2": 2
                ]
        ]
    },
    {
        "operacion": "Suma"
        "Valor1": [
        "operacion": "Seno"
        "Valor1": 90
        ]
        "Valor2": 5.32
    }
    "Configuraciones": [
        {
            "texto":"Operaciones",
            "fondo":"rojo",
            "fuente":"blanco",
            "forma":"circulo"
        }
    ]
}'''

#xd


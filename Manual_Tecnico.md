# Manual Tecnico
# LAB. LENGUAJES FORMALES Y DE PROGRAMACION Sección B
## Proyecto # 1
### SEGUNDO SEMESTRE 2023
```js
Universidad San Carlos de Guatemala
Programador: Josué Nabí Hurtarte Pinto
Carne: 202202481
Correo: josuepinto013@gmail.com
```

## Librerias usadas
Este proyecto fue elaborado en python el cual cuenta con muchas librerias en este proyecto se utilizaron varias las cuales son las siguientes: os, math, abc, tkinter en las cuales se usaron messagebox, filedialog, ScrolledText, Button, Menu, sin, cos, tan, etc

## Requisitos del Sistema
* Python 3.11: Debes de tener instalado python de la versión 3 en adelante. [Link de Descarga](https://www.python.org/downloads/).
* IDE (Entorno de Desarrollo Integrado) en nuestro caso usamos el editor de texto Visual Studio Code.
* Git: Es muy recomendable un control de versiones para gestionar y no perder cambios.

# Modulos

## Interfaz
### mostrar_menu_archivo():
Al darle click salen mas opciones.
![menu](https://i.ibb.co/h2Sz81z/mostrar-menu-archivo.png)

### Abrir():
Al darle click nos saldra otra ventra donde tenemos que seleccionar el archivo JSON a leer.
![abrir](https://i.ibb.co/ySgxKBR/Abrir.png)

### guardarArchivo():
Guarda lo que tengamos

![guardarArchivo](https://i.ibb.co/4WhdpNd/guardar-Archivo.png)

### guardarComo():
Podemos guardar lo que tengamos elgiendo ruta y nombre del archivo
![guardarComo](https://i.ibb.co/FhPNrRn/guardar-Como.png)

### Analizar():
Inicia el analisis del contenido JSON haciendo las operaciones
![Analizar](https://i.ibb.co/hXDQY8G/analizar.png)

### errores():
Comprueba si hay errores y verifica y muestra los errores en un archivo JSON
![Errores](https://i.ibb.co/sqQ19qp/errores.png)

## Analizador_Lexico

### instruccion(): 
Recorre una cadena de entrada y analiza sus caracteres para identificar y construir lexemas. Luego, crea objetos de lexema correspondientes a los elementos encontrados, como cadenas, números y caracteres especiales, y los agrega a una lista de lexemas. También gestiona errores de caracteres no reconocidos.

### armar_lexema(): 
Recorre los caracteres de la cadena hasta encontrar un carácter que no forme parte del número, devolviendo el número y el fragmento restante de la cadena o Arma nuestro lexema

### armar_numero(): 
Este metodo arma nuestro numero 
### operar():
Realiza el análisis de una serie de lexemas para construir una expresión matemática o una configuración de estilo de texto. Itera sobre la lista de lexemas y, en función del tipo de lexema y su contexto, crea y devuelve objetos que representan la expresión matemática o la configuración de estilo de texto.

### operar_():
Esta funcion sera la que haga recursividad 



## aritmeticas

### Constructor
![constructor](https://i.ibb.co/zGr1bZR/constructor.png)
### Operar():
Se hacen las operaciones aritmeticas

![operar](https://i.ibb.co/BtTyXJ8/Operar.png)
### getFila() y getColumna()
![get](https://i.ibb.co/pPPmtJQ/get-Filay-Columba.png)

## texto

### Constructor
![constructor](https://i.ibb.co/LxQR0RK/Constructor-Texto.png)
### Operar_Texto():

![operarTexto](https://i.ibb.co/kyW33Sg/Operar-Texto.png)
### getFila() y getColumna()
![get](https://i.ibb.co/pPPmtJQ/get-Filay-Columba.png)


## trigonometricas

### Constructor
![constructor](https://i.ibb.co/kQmLB2d/Constructor-Tri.png)
### operar():
![operar](https://i.ibb.co/FD8Qp6G/Operar-Tri.png)
### getFila() y getColumna()
![get](https://i.ibb.co/pPPmtJQ/get-Filay-Columba.png)

## Abstracto 

En esta clase es que se uso la libreria ABC y se definieron en el constructor las filas y columnas que son vitales para leer la entrada.

### class Expression
![expression](https://i.ibb.co/YQz7zPW/Expression.png)
### class Lexema
![lexema](https://i.ibb.co/grN7y5D/Lexema.png)
### class Numero
![numero](https://i.ibb.co/9hTnh6x/Numero.png)



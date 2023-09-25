import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
from tkinter.tix import Tree
from tkinter import *
from analizador_lexico import instruccion, operar_ , getErrores



class Interfaz():
    def __init__(self, root):
        self.root = root
        self.root.title("Interfaz con Tkinter")
        self.root.configure(bg="#4169E1")

        
        # Cuadro de texto
        self.textovacio = ScrolledText(self.root, wrap=tk.WORD, width=50, height=20, font=("Times New Roman", 12))
        self.textovacio.grid(row=1, column=0, columnspan=4, padx=50, pady=50)
        self.lineaActual = 1

        # Botón Archivo
        self.btn_archivo = tk.Button(self.root, text="Archivo", command=self.mostrar_menu_archivo, padx=15, pady=10, bg="#000080", fg="white")
        self.btn_archivo.grid(row=0, column=0, pady=(30, 0))

        # Botones en la parte superior
        btn_analizar = tk.Button(self.root, text="Analizar", command=self.analizar, padx=15, pady=10, bg="#000080", fg="white")
        btn_analizar.grid(row=0, column=1, pady=(30, 0))

        btn_errores = tk.Button(self.root, text="Errores", command=self.errores, padx=15, pady=10, bg="#000080", fg="white")
        btn_errores.grid(row=0, column=2, pady=(30, 0))

        btn_reporte = tk.Button(self.root, text="Reporte", command=self.graficar, padx=15, pady=10, bg="#000080", fg="white")
        btn_reporte.grid(row=0, column=3, pady=(30, 0))

        # Menú Archivo (Inicialmente oculto)
        self.menu_archivo = tk.Menu(self.root, tearoff=0, bg="#000080", fg="white")
        self.menu_archivo.add_command(label="Abrir", command=self.Abrir)
        self.menu_archivo.add_command(label="Guardar", command=self.guardarArchivo)
        self.menu_archivo.add_command(label="Guardar Como", command=self.guardarComo)
        self.menu_archivo.add_separator()
        self.menu_archivo.add_command(label="Salir", command=self.root.quit)

    def mostrar_menu_archivo(self):
        # Muestra el menú "Archivo" como un menú emergente al hacer clic en el botón Archivo
        x, y, _, _ = self.btn_archivo.bbox("insert")
        self.menu_archivo.post(self.btn_archivo.winfo_rootx() + x, self.btn_archivo.winfo_rooty() + y)

    def Abrir(self):
        archivo = filedialog.askopenfilename(filetypes=[("Archivo JSON", "*.JSON")])
        self.root.title('Ruta - ' + archivo)
        if archivo != "":
            with open(archivo, "r") as file:
                contenido = file.read()
                self.textovacio.delete(1.0, tk.END)
                self.textovacio.insert(tk.END, contenido)
        self.data = self.textovacio.get(1.0, tk.END)    
                

    def guardarArchivo(self):
        try:
            path = self.root.title().split('-')[1][1:]   
        except:
            path=""
        
        if path != '':        
            with open(path, 'w') as f:
                content = self.textovacio.get('1.0', tk.END)
                f.write(content)  
        self.textovacio.edit_modified(0)

    def guardarComo(self):
        archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos JSON", "*.JSON")])
        if archivo:
            contenido = self.textovacio.get(1.0, tk.END)
            with open(archivo, 'w') as file:
                file.write(contenido)
            messagebox.showinfo("Archivo Guardado Correctamente ", "El archivo se guardo correctamente")


    def analizar(self):
        try:
            instrucciones = instruccion(self.data)
            respuestas = operar_()
            Resultados = ''
            Operacion = 1
            configuracion = 1
            salto = "\n"
            for respuesta in respuestas:
                if isinstance(respuesta.operar(None), int) or isinstance(respuesta.operar(None), float) == True:
                    Resultados += str(f'Operacion {Operacion} es: {respuesta.tipo.operar(None)} = {respuesta.operar(None)}\n')
                    print(respuesta.operar(None))
                    Operacion += 1
            messagebox.showinfo("Analizando...", Resultados)
        except:
            messagebox.showinfo("Error", "Ha ocurrido un error al analizar el documento")

            
        

    def errores(self):
        lista_errores = getErrores()
        noerror = 1
        archivo = open('Errores.txt', 'w', encoding="utf-8")
        archivo.write('{\n')
        archivo.write('\t"errores": [\n')
        for miserrores in lista_errores:
            error = miserrores.operar(noerror)
            noerror += 1
            print (error)
            archivo.write(error)
        archivo.write('\t\t]\n')
        archivo.write('}')
        messagebox.showinfo("Se creo el Documento", "Se encontraron: " + str(noerror - 1) + "Errores")



    def graficar(self):
        try:
            operar_().clear()
            instrucciones = instruccion(self.data)
            respuestas = operar_()
            graf_contenido = "digraph G {\n\n"
            abrir = open("Operaciones.dot", "w", encoding="utf-8")
            graf_contenido += str(Graphviz(respuestas))
            graf_contenido += '\n}'
            abrir.write(graf_contenido)
            abrir.close()
            os.environ["PATH"] += os.pathsep + 'C:\Program Files\Graphviz\bin'
            os.system('dot -Tpng Operaciones.dot -o GraficasOperaciones.png')
        except Exception as e:
            messagebox.showinfo("Se produjo un error: ", str(e))
            messagebox.showinfo("Mensaje", f"Error al generar el archivo de entrada.")
        else:
            messagebox.showinfo("Mensaje", "Grafica generada exitosamente.")
            respuestas.clear()
            instrucciones.clear()



def Graphviz(respuestas):
    Titulo = ""
    color = ""
    fuente = ""
    forma = ""
    try:
        for respuesta in respuestas:
            if isinstance(respuesta.operar(None), int) or isinstance(respuesta.operar(None), float) == True:
                pass
            else:
                temporal = str(respuesta.texto.operar(None)).lower()
                if respuesta.Operar_Texto() == "texto":
                    Titulo = str(respuesta.texto.operar(None))
                # Color de fondo
                if respuesta.Operar_Texto() == "fondo" or respuesta.Operar_Texto() == "Fondo":
                    if temporal == ("amarillo"):
                        temporal = "yellow"
                        color = temporal
                    elif temporal == ("azul"):
                        temporal = "blue"
                        color = temporal
                    elif temporal == ("rojo"):
                        temporal = "red"
                        color = temporal
                    elif temporal == ("verde"):
                        temporal = "green"
                        color = temporal
                    elif temporal == ("morado"):
                        temporal = "purple"
                        color = temporal
                    elif temporal == "naranja":
                        color = temporal
                        color = "orange"  
                    elif temporal == "rosa":
                        color = temporal
                        color = "pink" 
                    elif temporal == "gris":
                        color = temporal
                        color = "gray"         
                    else: 
                        color = "white"    
                #else:
                    #color = "white"        
                # Color de fuente
                if respuesta.Operar_Texto() == "fuente" or respuesta.Operar_Texto() == "Fuente":
                    if temporal == ("amarillo" or "yellow"):
                        temporal = "yellow"
                        fuente = temporal
                    elif temporal == ("azul" or "blue"):
                        temporal = "blue"
                        fuente = temporal
                    elif temporal == ("rojo" or "red"):
                        temporal = "red"
                        fuente = temporal
                    elif temporal == ("verde" or "green"):
                        temporal = "green"
                        fuente = temporal
                    elif temporal == ("morado" or "purple"):
                        temporal = "purple"
                        fuente = temporal
                    elif temporal == ("negro" or "black"):
                        temporal = "black"
                        fuente = temporal
                    elif temporal == ("blanco" or "white"):
                        temporal = "white"
                        fuente = temporal
                    else: 
                        fuente = "black"    
                #else:
                    #fuente = "black"        
                # Forma
                if respuesta.Operar_Texto() == "forma" or respuesta.Operar_Texto() == "Forma":
                    if temporal == ("circulo" or "circle"):
                        temporal = "circle"
                        forma = temporal
                    elif temporal == ("cuadrado" or "square"):
                        temporal = "square"
                        forma = temporal
                    elif temporal == ("triangulo" or "triangle"):
                        temporal = "triangle"
                        forma = temporal
                    elif temporal == ("rectangulo" or "box"):
                        temporal = "box"
                        forma = temporal
                    elif temporal == ("elipse" or "ellipse"):
                        temporal = "ellipse"
                        forma = temporal
                    else: 
                        forma = "circle"    
                #else:
                    #forma = "circle"        
        temporal = ''
        ColumnumIzq = 0
        ColumnumDer = 0
        Columrespuesta = 0
        ColumTotal = 0

        text = ""
        text += f"\tnode [shape={forma}]\n"
        text += f"\tnodo0 [label = \"{Titulo}\"]\n"
        text += f"\tnodo0" + "[" + f"style =filled"+ f",fillcolor = {color}" + f", fontcolor = {fuente}" + "]\n"

        for respuesta in respuestas:
            ColumnumIzq += 1
            ColumnumDer += 1
            Columrespuesta += 1
            ColumTotal += 1

            if isinstance(respuesta.operar(None), int) or isinstance(respuesta.operar(None), float) == True:
                text += f"\tnodoRespuesta{Columrespuesta}" + "[" + f"style =filled" + f",fillcolor = {color}" + f", fontcolor = {fuente}" + "]\n"
                text += f"\tnodoIzqu{ColumnumIzq}" + "[" + f"style =filled" + f",fillcolor = {color}" + f", fontcolor = {fuente}" + "]\n"
                text += f"\tnodoDere{ColumnumDer}" + "[" + f"style =filled" + f",fillcolor = {color}" + f", fontcolor = {fuente}" + "]\n"
                text += f"\tnodoT{ColumTotal}" + "[" + f"style =filled" + f",fillcolor = {color}" + f", fontcolor = {fuente}" + "]\n"

                text += f"\tnodoRespuesta{Columrespuesta}" + f"[label = \"{str(respuesta.tipo.operar(None))}" + "\"]\n"
                text += f"\tnodoIzqu{ColumnumIzq}" + "[label = \"Varlor1: " + f"{str(respuesta.left.operar(None))}" + "\"]\n"
                text += f"\tnodoDere{ColumnumDer}" + "[label = \"Valor2: " + f"{str(respuesta.right.operar(None))}" + "\"]\n"

                text += f"\tnodoRespuesta{Columrespuesta} -> nodoIzqu{ColumnumIzq}\n"
                text += f"\tnodoRespuesta{Columrespuesta} -> nodoDere{ColumnumDer}\n"

                text += f"\tnodoT{ColumTotal}" + f"[label = \"{respuesta.operar(None)}" + "\"]\n"
                text += f"\tnodoT{ColumTotal} -> nodoRespuesta{Columrespuesta}\n"
            else:
                pass
        return text
    except Exception as e:
        messagebox.showinfo("Se produjo un error: ", str(e))    

if __name__ == "__main__":
    root = tk.Tk()
    interfaz = Interfaz(root)
    root.mainloop()

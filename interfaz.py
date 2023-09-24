import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
import tkinter.ttk as ttk

class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Interfaz con Tkinter")

        
        # Cuadro de texto
        self.textovacio = ScrolledText(self.root, wrap=tk.WORD, width=50, height=10)
        self.textovacio.grid(row=1, column=0, columnspan=4, padx=50, pady=50)
        self.lineaActual = 1

        # Botón Archivo
        self.btn_archivo = tk.Button(self.root, text="Archivo", command=self.mostrar_menu_archivo, padx=15, pady=10, bg="#252525", fg="white")
        self.btn_archivo.grid(row=0, column=0, pady=(30, 0))

        # Botones en la parte superior
        btn_analizar = tk.Button(self.root, text="Analizar", command=self.analizar, padx=15, pady=10, bg="#252525", fg="white")
        btn_analizar.grid(row=0, column=1, pady=(30, 0))

        btn_errores = tk.Button(self.root, text="Errores", command=self.errores, padx=15, pady=10, bg="#252525", fg="white")
        btn_errores.grid(row=0, column=2, pady=(30, 0))

        btn_reporte = tk.Button(self.root, text="Reporte", command=self.reporte_click, padx=15, pady=10, bg="#252525", fg="white")
        btn_reporte.grid(row=0, column=3, pady=(30, 0))

        # Menú Archivo (Inicialmente oculto)
        self.menu_archivo = tk.Menu(self.root, tearoff=0, bg="#252525", fg="white")
        self.menu_archivo.add_command(label="Abrir", command=self.abrirArchivo)
        self.menu_archivo.add_command(label="Guardar", command=self.guardarArchivo)
        self.menu_archivo.add_command(label="Guardar Como", command=self.guardarComo)
        self.menu_archivo.add_separator()
        self.menu_archivo.add_command(label="Salir", command=self.root.quit)

    def mostrar_menu_archivo(self):
        # Muestra el menú "Archivo" como un menú emergente al hacer clic en el botón Archivo
        x, y, _, _ = self.btn_archivo.bbox("insert")
        self.menu_archivo.post(self.btn_archivo.winfo_rootx() + x, self.btn_archivo.winfo_rooty() + y)

    def abrirArchivo(self):
        archivo = filedialog.askopenfilename(filetypes=[("Archivo JSON", "*.JSON")])
        if archivo != "":
            with open(archivo, "r") as file:
                contenido = file.read()
                self.textovacio.delete(1.0, tk.END)
                self.textovacio.insert(tk.END, contenido)

    def guardarArchivo(self):
        archivo = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Archivos JSON", "*.JSON")])
        if archivo:
            contenido = self.textovacio.get(1.0, tk.END)
            with open(archivo, 'w') as file:
                file.write(contenido)
            messagebox.showinfo("Guardado", "Archivo guardado!")

    def guardarComo(self):
        archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos JSON", "*.JSON")])
        if archivo:
            contenido = self.textovacio.get(1.0, tk.END)
            with open(archivo, 'w') as file:
                file.write(contenido)
            messagebox.showinfo("Guardado", "Archivo guardado!")


    def analizar(self):
        pass

    def errores(self):
        pass

    def reporte_click(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    interfaz = Interfaz(root)
    root.mainloop()

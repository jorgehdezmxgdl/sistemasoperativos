import tkinter as tk
from atributos import FileManager
from tkinter import filedialog

class Ventana:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Explorador de archivos")
        self.ventana.geometry("600x300")
        self.crear_etiqueta("Escribe la trayectoria a analizar", 10, 10, 170, 20)
        self.crear_campoTexto(190, 10, 200, 20)
        self.crear_boton("Analizar", 400, 10, 150, 20, self.evento_boton)
        self.ventana.mainloop()

    def crear_etiqueta(self, texto, x, y, width, height):
        self.etiqueta = tk.Label(self.ventana, text=texto)
        self.etiqueta.place(x=x, y=y, width=width, height=height)

    def crear_campoTexto(self, x, y, width, height):
        self.campoTexto = tk.Entry(self.ventana)
        self.campoTexto.place(x=x, y=y, width=width, height=height)

    def crear_boton(self, texto, x, y, width, height, evento):
        self.boton = tk.Button(self.ventana, text=texto, command=evento)
        self.boton.place(x=x, y=y, width=width, height=height)

    def evento_boton(self):
        ruta_archivo = filedialog.askopenfilename(
            title="Selecciona un archivo",
            filetypes=[
                ("Todos los archivos", "*.*")
            ]
        )
        if not ruta_archivo:
            print("No seleccionaste nada")
        else:
            file_manager = FileManager()
            file_manager.investigaPropiedad(ruta_archivo)

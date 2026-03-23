import tkinter as tk

class ProcesosUI:
    def __init__(self, padre):
        self.ventana = tk.Toplevel(padre)
        self.ventana.title("Procesos e Hilos")
        self.ventana.geometry("800x600")
        self.ventana.resizable(False, False)
        self.label1 = self.creaLabel(10, 10, 150, 50, "Procesos e Hilos")
        self.label2 = self.creaLabel(10, 60, 150, 50, "Procesos")
        self.boton1 = self.creaBoton(10, 120, 150, 50, "Crear Proceso")
        self.label3 = self.creaLabel(10, 180, 150, 50, "Hilos")
        self.boton2 = self.creaBoton(10, 240, 150, 50, "Crear Hilo")

    def creaBoton(self, x, y, width, height, texto):
        boton = tk.Button(self.ventana, text=texto)
        boton.place(x=x, y=y, width=width, height=height)
        return boton

    def creaLabel(self, x, y, width, height, texto):
        label = tk.Label(self.ventana, text=texto)
        label.place(x=x, y=y, width=width, height=height)
        return label


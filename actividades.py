import tkinter as tk
from procesosui import ProcesosUI

class Actividades:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Actividades de un S.O.")
        self.ventana.geometry("800x100")
        self.ventana.resizable(False, False)
        self.boton1 = self.creaBoton(10, 10, 150, 50,  "Procesos e Hilos", self.abreVentanaProcesos)
        self.boton2 = self.creaBoton(170, 10, 150, 50, "Planificadores",None)
        self.ventana.mainloop()

    def abreVentanaProcesos(self):
        ProcesosUI(self.ventana)

    def creaBoton(self, x, y, width, height, texto, evento):
        boton = tk.Button(self.ventana, text=texto, command=evento)
        boton.place(x=x, y=y, width=width, height=height)
        return boton

actividades = Actividades()
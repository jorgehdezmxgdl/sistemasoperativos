"""
   INCORPORE EL MECANISMO DE COLA PARA INSERTAR Y MOSTRAR UN ELEMENTO
   EN LA INTERFAZ GRAFICA.
"""

import tkinter as tk
from tkinter import ttk

class Ventana():
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Un OS v0.1")
        self.ventana.geometry("500x500")
        self.creaCombo(["Selecciona:", "Crear Proceso", "Iniciar Proceso", "Suspender Proceso", "Reanudar Proceso", "Terminar Proceso"])
        self.ventana.mainloop()

    def creaCombo(self, listado):
        self.combo = ttk.Combobox(self.ventana)
        self.combo['values'] = listado
        self.combo.current(0)
        self.combo.place(x=20, y=20)
        self.combo.bind("<<ComboboxSelected>>", self.eventoCombo)

    def eventoCombo(self, event):
        opcion = self.combo.get()
        if opcion == "Terminar Proceso":
            exit()


ventana = Ventana()

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
        self.creaEtiqueta("Dame el dato a registrar", 20, 50, 200, 20)
        self.creaEntrada(20, 80, 200, 20)
        self.creaBoton("Registrar", 20, 110, 200, 20)
        self.creaBoton("Regresa elemento", 20, 140, 200, 20)
        self.creaTextArea(20, 170, 200, 200)
        self.ventana.mainloop()

    def creaEtiqueta(self, texto, x, y, width, height):
        self.etiqueta = tk.Label(self.ventana, text=texto)
        self.etiqueta.place(x=x, y=y, width=width, height=height)

    def creaEntrada(self, x, y, width, height):
        self.entrada = tk.Entry(self.ventana)
        self.entrada.place(x=x, y=y, width=width, height=height)
        
    def creaBoton(self, texto, x, y, width, height):
        self.boton = tk.Button(self.ventana, text=texto)
        self.boton.place(x=x, y=y, width=width, height=height)

    def creaTextArea(self, x, y, width, height):
        self.textArea = tk.Text(self.ventana)
        self.textArea.place(x=x, y=y, width=width, height=height)

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

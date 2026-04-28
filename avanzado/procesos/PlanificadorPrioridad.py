from Proceso import Proceso
import random

class Prioridad:

    def __init__(self):
        self.lista    = []
        self.contador = 1

    def getProcesoXPrioridad(self, prioridad):
        for proceso in self.lista:
            if proceso.getPrioridad() == prioridad:
                self.lista.remove(proceso)
                return proceso
        return None

    def insertaProceso(self):
        proceso = Proceso()
        proceso.creaProceso(f"P{self.contador}",[])
        prioridad = random.choice(["M", "A", "B"])
        proceso.setPrioridad(prioridad)
        self.lista.append(proceso)
        self.contador += 1

    def ejecutaAlgoritmo(self):
        for _ in range(50):
            self.insertaProceso()
        for elemento in self.lista:
            print(f"Proceso: {elemento.nombre} Prioridad:{elemento.getPrioridad()}")
       
        while True:
            proceso = self.getProcesoXPrioridad("A")
            if not proceso:
                proceso = self.getProcesoXPrioridad("M")
            if not proceso:
                proceso = self.getProcesoXPrioridad("B")
            if proceso:
                print(f"Ejecutando proceso: {proceso.nombre} con prioridad {proceso.getPrioridad()}")
            

prioridad = Prioridad()
prioridad.ejecutaAlgoritmo()
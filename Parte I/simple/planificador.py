import random
from proceso import Proceso
class Planificador:

    def __init__(self):
        self.lista = []

    def adiciona_proceso(self, proceso):
        self.lista.append(proceso)
        
    def inicia_ejecucion(self):
        while len(self.lista) != 0:
            proceso   = self.lista.pop(0)
            if not proceso.ejecuta():
                self.lista.append(proceso)
            

class GeneradorProcesos:

    def genera(self, posicion):
        operador1 = random.randint(1, 1000)
        operador2 = random.randint(1001, 2000)
        operacion = random.choice(["+", "-", "*", "/"])
        tiempo    = random.randint(1, 5)
        nombre    = "P" + str(posicion)
        print(f"Generando proceso: {operador1} {operacion} {operador2} tiempo de ejecucion: {tiempo}")
        return Proceso(nombre, operador1, operacion, operador2, tiempo)
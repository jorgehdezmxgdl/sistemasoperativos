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
            resultado = proceso.ejecuta()
            print(f"El resultado es: {resultado}")

class GeneradorProcesos:

    def genera(self):
        operador1 = random.randint(1, 1000)
        operador2 = random.randint(1001, 2000)
        operacion = random.choice(["+", "-", "*", "/"])
        tiempo    = random.randint(1, 5)
        print(f"Generando proceso: {operador1} {operacion} {operador2} tiempo_espera: {tiempo}")
        return Proceso(operador1, operacion, operador2, tiempo)
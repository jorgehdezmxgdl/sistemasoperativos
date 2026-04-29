import time

class Proceso:
    def __init__(self,operador1, operacion, operador2, tiempo):
        self.operador1 = operador1
        self.operacion = operacion
        self.operador2 = operador2
        self.tiempo    = tiempo
        self.resultado = None
        self.cambiaEstado("Creado")

    def cambiaEstado(self, estado):
        self.estado = estado
        print(self.estado)
    
    def ejecuta(self):
        self.cambiaEstado("En ejecucion")
        if self.operacion == "+":
            self.resultado = self.operador1 + self.operador2           
        elif self.operacion == "-":
            self.resultado = self.operador1 - self.operador2
        elif self.operacion == "*":
            self.resultado = self.operador1 * self.operador2
        elif self.operacion == "/":
            self.resultado = self.operador1 / self.operador2
        self.cambiaEstado("En espera")
        time.sleep(self.tiempo)
        self.cambiaEstado("En ejecucion")
        self.cambiaEstado("Terminado")
        return self.resultado



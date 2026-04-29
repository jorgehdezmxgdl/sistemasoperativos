import time

class Proceso:
    def __init__(self,nombre, operador1, operacion, operador2, tiempo):
        self.operador1 = operador1
        self.operacion = operacion
        self.operador2 = operador2
        self.tiempo    = tiempo
        self.resultado = None
        self.contador  = 0
        self.nombre    = nombre
        self.cambiaEstado("Creado")

    def cambiaEstado(self, estado):
        self.estado = estado
        print(f"El proceso {self.nombre} ha cambiado de estado: {self.estado}")
    
    def ejecuta(self):
        if self.contador < self.tiempo:
            self.cambiaEstado("En ejecucion")
            self.contador += 1
            time.sleep(0.5)
            if self.contador == self.tiempo:
                if self.operacion == "+":
                    self.resultado = self.operador1 + self.operador2           
                elif self.operacion == "-":
                    self.resultado = self.operador1 - self.operador2
                elif self.operacion == "*":
                    self.resultado = self.operador1 * self.operador2
                elif self.operacion == "/":
                    self.resultado = self.operador1 / self.operador2
                print(f"{self.nombre}: {self.operador1} {self.operacion} {self.operador2} = {self.resultado}")
                self.cambiaEstado("Terminado")
                return True
            else:
                self.cambiaEstado("En espera")
            return False


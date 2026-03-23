import threading
from pcb import PCB

class Proceso():
    def __init__(self):
        self.proceso = []
        self.args = []
        self.nombre = []
        self.pcb = PCB()

    def creaProceso(self, nombre,args):
        self.nombre.append(nombre)
        self.args.append(args)
        self.pcb.pid = self.pcb.pid + 1
        self.pcb.estado = "L"


    def iniciarProceso(self): 
        for i in range(self.nombre.count):
            self.pcb.asigna_registros(self.args[i])
            self.proceso.add(threading.Thread(target=self.nombre[i], args=self.args[i]))
            
    def ejecutaProceso(self, posicion):
        if self.proceso[posicion]:
            self.pcb.estado = "E"
            self.proceso[posicion].start()
        else:
            print("El proceso no existe")

    def esperaEvento(self):
        self.pcb.estado = "B"

    def esperaProcesoParaTerminarlo(self, posicion):
        if self.proceso[posicion]:
            self.proceso[posicion].join()
        else:
            print("El proceso no existe")


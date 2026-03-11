import threading

class Proceso():
    def __init__(self):
        self.proceso = []
        self.args = []
        self.nombre = []

    def creaProceso(self, nombre,args):
        self.nombre.append(nombre)
        self.args.append(args)

    def iniciarProceso(self): 
        for i in range(self.nombre.count):
            self.proceso.add(threading.Thread(target=self.nombre[i], args=self.args[i]))
            
    def ejecutaProceso(self, posicion):
        if self.proceso[posicion]:
            self.proceso[posicion].start()
        else:
            print("El proceso no existe")

    def esperaProceso(self, posicion):
        if self.proceso[posicion]:
            self.proceso[posicion].join()
        else:
            print("El proceso no existe")
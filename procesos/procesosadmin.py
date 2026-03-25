import threading
import time
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Estructura.procesamiento import EstructuraCola

class AdministradorProcesos:
    def __init__(self, tamanio):
        self.listado_procesos = []
        self.TAMANIO = tamanio
        self.cola = EstructuraCola(self.TAMANIO)

    def insertar_proceso(self, proceso):
        if not self.cola.nuevo_item(proceso):
            self.listado_procesos.append(proceso)
            print("Proceso adicionado correctamente")
        else:
            print("Cola llena")
        
    def regresa_sig_proceso(self):
        proceso_temp = self.cola.regresa_sig_item()
        if proceso_temp:
            self.listado_procesos.remove(proceso_temp)
            return proceso_temp
        else:
            return None 

    def ejecuta_planificador(self):
        while True:
            proceso = self.regresa_sig_proceso()
            if proceso:
                print("Estoy procesando: ", proceso)
                time.sleep(1)

    def iniciaPlanificacion(self):
        hilo = threading.Thread(target=self.ejecuta_planificador)
        hilo.start()

a = AdministradorProcesos(20)
a.insertar_proceso("Proceso 1")
a.insertar_proceso("Proceso 2")
a.insertar_proceso("Proceso 3")
a.insertar_proceso("Proceso 4")
a.iniciaPlanificacion()
a.insertar_proceso("Proceso 5")
a.insertar_proceso("Proceso 6")
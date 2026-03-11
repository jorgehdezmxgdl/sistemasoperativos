import queue

class EstructuraCola:
    def __init__(self, tamanio):
        self.cola = queue.Queue(maxsize=tamanio) #el maximo de elementos de la cola

    def nuevo_item(self, item):
        print("No es posible registrar mas elementos") if self.cola.full() else self.cola.put(item)
        
    def regresa_sig_item(self):
        return None if self.cola.empty() else self.cola.get()

    def regresa_todos(self):
        while not self.cola.empty():
            print(self.cola.get())

estructura = EstructuraCola(2)
estructura.nuevo_item('proceso 1')
estructura.nuevo_item('proceso 2')
estructura.nuevo_item('proceso 3')
print(estructura.regresa_sig_item())
print(estructura.regresa_sig_item())
print(estructura.regresa_sig_item())

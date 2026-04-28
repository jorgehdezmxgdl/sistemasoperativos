import queue

class EstructuraCola:
    def __init__(self, tamanio):
        self.cola = queue.Queue(maxsize=tamanio) #el maximo de elementos de la cola

    def nuevo_item(self, item):
        if self.cola.full():
            return True
        else:
            self.cola.put(item)
            return False
        
    def regresa_sig_item(self):
        return None if self.cola.empty() else self.cola.get()

    def regresa_todos(self):
        cadena = ""
        while not self.cola.empty():
            cadena += self.cola.get() + "\n"
        return cadena


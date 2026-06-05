import time
import random
import threading

class BufferLimitado:
    """
    Representa el recurso compartido (Buffer) con capacidad finita.
    Utiliza semáforos para garantizar que el productor no inserte en un buffer lleno
    y el consumidor no retire de un buffer vacío.
    """
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.buffer = []
        
        # Semáforos de sincronización (Nombres alineados con la teoría de SO)
        self.mutex = threading.Semaphore(1)       # Exclusión mutua para modificar la lista
        self.vacios = threading.Semaphore(capacidad) # Cuenta los espacios libres disponibles
        self.llenos = threading.Semaphore(0)        # Cuenta los elementos listos para consumir

    def insertar(self, elemento, nombre_productor):
        # 1. Esperar a que exista al menos un espacio vacío
        self.vacios.acquire()
        
        # 2. Bloquear el acceso exclusivo al buffer (Sección Crítica)
        self.mutex.acquire()
        
        # --- SECCIÓN CRÍTICA ---
        self.buffer.append(elemento)
        print(f"[+] {nombre_productor} insertó: {elemento} | Buffer actual: {self.buffer}")
        # ------------------------
        
        # 3. Liberar el mutex y notificar que hay un nuevo elemento lleno
        self.mutex.release()
        self.llenos.release()

    def remover(self, nombre_consumidor):
        # 1. Esperar a que exista al menos un elemento lleno
        self.llenos.acquire()
        
        # 2. Bloquear el acceso exclusivo al buffer (Sección Crítica)
        self.mutex.acquire()
        
        # --- SECCIÓN CRÍTICA ---
        elemento = self.buffer.pop(0)
        print(f"[-] {nombre_consumidor} consumió: {elemento} | Buffer actual: {self.buffer}")
        # ------------------------
        
        # 3. Liberar el mutex y notificar que se liberó un espacio vacío
        self.mutex.release()
        self.vacios.release()
        
        return elemento


class Productor(threading.Thread):
    """Representa el hilo encargado de generar datos de manera concurrente."""
    def __init__(self, buffer_compartido, nombre):
        super().__init__()
        self.buffer_compartido = buffer_compartido
        self.nombre = nombre

    def run(self):
        while True:
            # Simula tiempo de producción aleatorio
            time.sleep(random.uniform(0.5, 1.5))
            item = random.randint(10, 99) # Produce un número de dos dígitos
            
            self.buffer_compartido.insertar(item, self.nombre)


class Consumidor(threading.Thread):
    """Representa el hilo encargado de procesar o consumir los datos del buffer."""
    def __init__(self, buffer_compartido, nombre):
        super().__init__()
        self.buffer_compartido = buffer_compartido
        self.nombre = nombre

    def run(self):
        while True:
            # Simula tiempo de procesamiento del elemento consumido
            time.sleep(random.uniform(0.8, 2.0))
            
            self.buffer_compartido.remover(self.nombre)


# --- EJECUCIÓN PRINCIPAL DEL ESCENARIO ---
if __name__ == "__main__":
    print("=== Iniciando Simulación de Buffer Limitado (Presiona Ctrl+C para salir) ===")
    
    # Configuración del escenario: Buffer con capacidad máxima de 3 elementos
    CAPACIDAD_MAXIMA = 3
    buffer_comun = BufferLimitado(CAPACIDAD_MAXIMA)

    # Creación de hilos (Objetos cooperativos concurrentes)
    hilo_productor_1 = Productor(buffer_comun, "Productor_A")
    hilo_productor_2 = Productor(buffer_comun, "Productor_B")
    hilo_consumidor_1 = Consumidor(buffer_comun, "Consumidor_X")

    # Configuración como daemon para que el script termine limpiamente al cerrar la consola
    hilo_productor_1.daemon = True
    hilo_productor_2.daemon = True
    hilo_consumidor_1.daemon = True

    # Inicialización de la ejecución concurrente
    hilo_productor_1.start()
    hilo_productor_2.start()
    hilo_consumidor_1.start()

    # Mantener el hilo principal vivo para observar la salida en terminal
    try:
        while True:
            time.sleep(0.3)
    except KeyboardInterrupt:
        print("\n=== Simulación finalizada por el usuario ===")
import time
import random
import threading

class Palillo:
    """
    Representa un palillo en la mesa. 
    Se modela usando un Semáforo binario para asegurar que solo un filósofo
    pueda usarlo a la vez.
    """
    def __init__(self, id_palillo):
        self.id = id_palillo
        # Un semáforo con valor 1 actúa como un cerrojo exclusivo (Mutex)
        self._semaforo = threading.Semaphore(1)

    def tomar(self, nombre_filosofo):
        self._semaforo.acquire()
        # El logging nos ayuda a rastrear el estado de la sección crítica
        # print(f"   [Palillo {self.id}] tomado por {nombre_filosofo}")

    def soltar(self, nombre_filosofo):
        self._semaforo.release()
        # print(f"   [Palillo {self.id}] liberado por {nombre_filosofo}")


class Filosofo(threading.Thread):
    """
    Representa a un filósofo como un hilo de ejecución concurrente.
    """
    def __init__(self, id_filosofo, palillo_izquierdo, palillo_derecho, es_el_ultimo=False):
        super().__init__()
        self.id = id_filosofo
        self.nombre = f"Filósofo {id_filosofo}"
        self.palillo_izquierdo = palillo_izquierdo
        self.palillo_derecho = palillo_derecho
        self.es_el_ultimo = es_el_ultimo

    def pensar(self):
        print(f"[O] {self.nombre} está pensando...")
        time.sleep(random.uniform(1.0, 3.0))

    def comer(self):
        print(f"[#] {self.nombre} ¡está COMIENDO con ambos palillos!")
        time.sleep(random.uniform(1.0, 2.0))

    def run(self):
        """Ciclo de vida infinito del filósofo."""
        while True:
            self.pensar()
            
            print(f"[?] {self.nombre} tiene hambre y busca palillos.")
            
            # --- ESTRATEGIA PARA EVITAR DEADLOCK (ASIMETRÍA) ---
            if self.es_el_ultimo:
                # El último filósofo rompe el ciclo tomando primero el derecho
                self.palillo_derecho.tomar(self.nombre)
                self.palillo_izquierdo.tomar(self.nombre)
            else:
                # Los demás filósofos toman primero el izquierdo
                self.palillo_izquierdo.tomar(self.nombre)
                self.palillo_derecho.tomar(self.nombre)
            
            # --- SECCIÓN CRÍTICA ---
            self.comer()
            # -----------------------
            
            # Devolver los recursos en cualquier orden seguro
            self.palillo_izquierdo.soltar(self.nombre)
            self.palillo_derecho.soltar(self.nombre)
            
            print(f"[V] {self.nombre} terminó de comer y soltó los palillos.")


# --- CONFIGURACIÓN E INICIACIÓN DEL ESCENARIO ---
if __name__ == "__main__":
    print("=== Iniciando la cena de los filósofos (Presiona Ctrl+C para salir) ===")
    
    CANTIDAD_FILOSOFOS = 5
    
    # 1. Crear los 5 palillos disponibles en la mesa
    palillos = [Palillo(i) for i in range(CANTIDAD_FILOSOFOS)]
    
    filosofos = []
    
    # 2. Instanciar los filósofos asignándoles sus respectivos palillos vecinos
    for i in range(CANTIDAD_FILOSOFOS):
        izquierdo = palillos[i]
        derecho = palillos[(i + 1) % CANTIDAD_FILOSOFOS] # Compartido de forma circular
        
        # El último filósofo (id == 4) se marca especialmente para romper la espera circular
        es_ultimo = (i == CANTIDAD_FILOSOFOS - 1)
        
        filosofo = Filosofo(i, izquierdo, derecho, es_el_ultimo=es_ultimo)
        filosofos.append(filosofo)
    
    # 3. Lanzar los hilos en segundo plano (daemon)
    for f in filosofos:
        f.daemon = True
        f.start()

    # Mantener el hilo principal despierto para ver la ejecución interactiva en consola
    try:
        while True:
            time.sleep(0.3)
    except KeyboardInterrupt:
        print("\n=== La cena ha concluido ===")
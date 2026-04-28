from planificador import GeneradorProcesos, Planificador

planificador = Planificador()
generador    = GeneradorProcesos()

print("Generando procesos.....")
for _ in range(10):
    proceso = generador.genera()
    planificador.adiciona_proceso(proceso)

print("Iniciando el planificador.....")
planificador.inicia_ejecucion()


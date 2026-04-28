import threading

def ejecuta_tarea_segundo_plano(limite):
    print("Proceso en ejecucion")
    resultado = 0
    for i in range(limite):
        for j in range(limite):
            for k in range(limite):
                resultado += 1
    print(f"Resultado: {resultado}")

print("Proceso creado")
proceso1 = threading.Thread(target=ejecuta_tarea_segundo_plano, args=(999,))
print("Proceso listo")
proceso1.start()
print("Continua con la ejecucion del programa")
proceso1.join()
print("Proceso terminado")

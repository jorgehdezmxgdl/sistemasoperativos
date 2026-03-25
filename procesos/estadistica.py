class Estadistica:
    def __init__(self):
      self.tiempo_cpu = 0
      self.tiempo_llegada = 0
      self.tiempo_finalizacion = 0
      self.tiempo_retorno = 0
      self.throughput = 0

    def calcula_tiempo_retorno(self):
        return self.tiempo_finalizacion - self.tiempo_llegada
    
    def calcula_tiempo_espera(self):
        return self.tiempo_retorno - self.tiempo_cpu

    def calcula_tiempo_respuesta(self, tiempo_primera_ejecucion):
        return tiempo_primera_ejecucion - self.tiempo_llegada

    def incrementa_throughput(self, tiempo):
        self.throughput += tiempo
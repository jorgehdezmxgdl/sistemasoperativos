class PCB:
    def __init__(self):
        self.pid = 0
        self.estado = "N"
        self.contador_programa = 0
        self.contador_registros = 0
        self.registros = { #diccionario
            'AL': 0,
            'AH': 0,
            'BL': 0,
            'BX': 0
        }
        self.prioridad = 1; #0 baja, 1 normal, 2 alta
        self.recursos = {
            'impresora': False,
            'disco': False,
            'memoria_ram': False,
            'memoria_virtual': False,
            'usb': False,
            'hdmi': False,
            'audio': False,
            'corriente': False,
            'mousetrack': False
        }
        self.limites_memoria = {
            'memoria_ram': 1024,
            'memoria_virtual': 2048
        }

    def asigna_registros(self, valor):
        if valor is None:
            return
        if self.contador_registros == 0:
            self.registros['AL'] = valor           
        elif self.contador_registros == 1:
            self.registros['AH'] = valor
        elif self.contador_registros == 2:
            self.registros['BL'] = valor
        elif self.contador_registros == 3:
            self.registros['BX'] = valor
        else:
            print("No hay mas registros")
        if self.contador.registros <= 3:
            self.contador_registros += 1

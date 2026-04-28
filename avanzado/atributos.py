from os import stat
import os
from pathlib import Path

class FileManager:
    def investigaPropiedad(self, ruta_archivo):
        ruta = Path(ruta_archivo)
        if not ruta.exists():
            print("La ruta no existe")
        else:
            if ruta.is_dir():
                print("es un directorio")
            elif ruta.is_file():
                informacion = ruta.stat()
                print(f"Tamaño del archivo: {informacion.st_size} bytes")
                try:
                    informacion = os.stat(ruta)
                    permisos = stat.S_IMODE(informacion.st_mode)
                    print(f"En formato octal: {oct(permisos)}")
                    print(f"En formato binario: {bin(permisos)}")
                    print(f"En formato decimal: {permisos}")
                except Exception as e:
                    print(f"Sistema operativo no compatible")
                
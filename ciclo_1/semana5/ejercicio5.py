# creación de archivos txt

ruta = r'C:\Users\israelarbonaguerrero\Desktop\RUTA2_MISIONTIC_2022\grupo_37\ciclo_1\semana5\archivo.txt'

# Crear o escritura el archivo txt
fichero = open(ruta,'w')

# Agregar informacion al final del archivo txt
fichero = open(ruta,'a')

# Solo lectura de un archivo txt
fichero = open(ruta, 'r')

fichero.close()
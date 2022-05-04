# Try y Except

temperatura_fahr = input('Ingrese la temperatura en grados Fahrenheit ')
try:
    fahr = float(temperatura_fahr)
    cel = (((fahr - 32.0) * 5.0) / 9.0)
    print(cel)
except:
    print('No ingreso ningún número, gracias')
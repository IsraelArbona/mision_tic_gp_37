def ordenes(rutinaContable):
    # Importar la función reduce desde la libreia functools
    from functools import reduce

    # Declarar una constante
    ordenMinima = 600000

    # Suma total de cada tupla de cada lista
    ordenTotal = list( map( lambda x: [x[0]] + list( map(lambda y: y[1]*y[2],x[1:]) ),rutinaContable ) )
    # Suma los totales de todas las tuplas de todas las listas.
    ordenTotal = list( map( lambda x: [x[0]] + [ reduce(lambda a,b: round(a+b,2),x[1:]) ], ordenTotal ) )
    # suma el incremento si la compra no llega al minimo de 600000
    ordenTotal = list( map( lambda x: x if x[1] >= ordenMinima else (x[0], x[1] + 25000), ordenTotal ) )

    print('------------------------ Inicio Registro diario ---------------------------------')
    # Ciclo para imprimir el total de cada factura
    for x in range(len(ordenTotal)):
        print(f'La factura {ordenTotal[x][0]} tiene un total en pesos de {ordenTotal[x][1]:,.2f}')
    print('-------------------------- Fin Registro diario ----------------------------------')



# Pruebas

'''
rutinaContable = [
 [1201, ("5464", 4, 25842.99), ("7854",18,23254.99), ("8521", 9, 48951.95)],
 [1202, ("8756", 3, 115362.58),("1112",18,2354.99)],
 [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20),("9965", 5, 1645.20)],
 [1204, ("9635", 7, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)]
]

print(ordenes(rutinaContable))
'''


'''
    [
        [1201, 103371.96, 418589.82, 440567.55], 
        [1202, 346087.74, 42389.81999999999], 
        [1203, 125698.2, 271290.4, 13645.2, 8226.0], 
        [1204, 83.93, 208.89, 1954.75]
    ]

[
    [1201, 962529.33], 
    [1202, 388477.56], 
    [1203, 418859.8], 
    [1204, 2247.57]
]

[
    [1201, 962529.33], 
    (1202, 413477.56), 
    (1203, 443859.8),
    (1204, 27247.57)
]

[
    [1201, 962529.33], 
    [1202, 413477.56], 
    [1203, 443859.8], 
    [1204, 27247.57]
]

'''
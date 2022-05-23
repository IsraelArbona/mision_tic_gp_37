def AutoPartes(ventas: list):
    # inicializar el diccionario
    venta = {}

    # ciclo para agregar un nuevo evento
    for idProducto, dProducto, pnProducto, cvProducto,sProducto, nComprador, cComprador,fVenta in ventas:
        # Forzar la entrada
        if venta.get(idProducto) == None:
            #Crecación de un nuevo evento
            venta[idProducto] = []
            # Registro de una nueva lista de tuplas en el dict venta
        venta[idProducto].append((dProducto,pnProducto,cvProducto,sProducto,nComprador,cComprador,fVenta))
    return venta

# Definir la consulta
def consultaRegistro(ventas, idProducto):
    #Ubicar una fecha dentro de las ventas
    if idProducto in ventas:
        for dProducto, pnProducto,cvProducto,sProducto, nComprador, cComprador,fVenta in ventas[idProducto]:
            print('Producto consultado :',idProducto, ' Descripción ', dProducto, ' #Parte ', pnProducto, ' Cantidad vendida ', cvProducto,' Stock ',sProducto, ' Comprador',nComprador, ' Documento ', cComprador,' Fecha Venta ', fVenta)
    else:
        print("No hay registro de venta de ese producto")


'''
consultaRegistro(AutoPartes([
    (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
    (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
    (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
    (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
    (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')]), 2010)
print()
'''
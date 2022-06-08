import pandas as pd

# rutaFileCsv -> ruta del archivo
rutaFileCsv = 'https://raw.githubusercontent.com/luisguillermomolero/MisionTIC2022_2/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv'

def listaPeliculas(rutaFileCsv: str)->str:

    # print(rutaFileCsv.split('.')[-1])
    if rutaFileCsv.split('.')[-1] == 'csv':
        
        try:
            # Leer el archivo csv
            arc_csv = pd.read_csv(rutaFileCsv)
            # print(type(arc_csv))

            # Se crea un subconjunto con las columnas 'Country', 'Language' e 'Gross Earnings'
            subGrupoPeliculas = arc_csv[['Country','Language','Gross Earnings']]
            #print(subGrupoPeliculas)

            ganaciaPaisLenguaje = subGrupoPeliculas.pivot_table(index=['Country','Language'])
            return ganaciaPaisLenguaje.head(10)

        except:
            print('Error al leer el archivo de datos.')
    else:
        print('Extensión inválida.')

print(listaPeliculas(rutaFileCsv))
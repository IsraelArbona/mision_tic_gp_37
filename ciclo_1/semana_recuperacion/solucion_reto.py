def CDT(usuario: str, capital: int, tiempo: int):
    porcentaje_interes = 0.03
    porcentaje_aperder = 0.02


    if tiempo > 2:
        valor_interes = (capital * porcentaje_interes * tiempo) / 12
        valor_total = capital + valor_interes
    else:
        valor_aperder = capital * porcentaje_aperder
        valor_total = capital - valor_aperder

    return 'Para el usuario ' + str(usuario) + ' La cantidad de dinero, según el monto inicial ' \
           + str(capital) + ' para un tiempo de '+ str(tiempo) + ' meses es: ' + str(valor_total)

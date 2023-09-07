#HAZ UNA FUCNION RECURSIVA QUE CALCULE LA POTENCIA DE UN NUMERO base ELEVADO A UN EXPONENTE NO NEGATIVO exponente. Y NO PUEDES UTILIZAR OPERADORES COMO (**) NI FUNCIONES PREDEFINIDAS PARA CALCULAR LA POTENCIA.

def potencia(base, exponente):
    if exponente < 0 or base < 0:
        return None
    elif exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
        
print(potencia(2,-1))




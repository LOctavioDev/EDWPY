#COMO CREAR LOS TIPOS DE EXCEPCIONES

import math

class NegativeNumber(Exception):
    "EXCEPCION DE TIPO NUMERO NEGATIVO"
    pass

def raiz_cuadrada(number):
    if number < 0:
        raise NegativeNumber("NUMERO NEGATIVO")
    return math.sqrt(number)

print(raiz_cuadrada(-1))
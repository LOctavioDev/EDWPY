import math

def raiz_cuadrada(number):
    if number < 0:
        raise ValueError('NUMERO NEGATIVO')  #RAISE ES PARA LEVANTAR EXCEPCIONES
    return math.sqrt(number)

print(raiz_cuadrada(-1))
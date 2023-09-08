# #Escribe una función recursiva que cuente y devuelva la cantidad de dígitos en un número entero positivo. Debes implementar esta función utilizando recursión, y no puedes convertir el número en una cadena de texto para resolverlo.

def conteo_digitos(numero):
    if numero >= 0 and numero < 10:
        return 1
    else:
        numero_sin_ultimo_digito = numero // 10  
        return 1 + conteo_digitos(numero_sin_ultimo_digito)


print(conteo_digitos(12345))  



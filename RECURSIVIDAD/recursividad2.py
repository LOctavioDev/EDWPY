#USANDO UNA FUNCION RECURSIVA CALCULAR TODOS LOS NUMEROS DESDE 1 HASTA UN NUMERO DADO.

def sumar_Numeros(n):
    if n == 1:
        return 1
    else:
        return n + sumar_Numeros(n -1 )
    
print(sumar_Numeros(5))


#CASO SON RECURSIVIDAD:
def sumar_numeros_normales(n):
    suma = 0
    for numero in range(1, n+1):
        suma += numero
    return suma

print(sumar_numeros_normales(5))
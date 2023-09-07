#LA RECURSIVIDAD ES UNA FUNCION QUE SE LLAMA A SI MISMA PARA RESOLVER UN PROBLEMA, CON LOA CONDICION DE QUE CADA LLAMADA RECURSIVA REDUZCA EL PROBLEMA HACIOA UN CASO LLAMADO: "CASO BASE"

#EJEMPLO DE UNA FUCNION RECURSIVA PARA CALCULAR EL FACTORIAL DE UN NUMERO
def factorial(n):
    #DEFINIR EL CASO BASEEL CUAL ES: SI n ES 0 O 1, EL FACTORIAL SERA 1
    if n == 0 or n == 1:
        return 1
    #CASO RECURSIVO EL FACTORIAL DE n ES n MULTIPLICADO POR EL FACTORIAL DE (n-1)
    else:
        return n * factorial(n - 1)


print(factorial(5))


#ASI SERIA SI NO SE LE APLICAN FUNCIONES RECURSIVAS
def factorial_Comun(n):
    factorial = 1
    for numero in range(1, n + 1):
        factorial *= numero
    return factorial

print(factorial_Comun(5))
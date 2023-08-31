#Suma de Elementos: Escribe un programa que tome una lista de números y calcule la suma de todos los elementos en la lista.
lista = [1,-2,3]

def SumaLista(lista):
    sumaTotal = 0
    for elemento in lista:
        sumaTotal += elemento
    return sumaTotal

print(SumaLista(lista))


#LA MANERA MAS RESUMIDA ES LA SIGUIENTE:
sumatotal = sum([elemento for elemento in lista])
print(sumatotal)

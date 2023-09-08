lista = [4,2,1,5,15,6,7,0]

#ORDENAR LA LISTA EN SITU
lista.sort()
print(lista)

lista_tuplas = [(1,2),(1,4),(3,5),(1,4)]
lista_tuplas.sort(key=lambda x: x[1])
print(lista_tuplas)

#REVIERTE LOS ELEMNTOS DE LA LISTA IN SITU
lista_reversa = [1,4,1,7,2,8,99]
lista_reversa.reverse()
print(lista_reversa)


#ORDENA LOS ELEMNTOS Y CREA UNA LISTA NUEVA
lista_nueva = [1,4,7,2,34,8,4,44]

sorted(lista_nueva)
print(lista_nueva)


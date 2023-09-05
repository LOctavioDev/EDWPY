lista = [1,2,3,4,5]

#DEVOLVER EL INDICE 
print(lista.index(2))

#LANZA UNA EXEPCION DEL TIPO ValueError
print(lista.index(10))

#OPCIONES INDICANDO UNA SUBLISTA
print(lista.index(4,1))
print(lista.index(4,0,2))
print(lista.index(4,1,4))
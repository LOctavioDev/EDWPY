lista = [3,5.2,'Hola', 7j +5, [1,2],3]

#ACCESO  MEDIANTE INDEXACION 
print(lista[0]) 
print(lista[2])
print(lista[-1])

#SLICING 
print(lista[1:])
print(lista[1:2])
print(lista[1:3])
print(lista[:2])
print(lista[:])


#FUNCIONES DEL OBJETO LISTAS:

#DEVUELVE LA CANTIDAD DE ELEMNTOS DE LA LISTA
print(len(lista))

# #AGREGAR UN ELEMENTO AL FINAL DE LA LISTA 
lista.append(5)
print(lista)

# #EXTENDER LA LISTA CON LOS ELEMENTOS DE OTRA LISTA
lista_2 = ['yayo',5]
lista.extend(lista_2)
print(lista)

#INSERTA UN ELEMENTO EN UNA POSIICON DETERMINADA
lista.insert(0,5)
lista.insert(12,1)      #SI EL VALOR SE PASA DEL RANGO, SE AGREGA AL FINAL DE LA LISTA
lista.insert(-1,'Hacia Atras')
print(lista)

#CUENTA CUANTOS ELEMENTOS HAY QUE COINCIDAN CON EL ARGUMENTO
print(lista.count(3))

#ELIMINA EL PRIMER ELEMENTO QUE QUE SE ENCUENTRA PASADO COMO PARAMETRO
lista.remove(3)
print(lista)

#HACE UNA COPIA SUOERFICIAL DE LA LISTA
lista_copiada = lista.copy()
print(lista_copiada)

#SACA EL ULTIMO ELEMENTO Y LO DEVUELVE
print(lista.pop())
#SAACR EL TERCER ELEMENTO DE LA LISTA Y DEVOLVERLO
print(lista.pop(3))
print(lista)

#BORRAR TODOS LOS ELEMNTOS DE UNA LISTA
lista.clear()
print(lista)
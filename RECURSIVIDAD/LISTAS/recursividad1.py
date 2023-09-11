#RECORRIDO DE UNA LISTA DE FORMA RECURISVA: 
def impirmir_lista(lista, indice = 0):
    if indice < len(lista):
        print(lista[indice])
        impirmir_lista(lista, indice + 1)
        
lista1 = [1,2,3,4,5]

print(impirmir_lista(lista1))
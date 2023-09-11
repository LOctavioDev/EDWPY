#SUMA DE ELEMENTOS DE UNA LISTA

def suma_elementos(lista):
    if not lista:
        return 0
    else:
        return lista[0] + suma_elementos(lista[1:])  
    
lista1  = [1,2,3,4,5]

print(suma_elementos(lista1))
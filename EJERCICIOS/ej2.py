#Eliminar Duplicados: Escribe una función que tome una lista y elimine todos los elementos duplicados, dejando solo una instancia de cada valor.

def elimina_duplicados(lista):
    lista_nueva = []
    for elemento in lista:
        if elemento not in lista_nueva:
            lista_nueva.append(elemento)
    return lista_nueva
            

lista1 = [1,1,2,3]

print(elimina_duplicados(lista1))


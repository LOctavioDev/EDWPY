#HACER UNA FUCNION RECURSIVA QUE CALCULE LA SUMA DE TODOS LOS ELEMENTOS EN UNA LISTA DE NUMEROS ENTEROS. NO PUEDES UTILIZAR BUCLES NI FUNCIONES PREDEFINIDAS PARA LA SUMA DE ELEMENTOS EN UNA LISTA

def suma_lista(lista):
    if not lista:
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])

print(suma_lista([1,2,3,4,5]))
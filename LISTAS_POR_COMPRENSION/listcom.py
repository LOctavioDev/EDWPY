#LISTA DE CUADRADOS
cuadrados = []

for x in range(10):
    cuadrados.append(x ** 2)
    

#LISTAS POR COMPERNSION... ACA NOS AHORRAMOS LAS TRES LINEAS DE CODIGO EN UNA SOLA:
cuadrados2 = [x**2 for x in range(10)]


# print(cuadrados)
# print(cuadrados2)   #PUEDEN COMPROBAR QUE ES EL MISMO RESLTADO PERO CON MENOS LIENAS DE CODIGO


#CUADRADOS UTILIZANDO LA FUNCION MAP
cuadrados3 = list(map(lambda x: x**2, range(10)))

# print(cuadrados3)


lista = [-4,-2,0,2,4]

#LISTA POR COMPRENSION CON LOS NUMEROS POSITIVOS DE lista
positivos = [x for x in lista if x >= 0]
print(positivos)


positivos2 = list(filter(lambda x: x >= 0, lista))
print(positivos2)

#PARES NUMEROS Y SU CUADRADO
print([(x, x**2) for x in range(10)])

#LISTA DE PARES COMBINADOS
pares = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(pares)

pares2 = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            pares2.append((x,y))

print(pares2)
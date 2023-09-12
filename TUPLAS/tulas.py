#TUPLAS SON UNA SECUENCIA ORDENADA DE VALORES Y A IGUAL QUE LOS STRINGS, SON INMUTABLES

tupla = (1, 2.5, 'holi')

print(tupla[0])
print(tupla[1])
print(tupla[2])
# print(tupla[5])
print(tupla[:2])

#CREAR UNA TUPLA VACIA
tupla_vacia = ()
tupla_vacia_2 = tuple()

#TUPLA DE UN ELEMENTO
tupla_2 = (4, ) # ESTO ES UNA TUPLA
numero = (4) # ESTO ES UN NUMERO
print(type(numero))

#LAS TUPLAS SON INMUTABLES
tupla[0] = 5

#LONGUITUD DE UNA TUPLA
print(len(tupla))
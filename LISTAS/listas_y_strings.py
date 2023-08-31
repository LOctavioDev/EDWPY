nombre = 'octavio'
lista = list(nombre)
print(lista)    #CONERTIR A UNA LISTA UN STRING

#EL INDEXADO FUNCIONA DE IGUAL MANERA
print(f'{nombre[0]} \n {lista[0]}')

#EL SLICING FUNCIONA DE IGUAL MANERA
print(f'{nombre[1:3]} \n {lista[1:3]}')

#LA FUNCION LEN FUNCIONA DE IGUAL MANERA
print(f'{len(nombre)} \n {len(lista)}')

#EL in FUNCIONA EN AMBAS
print('o' in nombre)
print('o' in lista)

#EL not in TAMBIEN
print('z' not in nombre)
print('z' not in lista)

#LOS STRINGS TAMBIEN SE PUEDEN RECORRER CON UN FOR
for letra in nombre:
    print(letra)
    
#LOS STRINGS SON INMUTABLES
lista[0] = '0'
nombre[0] = '0' #TYPE ERROR



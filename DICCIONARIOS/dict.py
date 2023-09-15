# FORMAS PARA DEFINIR UN DICCIONARIO

precios1 = {
    'manzana' : 10.9,
    'pera' : 14.2,
    'kiwi' : 45.9
}

precios2 = dict(manzana = 10.9, pera = 14.2, kiwi = 45.9)

# precios3 = dict([('manzana', 10.9),('pera', 14,2),('kiwi', 45.9)])

#MOSTRAR ELEMENTOS DE UN DICCIONARIO
print(precios1['manzana'])
print(precios1['pera'])
print(precios1['kiwi'])

# AGREGAR UN ELEMENTO CLAVE : VALOR
precios1['melon'] = 11.4
print(precios1['melon'])

# ACTUALIZAR UN ELEMENTO
precios1['pera'] = 4.5
print(precios1['pera'])

# BORRAR UN ELEMENTO CLAVE : VALOR

del precios1['kiwi']

# PERTENENCIA

print('kiwi' in precios1)
print('melon' in precios1)
print('kiwi' not in precios1)

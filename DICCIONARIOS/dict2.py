precios = {'manzana' : 12.0, 'banana' : 12.32, 'kiwi' : 34.7}

# OBTENER LA CANTIDAD DE ELEMNTOS DEL DICCIONARIO

print(len(precios))

# OBTENER EL VALOR PARA LAS CLAVES INDICADAS, SE PUEDE INDICAR UN DEFAULT SI NO EXISTE 
print(precios.get('manzana'))
print(precios.get('banana'))
print(precios.get('melon'))
print(precios.get('melon',0.00))

# SI EXISTE DEVUELVE EL VALOR, SINO LO CREA CON EL VALOR DEFAULT O SI NO SE INDICA EL DEFAULT CON NONE
print(precios.setdefault('banana'))
print(precios.setdefault('sandia', 12.6))

# ACTUALIZACION DE UN DICCIONARIO

precios.update({'banana' : 10.34, 'durazno' : 20.6})
# print(precios)

# DEVOLVER UNA VISTA CON LAS CLAVES DEL DICCIONARIO
print(precios.keys())

# DEVOLVER UNA VISTA CON LOS VALORES DEL DICCIONARIO
print(precios.values())

# DEVOLVER UNA VISTA CON LOS ITEMS DEL DICCIONARIO
print(precios.items())

# SACAR UN ELEMENTO SIGUIENDO EL ORDEN DE LIFO
precios.popitem()
print(precios)

#COPIA SUPERFICIAL DEL DICCIONARIO
copia_dict = precios.copy()
print(copia_dict)

# LIMPIAR EL DICCIONARIO
precios.clear()
print(precios)
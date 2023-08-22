import string 

name = 'Octavio'
formatter = string.Formatter()
formatter.format('Hola {}',name)

print('Hola {}'.format(name))

#EJEMPLOS DE LA FUNCION FORMAT 

print('{} + {} = {}'.format(2,5,7))
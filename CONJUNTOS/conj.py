# #Un conjunto es una colección desordenada de elementos únicos e inmutables. Esto significa que un conjunto no permite elementos duplicados y no mantiene un orden específico de los elementos.

# frutas = {'manzana','pera','banana','sandia','melon','nuez'}

# print('pera' in frutas)
# print('kiwi' in frutas)

# #CREAR UN CONJUNTO VACIO

# set()

# #OTRAS FORMAS DE CREAR CONJUNTOS
# a = set('abracadabra')
# print(a)

# b = set('shazam')
# print(f'b\n')

# #OPERACIONES CON CONJUNTOS

# print(f"""LETRAS EN a PERO NO EN b: {a - b}\n
# LETRAS EN a O en b O EN AMABAS {a | b}\n
# LETRAS EN a Y EN b {a & b}\n
# LETRAS QUE ESTAN EN a O EN b PERO NO EN AMBAS {a ^ b}  
# """)

# #COMPRENSION DE CONJUNTOS

# a = {x for x in 'abracadabra' if x not in 'abc'}
# print(a)

M = [[1,2,3],
     [1,3,2],
     [3,1,2]]

print(M[1][1] == 2)
#UNA EXCEPCION ES UN ERROR QUE OCURRE DURANTE LA EJECUCION DEL PROGRAMA

# print(1/0)
    
# try:
#     t = 1/0
# except ZeroDivisionError:
#     print("Division por cero")
    
def find(elemento, lista):
    '''
        DEVUELVE EL INDICE DONDE SE ENCUENTRA EL ELEMENTO EN LA LISTA.
        SI NO LO ENCUNTRA, DEVULEVE -1.
    '''
    index = 0
    while True:
        try:
            if lista[index] == elemento:
                return index
        except IndexError:
            return -1
        index += 1
        
print(find(4, [2, 3, 4, 5]))
print(find(1, [2, 3, 4, 5]))


def divide(x, y):
    "DIVIDE DOS NUMEROS"
    try:
        result = x / y
    except ZeroDivisionError:
        print("DIVISION POR CERO!")
    else:
        print(f'EL RESULTADO ES: {result}')
    finally:
        print('EJECUTANDOSE LA CLAUSULA finally')
        
print(divide(2, 0))
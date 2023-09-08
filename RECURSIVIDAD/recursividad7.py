#CREA UNA FUNCION RECURSIVA QUE CALCULE LA SERIE DE FIBONACCI HASAT QUE IGUALE O SUPER EL NUMERO
def fibonacci(n):
    if n < 0:
        raise ValueError("EL NUMERO NO DEBE DE SER NEGATIVO")
    elif n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        
print(fibonacci(3))
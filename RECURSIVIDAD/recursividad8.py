#CALCULAR EL MAXIMO COMUN DIVISIOR CON UNA FUNCION RECURSIVA QUE TOME DOS NUMEROS ENTEROS POSITIVOS

def mcd(a,b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)
    
print(mcd(6,8))
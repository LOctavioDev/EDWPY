#EMPAQUETADO

a = 20
b = "P"
c = "A"

tupla = a,b,c
print(type(tupla))

#DESEMPAQUETADO 

x,y,z = tupla

print(x)
print(y)
print(z)

#ERRORES POR DISTINTOS TAMANIO AL DESEMPAQUETAR

x,y = tupla
q,w,e,r,t,y = tupla
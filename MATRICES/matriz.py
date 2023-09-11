# #DEFINIR UNA MATRIZ DE 4 FILAS Y 4 COLUMNAS 

# matriz = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]
# # print(matriz)

# #ACCEDER A LOS ELEMENTOS

# print(matriz[0][0])
# print(matriz[1][2])

# #EJEMPLO FUNCION SUMA DE MATRICES

# def suma_matrices(A,B):
#     can_filas = len(A)
#     can_columnas = len(A[0])
    
#     C = []
    
#     for fila in range(can_filas):
#         fila_suma = []
#         for col in range(can_columnas):
#             fila_suma.append(A[fila][col] + B[fila][col])
#         C.append(fila_suma)
#     return C

# matriz1 = [[1,2,3],[1,2,3]]
# matriz2 = [[1,2,3],[1,2,3]]

# print(suma_matrices(matriz1,matriz2))
a = {1,2,3,4,5}
b = {3,7,8,9,1}

print(a^b)
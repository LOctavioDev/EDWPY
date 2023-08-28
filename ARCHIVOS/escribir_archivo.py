#ESCRIBIR UN STRING EN EL ARCHIVO
with open('C:/Users/52771/Documents/EDWPY/ARCHIVOS/prueba2.txt','w') as file:
    file.write('Hola Mundo')

#ESCRIBR MUCHAS LINEAS EN EL ARCHIVO
with open('C:/Users/52771/Documents/EDWPY/ARCHIVOS/prueba2.txt','w') as file:
    file.writelines(['Linea 1.\n','Linea 2.\n','Linea 3.\n'])

#ESCRIBIR UN STRING EN EL ARCHIVO, AGREGANDOLO AL FINAL DEL MISMO
with open('C:/Users/52771/Documents/EDWPY/ARCHIVOS/prueba2.txt','a') as file:
    file.write('this is THE END')
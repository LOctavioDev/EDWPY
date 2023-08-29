#LA FUNCION READ LEE TODO EL CONTENIDO DEL ARCHIVO
with open('ruta_de_tu_archivo.txt','r') as file:
    print(f'1.- {file.read()}\n')
    
#LA FUNCION readline LA LINEA ACTUAL DEL ARCHIVO
with open('ruta_de_tu_archivo.txt','r') as file:
    print(f'2.- {file.readline()}\n')
    
#LA FUNCION realines LAS LINEAS DEL ARCHIVO Y LAS GUARDA EN UNA LISTA
with open('ruta_de_tu_archivo.txt','r') as file:
    print(f'3.- {file.readlines()}\n')

#LA FUNCION list GENERA UNA LISTA CON LAS LINEAS DEL ARCHIVO
with open('ruta_de_tu_archivo.txt','r') as file:
    print(f'4.- {list(file)}\n')

#PARA PODER RECORRER CADA FILA DEL ARCHIVO LO PODEMOS HACER CON UN CICLO FOR
with open('ruta_de_tu_archivo.txt','r') as file:
    for line in file:
        print(f'{line}\n')
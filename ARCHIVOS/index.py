#ABRIR UN ARCHIVO
archivo = open('ruta_de_tu_archivo.txt','r')    #TIENE DOS PARAMETROS... LA RUTA DONDE ESTA EL ARCHIVO Y EL MODO DE COMO SE ABRIRA

#LEER TODO EL CONTENIDO DE ARCHIVO
archivo.read()

#CERRAR EL ARCHIVO
archivo.close()

#ABRIR EL ARCHIVO COMO UN CONTEXT MANAGER UTILIZANDO LA SENTENCIA WITH
with open('ruta_de_tu_archivo.txt','r') as file:
    file.read()

import json

#SERIALIZAR UN OBJETO
print(type(json.dumps([1,2,3])))    #CON LA FUNCION type PODEMOS VER DE QUE TIPO ES EL OBJETO

#DESERIALIZAR UN OBJETO
print(type(json.loads('[1,2,3]')))    


#ESCRIBIR COMO JSON DIRECTAMENTE EN UN ARHVIO
with open('C:/Users/52771/Documents/EDWPY/JSONs/json_example.txt', 'w') as file:
    json.dump([1,2,3,4,5], file)
    
#LEER UN JSON DIRECTAMENTE DESDE UN ARCHIVO
with open('C:/Users/52771/Documents/EDWPY/JSONs/json_example.txt', 'r') as lista:
    lista = json.load(lista)

print(lista)

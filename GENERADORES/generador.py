def first_1000():
    "GENERAR LOS PRIMEROS 1000 NUMEROS"
    for x in range(1000):
        yield x

gen_first_100 = first_1000()

for x in gen_first_100:
    print(x)
    
def gen_primos(cantidad = 1):
    "GENERADOR DE NUMEROS PRIMOS"
    contador = 1
    lista_primos = []
    
    while cantidad > contador:
        es_primo = True
        contador += 1
        if len(lista_primos) > 0:
            for primo in lista_primos:
                if contador % primo == 0:
                    break
        if es_primo:
            lista_primos.append(contador)
            yield contador

first_100_primes = gen_primos(100)

for x in first_100_primes:
    print(x)
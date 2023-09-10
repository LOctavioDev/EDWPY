def es_primo(n, divisor=2):
    if n <= 1:
        return False
    
    if n <= 3:
        return True
    
    if n % divisor == 0:
        return False
    
    if divisor * divisor > n:
        return True

    return es_primo(n, divisor + 1)


numero = 10

print(es_primo(numero))  
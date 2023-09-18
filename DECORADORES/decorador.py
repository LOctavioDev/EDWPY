def smart_division(div_func):
    def div(a, b):
        if b == 0:
            print('No se puede dividir por cero')
            return
        return div_func(a, b)
    return div

@smart_division
def division(a, b):
    return a / b

print(division(1, 2))
print(division(2, 0))

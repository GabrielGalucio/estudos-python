# Em breve eemplo de condicional com uma função

def comparacao_de_valores(x):
    if x > 3:
        return "É maior que 3"
    elif x < 3:
        return "É menor que 3"
    elif x == 3:
        return "É igual a 3"
    elif x < 0:
        return "É um número negativo"
    else:
        return "Operação invalida"

print(comparacao_de_valores(-1))
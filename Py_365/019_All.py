# Criando uma função que conta uma lista menor que vinte

def count(numeros):
    total_numero = 0
    for x in numeros:
        if x < 20:
            total_numero = total_numero + 1
    return total_numero

# Obtem-se uma lista com diversos valores aleatórios
lista01 = [4, 5, 9, 10, 15, 25, 28, 30, 45, 17] 

print(count(lista01))
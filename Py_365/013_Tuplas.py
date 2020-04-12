# Definindo algumas tuplas e indicando diferenças 
# DIferente de listas, as tupals são imutaveis

tupla01 = (10, 20, 30, 40)
tupla02 = (50, 60, 70, 80)
a, b, c = 90, 80, 70
print(tupla01)
print(tupla02)
print(a, b, c)

print(tupla01[0])
print(tupla02[2])

uniao_01 = [tupla01, tupla02]
print(uniao_01)

# Demonstrando uma tupla sendo referenciada por uma função -> calculo padrão de perimetro
def calculo_info(x):
    A = x ** 2
    P = 4 * x
    print("Área do perimetro:")
    return A,P

print(calculo_info(3))
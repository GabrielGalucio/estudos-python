# Exemplo de estruturas condicionais com o loop for

for n in range(10):
    print(2 ** n, end = " ")

print(" ")


# Criando uma condicional simples para verificar se o número é impar ou par

for x in range(20):
    if x % 2 == 0:
        print(x, end = " ")
    else:
        print("ímpar", end = " ")

# Há outros métodos para se obter os elementos de uma lisa
x = [1, 2, 3]
for item in x:
    print(item, end = " ")

print(" ")

for item in range(len(x)):
    print(x[item], end = " ")
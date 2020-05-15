# Definindo variavies locais e globais

# Variavel global (fora da função)
var_global = 10
def multiply(num01, num02):
    var_global = num01 + num02 #Variavel local (dentro da função)
    print(var_global)

multiply(5, 10)
print(var_global)


# Funções built-in no Python, funções que já vem na linguagem

print(abs(-10)) # abs para retornar um valor absoluto
print(bool(0)) # bool para retornar um valor boleano
print(bool(1)) # bool para retornar um valor boleano


# Funções para conversao
# srt() para string
# int() para inteiro
# float() para flutuante

idade = int(input("Digite aqui a sua idade:"))
if idade >= 13:
    print("Você pode criar um Facebook")
else:
    print("Você não pode criar um Facebook")

lista = [10,20,30,40,50]

print(len(lista)) # Contando valores
print(min(lista)) # Valor minimo
print(max(lista)) # Valor maximo
print(sum(lista)) # Somando valores
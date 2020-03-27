# Dicionários são diferentes de listas

listao1 = ["um", "dois", "tres", "quatro", "cinco"]
dicionario01 = {"um":1, "dois":2, "tres":3, "quatro":4, "cinco":5}
dicionario02 = {"seix":6, "sete":7, "oito":8, "nove":9, "dez":10}

# Exibindo na tela
print(listao1)
print(dicionario01)

# Pegando o valor de uma chave pelo seu indice
print(dicionario01["dois"])
print(dicionario01["tres"])

# Mudando o valor de uma chave
dicionario01["dois"] = 22
print(dicionario01["dois"])

# É possivel adicionar uma nova chave com um novo valor com a mesma sintaxe
dicionario01["zero"] = 0
print(dicionario01)

# Limpando um dicionário em Python com clear()
dicionario02.clear()
print(dicionario02)

# Podemos deletar o dicionário Python com del
# del dicionario02

# Verificando o tamanho com len()
print(len(dicionario01))

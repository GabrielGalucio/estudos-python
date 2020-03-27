# Trabalhando com listas em python

# 1- Lista são umm conjunto de coisas e que podem ter seus elementos modificados
# 2- SIntaxe -: lista01 = [1, 2, "três", 4] pode ser associado a uma matrix. só
# que mais flexiveis, pois não tem tamanho fixos e não tem restrição de tipo, é
# possivel também criar listas dentro de listas, o nome disso é Listas alinhadas

# Exemplo 01 -> Lista de 01 elemento
listamercado01 = ["Arroz, feijão, macarrão, sal"]
print(listamercado01)

# Exemplo 02 -> Lista de 04 elementos
listamercado02 = ["Maionese", "óleo", "Vinagre"]
print(listamercado02)

# Testado o que foi afimando em relação aos elementos, realizamos um slice simples:
print(listamercado01[0])
print(listamercado02[0])

# Lista com dados diferentes
listadiferente01 = [10, 20, "Trinta"]
print(listadiferente01)
print(listadiferente01[0])

# Atribuindo os valores de uma lista a novas variavies:
item01 = listadiferente01[0]
item02 = listadiferente01[1]
item03 = listadiferente01[2]
print(item01, item02, item03)


# Substituindo itens de uma lista -> declare a lista com a posição do item que
# deseja substituir e em seguida atribua um novo valor do mesmo tipo do item.
listadiferente02 = [10, 20, 30, "quarenta"]
listadiferente02[0] = 100
listadiferente02[1] = 200
listadiferente02[2] = 300
listadiferente02[3] = "cinquenta"
print(listadiferente02)

# Deletando itens de uma lista com a sintaxe del
del listadiferente02[3]
print(listadiferente02)

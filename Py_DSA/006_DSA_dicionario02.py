# Manipulando dicionario parte 02

# Não há restrição para os tipos de dados em um dicionário
# Dicionario {chave:valor} -> fixar nomenclatura correta
dicionario01 = {"Gabriel":22, "Nathasha":24, "João":23, "José":26}
dicionario02 = {"Luiza":56, "Graça":52, "João Portilho":56}
dicionario03 = {}

# Visualizando  o tamanho do dicionário novamente
print(len(dicionario01))

# Visualizando somente as chaves de um dicionário
print(dicionario01.keys())

# Visualizando somente os valores de um dicionário
print(dicionario01.values())

# Visualizando somente os itens (combinações) de um dicionário
print(dicionario01.items())

# Podemos atribuir o conteúdo do dicionário 02 ao dicionário01 como uma concatenação
# usando o método update() conforme exemplo. Observe que ao eecutar, há a união deles
dicionario01.update(dicionario02)
print(dicionario01)

# Podemos pegar o dicionário03 vazio e atribuir uma lista a ele
dicionario03["Ewertton"] = 19
print(dicionario03)

# Adicionando mais uma vez, tipos diferentes ao dicionário
dicionario03[100] = 100
print(dicionario03)

# O mesmo vale invertendo os tipo
dicionario03[0.8] = "Paulo"
print(dicionario03)

# Mais teste com os tipos de dados em dicionarios
dicionario04 = {}

dicionario04["key_01"] = 8.2
dicionario04["key_02"] = "oito"
dicionario04["key_03"] = 8
print(dicionario04)

# Agora podemos pegar cade chave a atribuir a novas variaveis
a = dicionario04["key_01"]
b = dicionario04["key_02"]
c = dicionario04["key_03"]
print(a, b, c)

# Ainda é possivel criar dicionário com valores em forma de lista
dicionario05 = {"key_01":2020, "key_02":[10, 20, 30, 40], "key_03":["um", "dois", "tres"]}
print(dicionario05)

# Retorna-se os valores normalmente atravé das chaves
print(dicionario05["key_01"])

# Em caso de retorno de uma lista, pode-se retornar ela inteira ou somente pelo index
print(dicionario05)                       # Pegando todo o dicionário
print(dicionario05["key_03"])             # Pegando a chave com o valor em lista (toda) 
print(dicionario05["key_03"][1])          # Pegando a chave com o valor com idex (unico)
print(dicionario05["key_03"][0].upper())  # Pegando a chave com o valor com idex e atribuindo um método (ainda valor unico)

# Podemos ainda realizar operações com os valores de um diconário, por exemplo:
# Neste vamos pegar o valor da lista da chave "key_02", subtrair por 10 e armazenar em uma nova variavel
print(dicionario05["key_02"][1] - 10)

# Por fim, podemos utilizar dicionario aninhados, que é um dicionário dentro de um dicionário
dicionario_aninhado = {"key_01":{"key_02_aninhado":{"key_03_aninhado":"dicionario_aninhado"}}}
print(dicionario_aninhado["key_01"]["key_02_aninhado"]["key_03_aninhado"])
print(dicionario_aninhado)
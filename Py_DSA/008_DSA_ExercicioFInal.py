# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.
impressao_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(impressao_numeros)

# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela
impressao_lista = ["um", "dois", "tres", "quatro", "cinco"]
print(impressao_lista)

# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
str01 = "Ola "
str02 = "Gabriel "
str03 = "Galúcio "

print(str01 + str02 + str03,"Seja bem vindo!")

# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla
tupla = (1, 2, 2, 3, 4, 4, 4, 5)
print(tupla.count(4))

# Exercício 5 - Crie um dicionário vazio e imprima na tela
dicionario_vazio = {}
print(dicionario_vazio)

# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
dicionario_3_valores = {22:"um", 23:"dois", 24:"tres"}
print(dicionario_3_valores)

# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
dicionario_3_valores["add"] = 19
print(dicionario_3_valores)

# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 
# elementos numéricos. Imprima o dicionário na tela.
dicionario_lista = {"valor":1, "valor2":2, "valor3":[1, 2, 3, 4, 5, "dois"]}
print(dicionario_lista)

# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista na tela.

misturado = ["string", (1, 2), {"chave01":1, "chave02":2}, 20.20]
print(misturado)

#Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'
print(frase[0:17])
# Testando String em Python

print("Testando uma string em python 01")
print("Testando uma string em python 02")
print("Testando uma string em python 03")
print("Testando uma 'string' em python 04")

# Testando string com formatadores pyhton
-ytreryuiop [ ]
print("Testando uma string \n em python \n 05")
print("Testando uma \n string \n em \n python 06")
print("\n")

# Indexando strings -> entre [] pega o caractere que está naquela
# posição da frase da string declarada (sempre começando do zero)
frase01 = "O rato roeu a roupa do rei de roma"
print(frase01[0])
print(frase01[7])
print(frase01[12])
print(frase01[10])

# Usando o método slice -> fatiamento para as strings, importante
# para a analise dados, pode ser aplicado a colunas e excel. ATÇ
# fatiamentos são EXCLUSIVOS ou seja, tudo até a poisção X, ele não
# retorna o index que você estipula.

frase02 = "O rato roeu a roupa do rei de Roma"
print(frase02[1:])    # Exibe na tela toda string a partir da posição 1 (para frente ->)
print(frase02[:6])    # Exibe na tela toda string antes da posição 6 (para trás <-)
print(frase02[1:5])   # Exibe na tela toda string a partir da posição 1 e antes da posição 5
print(frase02[1:6])   # Exibe na tela toda string a partir da posição 1 e antes da poisção 6
print(frase02[:])     # Exibe toda a string pois não há parametros para tratamento.
print(frase02[-6])    # Usa-se com sinal - para retornar caracteres de trás para frente
print(frase02[-5:])   # Retorna os 5 primeiros caracteres de trás para frente da string
print(frase02[:-5])   # Retorna toda a string exceto os ultimos 5 caracteres da string
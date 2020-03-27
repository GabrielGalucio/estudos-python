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

# Início da parte 02 DSA_cordas02.py

# Para fatiamentos mais criteriosos, podemos utilizar [::] como paramentro, conforme exemplo:
frase03 = "123456789"
print(frase03[::])   # Busca posição por posição de forma criteriosa por pedaços
print(frase03[::1])  # Busca posição por posição de forma criteriosa por pedaços de 1
print(frase03[::2])  # Busca posição por posição de forma criteriosa por pedaços de 2
print(frase03[::-2]) # Busca posição por posição de forma criteriossa por pedaços de 2  invertido

# Propriedades de String

# É possivel alternar o valor de uma posição na string conforme exemplificação abaixo:
"""
frase04 = "1234567890"
frase04[3] = 'A'
print(frase04)
"""

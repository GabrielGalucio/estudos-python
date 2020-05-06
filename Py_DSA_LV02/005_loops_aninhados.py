# Definindo loops for dentro de estruturas de repetição
# É possivel assim como qualquer estrutura em Python. é importante ter o dominio de analise
# desse tipo de loop pois é com elas que manipulamos matrizes bidimensionais em Python, com
# mum em atividades de álgebra Linear e de Aprendizado de Máquina na Ciência de Dados.


for i in range(0,5):
    for n in  range(0,5):
        print(n)

# Vamos aplicar o conceito de variaveis locais e globais
lista01 = [10,20,30,40,50]
soma = 0
for i in lista01:
    # variavel dobro é local
    dobro = i * 2
    soma = soma + dobro

print(soma)

# Percorrendo listas de listas 
lista02 = [[1,2,3,4],[5,6,7,8],[9,0,1,2]]
for i in lista02:
    print(i)

# Contando a quantidade de itens em uma lista
lista03 = [10,20,30,40,50,60,70,80,90,100]
contador = 0
for i in lista03:
    contador = contador + 1

print(contador) 

# Contando o número de colunas
lista_matriz = [[0,0,1,0],[1,2,0,1],[2,4,0,1],[3,0,0,0]]
primeira_linha = lista_matriz[0]
contador_lista = 0

for i in primeira_linha:
    contador_lista = contador_lista + 1

print(contador_lista)

# Pesquisando itens em uma lista
lista04 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in lista04:
    if i == 5:
        print("Achou")

# Podemos usar o loop for com dicionários. Podemos listar os valores de um dicionário
dicionario01 = {"chave01":1, "cahve02":2, "chave03":3, "chave04":4}
for i in dicionario01:
    print(i)

# Podemos retornar a chave e o valor do dicionario vamos utilizar o metodo chamado
# dict.items() que é um metodo do dicionario para retornar itens
for chave, valor in dict.items(dicionario01):
    print(chave, valor)

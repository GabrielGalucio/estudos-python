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

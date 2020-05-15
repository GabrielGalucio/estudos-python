# Função: é um dispositivo que agrupa um conjunto de código para que eles possam ser
# executadas mais de uma vez. Funções também permitem especificar com parametros que
# podem servir como entradas paras as funções.
# 
# Em um nível mais fundamental, a construção de funções nos permite reutilizar o codi
# go, sem ter que screve-lo novamente. Nas aulas de string, utilizamos a função len()
# para obter o comprimento de uma string. Com funções, escrevemos o código uma única
# vez e repetimos a mesma instrução através de chamadas, quantos vees forem necesaarias

# def nomeFuncao(arg1, arg2):
# # comentário da função 

# Definindo uma função simples
def funcaoSimples():
    print("Função simples sem parametro ou retorno")

funcaoSimples()

# Definindo uma função simples com parametro
def funcaoSimplesParametro(nome):
    print("Ola Sr.", nome)

funcaoSimplesParametro("Gabriel")

# Definindo uma função simples com um loop for (exibindo números na tela)
def funcaoLoop():
    for i in range(0,10):
        print("Número: " + str(i))

funcaoLoop()

# Somando dois numeros com parametros
def somaNumeros(num01, num02):
    print("O primeiro número é: ",num01)
    print("O segundo número é: ",num02)
    print("A soma dos dois números é: ",num01 + num02)

somaNumeros(10,10)
# A função range nos permite criar uma lista de números, com intervaos especificos
# range(começar, parar, passo)
# range(inicio, fim, condição)

# começar/inicio : é o número que inicia a sequencia
# parar/ fim: é o número que encerra a sequencia (não é incluso na sequencia) 
# passo/condição : diferença entre cada número da sequencia

# Impressão simples
for i in range(10, 20, 3):
    print(i)


# Impressão sem condição
for i in range(0, 10):
    print(i)

# Impressão com númers negativos
for i in range(0, -20, -2):
    print(i)

# Impressão com uma lista
lista = ["café", "morango", "açaí", "farinha", "peixe"] # Declara um lista
lista_tamanho = len(lista)                              # Aloca em uma variavel o tamanho da lista com a função len()
for i in range(0, lista_tamanho):                       # Cria um for com range 0(inicio) e o tamanho da lista (com len vira um numero)
    print(lista[i])                                     # Imprime a lista na posição em que i está, ou seja cada item a lista

# Verrificando o tamanho da lista, observe
print(lista_tamanho)
print(lista[0])
# print(lista_tamanho[0])

# Tudo em python é um objeto, inclusive range

print(type(range(0,10)))
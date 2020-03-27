# Testando laço de repetição FOR e iteradores de controle

# Iteração é o processo chamado na programação de repetição de uma ou mais ações.
# É importante salientar que cada iteração se refere a apenas uma instância da a-
# ção, ou seja, cada repetição possui uma ou mais iterações.

# É um conjunto de valores que segue uma determinada ordem
g = "gabriel"
for n in g:
    print("O iterador está em: ",n)


# Listas: um conjunto de coisas, assimiliando como por exemplo, uma lista de compras (vetor)
# a lista pode ser umm conjunto de dados com tipos primitivos diferentes, não precisa ser =
lista01 = [1, 2, 3, 4, 5]
lista02 = [6, 7, 8, 9, 0]
lista03 = ["teste", 1, -3, 3.9]
print(lista01)
print(lista02)
print(lista03)

# As listas são elementos iteraveis (conj. de valores com rodem) -> testando ela com for:
for i in lista03:
    print("O iterador está em: ", i)
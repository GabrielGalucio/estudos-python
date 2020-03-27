# Construindo listas aninhadas

# É importante frisar a definição de lista aninhadas (listas dentro de listas)
# pois a mesma nos permite contruir matrizes em python, conforme a sintaxe -->
# lista = [[a,b,c], [d,e,f], [g,h,i]]  --> há uma lista em cada posição da lista

# Exemplo 01
lista01 = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
print(lista01)

# Ao atribuir um item a uma variavel, é atribuido uma lista, pois em listas ani-
# nhadas, uma lista correspoden a um item na lista maior, conforme exemplo:

var01 = lista01[0]
print(var01)

# Após isso é possivel atribuir 1 ELEMENTO da lista repassada a variavel var01 pa
# ra a variavel var02, logo, ao imprimir, a var02 vai exibir o 1 item da lista.
var02 = var01[0]
print(var02)

var03 = lista01[1]
print(var03)

var04 = var03[0]
var05 = var03[1]
var06 = var03[2] 
print(var04)
print(var05)
print(var06)

# Listas funcionam como matriz, então é possivel:
lista02 = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
matriz01 = lista02[2][3]
# matriz01 = lista02[2][3] + 2 pode-se somar 
# matriz01 = lista02[2][3] * 2 pode-se mutip
# pode-se realizar operações livremente.
print(matriz01)

# 1 2 3 4
# 5 6 7 8
# 9 10 11 12


# É possivel ainda concatenar duas listas
conc01 = [1, 2, 3, 4]
conc02 = [5, 6, 7, 8]
conc_total = conc01 + conc02
print(conc_total)

# Podemos utilizar o operado INpara verificar s eum item existe em uma lista
# informa o que deseja procurar junto com o operador in e a lista, o resulta
# do ira retornar um boolean, confirmando ou não a instrução.
inlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(7 in inlist)
print(22 in inlist)

# Podemos utilizar funções built-in, ou seja, funções diversas para consultar
# a estutura das listas que manipulamos, conforme a necessidade de infomação

lista03 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
print(len(lista03))       # Verifica o tamanho da lista com a função len()
print(max(lista03))       # Verifica o maior valor da lista com a função max()
print(min(lista03))       # verifica o menor valor da lista com a função min()
lista03.append(-10)       # Adiciona um item no final da lista com a função .append()
print(lista03)

# Criando lista vazias. São muito utilizadas em modelos de Machine Learning, po
# is, se cria essas listas e elas são alimentadas  com resultados de um processo
# de treinamento até chegar em um modelo aceitavél.
listavazia = []

# Pode-se ainda utilizar o loop FOR para prencher uma lista vazia, a partir de uma
# lista já criada com itens dentro, conforme exemplo
old_list = [1, 2, 3, 4, 5, 6]
new_list = []

# (Para cada item na lista antiga -> faça um .append para a lista nova)
for item in old_list:
    new_list.append(item)

print(new_list)

# Criando uma lista e utilzando o método extend() para atribuir mais itens
cidades = ["Manaus", "Salvador"]
cidades.extend(["Fortaleza", "Palmas"])
print(cidades)


# Pegando o indice de um elemento da lista com a função index()
print(cidades.index("Fortaleza"))

# Adicionando um elemento em uma lista coma  função insert()
cidades.insert(2, "Brasilia")
print(cidades)

# Removendo um elemento em uma lista coma  função remove()
cidades.remove("Brasilia")
print(cidades)

# Revertando uma lista coma  função reverse()
# print(cidades.reverse)
cidades.reverse()
print(cidades)

# Ordenando uma lista coma  função sort()
# print(cidades.reverse)
cidades.sort()
print(cidades)
# Tuplas são como listas, mas não podem ter seus dados alterados
# Pode ser usado por exemplo, para declarar  datas de uma codigo

# Sintaxe tupla = (elemento1, elemento2, elemento3)

# É com lembrar
# tupla = ( TUPLA CRLH)
# lista = [ LISTA CRLH]
# dicionario = {DICIONARIO CRLH}

tupla01 = (1, 2, 3, "quatro", 5, 6, "sete", 8, 9, "dez")
tupla02 = (1, 2, 3, "sete", "oito", 9)

# Diferente de lista ou dicionario, as tuplas não podem ser mdoficadas, logo não podemos adi
# cionar um item, nem remover, nem modificar de qualquer forma, podemos criar uma lista de um
# unico item tambem, bem como a tupla também possui indices

print(tupla01)
print(tupla01[0])
print(tupla01[3])

# Podemos fazer slicing e leitura de tamanho

print(len(tupla01))
print(tupla01[2:4])
print(tupla01[1:])
print(tupla01[1:3])

# Possivel ver o indice se um dos elementos de uma tupla
print(tupla01.index(3))
print(tupla01.index(5))
print(tupla01.index("quatro"))
print(tupla01.index("sete"))

# É possivel deletar uma tupla também
del tupla02

# Podemos converter umas tupla em uma lista, caso queiramos modificar com o metodo lis()
# nome_lista = metodo(nome_tupla)
tupla_para_lista = list(tupla01)
print(tupla_para_lista)

# Agora podemos adicionar um item no final da lista
tupla_para_lista.append('Novo Item')
print(tupla_para_lista)

# Então vamos reconverter a lista para uma tupla com o metodo tuple()
nova_tupla = tuple(tupla_para_lista)
print(nova_tupla)

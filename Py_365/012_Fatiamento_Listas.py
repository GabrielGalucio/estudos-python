# Abordaremos aqui o conceito de slicing conforme já exemplificaod em Py_DSA e Py_LV01

# É interessantes fatiar listas para melhor manipular os objetos que nela contem, isso
# permite vsiaulizar e tratar melhor os dados contidos na lista, bem como obervar seu 
# comportamento.

lista01 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
lista02 = ["Joao", "Maria", "Jose", "Jaco", "Gabriel", "Stefanie", "Nathasha", "Marcelo", "Adriano", "Marcos"]
listaX1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
listaX2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
listaX3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
listaX4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
listaX5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
listaX6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
listaX7 = ["Joao", "Maria", "Jose", "Jaco", "Gabriel", "Stefanie", "Nathasha", "Marcelo", "Adriano", "Marcos"]

# Pegar somente os nomes de Maria e Jose na lista
# Importante indexar -> é pego o primeiro index [1] e o segundo é refrente a -1, logo é pego a segunda posição da lista
# é importante sempre ter em mente que ao manipular indexadores, lembrar do -1 no indexador final da lista.
print(lista02[1:3]) # Pegando de 1 a 2
print(lista02[:2])  # Pegando de < 3
print(lista02[-2])  # Pegando o antepenultimo
print(lista02[-2:]) # Pegando os dois ultimos
print(lista02[:-2]) # Pegando todos exceto os dois ultimos

# Co  o método index, é possivel saber a pisição de um objeto na lista
print(lista02.index("Maria"))
print(lista02.index("Gabriel"))

lista03 = ["Horacio", "Andre"]
lista04 = ["Josue", "Felipe"]

# Juntando duas listas
lista05 = [lista03, lista04]
print(lista05)

# Imprimindo a lista em ordem alfabetica com sort()
lista02.sort()
print(lista02)

# É possivel colocar parametros para inverter a lista em sort
lista02.sort(reverse=True)
print(lista02)

# O mesmo é possivel realizar com números
lista01.sort()
listaX1.sort(reverse=True)
listaX2.sort()
listaX3.sort(reverse=True)
listaX4.sort()
listaX5.sort(reverse=True)
listaX6.sort()
print(listaX1)
print(listaX2)
print(listaX3)
print(listaX4)
print(listaX5)
print(listaX6)
print(listaX7)

lista01.sort(reverse=True)
print(lista01)
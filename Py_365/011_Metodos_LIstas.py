# É possivel combinar métodos em Python para manipular as listas

# O "ponto" indica a invocação (pelo menos na maioria das vezes rs) de um método posterior
# conforme os métodos que utilizaremos no decorrer deste arquivo

lista01 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
lista02 = ["um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez"]

# Adiconando um item no final da lista com o metodo append()
lista01.append(31)
print(lista01)

# É possivel "estender" a lista com o método extend([])
lista01.extend([32,33,34,35,36,37,38,39,40])
print(lista01)

# É possivel criar sentenças utilizando o posicionamento das listas, conforme exemplo
# como é um número eu tive que converter com o método str() conforme exemplo>>>>>>>>>
print("O quarto item da lista 01 é o número " + str(lista01[4]) + ".")
print("O quarto item da lista 02 é a string " + lista02[4] + ".")

# Por fim utilizamos o metodo len() para ver o número de objeto que uma lista contem
print(len(lista01))
print(len(lista02))
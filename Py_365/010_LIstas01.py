# Algumas demonstraçõe com listas
lista01 = ["item01", "item02", "item03", 4, 5, 6, "item07"]
lista02 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
lista03 = [-1, -2, 2.2, 10, 0, -1000, 200, "teste", "ola", 90]

print(len(lista01))
print(len(lista02))
print(len(lista03))

# É possivle pegar as posições das listas
print(lista01[3])
print(lista02[3:])
print(lista02[:3])

# Substituindoo valor de uma lista
lista02[3] = "modificado"
print(lista02)

# Removendo um item da lista com a palavra (del)
del lista02[3]
print(lista02)

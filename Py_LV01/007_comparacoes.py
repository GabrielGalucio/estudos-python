# Realizando algumas comparações em python

# > : maior
# < : menor
# >= maior ou igual
# <= menor ou menor
# == igual
# != diferente

print(3 == 3)
print(3 < 3)
print(3 <= 3)
print(-3 != 3)

# Aplicando e variaveis
teste01 = 10
teste02 = 20
teste03 = 20.1
print(teste01 == teste02)
print(teste01 <= teste02)
print(teste01 != teste02)
print(teste01 > teste03)
print(teste01 >= teste03)
print(teste01 <= teste03) # Tormar cuidado com número com float por conta da precisão.

# Testando varios valores
print( 2 == 2 < 3 < 1)
print( 10 != 20 <= 20)

# Comparando strings - ATÇ: O python é case sensitive
print("Ola" == "Ola")
print("ola" == "OLA")

# O pyhton utiliza a tabela ASCII, siginifica que ele dá um numero a um caractere e, para
# descobrir que numero esta associado ao caractere, basta aplicar a função ord()
print(ord('a'))
print(ord('b'))
print('a' > 'b')

# É possivel aplicar o inverso, ou seja atribuir um caractere a um número, coma função chr()
print(chr(97))
print(chr(49))
print(97 > 49)
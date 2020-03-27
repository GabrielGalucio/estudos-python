
# Contraindo operações
n = 10
n += 1
print(n)

m = 20
m -= 5
print(m)


# Testando a estrutura de repetição while: (enquanto) que executa determinada ação até
# a mesma for verdadeira, conforme exemplo:
g = 0
while g <= 10:
    print(g)
    g += 1


# Pode se aplicar funções mais complexa, como no exemplo, utilizando as estruturas de decisão:
# and, or, not bem como os próprios operadores lógicos, deixando o while mais dinamico.
numero01 = 0
while numero01 != 7 and numero01 <= 7:
    print(numero01)
    numero01 += 1

numero02 = 0
while numero02 < 3 < 5:
    print(numero02)
    numero02 += 1

# Testando o comando break -> serve para parar um laço, ou seja ele sai enquanto o while esta ro-
# dando (ou em qualquer outra estrutura de repetição), ignorando as instruções que vem depois.
numero03 = 10
while numero03 > 0:
    if numero03 == 15:
        break
    print(numero03)
    numero03 += 1
print("Saiu do while e numero03 vale:", numero03)

# Testando o comando continue -> funciona como o break, que: ao ser aceito, faz o loop voltar para
# o início do comando while (ou qualquer outra estrutura de repetição), ignorando o que vim depois
numero04 = 0
while numero04 < 5:
    numero04 += 1
    if numero04 == 3:
        continue
    print(numero04)

# Em python, é possivel associar o else com o laço while (não é possivel na maioria das outras lin
# guagens), para indiciar quando a condição não entra, como na exemplificação abaixo:

numero05 = 4
while numero05 > 10:
    print("Número aceito no laço while")
else:
    print("Número não aceito no laço while")

numero06 = -1
while numero06 < 0:
    numero06 += 1
    print("Número aceito no laço while n < 0", numero06)
else:
    print("Número não aceito no laço while n > 0 ") 



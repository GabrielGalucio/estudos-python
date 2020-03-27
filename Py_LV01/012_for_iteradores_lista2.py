lista01 = [1, 2, 3, 4, 5]
lista02 = [1, 2, 3, 4, 5]
lista03 = ["a", "b", "c", "d", "e"]


# Exemplo 01 -> utilizando o iterador com break
for n in lista01:
    if n == 3:
        break
    print("O iterador está no elemento: ",n)

# Exemplo 02 -> utilizando o iterador com continue
for o in lista02:
    if o == 3:
        continue
    print("O iterador está no elemento: ",o)

# Exemplo 03 -> utilizando o else com for -> quando todas as condições forem percorridas
# o loop será falso e caira na condição else, executando a sua tarefa conforme sintaxe:
for p in lista03:
    print("O iterador está no elemento: ",p)
else:
    print("Saindo o loop de repetição")

# Criando um exemplo para saber qual letra é vogal ou consoante:
# "ABCDDEEFGHIJKLMNOPQRSTUVWXYZ"
alfabeto = ["A","B","C","D","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for letra in alfabeto:
    print(letra, end = " é uma ")
    if letra in "AEIOU":
        print("vogal")
    else:
        print("consoante")

# Verificando se o número é par ou impar
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,0]
for cont in numeros:
    print(cont, end = " é ")
    if cont % 2 == 0:
        print("par ")
    else:
        print("impar ")

# Faça um Programa que leia três números e mostre o maior deles.

numero01 = int(input("Digite aqui o primeiro número: "))
numero02 = int(input("Digite aqui o segundo número: "))
numero03 = int(input("Digite aqui o terceiro número: "))

if numero01 > numero02 and numero01 > numero03:
    print("O maior número é o número: ",numero01)
elif numero02 > numero01 and numero02 > numero03:
    print("O maior número é o número: ",numero02)
elif numero03 > numero01 and numero03 > numero02:
    print("O maio número é o número: ",numero03)
else:
    print("Invalido")
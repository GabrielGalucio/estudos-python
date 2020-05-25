# Faça um Programa que leia três números e mostre o maior e o menor deles.

numero01 = int(input("Digite aqui o primeiro número: "))
numero02 = int(input("Digite aqui o segundo número: "))
numero03 = int(input("Digite aqui o terceiro número: "))

if (numero01 > numero02) and (numero01 > numero03):
    print("O maior número é o número: ",numero01)
elif (numero02 > numero03):
    print("O maior número é o número: ",numero02)
else:
    print("O maior número é o número: ",numero03)

if (numero01 < numero02) and (numero01 < numero03):
    print("O menor número é o número: ",numero01)
elif (numero02 < numero03):
    print("O menor número é o número: ",numero02)
else:
    print("O menor número é o número: ",numero03)
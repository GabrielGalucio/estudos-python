# Faça um Programa que peça dois números e imprima o maior deles.

numero01 = int(input("Digite aqui o primeiro número: "))
numero02 = int(input("Digite aqui o segundo número: "))

if numero01 > numero02:
    print("O número: ",numero01," é maior que o número: ",numero02)
elif numero01 < numero02:
    print("O número: ",numero01," é menor que o número: ",numero02)
elif numero01 == numero02:
    print("O números são iguais")
else:
    print("Carateres informado invalidos")
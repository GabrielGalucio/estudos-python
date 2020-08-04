# Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.


print("Dias da semana")
print("1- Domingo")
print("2- Segunda")
print("3- Terça")
print("4- Quarta")
print("5- Quinta")
print("6- Sexta")
print("7- Sábado")

numero = int(input("Digite aqui o número do dia da semana que deseja: "))

if numero == 1:
    print("Você escolheu o domingo")
elif numero == 2:
    print("Você escolheu a segunda-feira")
elif numero == 3:
    print("Você escolheu a terça-feira")
elif numero == 4:
    print("Você escolheu a quarta-feira")
elif numero == 5:
    print("Você escolheu a quinta-feira")
elif numero == 6:
    print("Você escolheu a sexta-feira")
elif numero == 7:
    print("Você escolheu o sábado")
else:
    print("Escolha inválida")
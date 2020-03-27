# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

print("****CALCULADORA DE NOTAS BIMESTRAIS*****")
nota01 = float(input("Digite aqui a primeira nota: "))
nota02 = float(input("Digite aqui a segunda nota: "))
nota03 = float(input("Digite aqui a terceira nota: "))
nota04 = float(input("Digite aqui a quarta nota: "))

media = (nota01 + nota02 + nota03 + nota04) / 4
print("A média do aluno é:", media)
if media <= 3:
    print("O Aluno está reprovado ")
elif media > 3 and media < 7:
    print("O aluno vai para recuperação")
elif media >= 7:
    print("O Aluno está aprovado")



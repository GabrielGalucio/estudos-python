numero01 = int(input("Digite aqui o valor do primeiro número: "))
numero02 = int(input("Digite aqui o valor do segundo número: "))
media = (numero01 + numero02) / 2

if media >= 7 and media != 10:
    print("O Aluno está aprovado")
elif media < 7:
    print("O ALuno está reprovado")
else:
    print("O Aluno está aprovado com distinção")
# Faça um programa para a leitura de duas notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota01 = float(input("Digite aqui o valor da primeira nota: "))
nota02 = float(input("Digite aqui o valor da segunda nota: "))
media = (nota01 + nota02) / 2

if media >= 7 and media != 10:
    print("O aluno está aprovado com a média: ",media)
elif media < 7:
    print("O aluno está reprovado com a média: ",media)
else:
    print("O aluno está aprovado com distinção com a nota: ",media)
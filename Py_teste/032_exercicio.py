"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média.
A atribuição de conceitos obedece à tabela abaixo:

Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
"""
nota_01 = float(input("Digite aqui o valor da 1 nota: "))
nota_02 = float(input("Digite aqui o valor da 2 nota: "))
valor_media = (nota_01 + nota_02) / 2

if (valor_media >= 9) and (valor_media <= 10):
  print("Aluno aprovado no conceito A, APROVADO")

elif(valor_media >= 7.5) and (valor_media < 9):
  print("Aluno aprovado no conceito B, APROVADO")

elif(valor_media >= 6) and (valor_media < 7.5):
  print("Aluno aprovado no conceito C, APROVADO")

elif(valor_media >= 4) and (valor_media < 6):
  print("Aluno aprovado no conceito D, REPROVADO")

elif(valor_media >= 0) and (valor_media < 4):
  print("Aluno aprovado no conceito E, REPROVADO")

else:
  print("Valores invalidos")

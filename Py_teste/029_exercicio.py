"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram
para desenvolver o programa que calculará os reajustes.

Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério
baseado no salário atual:
1- salários até R$ 280,00 (incluindo) : aumento de 20%
2- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
3- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
4- salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:

o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""

salario = float(input("Digite aqui o valor do seu salário: "))

if (salario <= 280):
    salario_aumento = salario * 1.20
    print("Seu salario antes do reajusto era: ",salario)
    print("Seu salario aumentou em 20%:")
    print("O valor do aumento é: ", salario_aumento - salario)
    print("Seu salário após o reajusto é: ",salario_aumento)

elif (salario > 280) and (salario <= 700):
    salario_aumento = salario * 1.15
    print("Seu salario antes do reajusto era: ",salario)
    print("Seu salario aumentou em 15%:")
    print("O valor do aumento é: ", salario_aumento - salario)
    print("Seu salário após o reajusto é: ",salario_aumento)

elif (salario > 700) and (salario <= 1500):
    salario_aumento = salario * 1.10
    print("Seu salario antes do reajusto era: ",salario)
    print("Seu salario aumentou em 10%:")
    print("O valor do aumento é: ", salario_aumento - salario)
    print("Seu salário após o reajusto é: ",salario_aumento)

elif (salario > 1500):
    salario_aumento = salario * 1.5
    print("Seu salario antes do reajusto era: ",salario)
    print("Seu salario aumentou em 5%:")
    print("O valor do aumento é: ", salario_aumento - salario)
    print("Seu salário após o reajusto é: ",salario_aumento)

else:
    print("Salário inválido")




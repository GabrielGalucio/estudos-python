"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos
são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo)e 3% 
para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descont
ado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto meno
s os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantida
de de horas trabalhadas no mês.

Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
"""

qtd_salario_horas =int(input("Digite aqui o valor que você ganha por hora: "))
qtd_horas_trabalhadas = int(input("Digite aqui a quantidade de horas trabalhadas no mês: "))
salario_bruto = qtd_horas_trabalhadas * qtd_salario_horas

if (salario_bruto <= 900):
        desconto_INSS = (10 * salario_bruto) / 100
        desconto_FGTS = (11 * salario_bruto) / 100
        salario_liquido = salario_bruto - desconto_INSS
        total_descontos = desconto_INSS
        print("O valor do salário bruto é: R$",salario_bruto)
        print("O valor do desconto do INSS é: R$",desconto_INSS)
        print("O valor do desconto do FGTS é: R$",desconto_FGTS)
        print("O valor total de descontos é: R$",total_descontos)
        print("O valor do salário líquido é: R$",salario_liquido)

elif (salario_bruto > 900) and (salario_bruto <= 1500):
        desconto_IR = (5 * salario_bruto) / 100
        desconto_INSS = (10 * salario_bruto) / 100
        desconto_FGTS = (11 * salario_bruto) / 100
        total_descontos = desconto_IR + desconto_INSS
        salario_liquido = salario_bruto - desconto_INSS - desconto_IR
        print("O valor do salário bruto é: R$",salario_bruto)
        print("O valor do desconto do INSS é: R$",desconto_INSS)
        print("O valor do desconto do FGTS é: R$",desconto_FGTS)
        print("O valor total de descontos é: R$",total_descontos)
        print("O valor do salário líquido é: R$",salario_liquido)

elif (salario_bruto > 1500) and (salario_bruto <= 2500):
        desconto_IR = (10 * salario_bruto) / 100
        desconto_INSS = (10 * salario_bruto) / 100
        desconto_FGTS = (11 * salario_bruto) / 100
        total_descontos = desconto_IR + desconto_INSS
        salario_liquido = salario_bruto - desconto_INSS - desconto_IR
        print("O valor do salário bruto é: R$",salario_bruto)
        print("O valor do desconto do INSS é: R$",desconto_INSS)
        print("O valor do desconto do FGTS é: R$",desconto_FGTS)
        print("O valor total de descontos é: R$",total_descontos)
        print("O valor do salário líquido é: R$",salario_liquido)

elif (salario_bruto > 2500):
        desconto_IR = (20 * salario_bruto) / 100
        desconto_INSS = (10 * salario_bruto) / 100
        desconto_FGTS = (11 * salario_bruto) / 100
        total_descontos = desconto_IR + desconto_INSS
        salario_liquido = salario_bruto - desconto_INSS - desconto_IR
        print("O valor do salário bruto é: R$",salario_bruto)
        print("O valor do desconto do INSS é: R$",desconto_INSS)
        print("O valor do desconto do FGTS é: R$",desconto_FGTS)
        print("O valor total de descontos é: R$",total_descontos)
        print("O valor do salário líquido é: R$",salario_liquido)

else:
        print("Valor invalido, por favor volte ao menu")


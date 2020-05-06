# Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas
# ao mês, sabendo que é descontado 11% para o imposto de renda, 8% para o INSSe 5% para o
# sindicato, faça um programa que nos dê:

# A) O salário bruto
# B) Quanto pagou ao INSS
# C) Quanto pagou ao sindicato
# D) O salário líquido
# E) Calcule os descontos e o salário líquido conforme tabela abaixo

# Salario_Bruto 

valor_hora = (float(input("Digite aqui o valor que você ganha por hora: ")))
hora_trabalhada = (int(input("Digite aqui a quantidade de horas trabalhadas: ")))

salario_bruto = valor_hora * hora_trabalhada
salario_renda = (11 * salario_bruto) / 100
salario_inss = (8 * salario_bruto) / 100
salario_sindicato = (5 * salario_bruto) / 100
salario_liquido = salario_bruto - salario_renda - salario_inss - salario_sindicato

# OU

# salario_bruto = valor_hora * hora_trabalhada
# salario_renda = salario_bruto * 0.11
# salario_inss = salario_bruto * 0.08
# salario_sindicato = salario_bruto * 0.05
# salario_liquido = salario_bruto - salario_renda - salario_inss - salario_sindicato

print("Valor do salário bruto: ", salario_bruto)
print("Valor pago ao Imposto de renda: ", salario_renda)
print("Valor pago ao INSS: ", salario_inss)
print("Valor pago ao sindicato: ", salario_sindicato)
print("Valor líquido que você receberá: ", salario_liquido)
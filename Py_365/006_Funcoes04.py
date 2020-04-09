# Definindo função dentro de função


# É possível interligar funções dentro de funções, como no exemplo descritivo
# abaixo, onde a 1 função (input) se torna o (output) da 2 função. Segue a fun
# ção para calcular o ganho de salário por horas trabalhadas

def salario(horas_trabalho):
    return horas_trabalho * 25

def bonus(horas_trabalho):
    return salario(horas_trabalho) + 50

print(salario(5))
print(bonus(5))
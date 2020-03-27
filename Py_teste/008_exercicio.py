# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

print("****CALCULADORA DE REMUNERAÇÃO POR HORA*****")
valorHora = float(input("Digite aqui quanto você ganha por hoje: "))
valorHoraMes = int(input("Digite aqui a quantidade de horas trabalhadas por mês: "))
remuneracaoTotal = valorHora * valorHoraMes
print("Sua remuneração neste mês é de: ", remuneracaoTotal,"R$ reais")
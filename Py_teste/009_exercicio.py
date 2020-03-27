# Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura
# em graus Celsius. C = (5 * (F-32) / 9).

print("****TRANSFORMANDO GRAUS FARENHEIT PARA CELCIUS*****")
frht = float(input("Digite aqui a temperatura em Farenheit: "))
celcius = (5 * (frht - 32) / 9)
print("A temperatura ", frht, "em celcius equivale a: ", celcius, "graus celcius")
# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

print("****CALCULANDO A AREA DE UM CIRCULO*****")

# A área de qualquer circulo é igual a :  π  vezes o raio do circulo ao quadrado.
# Fica assim:    A =  π . r²     //sendo π  aproximadamente  3,14.

pi = 3.14
raio = float(input("Digite aqui o raio do circulo"))
area = pi * (raio ** 2)
print("A area do circulo é: ", area)
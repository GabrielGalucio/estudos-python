"""
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores 
podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, 
isósceles ou escaleno.

Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
"""

lado_01 = int(input("Digite aqui o valor do primeiro lado: "))
lado_02 = int(input("Digite aqui o valor do segundo lado: "))
lado_03 = int(input("Digite aqui o valor do terceiro lado: "))


if (lado_01 == lado_02) and (lado_01 == lado_03) and (lado_02 == lado_03):
    print("É um triangulo Equilatero")

elif (lado_01 == lado_02) or (lado_02 == lado_03) or (lado_01 == lado_03):
    print("É um triangulo Isósceles")

elif (lado_01 != lado_02) or (lado_02 != lado_03) or (lado_01 != lado_03):
    print("É um triangulo Escaleno")

elif (lado_01 + lado_02 > lado_03):
    print("É um triangulo")

else:
    print("erro")
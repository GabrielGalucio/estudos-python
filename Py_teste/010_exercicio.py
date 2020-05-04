# Faça um programa que peça 2 números inteiros e um numero real, Calcule e mostre:
# A) O produto do dobro do primeiro com a metade do segundo
# B) a soma do triplo do primeiro com o terceiro
# C) O terceiro elevado ao cubo
numero_inteiro_01 = (int(input("Digite aqui o valor do primeiro numero inteiro: ")))
numero_inteiro_02 = (int(input("Digite aqui o valor do segundo número inteiro: ")))
numero_real = (float(input("Digite aqui o valor do terceiron número real: ")))

print("O primeiro número inteiro é: ",numero_inteiro_01 )
print("O segundo número inteiro é: ", numero_inteiro_02)
print("O terceiro número real é:", numero_real)
print("*********************************************")

# A) O produto do dobro do primeiro com a metade do segundo
respA = numero_inteiro_01 * 2 * (numero_inteiro_02 / 2)
print("A) O produto do dobro do primeiro com a metade do segundo é: ", respA)

# B) A soma do triplo do primeiro com o terceiro
respB = (numero_inteiro_01 * 3) + numero_real
print("B) A soma do triplo do primeiro com o terceiro é: ", respB)

# C) O terceiro elevado ao cubo
respC = numero_real ** 3
print("C) O terceiro número elevado ao cubo é: ", respC)

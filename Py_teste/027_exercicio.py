# Faça um Programa que leia três números e mostre-os em ordem decrescente.

numero01 = int(input("Digite aqui o primeiro numero: ")) 
numero02 = int(input("Digite aqui o segundo numero: "))
numero03 = int(input("Digite aqui o terceiro numero: "))


123
132

231
213

321
312

if (numero01 < numero02) and (numero01 < numero03) and (numero02 < numero03):
    print(f"Menor pro maior: {numero01}, {numero02}, {numero03}")

elif (numero01 < numero02) and (numero01 < numero03) and (numero03 < numero02):
    print(f"Menor pro maior: {numero01}, {numero03}, {numero02}")

elif (numero02 < numero01) and (numero02 < numero03) and (numero03 < numero02):
    print(f"Menor pro maior: {numero02}, {numero03}, {numero01}")

elif (numero02 < numero01) and (numero02 < numero03) and (numero02 < numero03):
    print(f"Menor pro maior: {numero02}, {numero01}, {numero03}")

elif (numero03 < numero01) and (numero03 < numero02) and (numero02 < numero01):
    print(f"Menor pro maior: {numero03}, {numero02}, {numero01}")

elif (numero03 < numero01) and (numero03 < numero02) and (numero01 < numero02):
    print(f"Menor pro maior: {numero03}, {numero01}, {numero02}")

else:
    print("Fiquei com preguiça de fazer o tratamento do erro, mas foi esse crlh só com if")




    


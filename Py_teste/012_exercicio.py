# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule
# o seu peso ideal utilizando as seguintes formulas: 
# Para homens: (72.7 * h) - 58
# Para mulheres: (62.1 * h) - 44.7

altura_usuario = (float(input("Digite aqui a sua altura: ")))
sexo_usuario = input("Digite M para masculinah ou F para femininah: ")
if sexo_usuario.upper() == "M":
    peso_ideal_M = (72.7 * altura_usuario) - 58
    print("Olá! seu peso ideal é: ", peso_ideal_M)
elif sexo_usuario.upper() == "F":
    peso_ideal_F = (62.1 * h) - 44.7
    print("Olá! seu peso ideal é: ", peso_ideal_F )
else:
    print("Informação não compativel")

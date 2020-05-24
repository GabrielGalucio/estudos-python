##### CALCULADORA BÁSICA EM PYTHO #####

print("########### CALCULADORA DO GALU ###########")
print("################ OPÇÕES ###################")
print("1- PARA SOMAR +")
print("2- PARA SUBTRAIR -")
print("3- PARA MULTIPLICAR x")
print("4- PARA DIVISÃO %")

escolha = int(input("Digite aqui 1/2/3/4 para escolher a operação: "))

if escolha == 1:
    numero_som_01 = int(input("Digite aqui o primeiro número: "))
    numero_som_02 = int(input("Digite aqui o segundo número: "))
    resultado_som = numero_som_01 + numero_som_02
    print(f"O resultado da soma entre {numero_som_01} + {numero_som_02} é: {resultado_som}")

elif escolha == 2:
    numero_sub_01 = int(input("Digite aqui o primeiro número: "))
    numero_sub_02 = int(input("Digite aqui o segundo número: "))
    resultado_sub = numero_sub_01 - numero_sub_02
    print(f"O resultado da subtração entre {numero_sub_01} - {numero_sub_02} é: {resultado_sub}")

elif escolha == 3:
    numero_mul_01 = int(input("Digite aqui o primeiro número: "))
    numero_mul_02 = int(input("Digite aqui o segundo numero: "))
    resultado_mul = numero_mul_01 * numero_mul_02
    print(f"O resultado da multiplicação entre {numero_mul_01} x {numero_mul_02} é: {resultado_mul}")

elif escolha == 4:
    numero_div_01 = int(input("Digite aqui o primerio número: "))
    numero_div_02 = int(input("Digite aqui o segundo número: "))
    resultado_div = numero_div_01 / numero_div_02
    print(f"O resultado da multiplicação entre {numero_div_01} x {numero_div_02} é: {resultado_div}")
    
else:
    print("Escolha invalida, por favor digita 1, 2, 3 ou 4")
    print("Execute novamente o código para reiniciar.") 


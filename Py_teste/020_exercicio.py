# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

numero = float(input("DIgite aqui qualquer número"))

if numero == 0:
    print(f"O número {numero} é neutro")
elif numero > 0:
    print(f"O número {numero} é positivo")
elif numero < 0:
    print(f"O número {numero} é negativo")
else:
    print("Caractere informado invalido")
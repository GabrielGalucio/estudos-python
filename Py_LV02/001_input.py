# Declarando inputs
# input("Digite aqui qualquer coisa:")

# Declarando input com variavel

nome_usuario = input("Informe aqui o sue nome: ")
print("O nome do usuário é",nome_usuario," ;)")
print(f"O nome do usuário é {nome_usuario} x)")

# Verificando o tipo da variavel criada, observe que é uma string
print(type(nome_usuario))


# Agora vamos usar com calculo

numero01 = float(input("Digite aqui o primeiro número: "))
numero02 = float(input("Digite aqui o segundo número: "))
calculo = numero01 + numero02
print(calculo)
print(type(calculo))

# Pode-se converter após pegar o input
numero03 = input("Digite aqui o terceiro número: ")
numero04 = input("Digite aqui o quarto número: ")
calculo02 = int(numero03) + int(numero04)
print(calculo02)
print(type(calculo02))
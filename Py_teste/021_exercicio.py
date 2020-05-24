# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
letra = input("Digite aqui F para feminnino ou M para masculino: ")

# Só quis transformar mesmo ;)
L = letra.upper()

if L == "F":
    print("Sexo: Feminino")
elif L == "M":
    print("Sexo: Masculino")
else:
    print("Sexo invalido")


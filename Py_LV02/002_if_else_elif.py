login_usuario = input("Digite aqui o seu nome de usuário: ")
senha_usuario = input("Digite aqui a sua senha de usuário: ")

if login_usuario == "gabriel.galucio" and senha_usuario == "soufeliz1998":
    print("Login realizado com sucesso")
else:
    print("Login ou senha incorreto")


# Mais um teste
# Calcular media e:
# >= 7 : APROVADO
# < 7 : REPROVADO
# 10 : APROVADO CON DINSTINÇÃO

numero01 = int(input("Digite aqui o valor do primeiro número: "))
numero02 = int(input("Digite aqui o valor do segundo número: "))
media = (numero01 + numero02) / 2

if media >= 7 and media != 10:
    print("O Aluno está aprovado")
elif media < 7:
    print("O ALuno está reprovado")
else:
    print("O Aluno está aprovado com distinção")
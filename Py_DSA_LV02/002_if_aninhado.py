nome_usuario = input("Informe aqui o seu nome: ")
idade_usuario = int(input("Informe aqui a sua idade: "))

usuario_atual = nome_usuario.upper()

if usuario_atual == "GABRIEL":
    print("Olá Usuario", usuario_atual)
    if idade_usuario > 18:
        print("Você pode dirigir", nome_usuario)
    elif idade_usuario < 18 and idade_usuario != 17:
        print("Você não pode dirigir", usuario_atual)
    else:
        print("Você pode ter uma pré carteira", usuario_atual)
else:
    print("Usuario invalido")
'''
# Desafio 1 - Exiba todos os nomes dos inscritos que estão no arquivo inscritos.txt no console


with open("inscritos.txt","r") as arquivo:
    for listar in arquivo:
        print(listar)

'''
'''
Desafio 2 - Adicione o seu nome na lista de inscritos e depois todos 
os nomes que estão no arquivo inscritos.txt no console

nome = "Gabriel"
with open("inscritos.txt","a") as arquivo:
    arquivo.write("Gabriel")
'''
nlinhas = 0
with open("inscritos.txt","r") as arquivo: 
    for exibir in arquivo:
        print(nlinhas, exibir, end="")
        nlinhas = nlinhas + 1
        

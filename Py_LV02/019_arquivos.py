valores_celulares = [850, 1200, 1800, 2000, 2500]

'''
'r' -> Usado somente para ler algo
'w' -> Usado somente para escrever algo
'r+' -> Usado somente ler e escrever algo
'a' -> Usado somente para acrescentar algo

'''
# Abrindo um arquivo para ler _. ele subsescreve
#with open("valores_celulares.txt","w") as arquivo:
#    for valor in valores_celulares:
#        arquivo.write(str(valor) + "\n")

# O mesmo, mas agora adicionando com "a"
#with open("valores_celulares.txt","a") as arquivo:
#    for valor in valores_celulares:
#        arquivo.write(str(valor) + "\n")

# Somente consulta
#with open("valores_celulares.txt","r") as arquivo:
#    for valor in arquivo:
#        print(valor)

# Ler e escrever
with open("valores_celulares.txt","r+") as arquivo:
    for valor in arquivo:
        print(valor)
    arquivo.write("9000")
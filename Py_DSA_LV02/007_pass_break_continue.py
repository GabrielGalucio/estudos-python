# Podemos ultilizar o loop while com parametros de pass, break ou continue

# break : para completamente o loop
# pass: continua com a execução do loop
# continue: pula uma iteração

# Vamos testar agora o loop while com if

numero = 0
while numero <= 10:
    if numero == 4:
        break
    else:
        pass # Esse pass volta para o while
    print("Numero atual: ", numero)
    numero = numero + 1

# O continue nesse exemplo ficou meio nebuloso, mas vamos exemplificar com for
# Ao executar, percebea que o loop pula a condiçã estabelecida (printar o "h")
frase_string = "Galucio"
for caractere in frase_string:
    if caractere == "u":
        continue
    print("A letra atual é: ", caractere)

# Utilizando o loop while, for e if juntos

for i in range(0,20):
    j = 2
    contador = 0
    while j < i:
        if i % 2 == 0:
            contador = 1
            j = j + 1
        else:
            j = j + 1
    if contador == 0:
        print(str(i) + "é um número primo")
        contador = 0
    else:
        contador = 0
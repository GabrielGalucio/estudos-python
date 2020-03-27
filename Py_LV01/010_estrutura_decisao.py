condicao01 = 10


variavel01 = 2020
variavel02 = 2030

if condicao01 == 10:
    print("Condição verdadeira 01")

if variavel01 <= variavel02:
    print("COndição verdadeira 02")

# Aqui, convertemos o int para string:
if str(condicao01) == "10":
    print("Condição verdadeira 03")

if condicao01 != 2000 or variavel01 == 2020 or variavel02 > 1000:
    print("Condição verdadeira 04")

variavel03 = 3

if variavel03 == 1:
    print("Essa variavel é igual a 1")
elif variavel03 == 2:
    print("Essa variavel é igual a 2")
elif variavel03 == 4:
    print("Essa variavel é igual a 4")
else:
    print("A variavel não é igual a 1, 2 ou 4")


nota01 = 10
nota02 = 7
nota03 = 5
media = 2

if media >= nota01:
    print("Parabéns, você atingiu mais que 10 pontos")
elif media >= nota02:
    print("Parabéns, você atingiu mais que 7 pontos")
elif media <= nota03:
    print("Você está de recuperação")
    if  media == 5:
        print("Você tem direito a fazer um trabalho")
    else:
        print("Infelizmente você esta reprovado")
else:
    print("Parabéns")
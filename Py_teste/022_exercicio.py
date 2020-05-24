# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite aqui uma letra: ")
vogais = ["A","B","E","I","O","U"]
L = letra.upper()

if L in vogais:
    print("A letra é uma vogal")
elif L not in vogais:
    print("É uma consoante")
else:
    print("Comando invalido")


# Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

print("M = Matutino")
print("V = Vespertino")
print("N = Noturno")
turno = input("Digite aqui o turno que você estuda: ")

if turno.upper() == "M":
    print("Bom dia aluno")
elif turno.upper() == "V":
    print("Boa tarde aluno")
elif turno.upper() == ("N"):
    print("Boa noite aluno")
else:
    print("Caratere invalido")
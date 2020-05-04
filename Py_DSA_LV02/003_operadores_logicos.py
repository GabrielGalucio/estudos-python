# Operadores lógicos

# > maior
# < menor
# >= maior ou igual
# <= menor ou igual
# != diferente
# == igual


disciplina = input("Digite aqui o nome da disciplina: ")
nota_final = float(input("Digite aqui a sua nota final: "))
periodo = int(input("Digite aqui o periodo que você esta: "))

if nota_final >= 50 and nota_final != 45:
    print("Parabens você foi aprovado na disciplina de %a com a nota de %b no %c periodo", disciplina, nota_final, periodo)
elif nota_final < 44:
    print("Infelizmente você está reprovado")
else:
    print("Você pode optar pela recuperação")


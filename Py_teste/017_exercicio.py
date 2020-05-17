# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da
# área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
# que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que 
# custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# 1- comprar apenas latas de 18 litros;
# 2- comprar apenas galões de 3,6 litros;
# 3- misturar latas e galões, de forma que o preço seja o menor. 
# 4- Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

# recebe area m2
# 1 litro -> 6m2
# 1 tinta -> 18l -> 80 reais 
# 1 tinta -> 3,6l -> 25 reais


area = float(input("Digite aqui a quantidade de metros quadrado a ser pintado: "))
print("\n")

quantidade_litros_necessarios = (area / 6) * 1.1 # 10% de folga

quantidade_latas_tinta = int(quantidade_litros_necessarios / 18)
quantidade_galao_tinta = int(quantidade_litros_necessarios /3.6)

# Criando condição para calculo de quantidade de latas
if (quantidade_litros_necessarios % 18 != 0):
    quantidade_latas_tinta = quantidade_latas_tinta + 1

# Criando condição para calculo de quantidade de galao
if (quantidade_litros_necessarios % 3.6 != 0):
    quantidade_galao_tinta = quantidade_galao_tinta + 1

# Criando condição para calculo de mistura de latas e galoes
misturaLatas = int(quantidade_litros_necessarios / 18)
misturaGalao = int((quantidade_litros_necessarios - (misturaLatas * 18)) / 3.6)

if ((quantidade_litros_necessarios - (misturaLatas * 18) % 3.6 != 0)):
    misturaGalao = misturaGalao + 1

print("Latas: ", quantidade_latas_tinta)
print("Valor: ", quantidade_latas_tinta * 80)
print("\n")
print("Galão: ", quantidade_galao_tinta)
print("Valor: ", quantidade_galao_tinta * 25)
print("\n")
print("Latas: ",misturaLatas, "e", misturaGalao)
print("Valor: ", (misturaLatas * 80) + (misturaGalao * 25))


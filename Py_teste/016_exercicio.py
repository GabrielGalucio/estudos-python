# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados
# da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadr
# dos e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a
# quantidades de latas de tinta a serem compradas e o preço total.

tam_metro_quadrado = (float(input("Digite aqui o tamanho em m2 da área a ser pintada: ")))
# 1 litro para 3 metros
tinta_litro = 18
tinta_valor = 80

# 1 litro -> 3m
# 1 tinta -> 18l
# 1 tinta -> 80,00

quant_litros_necessario = tam_metro_quadrado / 3
quant_latas_tinta = quant_litros_necessario / tinta_litro
preco_total = quant_latas_tinta * tinta_valor

print(f"Você precisará de {quant_latas_tinta} para pintar")
print(f"Você precirá pagar {preco_total}")



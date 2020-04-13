# Exemplos de iterações com dicionários

# Declarando um dicionário:

precos = {
    "caixa_de_espaguete":4,
    "massa_de_lasanha":10,
    "carne_de_hamburguer":4
    }

quantidade = {
    "caixa_de_espaguete":10,
    "massa_de_lasanha":40,
    "carne_de_hamburguer":35
    }

# Verificando quanto foi gasto no supermercado
# precos * quantidade
dinheiro_gasto = 0
for i in precos:
    dinheiro_gasto = dinheiro_gasto + (precos[i] * quantidade[i])

print(dinheiro_gasto)

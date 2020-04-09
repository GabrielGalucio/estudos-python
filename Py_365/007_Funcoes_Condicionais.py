# Combinando funções com condicionais

# Dado um valor númerico, se o mesmo for mairo que 100 (cem) adicionar mais
# 10 (dez) ao valor original e retornar através de uma função.

def valor_add(dinheiro):
    if dinheiro > 100:
        dinheiro = dinheiro + 10
        return dinheiro
    else:
        return "Guarde mais dinheiro"


print(valor_add(200))
        
num01 = 1.2
num02 = -1.2
num03 = -992.18
num04 = 18.455
num05 = 1.      # É lido como 1.0 (forma reduzida)

# A comparação do tipo float pode ser limitada.

2.0 == 2.0                  # True
2.0 == 2.1                  # False
2.0000001 == 2.0            # False
2.000000000000001 == 2.0    # True
# A partir deste ponto, o computador (python) não consegue distinguir o tamanho
# de float que é cerca de 16 casas decimais e começa a genralizar como um igual.
# isso porde afetar muito o código que você está elaborando, números exatos são
# essenciais. O mesmo pode acontecer com operações matematicas, como exemplo:

resultado01= 0.1 + 0.1 + 0.2
# OU  NÃO
resultado02 = 0.1 + 0.1 + 0.2 - 0.3

print(resultado01)
print(resultado02)

# Quando os números tem muitos digitos, é conveniente encurtar a notação
# Usamos a notação cientifica nesses casos. Notação (n)e(expoente), onde
# n é o número que mutiplica 10 no expoente.

ntc01 = 1.13e15
ntc02 = 1e0
ntc03 = 1e1
ntc04 = 1e2
ntc05 = 25e1

print(ntc01)
print(ntc02)
print(ntc03)
print(ntc04)
print(ntc05)

# Python permite também trabalhar com números complexos, ou seja, podemos
# representar números complexos como uma soma de parte real e imaginária.
# A parte imaginária tem o formato (n)j onde n é um valor númerio e j in-
# dica que essa parte é uma valor imaginário, conforme o exemplo:
compx01 = 2 + 3j
compx02 = 2.55 + 1.52j
compx03 = 3.7 - 6j

print(compx01)
print(compx02)
print(compx03)








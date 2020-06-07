# Valores aleatoiros em python

# EX 1: Você quer simular um jogador de moedas que de cara ou coroa
# EX 2: Você quer fazer um sorteio de 300 nomes de uma lista de nomes
# EX 3: Você quer escolher aleatoriamente um número de 10 a 100
# EX 4: Você quer escolher uma carta aleatoriamente de um baralho
# EX 5: Você quer gerar nomes de um usuŕio aleatoriamente
# EX 6: Você quer usar senhas seguras

import random

print(random.random())      # valores aleatorio de 0 ate 1.0
print(random.uniform(4,10)) # gera um valor DECIMAL entre um inicio ao fim
print(random.randint(4,10)) # gera um valor INTEIRO entre um inicio ao fim

cores = ["azul","vermelho","verde","roxo","rosa","laranja","turquesa","marrom","amarelo","lilás","preto","branco"]
print(random.choice(cores)) # escolhe aleatoriamente de uma lista

# podemos embaralhar uma lista tambem
baralho = ["carta01","carta02","carta03","carta04","carta05","carta06","carta07","carta08"]
random.shuffle(baralho)
print(baralho)

moeda = ["cara","coroa"]
print(random.choice(moeda))
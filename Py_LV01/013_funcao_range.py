# Função range -> entrega para o usuário uma sequencia numerica (somente de números inteiros)
# Função range -> também pode ser utilizada como um laço de repetição for (mais utilizado) po
# isso talvez seja um dos fluos de repetição mais importante e utilziados na linguagem python.

# Formas de declaranção do comando range
# range (fim)
# range (inicio, fim)
# range (inicio, fim, passo)

# A função range retorna valores sob demanda, ou seja, ao chamar a função, será exibido um pri
# meiro valor daquele "conjunto" e assim sucessivamente em cada vez que o usuário chamar range

# Declarando range
range(10)
# OBS01: É exibido na tela somente os intervalos de range 
print(range(10))
# OBS02: Para exibir todo o conteúdo de range, é necessário modificar para uma lista
print(list(range(10)))

# Declarando o lop FOR com range
for i in range(10):
    print(i)

# Testando o range() com dois valores -> range (inicio, fim), é possivel manipular de onde o
# usuario vai começar o range, não necessáriamente da posição zero.
print(list(range(5, 10)))
for j in range(5, 10):
    print(j)

# Testando o range() com os 3 paramentros -> range(inicio, fim, passo) -> com isso é possivel
# mainipular melhor a função, informando como o passo deve se comportar, já que no dois exem
# plos anteriores, não havia passo, e por default o range() percorre de um em um (sob demanda)

# Contando de 0 à 10, pulando de duas em duas posições
# o npumero 10 não é exibido pois ele nunca chega no final
print(list(range(0, 10, 2)))
for k in range(0, 10, 2):
    print(k)

# Possivel utilizar com numeros negativos também, ele somente vai diminuir pelo valor da variavel
print(range(5, 0, -1))
for l in range(5, 0, -1):
    print(l)

# Testando as condição com o range para indicar que, raalmente os teste são tautologicos
teste = range(0, 10) == range(0, 10, 1)
print(teste)

#Pegando todos os números pares
for m in range(0, 11, 2):
    print(m)

for n in range(0, 22, 3):
    print(n)
# O Loop while é uma das forms mais comuns de se fazer iterações, ela será executada
# repetidamente, seja por um grupo de isnstrução ou uma unica, desde que seja VERDEIRA


# SINTAXE
# while (instrução 01):
#    faça print('xxxxxxxxxxxxxxxxxxxxxxxxxxx')

# É importante que em determinado momento, a instrução contida em while seja verdadeira
# para assim ela ter um fim, se não, criamos um loop infinito na expressão.

# Imprimindo numero de 0 a 9

conjunto = 0
while conjunto <= 9:
    print("O número nesse momento é: ", conjunto)
    conjunto = conjunto + 1

# Podemos utilizar o else no loop while para parar a expressão também
numeros = 0
while numeros< 10:
    print("Número: ", numeros)
    numeros = numeros + 1
else:
    print("Fim da execução")

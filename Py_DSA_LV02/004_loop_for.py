# ENTENDO O FOR GABRIEL
# for = para
# for item in serie_ de_qualquer_coisa
# for pega um item que pode ser qualquer nome/ coisa para percorrer qualquer tipo de conjunto

# Pode-se ser utilizado em 
# 1- strings
# 2- listas
# 3- tuplas
# 4- elementos de dicionarios
# 5- arquivos

# Machine Learning é iteração = repetir processos para treinamento
tupla01 = (2,5,6,7,8)
for i in tupla01:
    print(i)

# Usando com dicionario
dicionario01 = ["coisa01","coisa02","coisa03","coisa04"]
for n in dicionario01:
    print(n)

# Usar com com range
for numero in range(0,100):
    print(numero)

# Verificando se os números são pares em um conjunto
for numero in range(0,20):
    if numero % 2 == 0:
        print(numero)

# range pode ser usado range(inicio, fim, condição)
# quero uma lista de x a y pulando o z por exemplo

for numero in range(0, 10, 3):
    print(numero)

# Podemos usar em uma string
frase = "O rato roeu a roupa do rei de roma"
for caractere in frase:
    print(caractere)

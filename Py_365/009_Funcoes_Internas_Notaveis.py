# A função type() permite que você obtenha o tipo de variavel que você usa;
# A função int() permite que você transforme seu argumento em um tipo int;
# A função float() permite que você transforme seu argumento em tipo float;
# A função str() permite que você transforme seu argumento em um tipo String;

print(type(100))
print(type(10.1))
print(type("Xô"))

# A funcao max() permite que você pegue o maior valor de uma conjunto de dados;
lista01 = [10, 20, 30, 40]
print(max(lista01))

# A funcao min() permite que você pegue o menor valor de uma conjunto de dados;
print(min(lista01))

# A função abs() permite que você obtenha um valor absoluto
variavel01 = -20
print(abs(variavel01))

# A função sum() pode somar todos os elementos de uma lista designada como argumento
lista02 = [10, 20, 30, 40, 50]
print(sum(lista02))

# A função round(x,y) retorna a flutuação do seu argumento arredondando para um núme
# ro especificado após o digito especificaod do 2 argumento, segue o exemplo:
numero01 = 5.7777
print(round(numero01))
numero02 = round(3.555, 2)
print(numero02)

# A função pow(x,y) pode potencializar um argumento:
potencia = pow(10, 2)
print(potencia) 

# A função len() verifica quantos elemento há em um objeto
variavel02 = "O rato roeu a roupa do rei de roma"
variavel03 = [1, 2, 3, 4, 5, "seis", "sete", 8, 9]
variavel04 = {"um":1, "dois":2, "tres":3, "quatro":4}
print(len(variavel02))
print(len(variavel03))
print(len(variavel04))
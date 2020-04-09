# É totalmente possivel utilizar mais de um argumento em uma função:
# conforme exemplificação ao algoritmo abaixo:

def expressao(numero01, numero02, numero03):
    resultado = numero01 - numero02 * numero03
    print("Parametro numero01 igual a: ",numero01)
    print("Parametro numero02 igual a: ",numero02)
    print("Parametro numero03 igual a: ",numero03)
    return resultado


print(expressao(10, 4, 2))
print(expressao(20, 6, 1))
print(expressao(13, 2, 2))

# Podemostambém inverter a ordem, declarando o valor direto na variavel
print(expressao(numero02=30, numero01=100, numero03=2))
print(expressao(numero02=17, numero01=500, numero03=7))
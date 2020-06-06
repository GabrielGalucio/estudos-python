# Exception -> tratamento de erros
# Nome do erro sempre na ultima linha

# Exemplo de erro
# try:
#     ano_atual = int(input("Digite aqui o ano atual: "))
# except ValueError:
#     print("Você deve digitar um número valido crlh")

# Necessário tratar o erro -> criando exceções
try:
    print(5/0)
except ZeroDivisionError:
    print("Burro do crlh, não dá pra dividir")
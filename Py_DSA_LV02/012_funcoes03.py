# Definindo mais funções em python ->funções dentro de funções
import math

def numPrimo(num):
    # Verificando se um número é primo ou não
    if (num % 2) == 0 and num > 2:
        return "Este número não é primo"
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if (num % i) == 0:
            return "Este número não é primo"
    return "Este número é primo"

print(numPrimo(541))


# Fazendo um slip com os dados
def splitString(text):
    return text.split(" ")

texto = "ESSA FUNÇÃO É BASTANTE UTIL PARA SEPARAR GRANDES VOLUMES DE DADOS"
print(splitString(texto))

textoSeparado = splitString(texto)
print(textoSeparado)

# Usando função pada deixar tudo em caiba baixa
texto02 = "Esse Texto Deve Estar Todo em Caixa Baixa"
def lowerCase(text):
    return text.lower()

texto02Tratado = lowerCase(texto02)
print(texto02Tratado)


# Pode haver o caso em que não sabemos o número de parametros que a função irá
# receber como argumento, para isso usamos o *vartuple que define conforme a e
# xecução da função, quando a mesma é chamada e informada de seus argumentos

def funcaoVariosParametros(arg01, *vartuple):
    print("O parametro passado foi: ",arg01)
    for i in vartuple:
        print("O parametro passado foi: ",i)
    return;

funcaoVariosParametros(10)
funcaoVariosParametros("Gabriel","Nathasha","José")




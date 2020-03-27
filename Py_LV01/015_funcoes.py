# Iniciando alguns exemplos com funções

# Funções são "pedaços" de código que podem ser chamadas e eecutados em qualquer parte
# do codigo que estiver sendo escrito. Funcionam como blocos mais fáceis de manipular.

# Pricipais vantagens em utilizar funções no desenvolvimento do código:
# 1- Reutilização de codigo;
# 2- Melhor depuração do código (erros)
# 3- Melhor legibildiade para o código.

# Exemplo 01: Função básica com parametro
def mensagem():
    print("Exibindo a primeira mensagem da função.")

# Chamando a função do Exemplo 01
mensagem()

# Exemplo 02: FUnção básica com parametro
def nome_do_usuario(nome):
    print("O nome do usuário é: ",nome)

# Chamandoa função do Exemplo 02
nome_do_usuario("Gabriel")
nome_do_usuario(123)

# Dados exemplos básicos, o tipo de função mais utilizada é a função com o return
# funções geralmente tem 3 caracteristicas -> a ENTRADA (paramentros da função) o
# PROCESSAMENTO (código dentro da função que vai tratar os parametros) e a SAIDA
# que é o return 9saída / resultado do processamento da função.

# Exemplo 03: FUnção simples com retorno
def funcaoSoma(numero01, numero02):
    return numero01 + numero02

resultado01 = funcaoSoma(10, 20)
print(resultado01)

# Atento pois o Python não define uma tipo de variavel, então a mesma função po-
# de ser usada também no uso de strings, concatenando duas palavras como no exemplo:
resultado02 = funcaoSoma('Gab','riel')
print(resultado02) 

# Testando uma função com demais laços de repetição -> é importante lembrar que quando uma
# função tiver return, no momento em que o return é executado, o fluxo sai da função e não
# executa mais as instruções abaixo dela, conforme no exemplo abaixo:

def teste():
    for i in range(10):
        if i > 2:
            return i
    print("Saiu do for")

# Observe que a opção print() nao foi executada, pois o return cumpriu a finalização da função
teste()

# Exemplificando uma função com a sequencia Fibonacci onde
"""

f(n) = {0, 1, F(n-1)+F(n-2)}

"""
def fibonacci(n):
    F0, F1 = 0, 1
    if n < 2:
        return n
    for i in range(2, n+1):
        Fn = F1 + F0
        F0, F1 = F1, Fn
    return Fn

# Nesse momento, o laço acima consegue reproduzir os fundamentos da função Fibonacci, mas é 
# necessario observar a função para confirmar que a lógica está sendo tautologica, utilizan
# do então o lçao de repritção for junto com a função.
for i in range(10):
    print('F(',i, ') = ', fibonacci(i), sep = '')
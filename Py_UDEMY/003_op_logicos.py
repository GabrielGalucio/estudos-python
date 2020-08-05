"""
and
or
not
in
in not
"""
num01 = 2
num02 = 4
num03 = 6
num04 = 8

print( not num01 == num02 or not num03 == num04)

# o not é bastante utilizado para verificar o conteudo de veriaveis vazias
a = 'a'
b = 2

if not b:
    print("Informe um valor para a variavel")


# O in 'bem legal por que tambem pesquisa coisas em string
nome = "Gabriel Galucio"
vetor = [10,20,30,40,50,60]
lista = (10,20,30,40,50,60)
dicionario = {'vai':1, 'foi':2}

if 10 in dicionario:
    print("o Valor existe")
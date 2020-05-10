# Metodos são "funções" incorporadas ao objeto -> sua sintaxe .nomemetodo() pode ser anexada
# ao objeto que estamos manipulando, com ela podemos manipular ainda melhor esses objetos. Os
# metodos permitem eecutar ações especificas nos objetos e também podem levar parametros assim
# como as funções com a sintaxe objeto.metodo(arg1, arg2 ....)

lista = [10, 10, 20, 30, 40, 50, 60, 70]
print(lista)

# Metodo .append() permite adicionar um elemento no final de uma lista
lista.append(80)
print(lista)

# Metodo .count() conta quantos elementos (repetidos) aparecem em uma lista
print(lista.count(10))

# Metodo help() ajuda a mostrar o que determinado método realiza no objeto
# help(lista.pop)

# Metodo .dir() mostra todos os metodos atribuidos a um objeto
print(dir(lista))

# Metodo slip() fatia um objeto
frase = "Isso é uma string"
print(frase.split())

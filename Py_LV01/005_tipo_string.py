# String é basicamente um conjunto de caracteres;

string01 = "Exemplo de string aqui \n"
string02 = "Exemplo de string 1234 \n"
string03 = "1234567890123455678900 \n"
print(string01, string02, string03)

# As string em python já são apresentadas no formato UTF-8 ou seja
# elas podem receber acentuações sem problema nenhum> exemplo
string04 = "São João de Sá Enê"
print(string04)

# Inserindo aspas
string05 = "Gabriel disse 'olá' "
print(string05)

# Concatenação de strings
ex01 = "Olá "
ex02 = "Gabriel "
ex03 = "Galucio "
ex04 = "1998" 
print(ex01+ex02+ex03+ex04)

# Ainda é possivel aproveitar pequenas interações dos operadores com strings
# Ex: se utilizarmos o operado * -> o mesmo mutiplica a quantidade de carateres.
mult01 = "Galu "
mult02 = "Gabs "
print(mult01 * 10)
print(mult02 + 3 * mult01)

# Verificando o tamanho de uma string com a função len()
nome01 = "Gabriel Galúcio da Silva"
nome02 = "João Portilho Pereira da Silva Júnior"
print(len(nome01))
print(len(nome02))

# É possivel ainda dar um "zoom" e ver quais elementos formam uma string com o uso de []
zoom01 = "Lua"
print(zoom01[0])
print(zoom01[1])
print(zoom01[2])



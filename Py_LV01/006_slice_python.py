
# Trabalhando com cortes de string em python usandoa  fução slice[]
# existem basicamente 3 (três) formas de se fazer um slice com [] e
# que serão demonstradas aqui neste exemplo.

# A Primeira forma de slice é o proprio zoom mostrado em tipostring.py
# onde a variavel é fatiada e mostrado o valor pelo seu indice, confor
# me exemplificado abaixo:

variavel01 = "Lua"
print(variavel01[0])
print(variavel01[1])
print(variavel01[2])

# A segunda forma, utiliza 2 posições para fazer o fatiamento, sendo:
# assim ele pega os dados que estão entre as duas posições definidas.
variavel02 = "01234567890"
print(variavel02[0:3])
print(variavel02[3:6])
print(variavel02[1:7])

# Se não for indicado a primeira posição, por padrão começa do zero 0
# O mesmo vale para o fim do slice, se for colcoado somente o inicio o
# python por padrão pega todo o resto das posições na string
print(variavel02[:3])
print(variavel02[3:])

# Por fim, omitindo as posições de início e fim, o slice pega tudo
print(variavel02[:])

# É posivel utilizar indices negativos no fatiamento, o indice vai para
# o final da string e volta a partir do número informado
variavel03 = "0123456789"
print(variavel03[-4:]) 
print(variavel03[:-4])
print(variavel03[-6:-4])

# Finalizando, é possivel fatiar a string dentro da string, exemplos:
variavel04 = "0123456789"
print(variavel04[0:8:2]) # o ultimo valor "2" indica que a variavel vai pegar de 2 em 2 posições até 8 (a ultima)
                         # Pode-se aplica o mesmo fatiamento com intervalos nos outros modos
# Realizando testes com fatiamenteo de strings, dessa vez com uma string não numeral para entendimento.


frase01 = "O rato roeu a roupa do rei de roma"
print(len(frase01))
print(frase01[2:13])





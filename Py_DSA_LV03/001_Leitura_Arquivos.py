"""
Definindo arquivos

Python usa objetos de arquivo para interagir com arquivos em seu computador. Esses objetos de
arquivo podem ser qualquer tipo de arquivo como um arquivo de aúdio, um arquivo de texto, e-m
mails, documentos do Excel etc. Será necessário instalar bibliotecas ou modulos para execitar.

A linguagem (assim como outras) tem metodos built-in (internos) para manipulação de arquivos txt

open() Usado para abrir um arquivo
raad() Usado para ler um arquivo
write() Usado para gravação no arquivo
seek() Retorna para o inicio do arquivo
readlines() Retorna a lista de linhas do arquivo
close() Fecha o arquivo
"""

# Abrindo um arquivo para leitura
arq01 = open("/home/galucifer/Documentos/Estudos_Python/Py_DSA_LV03/arquivos/arquivo001.txt","r")
print(arq01.read())         # Exibe o conteúdo do arquivo
print(arq01.tell())         # Conta os caracteres do arquivo
print(arq01.seek(0,0))      # Retorna para o início do arquivo (0,0) posiciona na linha 0 coluna 0
print(arq01.read(10))       # Exibe os 10 primeiros caracteres de arquivo, como se fosse um slicing
                            # é importante frisar que ele pega a partir de onde está posicionado o 
                            # "ponteiro" no caso, colocamos no início com o método seek(0,0).

# Abrindo arquivo para escrita
arq02 = open("/home/galucifer/Documentos/Estudos_Python/Py_DSA_LV03/arquivos/arquivo001.txt","w")
arq02.write("Testando gravação de dados em um arquivo")     # Gravando os dados no arquivo
arq02.close()                                               # Fechando arquivo de escrita

# Lendo o arquivo gravado
arq02 = open("/home/galucifer/Documentos/Estudos_Python/Py_DSA_LV03/arquivos/arquivo001.txt","r")
print(arq02.read())

# Vamos tentar acrescentar cum conteúdo com o parametro "a"
arq02 = open("/home/galucifer/Documentos/Estudos_Python/Py_DSA_LV03/arquivos/arquivo001.txt","a")
arq02.write("Acrescentando mais uma informação ao arquivo 01")
arq02.close()

# Verificando se a gravação foi realizada sem sobrescrever
arq02 = open("/home/galucifer/Documentos/Estudos_Python/Py_DSA_LV03/arquivos/arquivo001.txt","r")
print(arq02.read())
print(arq02.seek(0,0))
print(arq02.read())







# obs01: Quando abrimos o arquivo somente para escrita, não é possivel ler, somente se fosse ambos

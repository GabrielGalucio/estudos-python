# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade 
# de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do 
# arquivo usando este link (em minutos).

tamanho_mb = int(input("Digite aqui o tamanho do dowload em MB: "))
velocidade = int(input("Digite aqui a velocidade da internet em Mbps: "))

tamanhoBits = tamanho_mb * 1024 * 1024 * 8
tempoSegundos = tamanhoBits / (velocidade * 1024 * 1024)
tempoMinutos = tempoSegundos / 60

print("Tempo aproximado de dowload: ", tempoMinutos, tempoSegundos)

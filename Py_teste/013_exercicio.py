# João é um pescador e precisa calcular o valor da multa de cada pesca que fez sendo que:
# 1-) 50 Kilos é o limite de peso da pesca
# 2-) Para cada quilo excedente a multa aumenta em 4 reais
# João quer que você faça um sistema de calule o valor da multa caso execeda o peso

peso_regulamento = 50

print("Olá João! seja bem vindo")
peso_pesca = (float(input("Digite aqui o peso da pesca de hoje: ")))

valor_multa = (peso_pesca - 50) 
valor_multa = valor_multa * 4

print("O Valor da multa atual é: ", valor_multa)


# Lembrando que nessa lista de exercicio não posso usar estrutura de decisão, logo essa foi
# uma das maneiras que consegui fazer, sendo necessario somente o tratamento caso não haja multa

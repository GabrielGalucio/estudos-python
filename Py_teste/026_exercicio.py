# Faça um programa que pergunte o preço de três produtos e informe qual produto você 
# deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto01 = float(input("Digite aqui o valor do 1 produto: "))
produto02 = float(input("Digite aqui o valor do 2 produto: "))
produto03 = float(input("Digite aqui o valot do 3 produto: "))

if (produto01 < produto02) and (produto01 < produto03):
    print("Você deve comprar o produto 01")
elif (produto02 < produto02):
    print("Você deve comprar o produto 02")
else:
    print("Você deve comprar o produto 03")
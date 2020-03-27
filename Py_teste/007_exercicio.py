# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta
# área para o usuário

# A = B X H -> Como um quadrado possui lado iguais, podemos substituir po L
print("****CALCULANDO A ÁREA DE UM QUADRADO****")
ladoB = float(input("Digite aqui o tamanho da base(b) do quadrado: "))
ladoA = float(input("Digite aqui o tamanho da altu(h) do quadrado: "))

area = ladoA * ladoB
dobro = area * 2
print("O tamanho da área do quadrado multiplicado é: ", area,"e o dobro é: ", dobro)
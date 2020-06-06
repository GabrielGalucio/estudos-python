estilo_musical = ["rock","pop","samba","pagode","classico","hip-hop"]

for estilo in estilo_musical:
    if estilo == "hip-hop":
        print("parado")
        break
    print(estilo)


print("############")


for estilo in estilo_musical:
    if estilo == "samba":
        continue
    print(estilo)

print("######################")

lista_precos = [3, 3.50, 4, 5, 6, 6.50, 7, 7.25]
for procurar in lista_precos:
    if procurar == 5:
        print(f"Encontramos o valor desejado, sendo ele o valor: {procurar}")
        break
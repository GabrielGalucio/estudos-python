# Alguns exemplos de dicionários em python
# Cada objeto do dicionário contem uma chave

dicionario01 = {"um":0, "dois":1, "tres":2, "quatro":3, "cinco":4, "seis":5, "sete":6, "oito":7}
dicionario02 = {10:0, 20:1, 30:2, 40:3, 50:4, 60:5, 70:6, 80:7, 90:8, 100:9, 110:10, 111:11}
print(dicionario01)
print(dicionario02)

# Pegando o valor de uma chave através dela
print(dicionario01["um"])

# Modificando o valor de um objeto no dicioario
dicionario01["dois"] = 22
print(dicionario01)

# Definindo uma lista de pessoas em departamentos
departamentos = {"dep_01":"Gabriel", "dep_02":["Luiza", "José", "Beatriz"]} 
print(departamentos)
dicionario01["dep_01"] = "teste"
print(departamentos)

# Mais uma forma de declaração de dicionários
time = {}
time["CEO"] = "Gabriel"
time["CTO"] = "José"
time["CFO"] = "Beatriz"
time["CRM"] = "Luiza"
time["CHRO"] = "Nonata"

print(time)
print(time["CEO"])

# Podemos utilizar o método get() também para pegar um valor
print(time.get("CTO"))
print(time.get("CFO"))


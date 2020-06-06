from datetime import datetime

# possivel acessar inteiro ou individualmente
print(datetime.now())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)

# datanascimento = datetime.strptime(input("Digite aqui a sua data de nascimento"),"%d/%m/%Y")
# print(datanascimento)
# print(type(datanascimento))

#  Simulando um prazo de entrega
data_inicio = datetime.now()
data_fim = datetime(2020,8,15)
data_entrega = data_fim - data_inicio
print(data_entrega)
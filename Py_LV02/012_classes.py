# Classes

# Devemos definir um construtor -> permite criar a funcionalidade inicial da classe
# o self nos permite acessar as propriedades ou métodos de uma instancia onde quiser

class Computador:
    def __init__(self, marca, memoria_ram, placa_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_video = placa_video
    
    # Definindo métodos
    def ligarPC(self):
        print("O computador está ligando")

    def desligarPC(self):
        print("O computador está desligando")

    def informacoesPC(self):
        print(self.marca)
        print(self.memoria_ram)
        print(self.placa_video)

computador01 = Computador("Samsung","4gb","Nvidia")  # Intanciando a classe = variavel do tipo computador01
computador02 = Computador("Assus","8gb","GeForce")   # Intanciando a classe = variavel do tipo computador02
computador03 = Computador("MAC","16gb","ATM")        # Intanciando a classe = variavel do tipo computador03

# Não é interessante deixar a classe estavel e sim dinamica, deve-se modelar a situação, propriedades n fixadas e sim dinamicas
print(computador01.marca, computador01.memoria_ram, computador01.placa_video) # Imprimindo na tela a marca do computador01
print(computador02.marca, computador02.memoria_ram, computador02.placa_video) # Imprimindo na tela a marca do computador01
print(computador03.marca, computador03.memoria_ram, computador03.placa_video) # Imprimindo na tela a marca do computador01

# Vamos pegar agora uma das instancias e chamar os metodos que criamos

computador01.ligarPC()
computador01.desligarPC()
computador01.informacoesPC()
# Criar classe carro
# 3 atributos
# 3 metodos
# exibir na tela


class Carro:
    def __init__(self, modelo, cor, placa):
        self.modelo = modelo
        self.cor = cor
        self.placa = placa

    def ligarCarro(self):
        print("Ligando o carro")

    def desligarCarro(self):
        print("Desligando o carro")

    def dadosCarro(self):
        print(self.modelo)
        print(self.cor)
        print(self.placa)

carro_gabriel = Carro("Gol","Vermelho","JXN-2943")

carro_gabriel.ligarCarro()
carro_gabriel.desligarCarro()
carro_gabriel.dadosCarro()
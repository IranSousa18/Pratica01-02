from classes.veiculo import Veiculo


class Carro(Veiculo):

    def __init__(self, placa, modelo, ano, valor_diaria, numero_portas):
        super().__init__(placa, modelo, ano, valor_diaria)
        self.numero_portas = numero_portas

    # Exibe os dados específicos do carro
    def exibir_dados(self):
        super().exibir_dados()
        print(f"Número de portas: {self.numero_portas}")

    # Retorna o tipo do veículo
    def tipo_veiculo(self):
        return "Carro"
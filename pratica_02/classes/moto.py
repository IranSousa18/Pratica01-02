from classes.veiculo import Veiculo


class Moto(Veiculo):

    def __init__(self, placa, modelo, ano, valor_diaria, cilindradas):
        super().__init__(placa, modelo, ano, valor_diaria)
        self.cilindradas = cilindradas

    # Exibe os dados específicos da moto
    def exibir_dados(self):
        super().exibir_dados()
        print(f"Cilindradas: {self.cilindradas}")

    # Retorna o tipo do veículo
    def tipo_veiculo(self):
        return "Moto"
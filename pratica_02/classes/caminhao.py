from classes.veiculo import Veiculo


class Caminhao(Veiculo):

    def __init__(self, placa, modelo, ano, valor_diaria, capacidade_carga):
        super().__init__(placa, modelo, ano, valor_diaria)
        self.capacidade_carga = capacidade_carga

    # Exibe os dados específicos do caminhão
    def exibir_dados(self):
        super().exibir_dados()
        print(f"Capacidade de carga: {self.capacidade_carga} toneladas")

    # Retorna o tipo do veículo
    def tipo_veiculo(self):
        return "Caminhão"
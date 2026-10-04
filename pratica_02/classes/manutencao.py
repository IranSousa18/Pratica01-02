class Manutencao:

    def __init__(self, data, tipo_servico, custo):
        self.data = data
        self.tipo_servico = tipo_servico
        self.custo = custo

    # Atualiza o custo da manutenção
    def atualizar_custo(self, novo_custo):
        self.custo = novo_custo

    # Exibe os dados da manutenção
    def exibir_dados(self):
        print(f"Data: {self.data}")
        print(f"Tipo de serviço: {self.tipo_servico}")
        print(f"Custo: R$ {self.custo:.2f}")
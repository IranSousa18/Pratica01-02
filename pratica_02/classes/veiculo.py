class Veiculo:

    def __init__(self, placa, modelo, ano, valor_diaria):
        self.placa = placa
        self.modelo = modelo
        self.ano = ano
        self.valor_diaria = valor_diaria

    # Exibe os dados do veículo
    def exibir_dados(self):
        print(f"Placa: {self.placa}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Valor da diária: R$ {self.valor_diaria:.2f}")

    # Altera o valor da diária
    def alterar_valor_diaria(self, novo_valor):
        self.valor_diaria = novo_valor
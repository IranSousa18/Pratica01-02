class Condutor:

    def __init__(self, nome, cnh, validade_cnh):
        self.nome = nome
        self.cnh = cnh
        self.validade_cnh = validade_cnh

    # Atualiza os dados do condutor
    def atualizar_dados(self, nome, cnh, validade_cnh):
        self.nome = nome
        self.cnh = cnh
        self.validade_cnh = validade_cnh

    # Exibe os dados do condutor
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CNH: {self.cnh}")
        print(f"Validade da CNH: {self.validade_cnh}")
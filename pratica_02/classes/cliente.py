class Cliente:

    def __init__(self, nome_razao_social, documento, telefone):
        self.nome_razao_social = nome_razao_social
        self.documento = documento
        self.telefone = telefone

    # Atualiza o telefone do cliente
    def atualizar_telefone(self, novo_telefone):
        self.telefone = novo_telefone

    # Exibe os dados do cliente
    def exibir_dados(self):
        print(f"Nome/Razão Social: {self.nome_razao_social}")
        print(f"Documento: {self.documento}")
        print(f"Telefone: {self.telefone}")
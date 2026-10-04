from classes.condutor import Condutor


class ContratoLocacao:

    def __init__(self, data_inicio, data_termino, valor_total, status, condutor):
        self.data_inicio = data_inicio
        self.data_termino = data_termino
        self.valor_total = valor_total
        self.status = status
        self.condutor = condutor

    # Finaliza o contrato
    def finalizar(self):
        self.status = "finalizado"

    # Cancela o contrato
    def cancelar(self):
        self.status = "cancelado"

    # Exibe os dados do contrato
    def exibir_dados(self):
        print(f"Data de início: {self.data_inicio}")
        print(f"Data de término: {self.data_termino}")
        print(f"Valor total: R$ {self.valor_total:.2f}")
        print(f"Status: {self.status}")

        print("\nCondutor:")
        self.condutor.exibir_dados()
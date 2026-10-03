class Endereco: # Cria a classe Endereco
    def __init__(self, rua, numero, cidade): # classe recebe rua, numero, cidade
        self.rua = rua # Guarda a rua
        self.numero = numero # Guarda o número
        self.cidade = cidade # Guarda a cidade


        def exibir_endereco(self): # Método criado para exibir o endereço
            return f"{self.rua}, {self.numero} - {self.cidade}"

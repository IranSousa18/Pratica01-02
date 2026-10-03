class Endereco: # Cria a classe Endereco
    def __init__(self, rua, numero, cidade): # A classe inicia com esses parâmetros
        self.rua = rua # Criação dos atributos
        self.numero = numero
        self.cidade = cidade


        def exibir_endereco(self): # Método criado para exibir o endereço
            return f"{self.rua}, {self.numero} - {self.cidade}"

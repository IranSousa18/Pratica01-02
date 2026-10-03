class Aluno: # Cria a classe aluno
    def __init__(self, nome, matricula, endereco): # Recebe nome, matricula e endereco
        self.nome = nome # guarda o nome
        self.metricula = matricula # guarda a matricula
        self.endereco = endereco # guarda um objeto endereco

    def estudar (self): # Exibe uma mensagem
        print(f'{self.nome} está estudadando.')
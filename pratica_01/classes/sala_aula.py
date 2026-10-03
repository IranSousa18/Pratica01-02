class SalaDeAula: # cria a classe SalaDeAula
    def __init__(self, numero, capacidade): # Recebe numero e capacidade
        self.numero = numero # Guarda o numero da sala
        self.capacidade = capacidade # Guarda a capacidade máxima de alunos na sala

    def abrirSala(self): # Exibe uma mensagem se a sala está aberta
        print(f'Sala n°{self.numero} está aberta.')
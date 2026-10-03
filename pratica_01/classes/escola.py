from classes.sala_aula import SalaDeAula # Importa a classe SalaDeAula

class Escola: # Cria a classe Escola
    def __init__ (self, nome): # Recene o nome da Escola
        self.nome = nome # Guarda p nome da escola
        self.salas = [] # Lista para guardar as salas
        self.professores = [] # Lista para guardar os professores

    def adicionar_sala(self, numero, capacidade): # Recebe dados da sala
        sala = SalaDeAula(numero, capacidade) # Cria uma sala
        self.salas.append(sala) # adiciona a sala a lista

    def adicionar_professor(self, professor): # Recebe um professor ja criado
        self.professores.append(professor) # Guarda o professor na escola

    def listar_salas(self): # Percorre cada sala e mostra seu número
        for sala in self.salas:
            print(f"Sala {sala.numero}")

    def listar_professores(self): # Percorre todos os professores e mostra seu nome
        for professor in self.professores:
            print(f"Professor {professor.nome}")
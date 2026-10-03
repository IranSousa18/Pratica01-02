class Professor: # Cria a classe Professor
    def __init__(self, nome, disciplina): # Clase recebe nome e disciplina
        self.nome = nome # Guarda o nome do Professor
        self.disciplina = disciplina # Guarda a Disciplina

    def ensinar (self): # Exibe o nome e a matéria que o professor está ensinando
        print(f'{self.nome} está ensinando {self.disciplina}')
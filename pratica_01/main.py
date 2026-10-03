from classes.aluno import Aluno # Importa todas as classe a serem utilizadas
from classes.professor import Professor
from classes.endereco import Endereco
from classes.escola import Escola

escola = Escola("Uninassau") # Cria a escola

escola.adicionar_sala(1, 40) # Criação de salas
escola.adicionar_sala(2, 40) # Primeira informção é o numero da sala e a segunda a capacidade

# Primeira informação é o nome e segunda sua matéria
professor = Professor("Coelho", "Coding") # Criação de professores
professor2 = Professor("Everton", "Engenharia de Requisitos")

# Associa o professor a uma escola
escola.adicionar_professor(professor)
escola.adicionar_professor(professor2)

# Cria um endereço
endereco1 = Endereco("Rua Dirceu", 4421, "Parnaíba")

# Cria um aluno e o associa ao endereço
aluno1 = Aluno("Tiririca", "20260101", endereco1)

#Exibe informações da escola
print(f"Escola \nNome: {escola.nome}")

#Exibindo salas
print("\nSalas")
escola.listar_salas()

#Exibindo professores
print('\nProfessores')
escola.listar_professores()

#Executando ações com os professores
professor.ensinar()
professor2.ensinar()

# Exibe informações do aluno
print(f"\nAluno\nNome: {aluno1.nome}\nMatrícula: {aluno1.metricula}")

# Exibe endereço do aluno
print(f"Endereço: {aluno1.endereco.exibir_endereco()}")

# Executando ação
aluno1.estudar()
from classes.carro import Carro
from classes.moto import Moto
from classes.caminhao import Caminhao
from classes.cliente import Cliente
from classes.condutor import Condutor
from classes.contrato_locacao import ContratoLocacao
from classes.manutencao import Manutencao


# Cria os veículos
carro = Carro("ABC1D23", "Toyota Corolla", 2025, 150.00, 4)
moto = Moto("XYZ4E56", "Honda CG 160", 2024, 80.00, 160)
caminhao = Caminhao("DEF7G89", "Volvo FH", 2023, 350.00, 25)


# Exibe os veículos
print("===== CARRO =====")
carro.exibir_dados()

print("\n===== MOTO =====")
moto.exibir_dados()

print("\n===== CAMINHÃO =====")
caminhao.exibir_dados()


# Cria um cliente
cliente = Cliente(
    "João da Silva",
    "123.456.789-00",
    "(86) 99999-9999"
)

print("\n===== CLIENTE =====")
cliente.exibir_dados()


# Cria um condutor
condutor = Condutor(
    "Carlos Souza",
    "12345678900",
    "10/10/2030"
)


# Cria um contrato e associa o condutor
contrato = ContratoLocacao(
    "04/10/2026",
    "10/10/2026",
    900.00,
    "ativo",
    condutor
)

print("\n===== CONTRATO =====")
contrato.exibir_dados()


# Finaliza o contrato
contrato.finalizar()

print("\n===== CONTRATO FINALIZADO =====")
print(f"Status: {contrato.status}")


# Cria uma manutenção para o carro
manutencao = Manutencao(
    "04/10/2026",
    "Troca de óleo",
    250.00
)

print("\n===== MANUTENÇÃO =====")
manutencao.exibir_dados()
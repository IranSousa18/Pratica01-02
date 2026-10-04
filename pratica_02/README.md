# Prática 02 - Sistema de Gerenciamento de uma Locadora de Veículos

## 1. Identificação de Classes

As classes identificadas no cenário são:

- `Veiculo`
- `Carro`
- `Moto`
- `Caminhao`
- `Cliente`
- `ContratoLocacao`
- `Condutor`
- `Manutencao`

## 2. Atributos e Métodos

### Veiculo

**Atributos:**

- `placa`
- `modelo`
- `ano`
- `valor_diaria`

**Métodos:**

- `exibir_dados()`
- `alterar_valor_diaria()`

### Carro

**Atributos:**

- `placa`
- `modelo`
- `ano`
- `valor_diaria`
- `numero_portas`

**Métodos:**

- `exibir_dados()`
- `tipo_veiculo()`

### Moto

**Atributos:**

- `placa`
- `modelo`
- `ano`
- `valor_diaria`
- `cilindradas`

**Métodos:**

- `exibir_dados()`
- `tipo_veiculo()`

### Caminhao

**Atributos:**

- `placa`
- `modelo`
- `ano`
- `valor_diaria`
- `capacidade_carga`

**Métodos:**

- `exibir_dados()`
- `tipo_veiculo()`

### Cliente

**Atributos:**

- `nome_razao_social`
- `documento`
- `telefone`

**Métodos:**

- `atualizar_telefone()`
- `exibir_dados()`

### ContratoLocacao

**Atributos:**

- `data_inicio`
- `data_termino`
- `valor_total`
- `status`
- `condutor`

**Métodos:**

- `finalizar()`
- `cancelar()`
- `exibir_dados()`

### Condutor

**Atributos:**

- `nome`
- `cnh`
- `validade_cnh`

**Métodos:**

- `atualizar_dados()`
- `exibir_dados()`

### Manutencao

**Atributos:**

- `data`
- `tipo_servico`
- `custo`

**Métodos:**

- `atualizar_custo()`
- `exibir_dados()`

## 3. Herança

Existe uma hierarquia de generalização/especialização entre as classes de veículos.

A classe `Veiculo` é a **superclasse**, enquanto `Carro`, `Moto` e `Caminhao` são **subclasses**.

A relação pode ser representada da seguinte forma:

```text
              Veiculo
             /   |   \
            /    |    \
        Carro   Moto   Caminhao

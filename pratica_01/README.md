# Atividade Prática 01

# Entidades

- aluno
- endereco
- escola
- professor
- sala_aula

## Relacionamentos

### Composição

A sala não existe sem a escola

escola --> sala_aula


### Associação

professor e escola existem independentemente

escola --> professor


### Agregação

O endereço pode continuar existindo mesmo sem o aluno

aluno --> endereco
"""
8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
"""

# Resposta 1:
# CÁLCULO DE SALÁRIO

# Solicita ao usuário quanto ele ganha por hora e armazena como string
valor_hora = input('Quanto você ganha R$ por hora: ')

# Solicita ao usuário quantas horas ele trabalha no mês e armazena como string
total_hora = input('Quantas horas você trabalha no mês: ')

# Converte o valor ganho por hora para tipo float
valor_hora_convertido = float(valor_hora)

# Converte o número total de horas trabalhadas no mês para tipo float
total_hora_convertido = float(total_hora)

# Calcula o salário multiplicando o valor por hora pelo número total de horas trabalhadas
salario = valor_hora_convertido * total_hora_convertido

# Exibe o salário formatado com duas casas decimais
print(f'Recebendo R$ {valor_hora} por hora e trabalhando {total_hora} horas no mês, '
      f'o seu salário no mês é igual a: R$ {salario:.2f}')

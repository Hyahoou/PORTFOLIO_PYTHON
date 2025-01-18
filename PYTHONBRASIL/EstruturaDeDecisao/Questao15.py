"""
15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados:
- 11% para o Imposto de Renda (IR),
- 8% para o INSS,
- 5% para o sindicato.
"""

# Solicita o valor que o usuário ganha por hora e o número de horas trabalhadas no mês
valor_hora = input('Quanto você ganha R$ por hora: ')
total_hora = input('Quantas horas você trabalha no mês: ')

# Converte os valores de entrada para float
valor_hora_convertido = float(valor_hora)
total_hora_convertido = float(total_hora)

# Calcula o salário bruto multiplicando o valor da hora pelo total de horas trabalhadas
salario = valor_hora_convertido * total_hora_convertido

# Calcula os descontos
inss = salario * 0.08  # Desconto do INSS (8%)
sindicato = salario * 0.05  # Desconto do Sindicato (5%)
ir = salario * 0.11  # Desconto do Imposto de Renda (11%)

# Calcula o salário líquido subtraindo os descontos do salário bruto
salario_liquido = salario - inss - sindicato - ir

# Exibe os resultados
print(f'O seu salário bruto é igual a: R$ {salario:.2f}.')
print(f'Você paga R${inss:.2f} de INSS.')
print(f'Você paga R${sindicato:.2f} de Sindicato.')
print(f'O seu salário líquido é de R$ {salario_liquido:.2f}.')

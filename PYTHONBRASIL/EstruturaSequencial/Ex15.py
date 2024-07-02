# 15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

# A. salário bruto.

# B. quanto pagou ao INSS.

# C. quanto pagou ao sindicato.

# D. o salário líquido.

# E. calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

valor_hora = input('Quanto você ganha R$ por hora: ')
total_hora = input('Quantas horas você trabalha no mês: ')
valor_hora_convertido = float(valor_hora)
total_hora_convertido = float(total_hora)
salario = valor_hora_convertido * total_hora_convertido
inss = salario*0.08
sindicato = salario*0.05
ir=salario*0.11
salario_liquido = salario-inss-sindicato-ir
print(f'O seu salário bruto é igual a: R$ {salario:.2f}.')
print(f'Você paga R${inss:.2f} INSS.')
print(f'Você paga R${sindicato:.2f} Sindicato.')
print(f'O seu salário liquido é de R${salario_liquido:.2f}.')
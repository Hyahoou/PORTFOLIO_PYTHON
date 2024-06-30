"""
8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

"""
# Resposta 1:
# Calculo de salário
valor_hora = input('Quanto você ganha R$ por hora: ')
total_hora = input('Quantas horas você trabalha no mês: ')
valor_hora_convertido = float(valor_hora)
total_hora_convertido = float(total_hora)
salario = valor_hora_convertido * total_hora_convertido
print(f'Recebendo R$ {valor_hora} e trabalhando {total_hora}, o seu salário no mês é igual a: R$ {salario:.2f}')
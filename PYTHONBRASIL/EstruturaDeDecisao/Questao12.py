"""
12. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
"""

# Solicita ao usuário o valor da hora e a quantidade de horas trabalhadas
valor_hora = float(input("Digite o valor da sua hora de trabalho: "))
horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas no mês: "))

# Calcula o salário bruto
salario_bruto = valor_hora * horas_trabalhadas

# Determina o desconto do Imposto de Renda
if salario_bruto <= 900:
    desconto_ir = 0
    percentual_ir = 0
elif salario_bruto <= 1500:
    desconto_ir = salario_bruto * 0.05
    percentual_ir = 5
elif salario_bruto <= 2500:
    desconto_ir = salario_bruto * 0.10
    percentual_ir = 10
else:
    desconto_ir = salario_bruto * 0.20
    percentual_ir = 20

# Calcula outros descontos e benefícios
desconto_sindicato = salario_bruto * 0.03
fgts = salario_bruto * 0.11

total_descontos = desconto_ir + desconto_sindicato
salario_liquido = salario_bruto - total_descontos

# Exibe o resultado na tela
print("+ Salário Bruto: ({:.2f} * {})      : R$ {:.2f}".format(valor_hora, horas_trabalhadas, salario_bruto))
print("- IR ({}%)                     : R$ {:.2f}".format(percentual_ir, desconto_ir))
print("- Sindicato (3%)               : R$ {:.2f}".format(desconto_sindicato))
print("= Salário Líquido              : R$ {:.2f}".format(salario_liquido))
print("+ FGTS (11%)                   : R$ {:.2f}".format(fgts))
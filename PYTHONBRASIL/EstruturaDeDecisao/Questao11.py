"""As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento."""

# Inicializa a variável salario como uma string vazia
salario = ""

# Definindo limites de salários para aplicar diferentes ajustes
salario1 = 280
salario2 = 700
salario3 = 1500

# Definindo as taxas de aumento para cada faixa salarial
ajuste1 = 0.20  # Aumento de 20% para salários abaixo de 280
ajuste2 = 0.15  # Aumento de 15% para salários entre 280 e 700
ajuste3 = 0.10  # Aumento de 10% para salários entre 700 e 1500
ajuste4 = 0.05  # Aumento de 5% para salários acima de 1500

# Solicita ao usuário que digite o seu salário atual
salario = float(input('Digite o seu salário para saber quanto irá receber de aumento R$: '))

# Calcula o novo salário para cada tipo de aumento
novosalario1 = salario + (salario * ajuste1)  # Novo salário com ajuste de 20%
novosalario2 = salario + (salario * ajuste2)  # Novo salário com ajuste de 15%
novosalario3 = salario + (salario * ajuste3)  # Novo salário com ajuste de 10%
novosalario4 = salario + (salario * ajuste4)  # Novo salário com ajuste de 5%

# Verifica em qual faixa de salário o valor informado se encaixa e aplica o aumento correspondente
if salario < salario1:
    # Se o salário for abaixo de 280, aplica aumento de 20%
    print(f'O seu aumento foi de {ajuste1 * 100:.2f}%, o seu novo salário é R${novosalario1:.2f}')
elif salario >= salario1 and salario <= salario2:
    # Se o salário estiver entre 280 e 700, aplica aumento de 15%
    print(f'O seu aumento foi de {ajuste2 * 100:.2f}%, o seu novo salário é R${novosalario2:.2f}')
elif salario >= salario2 and salario <= salario3:
    # Se o salário estiver entre 700 e 1500, aplica aumento de 10%
    print(f'O seu aumento foi de {ajuste3 * 100:.2f}%, o seu novo salário é R${novosalario3:.2f}')
else:
    # Se o salário for acima de 1500, aplica aumento de 5%
    print(f'O seu aumento foi de {ajuste4 * 100:.2f}%, o seu novo salário é R${novosalario4:.2f}')

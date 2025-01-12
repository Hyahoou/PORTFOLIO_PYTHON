"""
12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7 * altura) - 58
"""

# Exibe uma mensagem inicial informando o propósito do programa
print('Vamos calcular seu peso ideal')

# Solicita ao usuário a altura e converte para tipo float
altura = float(input('Digite a sua altura: '))

# Calcula o peso ideal usando a fórmula fornecida: (72.7 * altura) - 58
peso_ideal = (72.7 * altura) - 58

# Exibe o peso ideal formatado com duas casas decimais
print(f'O seu peso ideal é: {peso_ideal:.2f}')

"""
13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
A. Para homens: (72.7 * altura) - 58
B. Para mulheres: (62.1 * altura) - 44.7
"""

# Exibe uma mensagem inicial informando o propósito do programa
print('Vamos calcular seu peso ideal')

# Solicita ao usuário a altura e converte para tipo float
altura = float(input('Digite a sua altura: '))

# Calcula o peso ideal para homens utilizando a fórmula fornecida
peso_ideal_h = (72.7 * altura) - 58

# Calcula o peso ideal para mulheres utilizando a fórmula fornecida
peso_ideal_m = (62.1 * altura) - 44.7

# Exibe o peso ideal para homens
print(f'Se você for um homem, o seu peso ideal é: {peso_ideal_h:.2f}')

# Exibe o peso ideal para mulheres
print(f'Se você for uma mulher, o seu peso ideal é: {peso_ideal_m:.2f}')

# 13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# A. Para homens: (72.7*h) - 58
# B. Para mulheres: (62.1*h) - 44.7

print('vamos calcular seu peso ideal')
altura = float(input('Digite a sua altura: '))
peso_ideal_h = (72.7 * altura) - 58
peso_ideal_m = (62.1 * altura) - 44.7
print(f'Se você for um homem o seu peso ideal é: {peso_ideal_h:.2f}')
print(f'Se você for um mulher o seu peso ideal é: {peso_ideal_m:.2f}')

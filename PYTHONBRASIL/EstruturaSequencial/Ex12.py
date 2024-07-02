# 12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

print('vamos calcular seu peso ideal')
altura = float(input('Digite a sua altura: '))
peso_ideal = (72.7*altura)-58
print(f'O seu peso ideal é: {peso_ideal:.2f}')
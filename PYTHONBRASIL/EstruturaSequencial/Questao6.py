"""
6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""

# Importa o módulo math para usar constantes e funções matemáticas
import math

# Define a constante pi a partir do módulo math
pi = math.pi

# Resposta 1:
# CÁLCULO DA ÁREA DO CÍRCULO

# Solicita ao usuário o valor do raio do círculo e converte para float
raio = float(input('Digite o valor do raio: '))

# Calcula a área do círculo usando a fórmula: área = π * raio²
area = pi * raio**2

# Exibe o resultado da área com duas casas decimais
print(f'O valor da área do círculo é {area:.2f}')

"""
10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
Fórmula de conversão: F = (C * 1.8) + 32
"""

# Resposta 1:
# Conversão de temperatura de Celsius para Fahrenheit

# Solicita ao usuário a temperatura em graus Celsius e converte para float
temperatura_celsius = float(input('Digite a temperatura em Celsius: '))

# Aplica a fórmula de conversão para Fahrenheit: F = (C * 1.8) + 32
temperatura_fahrenheit = (temperatura_celsius * 1.8 + 32)

# Exibe o resultado da conversão
print(f'{temperatura_celsius} graus Celsius em graus Fahrenheit é {temperatura_fahrenheit:.2f}')

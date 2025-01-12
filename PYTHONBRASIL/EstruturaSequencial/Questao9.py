"""
9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
Fórmula de conversão: C = 5 * ((F - 32) / 9)
"""

# Resposta 1:
# Conversão de temperatura de Fahrenheit para Celsius

# Solicita ao usuário a temperatura em graus Fahrenheit e converte para float
temperatura_fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))

# Aplica a fórmula de conversão para Celsius: C = 5 * ((F - 32) / 9)
temperatura_celsius = 5 * ((temperatura_fahrenheit - 32) / 9)

# Exibe o resultado da conversão
print(f'{temperatura_fahrenheit} graus Fahrenheit em graus Celsius é {temperatura_celsius:.2f}')

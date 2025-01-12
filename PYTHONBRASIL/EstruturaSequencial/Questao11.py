"""
11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
A. O produto do dobro do primeiro com metade do segundo.
B. A soma do triplo do primeiro com o terceiro.
C. O terceiro elevado ao cubo.
"""

# Entradas:
# Solicita ao usuário o primeiro número inteiro e converte para inteiro
numero_1 = int(input('Digite o primeiro número inteiro: '))

# Solicita ao usuário o segundo número inteiro e converte para inteiro
numero_2 = int(input('Digite o segundo número inteiro: '))

# Solicita ao usuário o primeiro número real e converte para float
numero_3 = float(input('Digite o primeiro número real: '))

# A. Calcula o produto do dobro do primeiro com metade do segundo
numero_a = (numero_1 * 2) + (numero_2 / 2)

# B. Calcula a soma do triplo do primeiro com o terceiro número
numero_b = (numero_1 * 3) + numero_3

# C. Calcula o terceiro número elevado ao cubo
numero_c = numero_3 ** 3

# Exibe os resultados:
print('O produto do dobro do primeiro com metade do segundo: ', numero_a)
print('A soma do triplo do primeiro com o terceiro: ', numero_b)
print('O terceiro elevado ao cubo: ', numero_c)

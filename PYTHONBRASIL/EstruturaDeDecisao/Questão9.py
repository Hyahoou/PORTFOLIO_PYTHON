"""
9. Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""

# Solicita os três números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Adiciona os números em uma lista
numeros = [num1, num2, num3]

# Ordena a lista em ordem decrescente
numeros.sort(reverse=True)

# Exibe os números em ordem decrescente
print("Os números em ordem decrescente são:", numeros)

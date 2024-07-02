# 11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# A. o produto do dobro do primeiro com metade do segundo .
# B. a soma do triplo do primeiro com o terceiro.
# C. o terceiro elevado ao cubo.

# Entradas
numero_1 = int(input('Digite o primeiro número Inteiro: '))
numero_2 = int(input('Digite o segundo número Inteiro: '))
numero_3 = float(input('Digite o primeiro número Real: '))
# A
numero_a = (numero_1*2) + (numero_2/2)
# B
numero_b = (numero_1*3) + numero_3
# C
numero_c = numero_3**3

print('O produto do dobro do primeiro com metade do segundo: ', numero_a)
print('A soma do triplo do primeiro com o terceiro: ', numero_b)
print('O terceiro elevado ao cubo: ', numero_c)
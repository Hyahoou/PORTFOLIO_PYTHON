"""
16. Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidade de latas de tinta a serem compradas e o preço total.
"""

# Exibe uma mensagem inicial informando sobre o orçamento para pintura
print('Vamos fazer o seu orçamento para pintura')

# Solicita ao usuário o tamanho da área a ser pintada em metros quadrados
metro_quadrados = float(input('Quantos metros quadrados você quer pintar: '))

# Calcula a quantidade de litros necessários para pintar a área (1 litro para cada 3 metros quadrados)
litros = metro_quadrados / 3

# Calcula a quantidade de latas necessárias, considerando que cada lata tem 18 litros
latas = int(litros / 18)

# Se a quantidade de litros não for exatamente múltipla de 18, compra-se uma lata extra
if litros % 18 != 0:
    latas += 1

# Calcula o valor total a ser pago pelas latas de tinta
valor_total = latas * 80

# Exibe a quantidade de latas e o valor total
print('Você deverá comprar', latas, 'latas.')
print(f'O valor total é: R$ {valor_total:.2f}')

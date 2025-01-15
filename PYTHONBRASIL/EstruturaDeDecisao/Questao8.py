"""
8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""

# Solicita os preços dos três produtos
# Converte as entradas do usuário em valores de ponto flutuante para realizar comparações numéricas
preco1 = float(input("Digite o preço do primeiro produto: "))
preco2 = float(input("Digite o preço do segundo produto: "))
preco3 = float(input("Digite o preço do terceiro produto: "))

# Determina o menor preço e o produto correspondente
# Verifica se o primeiro produto tem o menor preço
if preco1 < preco2 and preco1 < preco3:
    print("Você deve comprar o primeiro produto.")
# Verifica se o segundo produto tem o menor preço
elif preco2 < preco1 and preco2 < preco3:
    print("Você deve comprar o segundo produto.")
# Se nenhuma das condições acima for verdadeira, o terceiro produto tem o menor preço
else:
    print("Você deve comprar o terceiro produto.")


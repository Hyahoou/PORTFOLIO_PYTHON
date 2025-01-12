"""
2.Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""

# Solicita um valor
valor = input("Digite um valor: ")

# Converte o valor para float
valor1 = float(valor)

# Verifica se o valor é positivo, negativo ou zero
if valor1 > 0:
    print(f'O {valor1} é Positivo')
elif valor1 < 0:
    print(f'O {valor1} é Negativo')
else:
    print(f'O {valor1} é Zero')

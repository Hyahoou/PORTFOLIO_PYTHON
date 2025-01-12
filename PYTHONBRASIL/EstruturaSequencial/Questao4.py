"""
4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""

# Exibe uma mensagem inicial para informar ao usuário o propósito do programa
print('Cálculo de média das notas\n')

# Solicita ao usuário a primeira nota como string e armazena na variável `numero1`
numero1 = input('Digite a 1ª nota: ')

# Solicita ao usuário a segunda nota como string e armazena na variável `numero2`
numero2 = input('Digite a 2ª nota: ')

# Solicita ao usuário a terceira nota como string e armazena na variável `numero3`
numero3 = input('Digite a 3ª nota: ')

# Solicita ao usuário a quarta nota como string e armazena na variável `numero4`
numero4 = input('Digite a 4ª nota: ')

# Converte as notas de string para float para permitir cálculos matemáticos
valor1 = float(numero1)
valor2 = float(numero2)
valor3 = float(numero3)
valor4 = float(numero4)

# Calcula a média das quatro notas
media = (valor1 + valor2 + valor3 + valor4) / 4

# Exibe o resultado com as notas fornecidas e a média calculada
print(f'A média das notas {valor1}, {valor2}, {valor3}, {valor4} é: {media}')

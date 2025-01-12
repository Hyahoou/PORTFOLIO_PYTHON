"""
5. Faça um Programa que converta metros para centímetros.
"""

# Resposta 1:
# Exibe uma mensagem inicial informando o propósito do programa
print('Converter de metros para centímetros\n')

# Solicita ao usuário o valor em metros como string e armazena na variável `valor1`
valor1 = input('Digite o valor que deseja converter (em metros): ')

# Converte o valor de string para float para permitir cálculos
valor1_convertido = float(valor1)

# Calcula o valor em centímetros multiplicando por 100
valor1_centimetros = int(valor1_convertido * 100)

# Exibe o resultado da conversão, mostrando o valor original e o convertido
print(f'{valor1} metros é igual a {valor1_centimetros} centímetros.')

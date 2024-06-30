"""
4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.

"""
print('Calculo de média das notas\n')
numero1 = input('Digite a 1º nota: ')
numero2 = input('Digite a 2º nota: ')
numero3 = input('Digite a 3º nota: ')
numero4 = input('Digite a 4º nota: ')

valor1 = float(numero1)
valor2 = float(numero2)
valor3 = float(numero3)
valor4 = float(numero4)
media = (valor1 + valor2 + valor3 + valor4)/4
print(f'A média das notas {valor1} + {valor2} + {valor3} + {valor4} é: {media}')
"""

"""
# BIBLIOTECAS
import math

# Variaveis
area = ''
base = ''
base_maior = ''
base_menor = ''
altura = ''
lado = ''
diagonal_maior = ''
diagonal_menor = ''
raio = ''
pi = math.pi

# MENU
print('CALCULO DE ÁREA \n')
print('--- MENU ---\n')
print('1. TRIÂNGULO')
print('2. QUADRADO')
print('3. LOSANGO')
print('4. RETÂNGULO')
print('5. TRAPÉZIO')
print('6. CÍRCULO \n')
print('7. SAIR')
print('-------------')

figura_geometrica = input('Qual Área deseja calcular? \n')

# CÁLCULO DA ÁREA DO TRIANGULO
if figura_geometrica == '1': 
    base = float(input('Digite o valor da Base: \n'))
    altura = float(input('Digite o valor da Altura: \n'))
    area = ((base*altura)/2)
    print('\n' f'Valor da Área do TRIANGULO é {area:.2f}')

# CÁLCULO DA ÁREA DO QUADRADO
if figura_geometrica == '2': 
    lado = float(input('Digite o valor do Lado: \n'))
    area = lado**2
    print('\n' f'Valor da Área do QUADRADO é {area:.2f}')

# CÁLCULO DA ÁREA DO LOSANGO
if figura_geometrica == '3': 
    diagonal_maior = float(input('Digite o valor da Diagonal Maior: \n'))
    diagonal_menor = float(input('Digite o valor da Diagonal Menor: \n'))
    area = ((diagonal_maior * diagonal_menor)/2)
    print('\n' f'Valor da Área do LOSANGO é {area:.2f}')

# CÁLCULO DA ÁREA DO RETÂNGULO
if figura_geometrica == '4': 
    base = float(input('Digite o valor da Base: \n'))
    altura = float(input('Digite o valor da Altura: \n'))
    area = (base*altura)
    print('\n' f'Valor da Área do RETÂNGULO é {area:.2f}')

# CÁLCULO DA ÁREA DO TRAPÉZIO
if figura_geometrica == '5': 
    base_maior = float(input('Digite o valor da Base Maior: \n'))
    base_menor = float(input('Digite o valor da Base Menor: \n'))
    altura = float(input('Digite o valor da Altura: \n'))
    area = ((base_maior + base_menor)*altura)/2
    print('\n' f'Valor da Área do TRAPÉZIO é {area:.2f}')

# CÁLCULO DA ÁREA DO CÍRCULO
if figura_geometrica == '6': 
    raio = float(input('Digite o valor do Raio: \n'))
    area = pi*raio**2
    print('\n' f'Valor da Área do CÍRCULO é {area:.2f}')

# SAIR
if figura_geometrica == '7':
    print('Você saiu do sistema')
    exit()

print('Desculpa essa opção não temos no menu')
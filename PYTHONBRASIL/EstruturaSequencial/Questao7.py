"""
7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
"""

# Resposta 1:
# CÁLCULO DA ÁREA DO QUADRADO

# Solicita ao usuário o valor do lado do quadrado e converte para float
lado = float(input('Digite o valor do lado do quadrado: '))

# Calcula a área do quadrado usando a fórmula: área = lado²
area = lado**2

# Calcula o dobro da área do quadrado
dobroarea = area * 2

# Exibe o valor da área e o dobro da área, ambos formatados com duas casas decimais
print(f'O valor da área do quadrado é {area:.2f} e o dobro da área do quadrado é {dobroarea:.2f}.')

"""
18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps).
Calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""

# Solicita o tamanho do arquivo em MB
tamanho = float(input('Tamanho do arquivo (MB): '))

# Solicita a velocidade da Internet em MBps (Megabytes por segundo)
velocidade = float(input('Velocidade de Internet (MBps): '))

# Calcula o tempo de download em minutos
# O tempo é dado pela fórmula: tempo = tamanho / velocidade
# Como a velocidade é dada em MBps e o tempo é em minutos, dividimos o resultado por 60.
tempo_download = (tamanho / velocidade) / 60

# Exibe o tempo aproximado de download arredondado para o número inteiro mais próximo
print(f'Tempo aproximado de download: {tempo_download:.0f} Minutos')

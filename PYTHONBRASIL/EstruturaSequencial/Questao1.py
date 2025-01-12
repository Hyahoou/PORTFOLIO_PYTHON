"""
1. Faça um Programa que mostre a mensagem "Alo mundo" na tela.
"""

# Resposta 1:
# Imprime diretamente a mensagem "Alo mundo" na tela
print('Alo mundo')

# Resposta 2:
# Solicita ao usuário que digite "Alo mundo"
Imprimir = input('Digite Alo mundo: ')

# Exibe na tela o que foi digitado pelo usuário
print(Imprimir)

# Resposta 3:
# Solicita ao usuário que digite "Alo mundo"
Imprimir = input('Digite Alo mundo: ')

# Verifica se a entrada do usuário é exatamente "Alo mundo"
if Imprimir == 'Alo mundo':
    # Se for igual, imprime a mensagem digitada
    print(Imprimir)
else:
    # Caso contrário, exibe uma mensagem informando o erro
    print(f'A sua digitação não está correta')

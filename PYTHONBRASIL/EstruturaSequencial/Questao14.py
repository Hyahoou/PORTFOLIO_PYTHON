"""
14. João Papo-de-Pescador comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos),
ele deve pagar uma multa de R$ 4,00 por quilo excedente.
O programa deve ler o peso do peixe, calcular o excesso e mostrar a multa correspondente.
"""

# Exibe uma mensagem inicial informando sobre a pesagem do peixe
print('Pesagem de peixe')

# Solicita ao usuário o peso do peixe em quilos e converte para float
peso_peixe = float(input('Digite o peso do peixe em kg: '))

# Inicializa a variável que armazenará o excesso de peso
excesso_peso = 0

# Verifica se o peso do peixe excede o limite de 50 quilos
if peso_peixe > 50:
    # Calcula o excesso de peso
    excesso_peso = peso_peixe - 50
    # Calcula o valor da multa, considerando R$ 4,00 por quilo excedente
    multa_excesso = excesso_peso * 4
    # Exibe o excesso de peso e o valor da multa
    print(f'O peixe está com excesso de {excesso_peso:.2f} quilos.')
    print(f'A multa a ser paga pelo excesso de peso é de R${multa_excesso:.2f}.')
else:
    # Caso o peso do peixe esteja dentro do limite, exibe uma mensagem informando
    print('O peso do peixe está dentro do limite de 50 quilos.')

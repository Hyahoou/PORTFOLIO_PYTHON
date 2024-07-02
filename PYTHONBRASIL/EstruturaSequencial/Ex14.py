# 14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
# Imprima os dados do programa com as mensagens adequadas.

print('Pesagem de peixe')
peso_peixe = float(input('Digite o peso do peixe em kg: '))
excesso_peso = 0

if peso_peixe > 50:
    excesso_peso = peso_peixe-50
    multa_excesso = excesso_peso*4
    print(f'O peixe esta com excesso de {excesso_peso:.2f} quilos.')
    print(f'A multa a ser paga pelo excesso de peso é de R${multa_excesso:.2f}.')
else:
    print('O peso do peixe esta dentro do limite de 50 quilos.')
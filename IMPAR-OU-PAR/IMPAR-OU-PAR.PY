
print('Vamos brincar de ímpar ou par?\n')

numero = input('Digite um número inteiro: ')

if numero.isdigit():
    entrada_int = int(numero)
    numero_par = entrada_int % 2 == 0
    resultado_impar_par = 'ímpar'

    if numero_par:
        resultado_impar_par = 'par'

    print(f'\nO número {entrada_int} é {resultado_impar_par}')

else :
    print('Você não digitou um numero inteiro')
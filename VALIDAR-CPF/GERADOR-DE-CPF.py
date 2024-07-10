
import random
import os
os.system('cls')#Limpar o terminal

while True: #loop para consulta
    item_1 = input('Gerar um novo CPF: [S]im ou [N]ão ').lower()
    if item_1 == "s":
        nove_digitos = ''
        for i in range(9):
            nove_digitos += str(random.randint(0,9))

        contador_1 = 10 #Primeiro contador para realizar a multiplicação
        
        # Primeiro dígito
        primeiro_digito = 0 #Inicialmente o primeiro digito recebe o valor de zero.
        for digito in nove_digitos: #For para realizar a multiplicação e a soma dos nove primeiros digitos
            primeiro_digito += int(digito) * contador_1
            contador_1 -= 1
        digito_1 = (primeiro_digito * 10) % 11 #Realiza a multiplicação da soma dos digitos e obtem o resultando do resto da divisão
        digito_1 = digito_1 if digito_1 <= 9 else 0 #Resultado da conta
        dez_digitos = nove_digitos + str(digito_1)
        contador_2 = 11
        # Segundo dígito
        segundo_digito = 0 #Inicialmente o segundo digito recebe o valor de zero.
        for digito in dez_digitos: #For para realizar a multiplicação e a soma dos nove primeiros digitos
            segundo_digito += int(digito)*contador_2
            contador_2 -= 1
        digito_2 = (segundo_digito * 10) % 11 #Realiza a multiplicação da soma dos digitos e obtem o resultando do resto da divisão
        digito_2 = digito_2 if digito_2 <= 9 else 0 #Resultado da conta
            

        cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}' # Gerar o novo CPF
        print(cpf_gerado)


    if item_1 == "n": #Sair do Loop da validação do CPF
        print('Você escolheu sair da verificação.')
        break


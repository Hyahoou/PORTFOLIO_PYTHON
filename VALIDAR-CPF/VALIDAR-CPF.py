"""
Site de apoio para gerar CPF https://www.4devs.com.br/gerador_de_cpf

Digito 1
    (123456789)
    ((1*10 + 2*9;...) * 10) % 11=?

    1. Coleta os 9 primeiro digitos do CPF Multiplica cada um dos valores por uma contagem regressiva começando de 10.
    2. Soma todos os valores.
    3. Multiplica o resultado da soma por 10.
    4. Obtem o resto da divisão por 11
    5. Resultado do resto da divisão por maior que 9 o digito recebe 0 se for menor que 9 ele continuar com o seu valor.

    Digito 2
    (123456789)+digito 1
    ((1*11 + 2*10;...) * 10) % 11=?

    1. Coleta os 9 primeiro digitos do CPF Multiplica cada um dos valores por uma contagem regressiva começando de 10.
    2. Soma todos os valores.
    3. Multiplica o resultado da soma por 10.
    4. Obtem o resto da divisão por 11
    5. Resultado do resto da divisão por maior que 9 o digito recebe 0 se for menor que 9 ele continuar com o seu valor.
"""
import re #Usando para mantar apenas numeros no envio do CPF
import os
os.system('cls')#Limpar o terminal

while True: #loop para consulta
    item_1 = input('Deseja verificar se o CPF é valido: [S]im ou [N]ão ').lower()
    if item_1 == "s":
        # cpf_enviado = input('Digite o seu CPF: ')\
        #     .replace('.','')\
        #     .replace(' ','')\
        #     .replace('-','')#Campo para inserir CPF
        cpf_enviado = re.sub(r'[^0-9]','',input('Digite o seu CPF: '))#Campo para inserir CPF
        nove_digitos = cpf_enviado[:9] #Coleta os 9 primeiros dígitos
        contador_1 = 10 #Primeiro contador para realizar a multiplicação
        if len(cpf_enviado) > 11: #verifica se o CPF tem mais de 11 dígitos
            print('CPF é inválido, O CPF contém:',len(cpf_enviado),'dígitos.')
        elif len(cpf_enviado) < 11:#verifica se o CPF tem menos de 11 dígitos
            print('CPF é inválido, O CPF contém:',len(cpf_enviado),'dígitos.')
        else:
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

        if cpf_enviado == cpf_gerado: #Validação se o novo CPF é igual ao CPF fornecido.
           print('CPF digitado é Valido.')
        else:
            print('CPF digitado é Inválido.')

    if item_1 == "n": #Sair do Loop da validação do CPF
        print('Você escolheu sair da verificação.')
        break



while True:

    # Menu
    print('\n--------Calculadora-----------')
    print('|       [+] Somar            |')
    print('|       [-] Subtrair         |')
    print('|       [*] Multiplicação    |')
    print('|       [/] Divisão          |')
    print('|       [**] Potenciação     |')
    print('------------------------------')

    # Entradas da calculadora
    numero_1 = input('\n*Digite o primeiro número: ')
    operacao = input('*Qual conta deseja realizar: ')
    numero_2 = input('*Digite o segundo número: ')

    # Convertendo de int para float as entradas
    numeros_validos = None
    numero_1_float = 0
    numero_2_float = 0
    
    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True
        resultado = 0
    except:
        numeros_validos = None

    # Valida os numeros
    if numeros_validos is None:
        print('\nUm ou ambos os números digitados são invalidos.')
        continue

    # Valida os operadores
    operadores_permitidos = '**+-/*'
    if operacao not in operadores_permitidos:
        print('\nOperador não reconhecido')
        continue

    # Verificar se tem apenas 1 operador
    if len(operacao) > 4:
        continue

    # Operações Matemáticas
    if operacao == '+':
        resultado = numero_1_float + numero_2_float
        print(f'O resultado de {numero_1} + {numero_2} =',resultado)
    elif operacao =='-':
        resultado = numero_1_float - numero_2_float
        print(f'O resultado de {numero_1} - {numero_2} =',resultado)
    elif operacao =='*':
        resultado = numero_1_float * numero_2_float
        print(f'O resultado de {numero_1} * {numero_2} =',resultado)
    elif operacao =='/':
        resultado = numero_1_float / numero_2_float
        print(f'O resultado de {numero_1} / {numero_2} =',resultado)
    elif operacao =='**':
        resultado = numero_1_float ** numero_2_float
        print(f'O resultado de {numero_1} ** {numero_2} =',resultado)
    else:
        print('Erro O.o') #Erro não esperado


     # Saída do Loop
    sair = input('Quer sair? [s]im ').lower().startswith('s')
    if sair is True:
        print('Você escolheu sair!!!')
        break
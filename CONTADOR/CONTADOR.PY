CONTADOR = 0

Sim_Nao = input('Vamos contar? S/N ')

if Sim_Nao == "s" or Sim_Nao == "S":
    
    TOTAL = int(input('Até quanto você quer contar? '))
    PULAR = int(input('\nContar de quanto em quanto?'))

    print('Vamos começar a contar\n')
    while CONTADOR <= TOTAL:
        print('Número: ', CONTADOR)
        CONTADOR += PULAR

if Sim_Nao =="n" or Sim_Nao =="N":
    print('\nVocê não quiz contar.')
    pass
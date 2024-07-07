"""


"""
import os
lista = []

while True:
    print('Selecione uma opção')
    print('[i]nserir')
    print('[a]pagar')
    print('[l]istar')
    print('[s]air')
    opcao = input('O que deseja execultar: ').lower()

    if opcao == 'i':
        os.system('cls')
        valor = input('Inserir novo item: ').lower()
        lista.append(valor)
    elif opcao == 'a':
        indece_str = input('Qual item deseja apagar: ').lower()

        try:
            indice = int(indece_str)
            del lista[indice]
        except ValueError:
            print( 'Não foi possivel apagar esse item!')
        except IndexError:
            print('Esse item não existe na lista!')
        except Exception:
            print('Erro desconhecido!')

    elif opcao == 'l':
        os.system( 'cls')

        if len(lista) == 0:
            print('Nenhum item encontrado na lista.')

        for i, valor in enumerate(lista, start=1):
            print(i,'-'*3, valor)
    elif opcao == 's':
        print('Você saiu da lista!')
        break
"""
10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""

# Exibe a pergunta para o usuário
print('Em que turno você estuda?')

# Solicita ao usuário que insira o turno desejado (M, V ou N) e converte a entrada para minúsculas
turno = input('Digitar [M]-matutino ou [V]-Vespertino ou [N]- Noturno: ').lower()

# Verifica se a entrada é uma única letra e se é alfabética
if turno.isalpha() and len(turno) == 1:  
    # Caso o usuário digite 'm', imprime "Bom dia!"
    if turno == 'm':
        print('Bom dia!')
    # Caso o usuário digite 'v', imprime "Boa tarde!"
    elif turno == 'v':
        print('Boa tarde!')
    # Caso o usuário digite 'n', imprime "Boa noite!"
    elif turno == 'n':
        print('Boa noite!')
    # Caso a entrada não seja 'm', 'v' ou 'n', é tratado como inválido
    else:
        print('Valor Inválido!')
# Caso a entrada não seja alfabética ou tenha mais de um caractere, imprime "Valor Inválido!"
else:
    print('Valor Inválido!')



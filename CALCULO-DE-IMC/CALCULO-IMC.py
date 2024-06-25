"""
https://vidasaudavel.einstein.br/calcular-o-seu-imc/

A tabela do IMC é a seguinte:

resultados menores que 16 — magreza grave;
resultados entre 16 e 16,9 — magreza moderada;
resultados entre 17 e 18,5 — magreza leve;
resultados entre 18,6 e 24,9 — peso ideal;
resultados entre 25 e 29,9 — sobrepeso;
resultados entre 30 e 34,9 — obesidade grau I;
resultados entre 35 e 39,9 — obesidade grau II ou severa;
resultados maiores do que 40 — obesidade grau III ou mórbida.

"""
# ÁREA DO CALCULO DO IMC

altura = input('Qual a sua altura? \n')

peso = input('Qual é o seu peso? \n')

imc = float(peso) / float(altura)**2

#---------------------------------------

# MAGREZA GRAVE
if imc < 16 :
    print('\n'f'O resultado do seu IMC é {imc:.2f} você está com MAGREZA GRAVE')

# MAGREZA MODERADA
if imc >= 16 and imc <= 16.9 :
    print('\n'f'O resultado do seu IMC é {imc:.2f} você está com MAGREZA MODERADA')

# MAGREZA LEVE
if imc >= 17 and imc <= 18.5 :
    print('\n'f'O resultado do seu IMC é {imc:.2f} você está com MAGREZA LEVE')

# PESO IDEAL
if imc >= 18.6 and imc <= 24.9 :
    print('\n'f'O resultado do seu IMC é {imc:.2f} você está com PESO IDEAL')

# SOBREPESO
if imc >= 25 and imc <= 29.9 :
    print('\n'f'O resultado do seu IMC é {imc:.2f} você está com SOBREPESO')

# OBESIDADE GRAU I
if imc >= 30 and imc <= 34.9 :
    print('\n'f'O resultado do seu IMC é {imc:.2f} você está com OBESIDADE GRAU I')

# OBESIDADE GRAU II
if imc >= 35 and imc <= 39.9 :
    print('\n'f'O resultado do seu IMC é {imc:.2f} você está com OBESIDADE GRAU II')

# OBESIDADE GRAU III
if imc >= 40 :
    print('\n'f'O resultado do seu IMC é {imc:.2f} você está com OBESIDADE GRAU III')
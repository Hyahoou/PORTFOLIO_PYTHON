"""
6. Faça um Programa que leia três números e mostre o maior deles.
"""

# Solicita os três números do usuário
numero1 = float(input("Digite o 1º número: "))
numero2 = float(input("Digite o 2º número: "))
numero3 = float(input("Digite o 3º número: "))

# Determina o maior número
if numero1 >= numero2 and numero1 >= numero3:
    maior = numero1
elif numero2 >= numero1 and numero2 >= numero3:
    maior = numero2
else:
    maior = numero3

# Exibe o maior número
print(f"O maior número é: {maior}")

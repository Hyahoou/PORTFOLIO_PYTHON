"""
3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""

# Solicita o sexo
sexo = input("Digite F ou M: ").lower()

# Verifica o sexo e exibe a mensagem correspondente
if sexo == 'f':
    print("F - Feminino")
elif sexo == 'm':
    print("M - Masculino")
else:
    print("Sexo Inválido")

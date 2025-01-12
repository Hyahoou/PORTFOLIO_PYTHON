"""
4.Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""
# Solicita uma letra do usuário
letra = input("Digite uma letra: ").lower()

# Verifica se a entrada é uma única letra
if len(letra) == 1 and letra.isalpha():
    # Verifica se é uma vogal ou consoante
    if letra in "aeiou":
        print("A letra digitada é uma vogal.")
    else:
        print("A letra digitada é uma consoante.")
else:
    print("Entrada inválida. Por favor, digite apenas uma letra.")

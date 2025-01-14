"""
5. Faça um programa para a leitura de duas notas parciais de um aluno. 
O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

# Solicita as notas do aluno
nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))

# Calcula a média
media = (nota1 + nota2) / 2

# Verifica as condições para determinar a situação do aluno
if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")

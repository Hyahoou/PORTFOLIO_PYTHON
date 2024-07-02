# 10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

# Resposta 1:
# Converter de Celsius para Fahrenheit 



temperatura_celcius = float(input('Digite a temperatura em Celcius: '))
# temperatura_fahrenheit = ((temperatura_celcius*(9 / 5))+32)
temperatura_fahrenheit = (temperatura_celcius*1.8+32)
print(f'{temperatura_celcius}graus Celsius em graus Fahrenheit é {temperatura_fahrenheit}')
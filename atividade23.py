# Crie um programa que receba um número do usuário e exiba a tabuada desse número de 1 a 10.

número = int(input('Digite um numero para ver a tabuada'))

print(f'tabuada do {número}:')
for Tabuada in range(1, 11):
    Resultado = número * Tabuada
    print (f"{número} x  {Tabuada} = {Resultado}")
    

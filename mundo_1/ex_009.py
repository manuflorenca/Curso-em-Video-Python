# faça um programa que leia um numero inteiro e faça a sua tabuada

i = int(input('Digite um número para ver a sua tabuada: '))

for multiplicador in range(1, 11):
    resultado = i * multiplicador
    print(f'{i} x {multiplicador} = {resultado}')


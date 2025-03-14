# faça um programa que leia um numero inteiro e faça a sua tabuada

i = int(input('Digite um número para ver a sua tabuada: '))

multiplicador = 1  # Começa multiplicando por 1

while multiplicador <= 10:
    resultado = i * multiplicador
    print(f'{i} x {multiplicador} = {resultado}')
    multiplicador += 1  # Incrementa o multiplicador para evitar loop infinito

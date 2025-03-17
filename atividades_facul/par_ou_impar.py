# Escreva um programa que peça ao usuário um número inteiro e determine se ele é PAR ou
# ÍMPAR.
# O programa deve exibir a mensagem correspondente:
# O número X é par.
# ou
# O número X é ímpar.

number = int(input('Escreva um número e veja se ele é par ou ímpar: '))

if number % 2 == 0:
    print('Ele é par')
else:
    print('Ele é impar')
#Crie um programa que solicite o nome e a idade do usuário e exiba a seguinte mensagem:
# Olá, [nome]! Você tem [idade] anos.

nome = str(input('Qual o seu nome? '))
idade = int(input('Qual a sua idade? '))

print(f'Olá, {nome}! Você tem {idade} anos.')
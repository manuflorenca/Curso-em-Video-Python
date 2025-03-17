# Crie um programa que peça ao usuário três números inteiros (a, b e c).
# O programa deve verificar se a é menor que b E b é maior que c, OU se a + b é igual a c.
# Exiba uma das seguintes mensagens conforme o resultado:
# A condição é verdadeira!
# ou
# A condição é falsa!

a = int(input('Escolha um número para ser o "a": '))
b = int(input('Escolha um número para ser o "b": '))
c = int(input('Escolha um número para ser o "c": '))

print('----------------------------------')
print('"a" é menor que "b"?')
if a < b:
    print('A condição é verdadeira!')
else:
    print('A condição é falsa!')
print('----------------------------------')

print('"b" é maior que "c"?')
if b > c:
    print('A condição é verdadeira!')
else:
    print('A condição é falsa!')
print('----------------------------------')

print('"a+b" é igual a "c"?')

if a+b == c:
    print('A condição é verdadeira!')
else:
    print('A condição é falsa!')
print('----------------------------------')
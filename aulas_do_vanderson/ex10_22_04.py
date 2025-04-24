# - 10 Validar idade - peça a idade do usúario até ele digitar um valor entre 0 e 120.

i = int(input('Digite a sua idade: '))

while i < 0 or i > 120:
    print('Essa idade não é válida. Digite um valor entre 0 e 120.')
    i = int(input('Digite a sua idade: '))

print(f'Sua idade {i} é válida.')

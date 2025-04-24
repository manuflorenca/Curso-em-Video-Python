# -7 tabuada com while  - peça um número ao usúario e mostre sua tabuada de 1 a 10 com while.

i = 1
n = int(input('Digite um número do qual você deseja ver a tabuada: '))

while i <= 10:
    m = n*i
    print(f'{n} x {i} = {m}')
    i +=1
print('------------------')
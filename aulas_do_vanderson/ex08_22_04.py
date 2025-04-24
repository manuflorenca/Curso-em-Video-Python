# - 8 Soma de números digtados - Peça números ao usúario até ele digitar 0. Mostre a soma total.

soma = 0
n = int(input('Digite números para serem somados (Para finalizar digite 0): '))

while n != 0:
    soma += n
    n = int(input('Digite números para serem somados (Para finalizar digite 0): '))

print('Soma total:', soma)
print('---------')

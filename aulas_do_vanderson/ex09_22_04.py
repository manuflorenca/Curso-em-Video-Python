# - 9. contar quantos números foram digitados - Conte quantos números diferentes de 0 o usúario digitou.

contador = 0
n = int(input('Digite números para o contador (Para finalizar digite 0): '))

while n != 0:
    contador += 1
    n = int(input('Digite números para o contador (Para finalizar digite 0): '))

print('Total de números digitados:', contador)
print('---------')

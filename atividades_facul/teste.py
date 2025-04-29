def soma_imp(n):
    soma = 0
    if n < 0:
        n = n * -1

    while n != 0:
        resto = n % 10
        if resto % 2 != 0:
            soma = soma + resto
        n = n // 10
    return soma

n = int(input('Digite um número inteiro: '))
res = soma_imp(n)
print('Números impares somados:', res)

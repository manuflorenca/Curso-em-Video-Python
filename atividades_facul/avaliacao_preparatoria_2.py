# def soma_digitos_impares(n):
#     soma = 0
#     for digito in str(n):
#         if int(digito) % 2 == 1:
#             soma += int(digito)
#     return soma

# n = int(input('Digite um número natural: '))
# resultado = soma_digitos_impares(n)
# print('Soma dos dígitos ímpares:', resultado)

# def soma_digitos_impares(n):
#     soma = 0
#     for digito in str(n):
#         digito_int = int(digito)
#         if digito_int % 2 == 1:
#             soma += digito_int
#     return soma

# n = int(input("Digite um número natural: "))
# resultado = soma_digitos_impares(n)
# print("Soma dos dígitos ímpares:", resultado)

# def soma_digitos_impares(n):
#     soma = 0
#     while n > 0:
#         digito = n % 10  # Pega o último dígito
#         if digito % 2 == 1:
#             soma += digito
#         n = n // 10  # Remove o último dígito
#     return soma

# # Programa principal
# n = int(input("Digite um número natural: "))
# resultado = soma_digitos_impares(n)
# print("Soma dos dígitos ímpares:", resultado)

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

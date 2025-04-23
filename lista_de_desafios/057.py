# Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores 'M'ou 'F'. Caso esteja errado,
# peça a digitação novamente até ter um valor correto

# sexo = str(input('Digite seu sexo [M/F]: ')).upper()
# print(f'Seu sexo é {sexo}')

# while sexo !='M' or sexo !='F':
#     print('Sexo não existente, digite [M/F]')
#     sexo = str(input('Digite seu sexo [M/F]: ')).upper()
# print(f'Seu sexo é {sexo}')

sexo = str(input('Digite seu sexo [M/F]: ')).upper()

while sexo not in ['M', 'F']:
    print('Sexo não existente, digite [M/F]')
    sexo = str(input('Digite seu sexo [M/F]: ')).upper()

print(f'Seu sexo é {sexo}')

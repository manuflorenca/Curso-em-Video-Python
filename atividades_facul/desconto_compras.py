# Crie um programa que solicite ao usuário:
# - O valor unitário de um produto;
# - A quantidade comprada.
# O programa deve calcular o valor total da compra e aplicar um DESCONTO DE 10% caso o
# total seja maior ou igual a R$100,00.
# Se o desconto for aplicado, exiba:
# O total da compra com desconto é: R$ [valor_com_desconto]
# Caso contrário, exiba:
# O total da compra sem desconto é: R$ [valor_sem_desconto]

product = float(input('Qual o valor do produto? '))
amount = int(input('Qual foi a quantidade desse produto adquirido? ')) 

v_total = product * amount
porcentagem = v_total * (10 / 100)
discount = v_total - porcentagem

if v_total >= 100:
    print(f'O total da compra com desconto é {discount}')
else:
    print(f'O total da sua compra sem descoto é {v_total}')
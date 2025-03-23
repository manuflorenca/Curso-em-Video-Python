#Calculando descontos

product = float(input('Qual o preço do produto? R$ '))

discount = product / 100*5

product_w_discount = product - discount

print(f'O seu produto que custava R${product:.2f}, na promoção com desconto de 5% vai custar R${product_w_discount:.2f}')
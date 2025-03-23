# Pergunta a quantidade de Kms percorrido por um carro e dias e fala o preço do aluguel dele

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
pago = dias * 60 + (km * 0.15)

print(f'O total a pagar é de R${pago:.2f}')
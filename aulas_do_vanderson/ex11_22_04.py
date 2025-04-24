# . 11 Jogo de adivinhação simples - peça números até o usúario acertar o número secreto (ex: 7).

numero = 7

adivinhe = int(input('Adivinhe a numero: '))

while adivinhe != numero:
    print('Você não vai conseguir XD')
    adivinhe = int(input('Adivinhe a numero: '))
print(f'Parabéns otario a numero realmente era {numero}, até o proximo desafio')
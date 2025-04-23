# -6 senha até acerta - Peça um número ao  usúario e continue pedindo até ele digitar 'python123'.

senha = 'python123'

adivinhe = str(input('Adivinhe a senha: '))

while adivinhe != senha:
    print('Você não vai conseguir XD')
    adivinhe = str(input('Adivinhe a senha: '))
print(f'Parabéns otario a senha realmente era {senha}, até o proximo desafio')


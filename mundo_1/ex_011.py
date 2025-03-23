# Programa que leia a largura e a altura de uma parede em metros, calcule 
# a sua área e a quantidade necessaria de tinta para pinta-la
# sabendo que cada litro de tinta, pinta uma area de 2m

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))

area = larg * alt

print(f'Sua parede tem a dimensão de {larg} x {alt} e a sua área é de {area}m[2]')

tinta = area / 2

print(f'Para pintar essa parede, você vai precisar de {tinta}l de tinta')
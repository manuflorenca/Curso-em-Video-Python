# Catetos e hipotenusa

import math

cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))

resultado = math.hypot(cateto_oposto, cateto_adjacente)
print(f'A hipotenusa vai medir {resultado:.2f}' )

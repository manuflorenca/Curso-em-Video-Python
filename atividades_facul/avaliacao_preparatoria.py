#  Crie um programa que solicite ao usuário três números que representam medidas de três retas,
#  o programa deverá indicar se essas três retas podem formar um triângulo.
#  Ao final o programa deverá exibir o seu número de matrícula (R.A.).
#  Pesquise qual é a condição de existência de um triângulo e procure compreender adequadamente,
#  de modo que consiga explicar para outras pessoas, pois o professor poderá sortear alguns alunos para explicarem
#  o próprio algoritmo como uma parte da avaliação.

ra = 2501185

print('Insira a medida dos 3 lados de um triangulo')

lado1 = float(input('Digite o primeiro lado: '))
lado2 = float(input('Digite o segundo lado: '))
lado3 = float(input('Digite o terceiro lado: '))

if (lado1 + lado2 > lado3) & (lado1 + lado3 > lado2) & (lado2 + lado3 > lado1):
    print('Forma um triangulo')
    print(ra)
else:
    print('Não forma um triangulo')
    print(ra)

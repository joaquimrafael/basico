from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca: float = float(input('Digite o comprimento do cateto adjacente: '))
hip = hypot(co, ca)
print('A hipotenusa vai medir: {:.2f}cm'.format(hip))

n = float(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('\033[32mO dobro de {:.0f} vale: {:.0f}'.format(n, d))
print('O triplo de {:.0f} vale: {:.0f}'.format(n, t))
print('A raiz quadrada de {:.0f} vale {:.2f}\033[m'.format(n, r))


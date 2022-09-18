from math import trunc
num = float(input('Digite um número: '))
inteiro = trunc(num)
print('O valor digitado foi {:.2f} e sua parte inteira foi {}'.format(num, inteiro))

t = int(input('Quantos dias alugados?: '))
d = float(input('Quantos km rodados?: '))
p = (t * 60) + (d * 0.15)
print('O total a se pagar é R${:.2f}'.format(p))

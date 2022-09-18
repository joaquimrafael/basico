largura = float(input('Largura da parede(m): '))
altura = float(input('Altura da parede(m): '))
area = altura * largura
print('Sua parede tem dimensões de {:.2f}mx{:.2f}m e sua área é de {:.3f}m²'.format(largura, altura, area))
print('Para pintar essa parede você precisa de {:.2f}l de tinta'.format(area * (1/2)))

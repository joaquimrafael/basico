d = int(input('Qual a distância da sua viagem? '))
p1 = float(d * 0.5)  # para distâncias de menos de 200km
p2 = float(d * 0.45)  # para distâncias de mais de 200km
print('Você esta prestes a começar sua viagem de {}Km'.format(d))
if d <= 200:
    print('E o preço da sua passagem será de R${:.2f}'.format(p1))
else:
    print('E o preço da sua passagem será de R${:.2f}'.format(p2))
print('TENHA UMA ÓTIMA VIAGEM!!')

v = int(input('Qual é a velocidade atual do carro? '))
m = float((v - 80) * 7)
if v < 80:
    print('Tenha um bom dia! Dirija com segurança')
else:
    print('MULTADO! Você excedeu o limite de velocidade que é de 80km/h')
    print('Você deve pagar uma multa de R${:.2f} '.format(m))
    print('Tenha um bom dia! Dirija com segurança')

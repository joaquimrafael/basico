salario = float(input('Qual o salário do funcionário? R$'))
r1 = salario * 115/100
r2 = salario * 11/10
if salario <= 1250:
    print('Quem ganhava R${:.2f} passou a ganhar R${:.2f} agora'.format(salario, r1))
else:
    print('Quem ganhava R${:.2f} passou a ganhar R${:.2f} agora'.format(salario, r2))





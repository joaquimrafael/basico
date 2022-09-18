salario = float(input('Qual é o salário do funcionário?: '))
novo = salario + (salario * (15/100))
print('Um funcionário que ganhava R${:.2f}, com o reajuste de 15% passsou a ganhar R${:.2f}'.format(salario, novo))


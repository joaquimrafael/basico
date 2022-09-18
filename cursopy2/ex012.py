preco = float(input('Qual é o preço do produto?: '))
novo = preco * 0.95
print('O produto que custava \033[31mR${:.2f}\033[m, com o desconto de 5% passou a custar R${:.2f}'.format(preco, novo))

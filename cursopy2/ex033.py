a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
# Verificando quem é o menor.
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é o maior.
maior = b
if a > b and a > c:
    maior = a
if c > b and c > a:
    maior = c
print('O menor valor digitado foi: \033[1;31m{}\033[m '.format(menor))
print('O maior valor digitado foi: \033[1;32m{}\033[m '.format(maior))

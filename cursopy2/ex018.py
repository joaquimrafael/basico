import math
an = int(input('Digite o ângulo que você deseja: '))
ang = math.radians(an)
sen = math.sin(ang)
cos = math.cos(ang)
tg = math.tan(ang)
print('O ângulo de {}° tem o SENO de {:.2f} \nO COSSENO {:.2f} \nE a TANGENTE {:.2f}'.format(an, sen, cos, tg))

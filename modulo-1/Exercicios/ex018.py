'''
faça um programa que leia um angulo qualquer e mostre na tela
o valor do Seno, cosseno e tangente desse angulo.
'''
import math
an = float(input('Digite o valor do angulo: '))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('O angulo de {} graus possui o SENO de {:.2f}'.format(an, sen))
print('O angulo de {} graus possui o COSSENO de {:.2f}'.format(an, cos))
print('O angulo de {} graus possui a TANGENTE de {:.2f}'.format(an, tan))

'''
from math import radians, sin, cos, tan
an = float(input('Digite o valor do angulo: '))
sen = sin(radians(an))
cos = cos(radians(an))
tan = tan(radians(an))
print('O angulo de {} graus possui o SENO de {:.2f}'.format(an, sen))
print('O angulo de {} graus possui o COSSENO de {:.2f}'.format(an, cos))
print('O angulo de {} graus possui a TANGENTE de {:.2f}'.format(an, tan))
'''

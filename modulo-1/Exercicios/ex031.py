'''
Desenvolva um programa que pergunte a distancia de uma viagem em KM.
Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de
ate 200KM e R$0,45 para viagens mais longas
'''
dist = float(input('Qual é a distancia da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.2f}Km'.format(dist))
if dist <= 200:
    preco = dist * 0.5
else:
    preco = dist * 0.45
print('O valor de sua passagem será de {:.2f}'.format(preco))

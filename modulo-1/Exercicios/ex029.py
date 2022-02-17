'''
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar
80km por hora mostre uma mensagem dizendo que ele foi multado, e a multa
vai custar R$ 7,00 reais para cada kilometro acima do limite.
'''
velo = float(input('Qual a velocidade atual do carro? '))
mult = (velo - 80) * 7
if velo >80:
    print('MULTADO! Você excedeu o limite permitido de 80km/h.')
    print('Você deve pagar o valor de {:.2f} reais'.format(mult))
print('Tenha um bom dia! Dirija com segurança!')
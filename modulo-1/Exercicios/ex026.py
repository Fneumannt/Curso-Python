'''
Faça um programa que leia uma frase e mostre:
- Quantas vezes aparece a letra "a":
- Em qual posição ela aparece a primeira vez:
- Em que posição ela aparece a última vez:
'''

frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra "A" aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra "A", aparece na posição {}'.format(frase.find('A')+1))
print('A última vez que a letra "A" aparece foi na posição {}'.format(frase.rfind('A')+1))

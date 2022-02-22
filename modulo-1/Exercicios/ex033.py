'''
Faça um programa que leia 03 números e
mostre qual é o maior e qual é o menor.
'''
n1 = float(input('Digite o primeiro número: '))
n2: float = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
maior = n1
menor = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O menor valor digitado foi {:.2f}'.format(menor))
print('O maior valor digitado foi {:.2f}'.format(maior))

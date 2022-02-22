'''
Desenvolva um programa que leia o comprimento de 03 retas e
e diga ao usuário se elas podem ou não formar um triangulo.
'''

print('-=' *20)
print('Analisador de Triângulos')
print('-=' *20)
s1 = float(input('Digite o primeiro segmento: '))
s2 = float(input('Digite o segundo segmento: '))
s3 = float(input('Digite o terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima PODEM FORMAR um triangulo!')
else:
    print('Os segmentos acima NÃO PODEM formar um triangulo!')

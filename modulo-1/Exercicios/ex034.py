'''
Escreva um programa que pergunte o salário do funcionário e calcule o valor
de seu aumento. Para salários superiores a R$ 2.000,00, calcule um aumento
de 10%, para inferiores ou iguais, o aumento é de 15%.
'''
sal = float(input('Qual o valor do salário? R$'))
if sal > 2000:
    nsal = sal * (10 / 100) + sal
else:
    nsal = sal * (15 / 100) + sal
print('O salário do funcionário passa de R${:.2f} reais para R${:.2f} reais'.format(sal, nsal))

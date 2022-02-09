sal = float(input('Digite o salário do funcionário: R$'))
nsal = sal + (sal*15/100)
print('O novo salário do funcionário com aumento de 15% é de R${:.2f}'.format(nsal))
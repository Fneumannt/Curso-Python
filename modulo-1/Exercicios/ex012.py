prod = float(input('Digite o preço do produto: R$'))
preco = prod - (prod*5/100)
print('O novo preço do produto, com desconto de 5% é de: R${:.2f}'.format(preco))

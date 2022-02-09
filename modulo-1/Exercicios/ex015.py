km = float(input('Quantos km foram percorridos? '))
car = int(input('Por quantos dias o carro foi alugado? '))
preco = km * 0.15 + car * 60
print('O valor a ser pago é de: R${:.2f}'.format(preco))

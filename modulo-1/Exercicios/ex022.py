'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiusculas e minusculas;
- Quantas letras ao todo sem considerar os espaços;
- Quantas letras tem o primeiro nome.
'''

nome = str(input('Digite o seu nome completo: ')).strip()
print('Analisando o seu nome...')
print('Seu nome em maiusculo é: {}'.format(nome.upper()))
print('Seu nome em minusculo é: {}'.format(nome.lower()))
print('Seu nome tem ao todo: {} letras'.format(len(nome) - nome.count(' ')))
# print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separado = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separado[0], len(separado[0])))

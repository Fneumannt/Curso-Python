'''
Crie um programa que leia o nome de uma cidade e diga se ela
começa ou não com o nome "Santo".
'''
city = str(input('Digite a cidade que você nasceu: ')).strip()
print(city[:5].upper() == 'SANTO')

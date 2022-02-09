larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = (larg*alt)
tinta = area/2
print('Sua parede tem a dimensão de {}x{} e sua area é {}m²'.format(larg, alt, area))
print('Para pintar esta parede será necessário {}l de tinta'. format(tinta))

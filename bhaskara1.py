print('Olá, resolverei uma equação de 2° grau para você. Primeiramente, preciso de alguns valores.')
a = input('Diga-me o "a" ')
b = input('Diga-me o "b" ')
c = input('Diga-me o "c" ')
x1 = (-int(b)+((int(b)**2-4*int(a)*int(c))**0.5))/(2*int(a))
x2 = (-int(b)-((int(b)**2-4*int(a)*int(c))**0.5))/(2*int(a))
print('As raízes desta equação são {} e {}'.format(x1, x2))

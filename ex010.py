n=float(input('Quanto dinheiro vc tem: R$'))
d=n/5.47
e=n/6.66
print('='*40)
print('Com R${:.2f} você pode comprar US${:.2f} '.format(n,d))
print('Com R${:.2f} você pode comprar  €{:.2f}'.format(n,e))
print('='*40)
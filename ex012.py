n=float(input('Digite seu preço: R$'))
d=float(input('Digite a % em desconto: '))
s=n-(n*d/100)
print('Seu novo preço com desconto de {:.0f}% é R${:.2f}'.format(d,s))
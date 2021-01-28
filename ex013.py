n=float(input('Digite seu salario: '))
a=float(input('Digite a % do seu aumento: '))
s=n+(n*a/100)
print('Seu novo salario com {:.0f}% de aumento é R${:.2f}'.format(a,s))
a = int(input("Digite seu salario: R$ "))
if a > 1250:
    print("Seu salario de R${} com um aumento de 10% é R${:.2f}".format(a,(a*0.10)+a))
else:
    print("\33[1:30:45mSeu salario de R${} com um aumento de 15% é R${:.2f}\33[m".format(a,(a*0.15)+a))

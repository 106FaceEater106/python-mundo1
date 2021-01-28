velocidade = int(input("Quantos Km/h vc estava?: "))
m = velocidade - 80
s = m*7
if velocidade >= 80:
    print('voce foi multado')
    print('A multa vai custar R$7,00 por cada km acima do limite')
    print('O total da sua multa é R${:.2f}'.format(s))
else:
    print('Velocidade permitida')

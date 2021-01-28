n = int(input("Quantos km foi rodado? "))
if n <= 200:
    print("O preço total da viagem foi R${:.2f}".format(n*0.50))
else:
    print('O preço total da sua viagem foi R${:.2f}'.format(n*0.45))